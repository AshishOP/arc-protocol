import os
import sys
import argparse
import difflib

def load_existing_files(root_dir="."):
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        if ".git" in root or ".arc" in root or "node_modules" in root or "venv" in root:
            continue
        for f in files:
            # Store relative path
            rel_path = os.path.relpath(os.path.join(root, f), root_dir)
            file_list.append(rel_path)
    return file_list

def check_redundancy(processed_target, existing_files):
    target_name = os.path.basename(processed_target)
    target_stem = os.path.splitext(target_name)[0]
    
    warnings = []
    
    for existing in existing_files:
        existing_name = os.path.basename(existing)
        existing_stem = os.path.splitext(existing_name)[0]
        
        # 1. Direct Name Match in different folder
        if target_name == existing_name:
             warnings.append(f"CRITICAL: File '{existing}' already exists with identical name.")
             continue

        # 2. Fuzzy Similarity (Simple Difflib)
        # Check similarity of filenames
        ratio = difflib.SequenceMatcher(None, target_stem.lower(), existing_stem.lower()).ratio()
        if ratio > 0.8: # High similarity threshold
            warnings.append(f"WARNING: '{existing}' is very similar to target '{target_name}'. Check for redundancy.")

        # 3. Keyword Heuristic (e.g. both have 'date')
        # This is a basic implementation of the "Solution Architect" logic
        common_terms = ['utils', 'helper', 'service', 'manager', 'client']
        for term in common_terms:
            if term in target_stem.lower() and term in existing_stem.lower():
                # If they share a generic suffix, check the prefix
                target_prefix = target_stem.lower().replace(term, "")
                existing_prefix = existing_stem.lower().replace(term, "")
                if target_prefix and existing_prefix and target_prefix == existing_prefix:
                     warnings.append(f"WARNING: Structural Redundancy? '{existing}' might already handle {term} logic for '{target_prefix}'.")

    return warnings

def main():
    parser = argparse.ArgumentParser(description="ARC Solution Architect Validator")
    parser.add_argument("target_file", help="The file path you intend to create")
    args = parser.parse_args()

    print(f"\033[94m[*] Validating Architecture for: {args.target_file}...\033[0m")
    
    existing_files = load_existing_files()
    warnings = check_redundancy(args.target_file, existing_files)

    if not warnings:
        print(f"\033[92m[✓] Architecture Check Passed. No obvious redundancies found.\033[0m")
        sys.exit(0)
    else:
        print(f"\033[93m[!] ARCHITECTURE CONFLICTS DETECTED:\033[0m")
        for w in warnings:
            print(f"  - {w}")
        print(f"\033[93m    Please verify if you truly need this new file.\033[0m")
        sys.exit(1) # Fail exit code to pause the agent

if __name__ == "__main__":
    main()
