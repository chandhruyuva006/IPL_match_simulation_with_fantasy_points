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
