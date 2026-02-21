def handle_log_file():
    try:
        with open('server.log', 'r') as file:
            content = file.read()
            # You can process `content` here or call other functions
            # extractor(content)
            # error_detect(content)
            # error_extract(content)
            # sum_logs()
    except FileNotFoundError as e:
        print(f"Log file not found: {e}")

##2
class InvalidConfigError(Exception):
    """Raised when the configuration file is invalid."""
    pass

import json

def load_config(filepath):
    try:
        with open(filepath, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found.")
    except json.JSONDecodeError:
        raise InvalidConfigError("Invalid JSON format in config file.")

    required_keys = ['database_url', 'api_key', 'mode']
    for key in required_keys:
        if key not in config:
            raise InvalidConfigError(f"The key '{key}' doesn't exist in the config file.")

    if config['mode'] not in ['debug', 'production']:
        raise InvalidConfigError("The value of 'mode' must be either 'debug' or 'production'.")

    return config

#_3
import json
import os


class InvalidConfigError(Exception):
    def __init__(self, message):
        self.message = message
        print(f"{self.message}")

def load_config(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"file {filepath}' not found")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"jason format not found {e.msg}", e.doc, e.pos)

    required_keys = ['api_key', 'database_url', 'mode']
    for key in required_keys:
        if key not in config:
            raise InvalidConfigError(f"the emergenssy key '{key}' dosent exist on setting file")

    if config['mode'] not in ['debug', 'production']:
        raise InvalidConfigError("the value of 'mode' should be 'debug' or 'production'.")

    return config


#_4
def main():
    config_path = "config.json"

    try:
        config = load_config(config_path)
        print(" Configuration loaded successfully:")
        print(config)

    except FileNotFoundError:
        print("Error: Configuration file not found. Please make sure 'config.json' exists in the correct path.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format. Please ensure the file contains valid JSON.")

    except InvalidConfigError as e:
        print(f"Configuration error: {e}")

    except Exception as e:
        print(f"unexpected error occurred: {e}")

if __name__ == "__main__":
    main()