import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        music_library = MusicLibrary()
        self.assertIsInstance(music_library, MusicLibrary)

    def test_initialses_with_empty_library(self):
        music_library = MusicLibrary()
        self.assertEqual(getattr(music_library, '_library'), {})

    def test_can_add_song_to_library(self):
        music_library = MusicLibrary()
        music_library.add("Creep")
        self.assertEqual(getattr(music_library, '_library'), {1: "Creep"})

    def test_can_two_songs_to_library(self):
        music_library = MusicLibrary()
        music_library.add("Creep")
        music_library.add("Woohoo")
        self.assertEqual(getattr(music_library, '_library'), {1: "Creep", 2: "Woohoo"})

    def test_can_list_all_songs(self):
        music_library = MusicLibrary()
        music_library.add("Creep")
        music_library.add("Woohoo")
        self.assertEqual(music_library.all(), ['Creep', 'Woohoo'])

    def test_can_remove_song_by_index(self):
        music_library = MusicLibrary()
        music_library.add("Creep")
        music_library.add("Woohoo")
        self.assertTrue(music_library.remove(2))
        # self.assertEqual(getattr(music_library, '_library'), {1: "Creep", 2: "Woohoo"})