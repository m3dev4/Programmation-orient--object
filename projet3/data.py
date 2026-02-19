import json
import os


class SaveDataFileDepense:
    DATA_FILE = "datas.json"

    def __init__(self):
        self.data_file = self.DATA_FILE

    def save_data(self, data):
        try:
            with open(self.data_file, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print("Erreur lors de la sauvegarde :", e)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return []
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []


class SaveDataFileCategorie:
    DATA_FILE = "datasCateg.json"

    def __init__(self):
        self.data_file = self.DATA_FILE

    def save_data(self, data):
        try:
            with open(self.data_file, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print("Erreur lors de la sauvegarde :", e)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return []
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
