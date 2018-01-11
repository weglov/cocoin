import logging
from app.grab import update_coin_list

logger = logging.getLogger(__name__)

update_coin_list()
logger.info('Update coin list')