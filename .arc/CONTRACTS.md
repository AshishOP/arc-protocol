# 📜 ARC Protocol: Internal Contracts

This file defines the strict internal rules for the Antigravity AI repository.

### **Section 1: Tool Registry**

#### GET .agent/tools/map_topology.py
- **Input:** Root Directory
- **Output:** Mermaid.js Topology

#### POST .agent/dashboard/update.py
- **Payload:** JSON State
- **Mutation:** Atomic File Lock

### **Section 2: Data Models**

#### AgentState
- `id`: `String`
- `status`: `Enum (IDLE, WORKING, DONE, ERROR)`
- `task`: `String`

#### RegistryUpdate
- `timestamp`: `DateTime`
- `author`: `AgentID`
