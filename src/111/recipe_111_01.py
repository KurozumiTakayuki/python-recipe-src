import logging

format_str = '%(asctime)s - %(process)d - %(thread)d - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)

logger = logging.getLogger(__name__)
logger.debug("デバッグ出力")
logger.info("情報出力")
logger.warning("警告発生！")
logger.error("エラー発生！！")
