import ConfigParser
import os

def read_config(c, section, key):
    try:
        c.get(section, key)
    except:
        return None

config = ConfigParser.ConfigParser()
config.read('parameters.ini')
GLOBALS = dict()
GLOBALS['env'] = os.getenv('BROWSER', 'firefox')
