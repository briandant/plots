from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.todoenv'
load_dotenv(dotenv_path=env_path)

TODO_DIR = "/Users/chaz/Dropbox/todo"
TODO_FILE = f"{TODO_DIR}/todo.txt"
DONE_FILE = f"{TODO_DIR}/done.txt"
REPORT_FILE = f"/{TODO_DIR}/report.txt"
