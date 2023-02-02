import os
import dotenv

dotenv.load_dotenv()

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY is not set")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
