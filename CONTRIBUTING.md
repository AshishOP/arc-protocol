# Contributing

We want this tool to be the best "Parallel Agent" runner available. Here is how you can help.

## Development Setup

1.  **Environment:** We use a standard Python `venv`.
    ```bash
    python3 setup_arc.py
    ```

2.  **Running Locally:**
    The dashboard is the main UI. Run it with `./dash`.
    The tools logic lives in `.agent/tools/`.

## What we need help with

*   **Skills:** New personas for `.agent/skills/definitions/`. We need better specific roles (e.g., `sql-optimizer`, `accessibility-auditor`).
*   **Workflows:** The logic in `.agent/workflows/` defines how the AI thinks. If you find a better prompt for `/arc-plan`, PR it.
*   **Dashboard:** Improvements to `monitor.py` (Textual UI) to show more useful real-time data.

## Rules for PRs

1.  **No breaking the pathing.** Windows support is hard-won. Do not use hardcoded `/` separators. Use `os.path.join` or `pathlib`.
2.  **No external API keys.** The system MUST rely on the `gemini` CLI for auth. Do not add `GEMINI_API_KEY` requirements.
3.  **Keep it lightweight.** We want ARC to feel like a standard unix tool.

Thanks for hacking with us.
