import os
from pathlib import Path

# Attempt to load environment variables from a .env file when available.
# Prefer python-dotenv if installed, otherwise fall back to a tiny safe parser.
def _load_dotenv(path: str = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        return

    try:
        # Try to use python-dotenv if available
        from dotenv import load_dotenv

        load_dotenv(dotenv_path=env_path)
        return
    except Exception:
        # Fallback: simple parser that handles KEY=VALUE lines and strips quotes
        try:
            with env_path.open("r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip()
                    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                        v = v[1:-1]
                    # Don't overwrite already set environment variables
                    if k not in os.environ:
                        os.environ[k] = v
        except Exception:
            # If anything goes wrong, don't crash here; we'll validate later
            return


# Load `.env` from repo root if present
_load_dotenv(Path(__file__).parent / ".env")

# ...existing code...

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Set GEMINI_API_KEY in the environment or add it to a .env file in the project root.\n"
        "If using a .env file, format it as: GEMINI_API_KEY=\"your_key_here\" (quotes optional)."
    )

# ...existing code...