import logging
import logging.config
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
            self.config_path = os.path.dirname(os.path.realpath(__file__)) + "_logger.conf"
        
        self.apply_config()

    def apply_config(self):
        """
            Appying current config
        """
        with open(self.config_path) as f:
            self.config = json.load(f) 
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fname = self.config["handlers"]["file"]["filename"] 
        self.config["handlers"]["file"]["filename"] = path + self.get_correct_slash() + fname 
        print(self.config["handlers"]["file"]["filename"])         
        logging.config.dictConfig(self.config)

    def get_correct_slash(self):
        if os.name == "nt":
            return "\\"
        else:
            return "/"

    def get_logger(self, name = "COMBAT"):
        """
            Retunr logger with current configs, by passing name
        """
        return logging.getLogger(name)