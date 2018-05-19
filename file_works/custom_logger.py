import logging
import os
import json

class CustomLogger():
    """
        Incapsulates logger operations
    """
    def __init__(self, config_path = None):
        """
            Configuring path to configuration file
        """
        if config_path:
            self.config_path = config_path
        else:
            self.config_path = os.path.dirname(os.path.realpath(__file__)) + "logger.config"
        
        self.apply_config()
    


    def apply_config(self):
        """
            Appying current config
        """
        with open(self.config_path) as f:
            self.config = json.load(f)      
        logging.config.dictConfig(self.config)

    def get_logger(self, name = "COMBAT"):
        """
            Retunr logger with current configs, by passing name
        """
        return logging.getLogger(name)