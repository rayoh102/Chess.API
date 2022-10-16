from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
	data = get_leaderboards().json
	categories = data.keys()

	for category in categories:
		print('CATEGORY:', category)
		for index, entry in enumerate(data[category]):
			print(f'Rank: {index + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')

def print_player_rating(username):
	data = get_player_stats(username).json
	categories = ['chess_blitz', 'chess_rapid', 'chess_bullet', 'puzzle_rush', 'tactics']

	for category in categories:
		print('Category:', category)
		print(f'Current: {data[category]["last"]["rating"]}')
		print(f'Best: {data[category]["best"]["rating"]}')
		print(f'Record: {data[category]["record"]}')

def print_most_recent_game(username):
	data = get_player_game_archives(username).json
	url = data['archives'][-1]
	games = requests.get(url).json()
	game = games['games'][-1]
	printer.pprint(game)

print_leaderboards('Hikaru')
print_player_rating('Hikaru')
print_most_recent_game('Hikaru')