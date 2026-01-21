import logging, sys, coloredlogs

def setup_logging(level=logging.INFO):
    """
    Setup logging configuration
    :param level: logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :param log_file: log file path
    """
    log_format = '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
    logging.basicConfig(
        level=level,
        format=log_format,
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler(sys.stderr)]
    )

    coloredlogs.install(
        level=level,
        fmt=log_format,
        datefmt='%Y-%m-%d %H:%M:%S'
    )