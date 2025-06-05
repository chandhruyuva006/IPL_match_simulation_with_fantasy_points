def skill_based_weights(skill: float) -> list[float]:
	#// This function is the key and controls the runs and wickets it needs to be tuned in a goodway
	#// but i dont know how to tune the parameters
	"""
	Weights for [0, 1, 2, 3, 4, 6, 'w'] tuned for IPL-style scores.

	• skill ≈ 1.30  → superstar
	• skill ≈ 1.15  → top-order regular
	• skill ≈ 1.00  → solid middle order
	• skill ≈ 0.85  → lower order
	• skill ≈ 0.65  → tail
	• skill ≈ 0.45  → genuine rabbit
	"""
	# Baseline for a skill-1.00 batter (we need to change this base ratios)
	base = [0.30, 0.34, 0.11, 0.01, 0.15, 0.05, 0.04]		  # dot,1,2,3,4,6,w

	# Boost (or shrink) the scoring shots linearly with skill
	boost = 1 + 0.70 * (skill - 1)							 # 0.70 = gentler slope
	scoring = [p * boost for p in base[1:6]]				   # 1-run through six-run

	# Re-allocate residual probability to dots & wickets
	residual = 1.0 - sum(scoring)
	dot_share = base[0] / (base[0] + base[6])				  # keep original dot:wicket ratio
	dot, wicket = residual * dot_share, residual * (1 - dot_share)

	weights = [round(dot, 3)] + [round(x, 3) for x in scoring] + [round(wicket, 3)]

	# tiny fix for rounding drift
	weights[0] += round(1.0 - sum(weights), 3)
	return weights

class Player:
	"""
	Represents a cricket player with a name and skill rating.

	Attributes:
		name (str): The player's name.
		skill (float): The player's skill rating.
	"""
	def __init__(self,name, skill):
		self.name = name 
		self.skill = skill
		self.is_bowler = False
		self.is_keeper = False
		self.each_ball_batted = []
		self.each_ball_bowled = []
		self.overs_bowled = 0
		self.catches = 0
		self.bowled = 0
		self.run_outs = 0
		self.stumpings = 0
		# self.fours = 0
		# self.sixes = 0
		self.wickets = 0
	@property
	def fours(self):
		return self.each_ball_batted.count(4)

	@property
	def sixes(self):
		return self.each_ball_batted.count(6)
	
	
	@property
	def skill_weights(self):
		return skill_based_weights(self.skill)

	@property
	def balls_faced(self):
		return len(self.each_ball_batted)

	@property
	def runs_scored(self):
		return sum(i for i in self.each_ball_batted if i != "w")

	@property
	def runs_conceded(self):
		return sum(i for i in self.each_ball_bowled if i != "w")
	
	@property
	def strike_rate(self):
		if self.balls_faced:
			return round(self.runs_scored*100/self.balls_faced,2)
		else:
			return 0
	@property
	def economy(self):
		balls_bowled = len(self.each_ball_bowled)
		if balls_bowled:
			return round(self.runs_conceded*6/balls_bowled, 2)

		else: return 0

	def calculate_batting_points(self):
		fantasy_points = 0
		for ball_outcome in self.each_ball_batted:
			if ball_outcome in [1,2,3]:
				fantasy_points+=ball_outcome
			elif ball_outcome == 4:
				fantasy_points+=8
			elif ball_outcome == 6:
				fantasy_points+=12

		fantasy_points += (self.runs_scored//25)*4

		return fantasy_points

	 
	def calculate_bowling_points(self):
		fantasy_points = 0
		for ball_outcome in self.each_ball_bowled:
			if ball_outcome == 0:
				fantasy_points += 1
			elif ball_outcome == "w":
				fantasy_points+=30
		return fantasy_points

	
	def calculate_other_points(self):
		fantasy_points = 0
		fantasy_points += self.catches*8
		fantasy_points += self.run_outs*8
		fantasy_points += self.stumpings *12
		fantasy_points += self.bowled * 8
		return fantasy_points

	@property
	def total_fantasy_points(self):
		return (
				4 +	  # four is the base point
				self.calculate_batting_points() +
				self.calculate_bowling_points() +
				self.calculate_other_points()
				)

	def __repr__(self):
		return f'Player(name = {self.name}, skill = {self.skill})'
	
def prepare_playing_eleven(total_team, bowlers, keeper):
	team = [Player(p, s) for p, s in total_team]
	for p in team:
		if p.name in bowlers: p.is_bowler = True
		if p.name == keeper:  p.is_keeper = True
	return team