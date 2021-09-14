import logging
from logging.handlers import TimedRotatingFileHandler

def create_timed_rotating_logger( path, name ):

    logger = logging.getLogger( name )
    logger.setLevel( logging.DEBUG )

    handler = TimedRotatingFileHandler( path,
                                       when="h",
                                       interval=1,
                                       backupCount=48 )

    formatter = logging.Formatter( '%(asctime)s %(levelname)s - %(message)s' )
    handler.setFormatter( formatter )

    logger.addHandler( handler )

    return logger
