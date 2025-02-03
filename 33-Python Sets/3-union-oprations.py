indian_team = {"Rohit Sharma", "Virat Kohli", "Jasprit Bumrah", "Ravindra Jadeja", "KL Rahul"}
ipl_players = {"Virat Kohli", "Hardik Pandya", "Suryakumar Yadav", "Rishabh Pant", "Shubman Gill"}

print("Aji" in ipl_players)
print("Virat Kohli"  in ipl_players)

all_player = indian_team | ipl_players
print(all_player)

common_players = indian_team & ipl_players
print(common_players)

difference_team = indian_team - ipl_players
print(difference_team)

symmetric_difference_team = indian_team ^ ipl_players
print(symmetric_difference_team)

subset_check = indian_team <= ipl_players
print(subset_check)

subset_players = {"Rohit Sharma", "Virat Kohli", "Jasprit Bumrah"}
subset_check = subset_players <= indian_team
print(subset_check)

superset_check = indian_team >= subset_players
print(superset_check)

copied_team = indian_team.copy()
print("Copied team:", copied_team)

indian_team.clear()
print("After clearing original team:", indian_team)
