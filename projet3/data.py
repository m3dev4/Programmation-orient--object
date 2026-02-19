import json


class SaveDataFile:
    DATA_FILE = "datas.json"

    def __init__(self):
        self.data_file = self.DATA_FILE

    def save_data(self):
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.data_file, file)
        except FileNotFoundError:
            print("error")

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("error")
            return None
