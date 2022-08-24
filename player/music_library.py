from dataclasses import dataclass


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
            self.re_index()
            return True
        else:
            return False

    def re_index(self):
        i = 1
        temp_dict = {}
        for k in self._library:
            temp_dict[i] = self._library[k]
            i += 1
        self._library = temp_dict
        
@dataclass
class Track:
    title: str
    artist: str
    file: str

    def __str__(self):
        return f"{self.title} by {self.artist}"
        