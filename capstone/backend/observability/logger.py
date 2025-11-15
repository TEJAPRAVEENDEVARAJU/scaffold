from loguru import logger

# Simple wrapper; extend with tracing / metrics
logger.add("autoapply.log", rotation="10 MB")
