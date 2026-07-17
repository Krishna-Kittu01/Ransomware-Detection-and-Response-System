from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from app.core.logger import logger
from app.database.database import insert_event
from app.core.entropy import file_entropy
import time


class FileMonitor(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"[CREATED] {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:

            logger.info(f"[MODIFIED] {event.src_path}")

            try:
                entropy = file_entropy(event.src_path)

                if entropy > 7.5:
                    status = "Suspicious"
                else:
                    status = "Normal"

            except Exception:
                entropy = 0.0
                status = "Error"

            insert_event(
                event.src_path,
                "MODIFIED",
                entropy,
                status
            )

            logger.info(f"Entropy: {entropy:.2f} | Status: {status}")

    def on_deleted(self, event):
        if not event.is_directory:
            logger.info(f"[DELETED] {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            logger.info(f"[RENAMED] {event.src_path} -> {event.dest_path}")


def start_monitor(path):
    observer = Observer()
    handler = FileMonitor()

    observer.schedule(handler, path, recursive=True)
    observer.start()

    logger.info(f"Monitoring started on: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()