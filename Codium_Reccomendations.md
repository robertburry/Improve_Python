# Codium Reccomendations

## Making playoff loop recursive. Giving this as the changes

```Python
def simulate_playoff_round(teams):
    winners = []

    # Sort teams and seeds before the playoff round
    teams.sort(key=lambda x: x[1])  # Sort by seeds

    if len(teams) > 1:
        team1, seed1 = teams.pop(0)
        team2, seed2 = teams.pop()  # Select teams from the end of the list to pair seeds correctly

        # Determine the home and away teams
        home_team, away_team = (team1, team2) if seed1 < seed2 else (team2, team1)

        # If seeds are the same, randomly assign home and away
        if seed1 == seed2:
            home_team, away_team = random.sample([team1, team2], k=2)

        # Get simultaneous user input for the scores with tie check
        while True:
            try:
                print(f"\nHome Team ({home_team} - Seed {seed1}) vs. Away Team ({away_team} - Seed {seed2}):")
                score_home_team = int(input(f"{home_team}: "))
                score_away_team = int(input(f"{away_team}: "))

                # Check for a tie
                if score_home_team == score_away_team:
                    raise ValueError("Scores cannot be tied. Please enter different scores.")

                break
            except ValueError as e:
                print(f"Error: {e}")

        # Determine the winner based on scores
        winner = home_team if score_home_team > score_away_team else away_team

        # Append the winner to the list, preserving the original seeds
        winners.append((winner, seed1 if winner == team1 else seed2))

        # Recursively call the function with the remaining teams
        winners += simulate_playoff_round(teams)

    return winners
```

## Removing the following lines

```Python
# Simulate playoff rounds for AFC and NFC
while len(afc_playoffs) > 1:
    afc_playoffs = simulate_playoff_round(afc_playoffs)

while len(nfc_playoffs) > 1:
    nfc_playoffs = simulate_playoff_round(nfc_playoffs)

# Simulate the final round for League Championship
league_championship = [(afc_playoffs[0][0], afc_playoffs[0][1]), (nfc_playoffs[0][0], nfc_playoffs[0][1])]

while len(league_championship) > 1:
    league_championship = simulate_playoff_round(league_championship)
```

**Will have to test this.**
