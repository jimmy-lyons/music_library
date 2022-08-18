class MusicLibrary:
    def __init__(self):
        self._library = {}
    
    def add(self, song):
        song_index = len(self._library) + 1
        self._library[song_index] = song

    def all(self):
        return list(self._library.values())

    def remove(self, index):
        if index in self._library:
            del self._library[index]
            return True
        else:
            return False
