import os
import shutil
from app.core.logger import logger
from app.core.config import config


def quarantine_file(file_path):
    """
    Move suspicious file into quarantine folder.
    """

    response = config.get("response")

    simulation = response["simulation_mode"]
    quarantine_dir = response["quarantine_dir"]

    os.makedirs(quarantine_dir, exist_ok=True)

    if simulation:
        logger.warning("Simulation Mode Enabled")
        logger.warning(f"Would move: {file_path}")
        logger.warning(f"Destination: {quarantine_dir}")
        return

    try:
        filename = os.path.basename(file_path)

        destination = os.path.join(
            quarantine_dir,
            filename
        )

        shutil.move(file_path, destination)

        logger.success(
            f"File moved to quarantine: {destination}"
        )

    except Exception as e:
        logger.error(f"Quarantine failed: {e}")