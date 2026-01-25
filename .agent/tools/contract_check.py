import os
import re
import sys
from rich.console import Console
from rich.table import Table

console = Console()

def parse_contracts(contract_file):
    if not os.path.exists(contract_file):
        return None
    
    with open(contract_file, "r") as f:
        content = f.read()

    models = {}
    apis = []
    
    current_model = None
    for line in content.split("\n"):
        line = line.strip()
        # API Match: #### GET /path
        api_match = re.match(r"#### (\w+) ([\./]?\S+)", line)
        if api_match:
            method, path = api_match.groups()
            # Intelligent cleanup: only strip leading / or ./
            clean_path = path
            if clean_path.startswith("./"):
                clean_path = clean_path[2:]
            elif clean_path.startswith("/"):
                clean_path = clean_path[1:]
            
            apis.append((method, clean_path))
            continue

        if line.startswith("#### ") and not ("/" in line):
            current_model = line.replace("#### ", "").strip()
            models[current_model] = []
            continue
            
        if line.startswith("- `") and ":" in line and current_model:
            parts = re.findall(r"`(\w+)`: `(\w+)`", line)
            if parts:
                models[current_model].append(parts[0])

    return {"apis": apis, "models": models}

def check_codebase(contracts):
    violations = []
    console.print("[yellow][*] Auditing implementation with path awareness...[/yellow]")
    
    for method, clean_path in contracts["apis"]:
        # 1. Direct file check
        if os.path.exists(clean_path):
            continue
            
        # 2. String search in code (fallback)
        cmd = f"grep -rn \"{clean_path}\" . --exclude-dir=.arc --exclude-dir=.agent --exclude-dir=node_modules --exclude-dir=.git"
        output = os.popen(cmd).read()
        
        if not output:
            violations.append(f"MISSING: {method} {clean_path}")

    return violations

def main():
    contract_path = ".arc/CONTRACTS.md"
    if not os.path.exists(contract_path):
        console.print("[red][ERROR] .arc/CONTRACTS.md not found.[/red]")
        sys.exit(1)

    contracts = parse_contracts(contract_path)
    if not (contracts and (contracts["apis"] or contracts["models"])):
        console.print("[red][ERROR] Could not parse any definitions from CONTRACTS.md.[/red]")
        sys.exit(1)

    table = Table(title="ARC Contract Registry")
    table.add_column("Type", style="cyan")
    table.add_column("Definition", style="magenta")

    for method, path in contracts["apis"]:
        table.add_row("API", f"{method} {path}")
    for model in contracts["models"]:
        table.add_row("Model", model)

    console.print(table)

    violations = check_codebase(contracts)
    if not violations:
        console.print("\n[green][✓] Codebase complies with all ARC Contracts.[/green]")
    else:
        for v in violations:
            console.print(f"[red][!] {v}[/red]")

if __name__ == "__main__":
    main()
