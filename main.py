from app.core.logger import logger
from app.core.entropy import file_entropy

logger.info("RDRS Started Successfully")

entropy = file_entropy("data/sandbox/hello.txt")

print(f"\nEntropy of hello.txt: {entropy:.2f}")