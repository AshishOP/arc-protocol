# ARC Protocol VS Code Extension

This extension enables **true multi-agent** development by providing browser_subagent with file read/write capabilities.

## How It Works

```
┌─────────────────────┐     HTTP      ┌──────────────────┐
│  browser_subagent   │  ──────────►  │  Bridge Server   │
│  (navigates browser)│               │  (this extension)│
└─────────────────────┘               └──────────────────┘
                                              │
                                              ▼
                                      ┌──────────────────┐
                                      │  File System     │
                                      │  read/write/exec │
                                      └──────────────────┘
```

## Installation

### From Source
```bash
cd vscode-extension
npm install
npm run compile
npm run package
code --install-extension arc-protocol-1.0.0.vsix
```

### From Marketplace (Coming Soon)
Search for "ARC Protocol" in VS Code extensions.

## Usage

1. **Auto-Start**: Bridge starts automatically when you open a workspace
2. **Manual Start**: `Ctrl+Shift+P` → "ARC: Start Subagent Bridge"
3. **Status Bar**: Click "ARC" in status bar to toggle

## For Subagents

Browser subagent can now:

```javascript
// Navigate to bridge
open_browser_url("http://localhost:8765")

// Read a file
// - Enter path in "Read File" input
// - Click "Read File" button
// - Output shows file content

// Write a file
// - Enter path in "Write File" input
// - Enter content in textarea
// - Click "Write File" button

// Execute commands
// - Enter command in "Execute" input
// - Click "Execute" button
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/read?path=...` | GET | Read file content |
| `/api/list?path=...` | GET | List directory |
| `/api/write` | POST | Write file (body: `{path, content}`) |
| `/api/exec` | POST | Execute command (body: `{command}`) |
| `/api/status` | GET | Get ARC workflow state |

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `arc.bridgePort` | 8765 | Port for bridge server |
| `arc.autoStartBridge` | true | Auto-start on workspace open |
