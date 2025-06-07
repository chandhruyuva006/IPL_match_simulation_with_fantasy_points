import random
MI = {"name": "MI", 
        "player_names": [("Rohit", 1), ("Jacks", 1), ("Surya",1.2), ("Tilak", 0.95), 
                         ("Pandya", 0.9), ("Naman", 0.8), ("Santner", 0.76), ("Gleeson",0.72), 
                         ("Ashwani", 0.55), ("Bumrah", 0.5), ("Boult", 0.6)],
        
        "bowlers" : ["Pandya", "Santner", "Gleeson", "Ashwani", "Bumrah", "Boult"],
        
        "keeper" : "Jacks"}  #done

RCB = {
        "name" : "RCB" ,
        "player_names" : [("Salt", 1),("Kohli",1.2),("Agarwal", 0.95),("Rajat",1),
                          ("Livingstone", 0.9),("Jitesh", 0.95),("Romario", 0.82),("Krunal",  0.7),
                          ("Bhuvi", 0.59),("Yash_dayal", 0.5),("Hazlewood", 0.5)],       
        "bowlers" : ["Krunal", "Bhuvi", "Yash_dayal", "Romario", "Hazlewood"],
        "keeper" : "Jitesh"} #done

SRH = {
    "name": "SRH",
    "player_names": [("Head", 1.1), ("Abhishek", 1), ("Ishan", 0.85),("Klaasen", 1.2),
                     ("Aniket", 0.75), ("Nitish", 0.72), ("Cummins", 0.75),
                     ("Harshal", 0.5), ("Eshan", 0.6), ("Unadkat", 0.55), ("Harsh_Dubey", 0.55)],
    "bowlers": ["Cummins", "Harshal", "Eshan", "Harsh_Dubey", "Unadkat"],
    "keeper": "Ishan"
} #done

KKR = {
    "name": "KKR",
    "player_names": [("De_cock", 1.05), ("Narine", 0.9), ("Rahane", 1.1), ("Rinku", 1.15),
                     ("Russell", 1), ("Raguvanshi", 0.9), ("Ramandeep", 0.7), ("Harshit", 0.6),
                     ("Varun", 0.55), ("Nortje", 0.65), ("Arora", 0.5)],
    "bowlers": ["Narine", "Russell",  "Harshit", "Varun", "Nortje", "Arora"],
    "keeper": "De_cock"
} # done

DC = {
    "name": "DC",
    "player_names": [("Rahul", 1.1), ("Faf", 0.95), ("Nair", 1), ("Axar", 1.15),
                     ("Rizvi", 0.9), ("Stubbs", 0.85), ("Vipraj", 0.6), ("Kuldeep", 0.65), 
                     ("Mukesh", 0.55), ("Rahman", 0.5), ("Mohit", 0.5)],
    "bowlers": ["Axar", "Kuldeep", "Rahman", "Mukesh", "Mohit", "Vipraj"],
    "keeper": "Stubbs"
} #done

PBKS = {
    "name": "PBKS",
    "player_names": [("Arya", 1), ("Prabhsimran", 1), ("Inglis", 1), ("Iyer", 1.1),
                     ("Wadhera", 0.8), ("Shashank", 0.85), ("Omarzai", 0.65), ("Jamieson", 0.6),
                     ("Vyshak", 0.7), ("Arshdeep", 0.55), ("Chahal", 0.55)],
    "bowlers": ["Omarzai", "Jamieson", "Vyshak", "Arshdeep", "Chahal"],
    "keeper": "Inglis"
}  #done

RR = {
    "name": "RR",
    "player_names": [("Jaiswal", 1.05), ("Vaibhav", 1.2), ("Samson", 1.15), ("Parag", 0.9),
                     ("Hetmyer", 0.95), ("Jurel", 0.75), ("Hasaranga", 0.75), ("Maphaka", 0.55),
                     ("Yudhvir", 0.6), ("Tushar", 0.55), ("Madhwal", 0.65)],
    "bowlers": ["Hasaranga", "Maphaka", "Yudhvir", "Tushar", "Madhwal", "Parag"],
    "keeper": "Samson"
} #done

CSK = {
    "name": "CSK",
    "player_names": [("Ruturaj", 1.1), ("Conway", 1.05), ("Mathre", 0.9), ("Dube", 1), 
                     ("Jadeja", 0.85), ("Dhoni", 0.8), ("Ashwin", 0.9), ("Kamboj", 0.6),
                     ("Pathirana", 0.55), ("Noor", 0.5), ("Khaleel", 0.55)],
    "bowlers": ["Jadeja", "Ashwin", "Noor", "Pathirana", "Khaleel", "Kamboj"],
    "keeper": "Dhoni"
} #done
 
LSG = {
    "name": "LSG",
    "player_names": [("Marsh", 1.1), ("Breetzke", 1), ("Pooran", 1.15), ("Pant", 1),
                     ("Samad", 0.85), ("Badoni", 0.9),("Shabash", 0.75), ("Digvesh", 0.6), ("Avesh", 0.55),
                     ("Orourke", 0.5), ("Akash", 0.6), ],
    "bowlers": ["Shabash", "Digvesh", "Avesh", "Orourke", "Akash", "Badoni"],
    "keeper": "Pant"
} #done

GT = {
    "name": "GT",
    "player_names": [("Gill", 1.2), ("Sudharsan", 1), ("Mendis", 0.85), ("Sundar", 1),
                     ("Rutherford", 1.05), ("Tewatia", 0.9), ("Rashid", 0.75), ("Shami", 0.6),
                     ("Kishore", 0.55), ("Siraj", 0.5), ("Prasidh", 0.5)],
    "bowlers": ["Kishore", "Rashid", "Shami", "Siraj", "Prasidh"],
    "keeper": "Mendis"
} #done



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
    base = [0.30, 0.34, 0.11, 0.01, 0.15, 0.05, 0.04]         # dot,1,2,3,4,6,w

    # Boost (or shrink) the scoring shots linearly with skill
    boost = 1 + 0.70 * (skill - 1)                           # 0.70 = gentler slope
    scoring = [p * boost for p in base[1:6]]                   # 1-run through six-run

    # Re-allocate residual probability to dots & wickets
    residual = 1.0 - sum(scoring)
    dot_share = base[0] / (base[0] + base[6])                 # keep original dot:wicket ratio
    dot, wicket = residual * dot_share, residual * (1 - dot_share)

    weights = [round(dot, 3)] + [round(x, 3) for x in scoring] + [round(wicket, 3)]

    # tiny fix for rounding drift
    weights[0] += round(1.0 - sum(weights), 3)
    return weights

class Player:
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

    # Helper function to the fantasy points main function
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

    # Helper function to the fantasy points main function
    def calculate_bowling_points(self):
        fantasy_points = 0
        for ball_outcome in self.each_ball_bowled:
            if ball_outcome == 0:
                fantasy_points += 1
            elif ball_outcome == "w":
                fantasy_points+=30
        return fantasy_points

    # Helper function to the fantasy points main function
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
                4 +   # four is the base point
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

def wicket_type_manager(bowler, fielders):
    wicket_type = random.choices(["caught", "bowled", "caught_and_bowled", "run_out"], weights=[0.5,0.4,0.05,0.05], k=1)[0]
    if wicket_type == "caught_and_bowled":
        bowler.wickets+=1
        bowler.catches+=1
    elif wicket_type  == "bowled":
        bowler.wickets+=1
        bowler.bowled +=1
    elif wicket_type == "caught":
        bowler.wickets+=1
        fielder = random.choice(fielders)
        fielder.catches+=1
    else:
        fielder = random.choice(fielders)
        fielder.run_outs+=1

def simulate_innings(inning_number, batting_team, fielding_team, target = None):
    possibilities = [0,1,2,3,4,6,"w"]
    score = wickets = balls = 0
    striker_i, non_striker_i, next_i = 0, 1, 2
    

    bowlers = [p for p in fielding_team if p.is_bowler]
    balls_in_over = 0
    bowler = random.choice(bowlers)
    
    over_no, ball_no_in_over = 0, 0
    while wickets <10 and balls<120 :
        if balls_in_over == 0:
            available = [b for b in bowlers if b.overs_bowled < 4]
            bowler = random.choice(available)
        

        striker = batting_team[striker_i]
        
        ball_outcome = random.choices(possibilities, weights = striker.skill_weights, k=1)[0]
        

        striker.each_ball_batted.append(ball_outcome)
        bowler.each_ball_bowled.append(ball_outcome)

        balls+=1
        balls_in_over += 1

        if ball_outcome == "w":
            wickets+=1
            wicket_type_manager(bowler, fielding_team)
            if next_i >= 11: break
            striker_i = next_i
            next_i+=1
            
        else:
            score += ball_outcome
            if ball_outcome %2:
                striker_i, non_striker_i = non_striker_i, striker_i
            
        #over count and strike change
        if balls_in_over ==6:
            bowler.overs_bowled += 1
            striker_i, non_striker_i = non_striker_i, striker_i
            balls_in_over = 0
            over_no += 1

        # if a team wins break the loop
        if target and score > target:
            break

    return score, wickets, balls

def simulate_match(team1, team2):
    
    runsA, wicketsA, ballsA = simulate_innings(1,team1, team2)
    runsB, wicketsB, ballsB = simulate_innings(2,team2, team1, target = runsA)
    
    return (runsA, wicketsA, ballsA, runsB, wicketsB, ballsB )
    
def print_match_results(simulated_match, team1_name, team2_name):
    runsA, wicketsA, ballsA , runsB, wicketsB, ballsB = simulated_match
    with open (filename, "a") as f:
        f.write("=======================================\n")
        f.write(f"      {team1_name} vs {team2_name}\n")   
        f.write("=======================================\n")

        f.write(f"Innings 1: {team1_name}-> {runsA}/{wicketsA} in {ballsA//6}.{ballsA%6}\n")
        f.write(f"Innings 1: {team2_name}-> {runsB}/{wicketsB} in {ballsB//6}.{ballsB%6}\n")

        if runsA > runsB:
            f.write(f'{team1_name} won by {runsA-runsB} runs \n')
        elif runsA<runsB:
            f.write(f'{team2_name} won by {10-wicketsB} wickets\n')
        else:
            f.write("match is a tie\n")
        f.write("---------------------------------------\n")
        f.write("\n")

def print_regular_stats(team1, team2):
    with open (filename, "a") as f:
        f.write("Batter        R   B  4s  6s   SR\n")
        f.write("-------------------------------------\n")
        for i in team1: 
            i.total_fantasy_points
            f.write(f'{i.name:<12s}{i.runs_scored:>3} {i.balls_faced: >3} {i.fours: >2}  {i.sixes: >2}   {i.strike_rate}\n')
        f.write("-------------------------------------\n")
        f.write("Bowler    O M  R W Eco\n")
        f.write("-------------------------------------\n")
        for i in team2:
            i.total_fantasy_points
            if i.is_bowler:
                f.write(f'{i.name:<10s} {i.overs_bowled} {0} {i.runs_conceded:<2} {i.wickets} {i.economy:<4}\n')
        f.write("-------------------------------------\n\n")

def print_fantasy_points(team1, team2):
    player_points = sorted([(p, p.total_fantasy_points) for p in team1+team2], key= lambda x: x[1], reverse = True)
    with open (filename, "a") as f:
        f.write (f'Player name  Pts   R   W   C   RO\n')
        for p,points in player_points:

            f.write(f'{p.name:<12s} {points:>3} {p.runs_scored:>3}  {p.wickets:<2}  {p.catches:<2}  {p.run_outs:<2}\n')
        f.write("\n")




# CURRENT_MATCH_ID = "jj1"



def main(team_a, team_b):

    team1 = prepare_playing_eleven( team_a["player_names"], team_a["bowlers"], team_a["keeper"])
    team2 = prepare_playing_eleven( team_b["player_names"], team_b["bowlers"], team_b["keeper"])


    simulated_match_results = simulate_match(team1, team2)

    print_match_results(simulated_match_results, team_a["name"], team_b["name"])
        
    with open (filename, "a") as f:
        f.write("==============Match Stats============\n")

    print_regular_stats(team1, team2)

    with open (filename, "a") as f:
        f.write("==============Second innings=========\n")

    print_regular_stats(team2, team1)

    print_fantasy_points(team1,team2)




ipl_teams = [MI, RCB, SRH, KKR, DC, PBKS, RR, CSK, LSG, GT ]




from itertools import combinations

matchups_1 = list(combinations(ipl_teams,2))

# First round robin matchups
for i in matchups_1:
    team_a, team_b = i[0], i[1]
    filename = f'{team_a["name"]}_vs_{team_b["name"]}.txt'
    main (team_a, team_b)

#second round robin matchups
matchups_2 = list(combinations(ipl_teams[::-1],2))
for i in matchups_2:
    team_a, team_b = i[0], i[1]
    filename = f'{team_a["name"]}_vs_{team_b["name"]}.txt'
    main (team_a, team_b)

