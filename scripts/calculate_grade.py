import math

def calculate_grade(p_deadline1,p_deadline2,n_teams, baseline = 4, oneperson = False):
    s1 = 19 - 19 * math.log2((p_deadline1-1)/(n_teams-1)+1)
    s2 = 19 - 19 * math.log2((p_deadline2-1)/(n_teams-1)+1)

    baselines_scores = [ 1, 2, 4, 6, 8]

    standing_points = (s1+s2*4)/5
    baseline_points = baselines_scores[baseline]
    
    return standing_points + baseline_points + oneperson

# INSERT HERE THE POSITION ON 1 DEADLINE
p_deadline1 = 2
# INSERT HERE THE POSITION ON 2 DEADLINE 
p_deadline2 = 2
# NUMBER OF TEAMS
n_teams = 63


gra = round(calculate_grade(p_deadline1= p_deadline1,p_deadline2= p_deadline2,n_teams= n_teams))
print("Voto Challenge: {}".format(gra))
print("Voto totale considerando 5 punti in esame: {}".format(gra + 5))


