from app.core.logger import logger


def ransomware_alert(file_path, entropy):
    logger.warning("=" * 60)
    logger.warning("🚨 RANSOMWARE ALERT 🚨")
    logger.warning(f"File       : {file_path}")
    logger.warning(f"Entropy    : {entropy:.2f}")
    logger.warning("Status     : Suspicious")
    logger.warning("Action     : Simulation Mode (No file moved)")
    logger.warning("=" * 60)