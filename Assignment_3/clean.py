from pathlib import Path
import shutil


def remove_dir(path: Path) -> None:
    """Delete directory path if it exists."""
    if path.exists() and path.is_dir():
        shutil.rmtree(path)


def remove_all_pycache(root: Path) -> None:
    """Remove every __pycache__ directory under root."""
    for pycache_dir in root.rglob("__pycache__"):
        remove_dir(pycache_dir)


def main() -> None:
    root = Path(__file__).resolve().parent
    remove_dir(root / "venv")
    remove_all_pycache(root)


if __name__ == "__main__":
    main()

