import random

teams = [
        "Get In",
        "The F boys",
        "ABBT",
        "Corn Stars",
]

n_teams = len(teams)
t1 = random.randrange(n_teams)
t2 = random.randrange(n_teams)

while t1 == t2:
    t2 = random.randrange(n_teams)

t3, t4 = [t for t in range(len(teams)) if t not in [t1, t2]]

print(f"{teams[t1]} vs {teams[t2]}")
print(f"{teams[t3]} vs {teams[t4]}")
