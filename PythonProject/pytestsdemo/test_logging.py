import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandlerObj = logging.FileHandler('logfile.log')
    logger.addHandler(fileHandlerObj)

    formats = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandlerObj.setFormatter(formats)

    logger.setLevel(logging.DEBUG)
    logger.debug("A Debug statement is executed")
    logger.info("Information statement is executed")
    logger.warning("A warning statement is executed")
    logger.error("A error statement is executed")
    logger.critical("A critical statement is executed")