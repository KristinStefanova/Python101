from random import sample
import tabulate
import json
import os
import mutagen.mp3


class Song:
    def __init__(self, title, artist, album, song_len):
        if type(title) is not str or\
            type(artist) is not str or\
            type(album) is not str or\
                type(song_len) is not str:
            raise TypeError
        if ':' not in song_len:
            raise ValueError
        self.title = title
        self.artist = artist
        self.album = album
        self.song_len = song_len

    def __str__(self):
        return
        f'{self.title} - {self.artist} from {self.album} - {self.song_len}'

    def __repr__(self):
        return f'{self.title} - {self.artist} - {self.song_len}'

    def __eq__(self, other):
        return self.title == other.title and\
            self.artist == other.artist and\
            self.album == other.album and\
            self.song_len == other.song_len

    def __hash__(self):
        return hash(str(self))

    def length(self, seconds=False, minutes=False, hours=False):
        temp = self.song_len.split(':')
        if seconds and not minutes and not hours:
            if len(temp) == 3:
                return int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])
            if len(temp) == 2:
                return int(temp[0]) * 60 + int(temp[1])
        elif minutes and not seconds and not hours:
            if len(temp) == 3:
                return int(temp[0]) * 60 + int(temp[1])
            if len(temp) == 2:
                return int(temp[0])
        elif hours and not seconds and not minutes:
            return int(temp[0])
        else:
            return self.song_len


class Playlist:
    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.played = []

    def add_song(self, Song):
        self.songs.append(Song)

    def remove_song(self, Song):
        self.songs.remove(Song)

    def add_songs(self, songs):
        self.songs.extend(songs)

    def total_length(self):
        total_in_seconds = sum([song.length(seconds=True)
                                for song in self.songs])
        hours = total_in_seconds // 3600
        minutes = (total_in_seconds % 3600) // 60
        seconds = total_in_seconds % 60
        if hours == 0:
            return f"{minutes}:{seconds}"
        return f"{hours}:{minutes}:{seconds}"

    def count_artist(self, artist):
        return sum([1 for song in self.songs if song.artist == artist])

    def artists(self):
        return {f'{song.artist}': self.count_artist(song.artist)
                for song in self.songs}

    def next_song(self):
        if len(self.played) == 0:
            if self.shuffle:
                self.songs = sample(self.songs, len(self.songs))
            self.played.append(self.songs[0])
            return self.songs[0]
        elif len(self.played) == len(self.songs) and self.repeat:
            self.played = [self.songs[0]]
            return self.songs[0]
        else:
            last_song_index = self.songs.index(self.played[-1])
            current = self.songs[last_song_index + 1]
            self.played.append(current)
            return current

    def pprint_playlist(self):
        return tabulate.tabulate([[song.artist, song.title, song.song_len]
                                  for song in self.songs],
                                 headers=['Artist', 'Song', 'Length'],
                                 tablefmt='orgtbl')

    def save(self):
        new_name = self.name
        if ' ' in self.name:
            new_name = new_name.replace(' ', '-')
        my_dict = {}
        for k, v in self.__dict__.items():
            if type(v) is not list:
                my_dict[k] = v
            else:
                song_list = []
                for song in v:
                    song_list.append(song.__dict__)
                my_dict[k] = song_list

        with open(f'{new_name}.json', "w") as file:
            json.dump(my_dict, file, indent=4)

    @classmethod
    def load(cls, path):
        with open(path, "r") as file:
            my_dict = json.load(file)
        obj = cls()
        for k, v in my_dict.items():
            if type(v) is not list:
                setattr(obj, k, v)
            else:
                song_list = []
                for song in v:
                    song_list.append(Song(**song))
                setattr(obj, k, song_list)
        return obj


def get_length_from_seconds(seconds):
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours == 0:
        if seconds < 10:
            return f"{minutes}:0{seconds}"
        else:
            return f"{minutes}:{seconds}"
    else:
        if seconds < 10 and minutes > 10:
            return f"{hours}:{minutes}:0{seconds}"
        if seconds < 10 and minutes < 10:
            return f"{hours}:0{minutes}:0{seconds}"
        if seconds > 10 and minutes < 10:
            return f"{hours}:0{minutes}:{seconds}"
    return f"{hours}:{minutes}:{seconds}"


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        # print(os.listdir(self.path))
        playlist = []
        with os.scandir(self.path) as it:
            for entry in it:
                if entry.is_file():
                    audio = mutagen.mp3.EasyMP3(entry)
                    song = Song(title=(audio.tags['title'][0]),
                                artist=(audio.tags['artist'][0]),
                                album=(audio.tags['album'][0]),
                                song_len=get_length_from_seconds(
                                    audio.info.length))
                    playlist.append(song)
        result = Playlist("Generated")
        result.add_songs(playlist)
        return result


def main():
    one = Song("bbb", "aaa", "ccc", "3:36")
    two = Song("ddd", "aaa", "eee", "4:20")
    three = Song("eee", "aaa", "ccc", "12:28")
    four = Song("nnn", "mmm", "ooo", "6:32")
    five = Song("sss", "ppp", "rrr", "1:20:03")
    six = Song("yyy", "xxx", "zzz", "2:32:15")

    playlist_four = Playlist(name="First playlist", repeat=True, shuffle=True)
    list_of_songs = [one, two, three, four, five, six]
    playlist_four.add_songs(list_of_songs)

    for i in range(10):
        print(str(playlist_four.next_song()))

    print(playlist_four.pprint_playlist())
    playlist_four.save()
    print()

    playlist_five = Playlist.load("First-playlist.json")
    print(playlist_five.pprint_playlist())

    print(playlist_four.name == playlist_five.name)

    crawler = MusicCrawler("/home/kristin/Downloads/Rihanna - BOOM.-WEB-2018")
    playlist = crawler.generate_playlist()
    print(playlist.pprint_playlist())


if __name__ == '__main__':
    main()
