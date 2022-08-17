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
