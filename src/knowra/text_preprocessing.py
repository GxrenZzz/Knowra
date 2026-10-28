from pathlib import Path

def load_statement() -> set[str]:
  project_root = Path(__file__).resolve.parents[2]
  stopward_path = project_root / "config" / "stopward.txt"

  with stopward_path.open("r",encoding="utf-8") as file:
    return{
      line.strip().lower()
      for line in file
      if line.strip()
    }

  