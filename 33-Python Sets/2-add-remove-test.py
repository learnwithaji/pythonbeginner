indian_team = {"Virat Kohli", "Rohit Sharma", "KL Rahul", "Jasprit Bumrah", "Hardik Pandya"}

indian_team.add("Shubman Gill")
print(indian_team)

indian_team.update(["Rishabh Pant", "Suryakumar Yadav"])
print(indian_team)

indian_team.remove("KL Rahul")
print( indian_team)

indian_team.discard("Ishant Sharma")
print(indian_team)

popped_player = indian_team.pop()
print("After pop:", indian_team)
print("Popped player:", popped_player)

print("Virat Kohli" in indian_team)
print("Shubman Gill" in indian_team)

