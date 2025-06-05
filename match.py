import random


def log_ball(ball_log_list,match_id, inning, over_no, ball_no, striker, bowler,
			 outcome, runs, wicket):
	"""
	Append a single delivery to BALL_LOG.
	Kept as a *small* function so the main loop stays legible.
	"""
	ball_log_list.append({
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

def simulate_innings(BALL_LOG_LIST, CURRENT_MATCH_ID, inning_number, batting_team, fielding_team, target = None):
	# start of the innings.
	# two batters are in the crease and 
	# next_i will give the next batters index in the batting_team
	possibilities = [0,1,2,3,4,6,"w"]
	score = wickets = balls = 0
	striker_i, non_striker_i, next_i = 0, 1, 2
	

	# creates a bowlers list from the fielding team
	bowlers = [p for p in fielding_team if p.is_bowler]
	balls_in_over = 0
	bowler = random.choice(bowlers)
	
	over_no, ball_no_in_over = 0, 0
	while wickets <10 and balls<120 :
		if balls_in_over == 0:
			available = [b for b in bowlers if b.overs_bowled < 4]
			bowler = random.choice(available)
		

		striker = batting_team[striker_i]
		# based on the batsmen's skill the ball outcome varies.

		ball_outcome = random.choices(possibilities, weights = striker.skill_weights, k=1)[0]
		# currently the log_ball is useless. 
		# still didn't find a good structure to store the ball logs
		log_ball(
				ball_log_list = BALL_LOG_LIST,
				match_id   = CURRENT_MATCH_ID,	 # define this before the innings call
				inning	 = inning_number,		# 1 or 2, pass it in
				over_no	= over_no,
				ball_no	= ball_no_in_over,
				striker	= striker,
				bowler	 = bowler,
				outcome	= ball_outcome,
				runs	   = 0 if ball_outcome == "w" else ball_outcome,
				wicket	 = 1 if ball_outcome == "w" else 0
			)

		striker.each_ball_batted.append(ball_outcome)
		bowler.each_ball_bowled.append(ball_outcome)

		balls+=1
		balls_in_over += 1

		if ball_outcome == "w":
			wickets+=1
			if next_i >= 11: break
			striker_i = next_i
			next_i+=1
			bowler.wickets+=1
		# odd run strike change	
		else:
			score += ball_outcome
			if ball_outcome %2:
				striker_i, non_striker_i = non_striker_i, striker_i
			
		#over count and strike change
		if balls_in_over ==6:
			bowler.overs_bowled += 1
			striker_i, non_striker_i = non_striker_i, striker_i
			balls_in_over = 0
		
		#redundant but useful when creating ball logs
		# but need to find a good way to combine the above and below
		# both does the same thing but for different purposes
		ball_no_in_over += 1
		if ball_no_in_over == 6:
			over_no += 1
			ball_no_in_over = 0


		if target and score > target:
			break


	return score, wickets, balls

def simulate_match(BALL_LOG_LIST, CURRENT_MATCH_ID,team1, team2):
	"""
		return a tuple containing 6 int items.
	"""
	runsA, wicketsA, ballsA = simulate_innings(BALL_LOG_LIST,CURRENT_MATCH_ID,1,team1, team2)
	runsB, wicketsB, ballsB = simulate_innings(BALL_LOG_LIST,CURRENT_MATCH_ID,2,team2, team1, target = runsA)
	
	return (runsA, wicketsA, ballsA, runsB, wicketsB, ballsB )
	
def print_match_results(simulated_match, team1_name, team2_name):
	runsA, wicketsA, ballsA , runsB, wicketsB, ballsB = simulated_match

	print("=======================================")
	print(f"		  {team1_name} vs {team2_name}")   
	print("=======================================")

	print(f"Innings 1: {team1_name:<4}-> {runsA}/{wicketsA} in {ballsA//6}.{ballsA%6}")
	print(f"Innings 2: {team2_name:<4}-> {runsB}/{wicketsB} in {ballsB//6}.{ballsB%6}")

	if runsA > runsB:
		print(f'{team1_name} won by {runsA-runsB} runs')
	elif runsA<runsB:
		print(f'{team2_name} won by {10-wicketsB} wickets')
	else:
		print("match is a tie")
	print("---------------------------------------")
	print()

def print_regular_stats(team1, team2):
	
	print("Batter	      R	  B  4s  6s	  SR")
	print("-------------------------------------")
	for i in team1: 
		i.total_fantasy_points
		print(f'{i.name:<12s}{i.runs_scored:>3} {i.balls_faced: >3} {i.fours: >2}  {i.sixes: >2}   {i.strike_rate}')
	print("-------------------------------------")
	print("Bowler	   O M  R W Eco")
	print("-------------------------------------")
	for i in team2:
		i.total_fantasy_points
		if i.is_bowler:
			print(f'{i.name:<10s} {i.overs_bowled} {0} {i.runs_conceded:<2} {i.wickets} {i.economy:<4}')
	print("-------------------------------------")

def print_fantasy_points(team1, team2):
	player_points = sorted([(p, p.total_fantasy_points) for p in team1+team2], key= lambda x: x[1], reverse = True)

	for p,points in player_points:
		print(f'{p.name:<12s} {points:<3}')