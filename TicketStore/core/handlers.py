import pickle


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_list_data(self):
        try:
            with open(self.file_path, "rb") as file:
                return pickle.load(file)

        except FileNotFoundError:
            with open(self.file_path, "wb") as file:
                pickle.dump([], file)
                return []

    def update(self, data: list):
        with open(self.file_path, "wb") as file:
            pickle.dump(data, file)

    def append(self, item):
        data = self.get_list_data() or []
        data.append(item)

        self.update(data)
