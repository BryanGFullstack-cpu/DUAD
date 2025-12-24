#Exercise 1 week 8
import os

MUSIC_FILE = os.path.join(os.path.dirname(__file__), 'MusicList.txt')


def my_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.rstrip())
    except FileNotFoundError:
        print(f'File not found: {path}')


def new_list(path):
    songs_alphabetical = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    songs_alphabetical.append(line)
    except FileNotFoundError:
        print(f'File not found: {path}')
    return songs_alphabetical


def sorted_songs(path, songs):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            for song in songs:
                file.write(f'{song}\n')
    except IOError:
        print(f'Error writing to file: {path}')

sorted_file= "MusicSorted.txt"


print(f'Using file: {MUSIC_FILE}')
songs = new_list(MUSIC_FILE)
print('\nSongs in alphabetical order:')
for song in songs:
    print(song)


sorted_songs(sorted_file, sorted(songs))
print(f'\nSorted songs have been written to: {sorted_file}')