team_a = []
team_b = []

for player in range(1, 12):
    team_a.append(player)
    team_b.append(player)

input_card = input().split(" ")

ended = None
for card in input_card:
    card_data = card.split("-")
    team = card[0]
    player = int(card_data[1])
    if team == "A" and player in team_a:
        team_a.remove(player)
    elif team == "B" and player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        ended = True
        break

print(f"Team A - {len(team_a)}; "
      f"Team B - {len(team_b)}")
if ended:
    print("Game was terminated")


