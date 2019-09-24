class Player:
    def __init__(self, name: str, result: int, count: int):
        self.name = name
        self.result = result
        self.count = count


players_list = []

while True:
    new_player_input = input().split(" -> ")
    if new_player_input[0] == "report":
        break
    player_name = new_player_input[0]
    player_results = list(map(int, new_player_input[1].split(", ")))
    new_object = Player(player_name, sum(player_results), len(player_results))
    players_list.append(new_object)

while True:
    command = input()
    if command == "end":
        break
    elif command == "score descending":
        for player in sorted(players_list, key=lambda x: (-x.result, x.name)):
            print(f"{player.name}: {player.result}")
    elif command == "score ascending":
        for player in sorted(players_list, key=lambda x: (x.result, x.name)):
            print(f"{player.name}: {player.result}")
    elif command == "numberOfGames descending":
        for player in sorted(players_list, key=lambda x: (-x.count, x.name)):
            print(f"{player.name}: {player.count}")
    elif command == "numberOfGames ascending":
        for player in sorted(players_list, key=lambda x: (x.count, x.name)):
            print(f"{player.name}: {player.count}")