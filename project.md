# Project: CCTV Installation Training Manual

## Overview
This project is a comprehensive, beginner-friendly training manual for CCTV installation technicians, diploma students, interns, electricians, and freshers. Written in Hinglish (Hindi + English mix) with a practical-first approach, it covers 14 chapters and over 21,000 lines of Markdown content.

## Key Features
- **Modern HTML Viewer**: Includes a dark/light theme toggle, responsive design, interactive sidebar, and search functionality.
- **Status Dashboard**: Provides a grid view of chapters, image gallery, and progress statistics.
- **Interactive Elements**: Image placeholders, diagram placeholders, callout boxes, and font size controls.
- **One-Click Launchers**: Easy-to-use batch files for starting the server and opening the manual.

## Project Structure
- **Main Manual**: `CCTV_Training_Manual.md` (21,000+ lines)
- **HTML Viewer**: `manual.html`
- **Status Dashboard**: `index.html`
- **Images**: Stored in the `images/` folder (25 images currently available)
- **Diagrams**: Stored in the `diagrams/` folder (22 of 26 completed)

## MCP Servers
The project is configured with three MCP servers in `opencode.json`:
1.  **notebooklm**: `npx -y notebooklm-mcp@latest`
2.  **puppeteer**: `npx -y @modelcontextprotocol/server-puppeteer`
3.  **memory**: `npx -y @modelcontextprotocol/server-memory`

## Project Status
- **Manual Content**: 100% Complete (14 chapters)
- **HTML Viewer**: 100% Complete
- **Images**: 50% Complete (25 out of 50 images linked)
- **Diagrams**: 85% Complete (22 out of 26 diagrams created)

## How to Use
1.  **Launch**: Double-click `Open Manual.bat` to start the server and open the manual in your browser.
2.  **Navigate**: Use the interactive sidebar to jump between chapters.
3.  **Search**: Use the search bar to find specific topics instantly.
