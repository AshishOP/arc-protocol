#!/usr/bin/env python3
"""
ARC Protocol - MCP Server for Subagent File Operations

This implements the Model Context Protocol (MCP) to provide
file read/write tools directly to AI agents and subagents.

Based on the MCP specification: https://modelcontextprotocol.io
"""

import sys
import json
import os

# MCP Protocol implementation
class MCPServer:
    def __init__(self):
        self.tools = {
            "arc_read_file": {
                "name": "arc_read_file",
                "description": "Read the contents of a file from the workspace",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path to the file to read (relative to workspace)"
                        }
                    },
                    "required": ["path"]
                }
            },
            "arc_write_file": {
                "name": "arc_write_file", 
                "description": "Write content to a file in the workspace",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path to the file to write (relative to workspace)"
                        },
                        "content": {
                            "type": "string",
                            "description": "Content to write to the file"
                        }
                    },
                    "required": ["path", "content"]
                }
            },
            "arc_list_dir": {
                "name": "arc_list_dir",
                "description": "List contents of a directory",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path to the directory to list"
                        }
                    },
                    "required": ["path"]
                }
            },
            "arc_exec": {
                "name": "arc_exec",
                "description": "Execute a shell command",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "Command to execute"
                        }
                    },
                    "required": ["command"]
                }
            },
            "arc_update_dashboard": {
                "name": "arc_update_dashboard",
                "description": "Update the ARC dashboard state",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "agent": {"type": "string", "description": "Agent name (Architect/Executor/Reviewer)"},
                        "status": {"type": "string", "description": "Status (WORKING/DONE/IDLE)"},
                        "task": {"type": "string", "description": "Current task description"}
                    }
                }
            },
            "arc_dispatch_worker": {
                "name": "arc_dispatch_worker",
                "description": "Dispatch a task to background worker daemon",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "task_type": {"type": "string", "description": "Task type: read_file, write_file, exec, batch_write"},
                        "path": {"type": "string", "description": "File path (for read/write)"},
                        "content": {"type": "string", "description": "Content to write"},
                        "files": {
                            "type": "array", 
                            "description": "Array of {path, content} for batch_write",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "path": {"type": "string"},
                                    "content": {"type": "string"}
                                },
                                "required": ["path", "content"]
                            }
                        }
                    },
                    "required": ["task_type"]
                }
            },
            "arc_spawn_agent": {
                "name": "arc_spawn_agent",
                "description": "Spawn a parallel background agent to handle a sub-task",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "agent_id": {"type": "string", "description": "Unique ID for this background agent (e.g., 'Stylist', 'Refactorer')"},
                        "task": {"type": "string", "description": "Detailed task description for the background agent"},
                        "model": {"type": "string", "description": "Optional: AI model to use (default: gemini-1.5-flash)"},
                        "skill": {"type": "string", "description": "Optional: Skill to inject (researcher, coder, auditor, architect, debugger). Default: general"}
                    },
                    "required": ["agent_id", "task"]
                }
            }
        }
        self.workspace = os.getcwd()

    def handle_initialize(self, params):
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "arc-mcp-server",
                "version": "1.0.0"
            }
        }

    def handle_tools_list(self, params):
        return {"tools": list(self.tools.values())}

    def handle_tools_call(self, params):
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        try:
            if tool_name == "arc_read_file":
                return self.read_file(arguments["path"])
            elif tool_name == "arc_write_file":
                return self.write_file(arguments["path"], arguments["content"])
            elif tool_name == "arc_list_dir":
                return self.list_dir(arguments["path"])
            elif tool_name == "arc_exec":
                return self.exec_command(arguments["command"])
            elif tool_name == "arc_update_dashboard":
                return self.update_dashboard(arguments)
            elif tool_name == "arc_dispatch_worker":
                return self.dispatch_worker(arguments)
            elif tool_name == "arc_spawn_agent":
                return self.spawn_agent(arguments)
            else:
                return {"isError": True, "content": [{"type": "text", "text": f"Unknown tool: {tool_name}"}]}
        except Exception as e:
            return {"isError": True, "content": [{"type": "text", "text": str(e)}]}

    def read_file(self, path):
        full_path = os.path.join(self.workspace, path)
        with open(full_path, 'r') as f:
            content = f.read()
        return {"content": [{"type": "text", "text": content}]}

    def write_file(self, path, content):
        full_path = os.path.join(self.workspace, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
        return {"content": [{"type": "text", "text": f"Written to {path}"}]}

    def list_dir(self, path):
        full_path = os.path.join(self.workspace, path)
        items = os.listdir(full_path)
        return {"content": [{"type": "text", "text": "\n".join(items)}]}

    def exec_command(self, command):
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=self.workspace)
        output = result.stdout + result.stderr
        return {"content": [{"type": "text", "text": output}]}

    def update_dashboard(self, args):
        state_file = os.path.join(self.workspace, ".arc", "arc_workflow_state.json")
        if os.path.exists(state_file):
            with open(state_file, 'r') as f:
                state = json.load(f)
        else:
            state = {"agents": {}, "logs": []}
        
        agent = args.get("agent", "Main")
        if agent not in state.get("agents", {}):
            state.setdefault("agents", {})[agent] = {"status": "IDLE", "task": ""}
        
        if args.get("status"):
            state["agents"][agent]["status"] = args["status"]
        if args.get("task"):
            state["agents"][agent]["task"] = args["task"]
        
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)
        
        return {"content": [{"type": "text", "text": "Dashboard updated"}]}

    def spawn_agent(self, args):
        import subprocess
        agent_id = args.get("agent_id")
        task = args.get("task")
        # Use env var for default, fallback to flash
        default_model = os.environ.get("GEMINI_MODEL", "flash")
        model = args.get("model", default_model)
        skill = args.get("skill", "general")
        
        script_path = os.path.join(self.workspace, ".agent", "workers", "background_agent.py")
        
        # Start the background agent process
        subprocess.Popen(
            [sys.executable, script_path, agent_id, task, model, skill],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        
        return {"content": [{"type": "text", "text": f"Background agent '{agent_id}' spawned for task: {task} (Model: {model}, Skill: {skill})"}]}

    def dispatch_worker(self, args):
        queue_file = os.path.join(self.workspace, ".arc", "state", "worker_queue.json")
        os.makedirs(os.path.dirname(queue_file), exist_ok=True)
        
        if os.path.exists(queue_file):
            with open(queue_file, 'r') as f:
                data = json.load(f)
        else:
            data = {"tasks": []}
            
        import uuid
        args["id"] = str(uuid.uuid4())[:8]
        data["tasks"].append(args)
        
        with open(queue_file, 'w') as f:
            json.dump(data, f, indent=2)
            
        return {"content": [{"type": "text", "text": f"Task queued for background worker (ID: {args['id']})"}]}

    def process_message(self, message):
        method = message.get("method")
        params = message.get("params", {})
        msg_id = message.get("id")
        
        if method == "initialize":
            result = self.handle_initialize(params)
        elif method == "tools/list":
            result = self.handle_tools_list(params)
        elif method == "tools/call":
            result = self.handle_tools_call(params)
        elif method == "notifications/initialized":
            return None  # No response needed
        else:
            result = {"error": {"code": -32601, "message": f"Unknown method: {method}"}}
        
        if msg_id is not None:
            return {"jsonrpc": "2.0", "id": msg_id, "result": result}
        return None

    def run(self):
        """Run the MCP server using stdio transport"""
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                message = json.loads(line)
                response = self.process_message(message)
                
                if response:
                    sys.stdout.write(json.dumps(response) + "\n")
                    sys.stdout.flush()
                    
            except json.JSONDecodeError:
                continue
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": str(e)}
                }
                sys.stdout.write(json.dumps(error_response) + "\n")
                sys.stdout.flush()

if __name__ == "__main__":
    server = MCPServer()
    server.run()
