from app.database.database import init_database
from app.detectors.file_monitor import start_monitor

if __name__ == "__main__":
    init_database()
    start_monitor("data/sandbox")