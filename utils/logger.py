import logging
import os
from datetime import datetime

def get_logger(name):
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger
    
    logger.setLevel(logging.INFO) 
 
    root_dir = os.path.dirname(os.path.dirname(__file__)) 
    logs_dir = os.path.join(root_dir, "logs") 
    os.makedirs(logs_dir, exist_ok=True) 
 
    log_file = os.path.join( 
        logs_dir, 
        f"test_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log" 
    ) 
 
    file_handler = logging.FileHandler(log_file) 
    formatter = logging.Formatter( 
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s" 
    ) 
 
    file_handler.setFormatter(formatter) 
    logger.addHandler(file_handler) 
 
    return logger