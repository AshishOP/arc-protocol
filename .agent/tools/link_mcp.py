import os
import json
import sys
from pathlib import Path

def link_mcp():
    print("🚀 ARC Bridge Auto-Linker v2.1")
    
    # Define paths
    script_dir = Path(__file__).parent.absolute()

    # Possible locations for the MCP server (some installs put it under .agent/mcp)
    candidate_paths = [
        script_dir / "mcp" / "arc_mcp_server.py",
        script_dir.parent / "mcp" / "arc_mcp_server.py",
    ]

    mcp_path = None
    for p in candidate_paths:
        if p.exists():
            mcp_path = p
            break

    if mcp_path is None:
        print(f"❌ Error: MCP Server not found. Checked: {', '.join(str(p) for p in candidate_paths)}")
        return
    else:
        print(f"Found MCP Server at: {mcp_path}")

    # MCP Config Structure
    mcp_config = {
        "mcpServers": {
            "arc-bridge": {
                "command": "python3",
                "args": [str(mcp_path)],
                "env": {
                    "GEMINI_MODEL": "flash"
                }
            }
        }
    }

    # Potential Config Locations
    locations = []
    
    if sys.platform == "linux" or sys.platform == "darwin":
        # Claude Desktop (Common MCP Target)
        locations.append(Path.home() / ".config" / "Claude" / "claude_desktop_config.json")
        # Windsurf / specialized IDEs Often use a global config
        locations.append(Path.home() / ".codeium" / "windsurf" / "mcp_config.json")
    elif sys.platform == "win32":
        # Windows AppData
        appdata = Path(os.environ.get("APPDATA", ""))
        locations.append(appdata / "Claude" / "claude_desktop_config.json")
        locations.append(Path.home() / ".codeium" / "windsurf" / "mcp_config.json")

    # Check for OpenCode specifically (if it has a unique path)
    # Most VS Code forks use ~/.config/[IDE_NAME]/...
    
    found_any = False
    for loc in locations:
        try:
            loc.parent.mkdir(parents=True, exist_ok=True)
            
            # Read existing config if it exists
            current_data = {"mcpServers": {}}
            if loc.exists():
                with open(loc, 'r') as f:
                    try:
                        current_data = json.load(f)
                    except:
                        pass
            
            # Merge
            if "mcpServers" not in current_data:
                current_data["mcpServers"] = {}
                
            current_data["mcpServers"]["arc-bridge"] = mcp_config["mcpServers"]["arc-bridge"]
            
            # Write back
            with open(loc, 'w') as f:
                json.dump(current_data, f, indent=2)
            
            print(f"✅ Successfully linked to: {loc}")
            found_any = True
        except Exception as e:
            print(f"⚠️  Skipped {loc}: {e}")

    if not found_any:
        print("\n❌ Could not find a standard MCP config location.")
        print("Please copy the JSON below manually into your IDE's MCP settings:")
        print("-" * 20)
        print(json.dumps(mcp_config, indent=2))
        print("-" * 20)

if __name__ == "__main__":
    link_mcp()
