#Exercise 2 csv week 8

import csv

def video_games_info():
    games = []
    while True:
        name = input("Enter the name of the video game (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        genre = input("Enter the genre: ")
        platform = input("Enter the platform: ")
        year = input("Enter the release year: ")
        games.append({'name': name, 'genre': genre, 'platform': platform, 'year': year})

    with open('video_games.tsv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'genre', 'platform', 'year']
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
            delimiter='\t',               
            quoting=csv.QUOTE_MINIMAL     
        )
        writer.writeheader()
        writer.writerows(games)

    print(f"Saved {len(games)} games to video_games.tsv")

video_games_info()