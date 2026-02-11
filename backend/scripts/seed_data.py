import sys
from pathlib import Path

# Add backend root to PYTHONPATH
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from app.core.database import SessionLocal
from app.seed.seed_categories import seed_categories


def run():
    db = SessionLocal()
    try:
        seed_categories(db)
        print("Categories and subcategories seeded successfully.")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    run()
