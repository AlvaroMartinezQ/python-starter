# Script stores the logs of the ping call in a .log file

import logging

def store_logs(status, web, checks):
    logger = logging.getLogger('web_availability')
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler('web.log')
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info(f'Ping to domain: {web}, returned a status of: {status} after {checks} checks')
