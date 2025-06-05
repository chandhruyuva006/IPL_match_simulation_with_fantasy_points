def log_ball(BALL_LOG, match_id, inning, over_no, ball_no, striker, bowler,
			 outcome, runs, wicket):
	"""
	Append a single delivery to BALL_LOG.
	Kept as a *small* function so the main loop stays legible.
	"""
	BALL_LOG.append({
		"match_id":  match_id,
		"inning":	inning,
		"over":	  over_no,
		"ball":	  ball_no,
		"batter":	striker.name,
		"bowler":	bowler.name,
		"outcome":   outcome,		  # 0/1/2/3/4/6 or 'w'
		"runs":	  runs,			 # 0-6
		"wicket":	wicket			# 0/1
	})

from team import Player, skill_based_weights, prepare_playing_eleven
from match import simulate_innings, simulate_match, print_match_results

CURRENT_MATCH_ID = "jj1"
MI_vs_RCB = []

team1_name = "MI"
team1_player_names = [("Rohit", 1), ("Jacks", 1), ("Surya", 1.2), ("Tilak", 0.95),
                      ("Pandya", 0.9), ("Naman", 0.8), ("Santner", 0.76), ("Gleeson", 0.72),
                      ("Ashwani", 0.55), ("Bumrah", 0.5), ("Boult", 0.6)]
team1_bowlers = ["Pandya", "Santner", "Gleeson", "Ashwani", "Bumrah", "Boult"]
team1_keeper = "Jacks"

team2_name = "RCB"
team2_player_names = [("Salt", 1), ("Kohli", 1.2), ("Agarwal", 0.95), ("Rajat", 1),
                      ("Livingstone", 0.9), ("Jitesh", 0.95), ("Romario", 0.82), ("Krunal", 0.7),
                      ("Bhuvi", 0.59), ("Yash_dayal", 0.5), ("Hazlewood", 0.5)]
team2_bowlers = ["Krunal", "Bhuvi", "Yash_dayal", "Romario", "Hazlewood"]
team2_keeper = "Jitesh"

def main():
    # Prepare teams
    team1 = prepare_playing_eleven(team1_player_names, team1_bowlers, team1_keeper)
    team2 = prepare_playing_eleven(team2_player_names, team2_bowlers, team2_keeper)

    # Simulate the match
    simulated_match_results = simulate_match(MI_vs_RCB, CURRENT_MATCH_ID, team1, team2)

    # Print the match results
    print_match_results(simulated_match_results)

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()

 matches = {}

# Team names
team1 = "MI"
team2 = "RCB"

# Generate dynamic key
match_key = f"{team1.lower()}_{team2.lower()}"

# Store match data in dictionary
matches[match_key] = {
    "team1": team1,
    "team2": team2,
    "score": {"MI": 180, "RCB": 175},  # Example score
}

print(matches)
# Output: {'mi_rcb': {'team1': 'MI', 'team2': 'RCB', 'score': {'MI': 180, 'RCB': 175}}}