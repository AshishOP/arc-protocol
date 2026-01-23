#!/usr/bin/env python3
"""
ARC Protocol - Subagent Bridge Server

This enables browser_subagent to perform file read/write operations
by exposing them through a local web interface.

Usage:
    python3 .agent/bridge/server.py
    
Then browser_subagent can navigate to http://localhost:8765
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import urllib.parse
import subprocess

PORT = 8765
BASE_DIR = os.getcwd()

class SubagentBridgeHandler(BaseHTTPRequestHandler):
    
    def _send_response(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def _send_html(self, html):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)
        
        if path == '/':
            # Main dashboard
            self._send_html(self._get_dashboard_html())
        
        elif path == '/api/read':
            # Read a file
            filepath = params.get('path', [''])[0]
            full_path = os.path.join(BASE_DIR, filepath)
            try:
                with open(full_path, 'r') as f:
                    content = f.read()
                self._send_response(200, {'success': True, 'content': content, 'path': filepath})
            except Exception as e:
                self._send_response(400, {'success': False, 'error': str(e)})
        
        elif path == '/api/list':
            # List directory
            dirpath = params.get('path', [''])[0]
            full_path = os.path.join(BASE_DIR, dirpath)
            try:
                items = os.listdir(full_path)
                self._send_response(200, {'success': True, 'items': items, 'path': dirpath})
            except Exception as e:
                self._send_response(400, {'success': False, 'error': str(e)})
        
        elif path == '/api/status':
            # ARC status
            state_file = os.path.join(BASE_DIR, '.arc', 'arc_workflow_state.json')
            try:
                with open(state_file, 'r') as f:
                    state = json.load(f)
                self._send_response(200, {'success': True, 'state': state})
            except:
                self._send_response(200, {'success': True, 'state': {}})
        
        else:
            self._send_response(404, {'error': 'Not found'})

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        
        try:
            data = json.loads(post_data) if post_data else {}
        except:
            data = {}
        
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        
        if path == '/api/write':
            # Write to file
            filepath = data.get('path', '')
            content = data.get('content', '')
            full_path = os.path.join(BASE_DIR, filepath)
            try:
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as f:
                    f.write(content)
                self._send_response(200, {'success': True, 'path': filepath})
            except Exception as e:
                self._send_response(400, {'success': False, 'error': str(e)})
        
        elif path == '/api/exec':
            # Execute command
            cmd = data.get('command', '')
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=BASE_DIR, timeout=30)
                self._send_response(200, {
                    'success': True,
                    'stdout': result.stdout,
                    'stderr': result.stderr,
                    'returncode': result.returncode
                })
            except Exception as e:
                self._send_response(400, {'success': False, 'error': str(e)})
        
        elif path == '/api/dashboard':
            # Update dashboard state
            try:
                state_file = os.path.join(BASE_DIR, '.arc', 'arc_workflow_state.json')
                if os.path.exists(state_file):
                    with open(state_file, 'r') as f:
                        state = json.load(f)
                else:
                    state = {}
                
                # Merge updates
                for key in data:
                    state[key] = data[key]
                
                with open(state_file, 'w') as f:
                    json.dump(state, f, indent=2)
                
                self._send_response(200, {'success': True})
            except Exception as e:
                self._send_response(400, {'success': False, 'error': str(e)})
        
        else:
            self._send_response(404, {'error': 'Not found'})
    
    def _get_dashboard_html(self):
        return '''<!DOCTYPE html>
<html>
<head>
    <title>ARC Subagent Bridge</title>
    <style>
        body { font-family: monospace; background: #0d1117; color: #c9d1d9; padding: 20px; }
        h1 { color: #58a6ff; }
        .section { background: #161b22; padding: 15px; margin: 10px 0; border-radius: 8px; }
        input, textarea { background: #21262d; border: 1px solid #30363d; color: #c9d1d9; padding: 8px; width: 100%; margin: 5px 0; }
        button { background: #238636; color: white; border: none; padding: 10px 20px; cursor: pointer; margin: 5px; }
        button:hover { background: #2ea043; }
        #output { background: #21262d; padding: 10px; white-space: pre-wrap; max-height: 300px; overflow-y: auto; }
        .api-docs { font-size: 12px; color: #8b949e; }
    </style>
</head>
<body>
    <h1>🚀 ARC Subagent Bridge</h1>
    <p>This interface allows browser_subagent to perform file operations.</p>
    
    <div class="section">
        <h3>📖 Read File</h3>
        <input type="text" id="readPath" placeholder="Path (e.g., .arc/PROJECT.md)">
        <button onclick="readFile()">Read</button>
    </div>
    
    <div class="section">
        <h3>📝 Write File</h3>
        <input type="text" id="writePath" placeholder="Path (e.g., .arc/STATE.md)">
        <textarea id="writeContent" rows="5" placeholder="File content..."></textarea>
        <button onclick="writeFile()">Write</button>
    </div>
    
    <div class="section">
        <h3>💻 Execute Command</h3>
        <input type="text" id="execCmd" placeholder="Command (e.g., ls -la)">
        <button onclick="execCommand()">Execute</button>
    </div>
    
    <div class="section">
        <h3>📊 Output</h3>
        <div id="output">Ready...</div>
    </div>
    
    <div class="section api-docs">
        <h4>API Endpoints:</h4>
        <p>GET /api/read?path=... - Read file</p>
        <p>GET /api/list?path=... - List directory</p>
        <p>POST /api/write {path, content} - Write file</p>
        <p>POST /api/exec {command} - Execute command</p>
        <p>POST /api/dashboard {...} - Update dashboard state</p>
    </div>
    
    <script>
        const output = document.getElementById('output');
        
        async function readFile() {
            const path = document.getElementById('readPath').value;
            const res = await fetch('/api/read?path=' + encodeURIComponent(path));
            const data = await res.json();
            output.textContent = data.success ? data.content : 'Error: ' + data.error;
        }
        
        async function writeFile() {
            const path = document.getElementById('writePath').value;
            const content = document.getElementById('writeContent').value;
            const res = await fetch('/api/write', {
                method: 'POST',
                body: JSON.stringify({path, content})
            });
            const data = await res.json();
            output.textContent = data.success ? 'Written to ' + path : 'Error: ' + data.error;
        }
        
        async function execCommand() {
            const command = document.getElementById('execCmd').value;
            const res = await fetch('/api/exec', {
                method: 'POST',
                body: JSON.stringify({command})
            });
            const data = await res.json();
            output.textContent = data.success ? data.stdout + data.stderr : 'Error: ' + data.error;
        }
    </script>
</body>
</html>'''
    
    def log_message(self, format, *args):
        print(f"[ARC Bridge] {args[0]}")

def run_server():
    print(f"🌉 ARC Subagent Bridge starting on http://localhost:{PORT}")
    print(f"📁 Base directory: {BASE_DIR}")
    print("Press Ctrl+C to stop")
    server = HTTPServer(('localhost', PORT), SubagentBridgeHandler)
    server.serve_forever()

if __name__ == '__main__':
    run_server()
