import logging
import logging.config
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] line - %(lineno)d %(name)s %(levelname)s in %(module)s: %(message)s",
    level=logging.INFO
)

# logging.info('Hii')