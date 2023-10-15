import csv
import hashlib
import json
import os
import random
from json.decoder import JSONDecodeError

from core.logger import logger


class WordsDBManager:
    @staticmethod
    def save_words(path):
        try:
            new_data = {}
            reader = csv.reader(open(path, encoding="utf-8"))
            for line in reader:
                new_data[line[0]] = line[1]
            with open("./src/db/base/data.json", "r") as data_file:
                json.load(data_file)
        except (FileNotFoundError, JSONDecodeError, IndexError) as Err:
            logger.error(Err)
            with open("./src/db/base/data.json", "w") as data_file:
                data_file.write("{}")
        finally:
            with open("./src/db/base/data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("./src/db/base/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    @staticmethod
    def get_word():
        try:
            with open("./src/db/base/data.json", "r") as data_file:
                data = json.load(data_file)
                creds = random.choice(list(data.items()))
                if creds:
                    return creds[0], creds[1]
                else:
                    return None, None

        except (FileNotFoundError, JSONDecodeError, IndexError) as Err:
            logger.error(Err)
            with open("./src/db/base/data.json", "w") as data_file:
                data_file.write("{}")
            return None, None

    @staticmethod
    def delete_words():
        try:
            os.remove("./src/db/base/data.json")
            with open("./src/db/base/data.json", "w") as data_file:
                data_file.write("{}")
        except FileNotFoundError as Err:
            logger.error(Err)
