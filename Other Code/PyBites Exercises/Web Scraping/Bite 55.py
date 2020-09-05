from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    games_list = []
    feed_info = feedparser.parse(FEED_URL)

    for item in feed_info.entries:
        game_name = item.title.split(" - ")[1].split(', ')[0]
        game_link = item.link
        games_list.append(Game(title=game_name, link=game_link))
    return games_list
