# simulation.py
import random

class PlayoffSimulation:
    @staticmethod
    def simulate_playoff_round(teams):
        winners = []
        teams.sort(key=lambda x: x[1])

        while len(teams) > 1:
            team1, seed1 = teams.pop(0)
            team2, seed2 = teams.pop()
            home_team, away_team = (team1, team2) if seed1 < seed2 else (team2, team1)

            if seed1 == seed2:
                home_team, away_team = random.sample([team1, team2], k=2)

            while True:
                try:
                    print(f"\nHome Team ({home_team} - Seed {seed1}) vs. Away Team ({away_team} - Seed {seed2}):")
                    # score_home_team = int(input(f"{home_team}: "))
                    # score_away_team = int(input(f"{away_team}: "))
                    score_home_team = random.randint(0,127)
                    score_away_team = random.randint(0,127)

                    if score_home_team == score_away_team:
                        raise ValueError("Scores cannot be tied. Please enter different scores.")

                    break
                except ValueError as e:
                    print(f"Error: {e}")

            winner = home_team if score_home_team > score_away_team else away_team
            winners.append((winner, seed1 if winner == team1 else seed2))

        return winners
