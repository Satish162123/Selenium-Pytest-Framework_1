import configparser 
import os 
 
class ConfigReader: 
    _config = None 
 
    @classmethod 
    def _load_config(cls): 
        if cls._config is None: 
            config_path = os.path.join( 
                os.path.dirname(os.path.dirname(__file__)), 
                "config.ini" 
            ) 
            cls._config = configparser.ConfigParser() 
            cls._config.read(config_path) 
 
    @classmethod 
    def get(cls, section, key): 
        cls._load_config() 
        return cls._config.get(section, key)