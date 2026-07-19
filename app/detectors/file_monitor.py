from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from app.core.logger import logger
from app.database.database import insert_event
from app.core.entropy import file_entropy
from app.core.config import config
from app.response.alert import ransomware_alert
from app.response.quarantine import quarantine_file
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

                threshold = config.get("thresholds")["entropy"]

                if entropy > threshold:
                    status = "Suspicious"

                    ransomware_alert(
                        event.src_path,
                        entropy
                    )

                    quarantine_file(
                        event.src_path
                    )

                else:
                    status = "Normal"

            except Exception as e:
                logger.error(f"Error analyzing file: {e}")
                entropy = 0.0
                status = "Error"

            insert_event(
                event.src_path,
                "MODIFIED",
                entropy,
                status
            )

            logger.info(
                f"Entropy: {entropy:.2f} | Status: {status}"
            )

    def on_deleted(self, event):
        if not event.is_directory:
            logger.info(f"[DELETED] {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            logger.info(
                f"[RENAMED] {event.src_path} -> {event.dest_path}"
            )


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