
from team import Player, skill_based_weights, prepare_playing_eleven

from match import *

#// skill_based_weights function is the key and controls the runs and wickets it needs to be tuned in a goodway
#// but i dont know how to tune the parameters
"""
Weights for [0, 1, 2, 3, 4, 6, 'w'] tuned for IPL-style scores.

• skill ≈ 1.30  → superstar like Kohli and SKY
• skill ≈ 1.15  → top-order regular
• skill ≈ 1.00  → solid middle order
• skill ≈ 0.85  → lower order
• skill ≈ 0.65  → tail
• skill ≈ 0.45  → genuine rabbit

# Baseline for a skill-1.00 batter (we need to change this base ratios)
base = [0.30, 0.34, 0.11, 0.01, 0.15, 0.05, 0.04] This is based on the previous IPL scores and stats
But it closely resembles the pre-COVID era IPL and not the new age IPL Where Batsmen are overpowered"""

CURRENT_MATCH_ID = "jj1"

MI_vs_RCB = []

team1_name = "MI"
team1_player_names= [("Rohit", 1), ("Jacks", 1), ("Surya",1.2), ("Tilak", 0.95), 
		("Pandya", 0.9), ("Naman", 0.8), ("Santner", 0.76), ("Gleeson",0.72), 
		("Ashwani", 0.55), ("Bumrah", 0.5), ("Boult", 0.6)]
team1_bowlers = ["Pandya", "Santner", "Gleeson", "Ashwani", "Bumrah", "Boult"]
team1_keeper = "Jacks"


team2_name = "RCB"
team2_player_names = [("Salt", 1),("Kohli",1.2),("Agarwal", 0.95),("Rajat",1),
					("Livingstone", 0.9),("Jitesh", 0.95),("Romario", 0.82),("Krunal",  0.7),
					("Bhuvi", 0.59),("Yash_dayal", 0.5),("Hazlewood", 0.5)]
team2_bowlers = ["Krunal", "Bhuvi", "Yash_dayal", "Romario", "Hazlewood"]
team2_keeper = "Jitesh"


def main():
	# Prepare teams
	team1 = prepare_playing_eleven(team1_player_names, team1_bowlers, team1_keeper)
	team2 = prepare_playing_eleven(team2_player_names, team2_bowlers, team2_keeper)

	# Simulate the match
	simulated_match_results = simulate_match(MI_vs_RCB, CURRENT_MATCH_ID, team1, team2)

	# Print the match results
	print_match_results(simulated_match_results, team1_name, team2_name)

	print("==============Match Stats============")
	print_regular_stats(team1, team2)
	print("==============Second innings=========")
	print_regular_stats(team2, team1)

	print_fantasy_points(team1, team2)


if __name__ == "__main__":
	main()