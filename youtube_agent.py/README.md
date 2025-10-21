```markdown
# youtube-content-manager

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Provide your Gemini API key via environment or a `.env` file in the project root:

```
GEMINI_API_KEY="REPLACE_WITH_YOUR_ACTUAL_API_KEY"
```

3. Run the script:

```bash
source .venv/bin/activate
python ../your_script.py
```

The script will read `GEMINI_API_KEY` from the environment. If a `.env` file exists the project will load it automatically (uses `python-dotenv` when available, with a safe fallback parser).

```
# youtube-content-manager