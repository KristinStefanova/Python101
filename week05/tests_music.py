import unittest
from music import Song, Playlist


class SongTests(unittest.TestCase):
    def setUp(self):
        self.one = Song("bbbbb", "nnnnn", "aaaaa", "1:20:3")
        self.two = Song("bbbbb", "nnnnn", "aaaaa", "1:20:3")
        self.three = Song("aaaaa", "nnnnn", "bbbbb", "1:20")

    def test_type_error_init_song(self):
        with self.subTest("test title"):
            with self.assertRaises(TypeError):
                Song(title=13, artist="", album="", length="")

        with self.subTest("test artist"):
            with self.assertRaises(TypeError):
                Song(title="", artist=13, album="", length="")

        with self.subTest("test album"):
            with self.assertRaises(TypeError):
                Song(title="", artist="", album=13, length="")

        with self.subTest("test length"):
            with self.assertRaises(TypeError):
                Song(title="", artist="", album="", length=13)

    def test_song_str_representation(self):
        expected = "bbbbb - nnnnn from aaaaa - 1:20:3"
        self.assertEqual(str(self.one), expected)

    def test_songs_equal_or_not(self):
        with self.subTest("one and two are equal"):
            self.assertTrue(self.one == self.two)

        with self.subTest("one and three are not equal"):
            self.assertFalse(self.one == self.three)

    def test_songs_hash_equal_or_not(self):
        with self.subTest("one and two are equal"):
            self.assertTrue(hash(self.one) == hash(self.two))

        with self.subTest("one and three are not equal"):
            self.assertFalse(hash(self.one) == hash(self.three))

    def test_songs_length(self):
        with self.subTest("without parameters"):
            self.assertEqual(self.one.length(), "1:20:3")

        with self.subTest("seconds"):
            self.assertEqual(self.one.length(seconds=True), 4803)

        with self.subTest("minutes"):
            self.assertEqual(self.one.length(minutes=True), 80)

        with self.subTest("hours"):
            self.assertEqual(self.one.length(hours=True), 1)


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.one = Song("bbb", "aaa", "ccc", "3:36")
        self.two = Song("ddd", "aaa", "eee", "4:20")
        self.three = Song("eee", "aaa", "ccc", "12:28")
        self.four = Song("nnn", "mmm", "ooo", "6:32")
        self.five = Song("sss", "ppp", "rrr", "1:20:03")
        self.six = Song("yyy", "xxx", "zzz", "2:32:15")

        self.playlist_one = Playlist(name="First")
        self.playlist_two = Playlist(name="First", repeat=True)
        self.playlist_three = Playlist(name="First", shuffle=True)
        self.playlist_four = Playlist(name="First", repeat=True, shuffle=True)

        self.list_of_songs = [self.one, self.two, self.three, self.four,
                              self.five, self.six]

    def test_init_playlist(self):
        with self.subTest("test init"):
            Playlist(name="Test_Playlist")

        with self.subTest("test init"):
            Playlist(name="Test_Playlist", repeat=True)

        with self.subTest("test init"):
            Playlist(name="Test_Playlist", shuffle=True)

        with self.subTest("test init"):
            Playlist(name="Test_Playlist", repeat=True, shuffle=True)

    def test_add_song_to_playlist(self):
        expected = [self.one]
        self.playlist_one.add_song(self.one)
        result = self.playlist_one.songs
        self.assertEqual(result, expected)

    def test_add_songs_to_playlist(self):
        expected = [self.one, self.two, self.three, self.four,
                    self.five, self.six]
        self.playlist_one.add_songs(self.list_of_songs)
        result = self.playlist_one.songs
        self.assertEqual(result, expected)

    def test_remove_song_from_playlist(self):
        expected = [self.one, self.three, self.four,
                    self.five, self.six]
        self.playlist_one.add_songs(self.list_of_songs)
        self.playlist_one.remove_song(self.two)
        result = self.playlist_one.songs
        self.assertEqual(result, expected)

    def test_total_length_of_playlist(self):
        expected = "4:19:14"
        self.playlist_one.add_songs(self.list_of_songs)
        result = self.playlist_one.total_length()
        self.assertEqual(result, expected)

    def test_artists_of_playlist(self):
        expected = {
            'aaa': 3,
            'mmm': 1,
            'ppp': 1,
            'xxx': 1
        }
        self.playlist_one.add_songs(self.list_of_songs)
        result = self.playlist_one.artists()
        self.assertDictEqual(result, expected)

    def test_next_song_of_playlist(self):
        with self.subTest("next song without shuffle and repeat"):
            expected = [self.one, self.two, self.three, self.four,
                        self.five, self.six]
            self.playlist_one.add_songs(self.list_of_songs)
            result = []
            for i in range(len(expected)):
                result.append(self.playlist_one.next_song())
            self.assertListEqual(result, expected)

        with self.subTest("next song with repeat without shuffle"):
            expected = [self.one, self.two, self.three,
                        self.four, self.five, self.six,
                        self.one, self.two
                        ]
            self.playlist_two.add_songs(self.list_of_songs)
            result = []
            for i in range(len(expected)):
                result.append(self.playlist_two.next_song())
            self.assertListEqual(result, expected)

        with self.subTest("next song with shuffle without repeat"):
            expected = [self.one, self.two, self.three,
                        self.four, self.five, self.six
                        ]
            self.playlist_three.add_songs(self.list_of_songs)
            result = []
            for i in range(len(expected)):
                result.append(self.playlist_three.next_song())
            self.assertTrue(len(result) == len(expected) and all(
                [result.count(i) == expected.count(i) for i in result]))

        with self.subTest("HOW TO: next song with shuffle with repeat"):
            expected = self.playlist_four.played
            self.playlist_four.add_songs(self.list_of_songs)
            result = []
            for i in range(len(expected)):
                result.append(self.playlist_four.next_song())
            self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
