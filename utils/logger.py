import logging
from datetime import datetime
import os

def setup_logger(name: str, log_dir:str = "logs") -> logging.Logger:
    os.makedirs(log_dir,exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f'{name}_{timestamp}.log')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG) #write log to file
    console_handler = logging.StreamHandler() 
    console_handler.setLevel(logging.INFO)#write log to terminal
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger 

print(setup_logger("log_test"))