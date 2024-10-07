import os
import json

from PySide6.QtCore import Qt

from PySide6.QtCore import QAbstractListModel


class DirWalker:
    def __init__(self, address, jsonfile):
        self.dbName = jsonfile
        self.address = address

    def moveToJson(self):
        musics = []

        # Get All musics files with paths
        for root, dirs, files in os.walk(self.address, topdown=True):
            for file in files:
                if file.endswith(".mp3"):
                    fileAddress = root + "\\" + file

                    musics.append((fileAddress, file))

        self.__commitInJson(musics)

    def __commitInJson(self, data):
        with open(f"{self.dbName}", "w") as db:
            json.dump(data, db)

    def load(self):
        try:
            with open(f"{self.dbName}", "r") as f:
                return json.load(f)
        except:
            return

    def save(self):
        pass


class PlayerModel(QAbstractListModel):
    def __init__(self, data):
        super().__init__()
        self.playlist = data or []

    def data(self, index, role):
        address, trackName = self.playlist[index.row()]

        if role == Qt.DisplayRole:
            return trackName

    def rowCount(self, index=None):
        return len(self.playlist)


