import logging

# ハンドラを生成する
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler("tmp.log")

# フォーマット、ログレベル、ハンドラを設定する
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    handlers=[std_handler, file_handler])

logger = logging.getLogger(__name__)
logger.debug("デバッグ出力")
logger.info("情報出力")
logger.warning("警告発生！")
logger.error("エラー発生！！")
