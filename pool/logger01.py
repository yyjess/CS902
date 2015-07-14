import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("start reading database")

records = {'join':55, 'tom':66}
logger.debug('records:%s',records)
logger.info('updating records...')

logger.info('finish updating records')
