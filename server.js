/**
 * CCTV Manual — NotebookLM Chatbot Server
 * 
 * Bridges the browser chatbot to NotebookLM via MCP.
 * Run: npm start
 * Then open: http://localhost:3000/manual.html
 * 
 * First time: visit http://localhost:3000/api/auth to login with Google.
 */

const express = require('express');
const path = require('path');
const { Client } = require('@modelcontextprotocol/sdk/client/index.js');
const { StdioClientTransport } = require('@modelcontextprotocol/sdk/client/stdio.js');

const app = express();
const PORT = process.env.PORT || 3000;

// ── MCP Client ──────────────────────────────────────────────
let mcpClient = null;
let isConnected = false;
let isConnecting = false;
let notebookId = null;
let notebookReady = false;

function parseMCPResult(result) {
  try {
    const raw = result.content?.[0]?.text || '';
    const parsed = JSON.parse(raw);
    return parsed.data || parsed;
  } catch {
    return result.content?.[0]?.text || '';
  }
}

async function ensureMCP() {
  if (isConnected && mcpClient) return mcpClient;
  if (isConnecting) return null;

  isConnecting = true;
  try {
    const transport = new StdioClientTransport({
      command: 'npx',
      args: ['-y', 'notebooklm-mcp@latest'],
      env: { ...process.env, HEADLESS: 'true' },
    });

    mcpClient = new Client(
      { name: 'cctv-manual-server', version: '1.0.0' },
      { capabilities: {} }
    );

    await mcpClient.connect(transport);
    isConnected = true;
    isConnecting = false;
    console.log('[MCP] Connected to NotebookLM server');
    return mcpClient;
  } catch (err) {
    console.error('[MCP] Connection failed:', err.message);
    isConnected = false;
    mcpClient = null;
    isConnecting = false;
    return null;
  }
}

async function ensureNotebook() {
  if (notebookReady && notebookId) return notebookId;
  if (!mcpClient) return null;

  try {
    const result = await mcpClient.callTool({ name: 'list_notebooks', arguments: {} });
    const data = parseMCPResult(result);
    const notebooks = data.notebooks || [];

    // Look for existing CCTV notebook
    for (const nb of notebooks) {
      const name = (nb.name || '').toLowerCase();
      if (name.includes('cctv') || name.includes('camera')) {
        notebookId = nb.id;
        await mcpClient.callTool({
          name: 'select_notebook',
          arguments: { notebook_id: notebookId },
        });
        notebookReady = true;
        console.log('[MCP] Selected existing notebook:', notebookId);
        return notebookId;
      }
    }

    console.log('[MCP] No CCTV notebook found. Create one via /api/setup-notebook');
    return null;
  } catch (err) {
    console.error('[MCP] Notebook lookup error:', err.message);
    return null;
  }
}

// ── Middleware ───────────────────────────────────────────────
app.use(express.json());
app.use(express.static(path.join(__dirname)));

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  if (req.method === 'OPTIONS') return res.sendStatus(200);
  next();
});

// ── API Routes ──────────────────────────────────────────────

app.get('/api/health', async (req, res) => {
  try {
    const client = await ensureMCP();
    if (!client) {
      return res.json({ status: 'offline', authenticated: false });
    }
    const result = await client.callTool({ name: 'get_health', arguments: {} });
    const data = parseMCPResult(result);
    res.json({
      status: 'online',
      authenticated: data.authenticated || false,
      notebookReady,
      notebookId,
    });
  } catch (err) {
    res.json({ status: 'error', message: err.message });
  }
});

app.post('/api/chat', async (req, res) => {
  const { question } = req.body;
  if (!question) return res.status(400).json({ error: 'Question required' });

  try {
    const client = await ensureMCP();
    if (!client) {
      return res.json({ answer: null, fallback: true });
    }

    // Ensure notebook is ready
    const nbId = await ensureNotebook();

    const args = { question, source_format: 'inline' };
    if (nbId) args.notebook_id = nbId;

    const result = await client.callTool({ name: 'ask_question', arguments: args });
    const data = parseMCPResult(result);
    const answer = data.answer || data.text || result.content?.[0]?.text || 'No answer generated.';
    res.json({ answer, fallback: false });
  } catch (err) {
    console.error('[API] Chat error:', err.message);
    res.json({ answer: null, fallback: true, error: err.message });
  }
});

app.get('/api/auth', async (req, res) => {
  try {
    const client = await ensureMCP();
    if (!client) return res.status(503).json({ error: 'MCP not connected' });

    const result = await client.callTool({
      name: 'setup_auth',
      arguments: { show_browser: true },
    });
    const data = parseMCPResult(result);
    res.json({ status: 'auth_started', details: data });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/setup-notebook', async (req, res) => {
  try {
    const client = await ensureMCP();
    if (!client) return res.status(503).json({ error: 'MCP not connected' });

    // Add notebook with manual URL
    const result = await client.callTool({
      name: 'add_notebook',
      arguments: {
        url: 'https://hiiren.github.io/CCTV_Manual/manual.html',
        name: 'CCTV Installation Training Manual',
        description: 'Complete training guide for CCTV installation. 20 chapters covering cameras, networking, troubleshooting, home automation, access control.',
        topics: ['CCTV', 'cameras', 'installation', 'networking', 'troubleshooting', 'home automation', 'access control'],
        content_types: ['training manual'],
        use_cases: ['CCTV installation questions', 'camera troubleshooting', 'product recommendations'],
      },
    });
    const data = parseMCPResult(result);
    const id = data.id || data.notebook_id;
    if (id) {
      notebookId = id;
      notebookReady = true;
      await client.callTool({ name: 'select_notebook', arguments: { notebook_id: id } });
    }

    // Add source
    await client.callTool({
      name: 'add_source',
      arguments: {
        type: 'url',
        content: 'https://hiiren.github.io/CCTV_Manual/manual.html',
        title: 'CCTV Training Manual',
      },
    });

    res.json({ status: 'notebook_ready', notebookId: id, data });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/notebooks', async (req, res) => {
  try {
    const client = await ensureMCP();
    if (!client) return res.status(503).json({ error: 'MCP not connected' });
    const result = await client.callTool({ name: 'list_notebooks', arguments: {} });
    res.json(parseMCPResult(result));
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/reset', async (req, res) => {
  try {
    const client = await ensureMCP();
    if (!client) return res.status(503).json({ error: 'MCP not connected' });
    const result = await client.callTool({ name: 'reset_session', arguments: {} });
    res.json({ status: 'reset' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ── Start ───────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log('');
  console.log('  ╔══════════════════════════════════════════════╗');
  console.log('  ║  CCTV Manual — NotebookLM Chatbot Server     ║');
  console.log('  ╠══════════════════════════════════════════════╣');
  console.log(`  ║  Manual:  http://localhost:${PORT}/manual.html    ║`);
  console.log(`  ║  Auth:    http://localhost:${PORT}/api/auth        ║`);
  console.log(`  ║  Health:  http://localhost:${PORT}/api/health      ║`);
  console.log('  ╚══════════════════════════════════════════════╝');
  console.log('');
  console.log('  Steps:');
  console.log('  1. Visit /api/auth to login with Google');
  console.log('  2. POST /api/setup-notebook to create the CCTV notebook');
  console.log('  3. Open /manual.html and chat!');
  console.log('');
  ensureMCP().catch(() => {});
});
