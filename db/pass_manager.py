import json
from json.decoder import JSONDecodeError

import hashlib

from core.logger import logger


class PassDBManager:
    @staticmethod
    def save_pass(hash_word, first_side, sec_side):
        new_data = {hash_word: {"first_side": first_side, "sec_side": sec_side}}
        try:
            with open("./db/base/data.json", "r") as data_file:
                json.load(data_file)
        except (FileNotFoundError, JSONDecodeError) as Err:
            logger.error(Err)
            with open("./db/base/data.json", "w") as data_file:
                data_file.write("{}")
        finally:
            with open("./db/base/data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("./db/base/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    @staticmethod
    def make_hash(first_side, sec_side):
        m = hashlib.sha256(first_side + sec_side)
        return m.hexdigest()

    @staticmethod
    def get_pass(hash_word):
        try:
            with open("./db/base/data.json", "r") as data_file:
                data = json.load(data_file)
                creds = data.get(hash_word)
                if creds:
                    first_side = creds.get("first_side")
                    sec_side = creds.get("sec_side")
                    return first_side, sec_side
                else:
                    return None, None

        except (FileNotFoundError, JSONDecodeError) as Err:
            logger.error(Err)
            with open("./db/base/data.json", "w") as data_file:
                data_file.write("{}")
            return None, None
