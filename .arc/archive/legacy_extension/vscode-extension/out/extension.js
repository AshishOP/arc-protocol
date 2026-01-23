"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const http = __importStar(require("http"));
const fs = __importStar(require("fs"));
const path = __importStar(require("path"));
const child_process = __importStar(require("child_process"));
let bridgeServer = null;
let statusBarItem;
function activate(context) {
    console.log('ARC Protocol extension activated');
    // Create status bar item
    statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
    statusBarItem.text = "$(plug) ARC";
    statusBarItem.tooltip = "ARC Protocol - Click to toggle bridge";
    statusBarItem.command = 'arc.startBridge';
    statusBarItem.show();
    context.subscriptions.push(statusBarItem);
    // Register commands
    context.subscriptions.push(vscode.commands.registerCommand('arc.startBridge', startBridge), vscode.commands.registerCommand('arc.stopBridge', stopBridge), vscode.commands.registerCommand('arc.openDashboard', openDashboard), vscode.commands.registerCommand('arc.showStatus', showStatus));
    // Auto-start bridge if configured
    const config = vscode.workspace.getConfiguration('arc');
    if (config.get('autoStartBridge')) {
        startBridge();
    }
}
function startBridge() {
    if (bridgeServer) {
        vscode.window.showInformationMessage('ARC Bridge already running');
        return;
    }
    const config = vscode.workspace.getConfiguration('arc');
    const port = config.get('bridgePort') || 8765;
    const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd();
    bridgeServer = http.createServer((req, res) => {
        const url = new URL(req.url || '/', `http://localhost:${port}`);
        // CORS headers
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
        if (req.method === 'OPTIONS') {
            res.writeHead(200);
            res.end();
            return;
        }
        // Routes
        if (url.pathname === '/') {
            serveUI(res);
        }
        else if (url.pathname === '/api/read' && req.method === 'GET') {
            handleRead(url, res, workspaceRoot);
        }
        else if (url.pathname === '/api/list' && req.method === 'GET') {
            handleList(url, res, workspaceRoot);
        }
        else if (url.pathname === '/api/write' && req.method === 'POST') {
            handleWrite(req, res, workspaceRoot);
        }
        else if (url.pathname === '/api/exec' && req.method === 'POST') {
            handleExec(req, res, workspaceRoot);
        }
        else if (url.pathname === '/api/status') {
            handleStatus(res, workspaceRoot);
        }
        else {
            res.writeHead(404);
            res.end(JSON.stringify({ error: 'Not found' }));
        }
    });
    bridgeServer.listen(port, 'localhost', () => {
        statusBarItem.text = "$(zap) ARC";
        statusBarItem.backgroundColor = new vscode.ThemeColor('statusBarItem.warningBackground');
        vscode.window.showInformationMessage(`ARC Bridge started on http://localhost:${port}`);
    });
    bridgeServer.on('error', (err) => {
        vscode.window.showErrorMessage(`ARC Bridge error: ${err.message}`);
        bridgeServer = null;
        statusBarItem.text = "$(plug) ARC";
    });
}
function stopBridge() {
    if (bridgeServer) {
        bridgeServer.close();
        bridgeServer = null;
        statusBarItem.text = "$(plug) ARC";
        statusBarItem.backgroundColor = undefined;
        vscode.window.showInformationMessage('ARC Bridge stopped');
    }
}
function openDashboard() {
    const config = vscode.workspace.getConfiguration('arc');
    const port = config.get('bridgePort') || 8765;
    vscode.env.openExternal(vscode.Uri.parse(`http://localhost:${port}`));
}
function showStatus() {
    const running = bridgeServer !== null;
    const config = vscode.workspace.getConfiguration('arc');
    const port = config.get('bridgePort') || 8765;
    vscode.window.showInformationMessage(`ARC Protocol\nBridge: ${running ? 'Running' : 'Stopped'}\nPort: ${port}`);
}
// API Handlers
function handleRead(url, res, root) {
    const filePath = url.searchParams.get('path') || '';
    const fullPath = path.join(root, filePath);
    try {
        const content = fs.readFileSync(fullPath, 'utf-8');
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, content, path: filePath }));
    }
    catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: err.message }));
    }
}
function handleList(url, res, root) {
    const dirPath = url.searchParams.get('path') || '';
    const fullPath = path.join(root, dirPath);
    try {
        const items = fs.readdirSync(fullPath);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, items, path: dirPath }));
    }
    catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: err.message }));
    }
}
function handleWrite(req, res, root) {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
        try {
            const { path: filePath, content } = JSON.parse(body);
            const fullPath = path.join(root, filePath);
            // Create directories if needed
            fs.mkdirSync(path.dirname(fullPath), { recursive: true });
            fs.writeFileSync(fullPath, content);
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true, path: filePath }));
        }
        catch (err) {
            res.writeHead(400, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: false, error: err.message }));
        }
    });
}
function handleExec(req, res, root) {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
        try {
            const { command } = JSON.parse(body);
            const result = child_process.execSync(command, {
                cwd: root,
                encoding: 'utf-8',
                timeout: 30000
            });
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true, stdout: result, stderr: '' }));
        }
        catch (err) {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                success: true,
                stdout: err.stdout || '',
                stderr: err.stderr || err.message,
                returncode: err.status || 1
            }));
        }
    });
}
function handleStatus(res, root) {
    const stateFile = path.join(root, '.arc', 'arc_workflow_state.json');
    try {
        const state = JSON.parse(fs.readFileSync(stateFile, 'utf-8'));
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, state }));
    }
    catch {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, state: {} }));
    }
}
function serveUI(res) {
    const html = `<!DOCTYPE html>
<html>
<head>
    <title>ARC Subagent Bridge</title>
    <style>
        * { box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', system-ui, sans-serif; 
            background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            color: #c9d1d9; 
            padding: 20px;
            min-height: 100vh;
            margin: 0;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { 
            color: #58a6ff; 
            font-size: 2.5em;
            margin-bottom: 0;
        }
        .subtitle { color: #8b949e; margin-bottom: 30px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px; }
        .card { 
            background: rgba(22, 27, 34, 0.8);
            backdrop-filter: blur(10px);
            padding: 20px; 
            border-radius: 12px;
            border: 1px solid #30363d;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.4);
        }
        .card h3 { color: #58a6ff; margin-top: 0; display: flex; align-items: center; gap: 8px; }
        input, textarea { 
            background: #21262d; 
            border: 1px solid #30363d; 
            color: #c9d1d9; 
            padding: 12px; 
            width: 100%; 
            margin: 8px 0;
            border-radius: 6px;
            font-size: 14px;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: #58a6ff;
            box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.1);
        }
        button { 
            background: linear-gradient(135deg, #238636 0%, #2ea043 100%);
            color: white; 
            border: none; 
            padding: 12px 24px; 
            cursor: pointer; 
            border-radius: 6px;
            font-weight: 600;
            margin: 5px 5px 5px 0;
            transition: all 0.2s;
        }
        button:hover { 
            background: linear-gradient(135deg, #2ea043 0%, #3fb950 100%);
            transform: translateY(-1px);
        }
        #output { 
            background: #0d1117; 
            padding: 15px; 
            white-space: pre-wrap; 
            max-height: 350px; 
            overflow-y: auto; 
            border-radius: 8px;
            font-family: 'Fira Code', 'Consolas', monospace;
            font-size: 13px;
            border: 1px solid #21262d;
        }
        .status { 
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            background: #238636;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }
        .status::before {
            content: '';
            width: 8px;
            height: 8px;
            background: #3fb950;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .api-section {
            margin-top: 30px;
            padding: 20px;
            background: rgba(22, 27, 34, 0.5);
            border-radius: 12px;
            border: 1px solid #21262d;
        }
        .api-section h4 { color: #8b949e; margin-top: 0; }
        code { 
            background: #21262d; 
            padding: 2px 6px; 
            border-radius: 4px;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 ARC Subagent Bridge</h1>
        <p class="subtitle">
            <span class="status">Active</span>
            Enabling browser_subagent to perform file operations
        </p>
        
        <div class="grid">
            <div class="card">
                <h3>📖 Read File</h3>
                <input type="text" id="readPath" placeholder="Path (e.g., .arc/PROJECT.md)">
                <button onclick="readFile()">Read File</button>
            </div>
            
            <div class="card">
                <h3>📝 Write File</h3>
                <input type="text" id="writePath" placeholder="Path (e.g., .arc/STATE.md)">
                <textarea id="writeContent" rows="4" placeholder="File content..."></textarea>
                <button onclick="writeFile()">Write File</button>
            </div>
            
            <div class="card">
                <h3>📁 List Directory</h3>
                <input type="text" id="listPath" placeholder="Path (e.g., .arc/)">
                <button onclick="listDir()">List Contents</button>
            </div>
            
            <div class="card">
                <h3>💻 Execute Command</h3>
                <input type="text" id="execCmd" placeholder="Command (e.g., git status)">
                <button onclick="execCommand()">Execute</button>
            </div>
        </div>
        
        <div class="card" style="margin-top: 20px;">
            <h3>📊 Output</h3>
            <div id="output">Ready for subagent commands...</div>
        </div>
        
        <div class="api-section">
            <h4>🔌 API Endpoints for Subagents</h4>
            <p><code>GET /api/read?path=...</code> Read a file</p>
            <p><code>GET /api/list?path=...</code> List directory</p>
            <p><code>POST /api/write</code> Write file (body: {path, content})</p>
            <p><code>POST /api/exec</code> Execute command (body: {command})</p>
        </div>
    </div>
    
    <script>
        const output = document.getElementById('output');
        
        async function readFile() {
            const path = document.getElementById('readPath').value;
            try {
                const res = await fetch('/api/read?path=' + encodeURIComponent(path));
                const data = await res.json();
                output.textContent = data.success ? data.content : 'Error: ' + data.error;
            } catch(e) { output.textContent = 'Error: ' + e.message; }
        }
        
        async function writeFile() {
            const path = document.getElementById('writePath').value;
            const content = document.getElementById('writeContent').value;
            try {
                const res = await fetch('/api/write', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({path, content})
                });
                const data = await res.json();
                output.textContent = data.success ? '✅ Written to ' + path : 'Error: ' + data.error;
            } catch(e) { output.textContent = 'Error: ' + e.message; }
        }
        
        async function listDir() {
            const path = document.getElementById('listPath').value;
            try {
                const res = await fetch('/api/list?path=' + encodeURIComponent(path));
                const data = await res.json();
                output.textContent = data.success ? data.items.join('\\n') : 'Error: ' + data.error;
            } catch(e) { output.textContent = 'Error: ' + e.message; }
        }
        
        async function execCommand() {
            const command = document.getElementById('execCmd').value;
            try {
                const res = await fetch('/api/exec', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({command})
                });
                const data = await res.json();
                output.textContent = data.stdout + (data.stderr ? '\\n[stderr] ' + data.stderr : '');
            } catch(e) { output.textContent = 'Error: ' + e.message; }
        }
    </script>
</body>
</html>`;
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(html);
}
function deactivate() {
    stopBridge();
}
//# sourceMappingURL=extension.js.map