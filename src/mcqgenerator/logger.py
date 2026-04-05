import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_path=os.path.join(os.getcwd(), 'logs')


os.makedirs(log_path, exist_ok=True)

import os
import logging
from datetime import datetime

# 1. Define the names
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")

# 2. CRITICAL STEP: Create the directory if it's not there
os.makedirs(log_path, exist_ok=True) 

# 3. Join the path and file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# 4. Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)
