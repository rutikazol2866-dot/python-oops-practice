class player:
    def __init__(self,n,t,r,m,a):
        self.name = n
        self.team = t
        self.role = r
        self.matches = m
        self.age = a

p1 = player("rohit sharma", "india", "batsman", 5000, 37)
p2 = player("virat kohli", "india", "batsman", 5500, 37)
p3 = player("bumrah", "india", "bowler", 50, 32)
p4 = player("dhoni", "wicketkipper","india", 90, 45)
p5 = player("hardik", "all-rounder", "india", 300, 45)

print(p2.name,p2.team,p2.role,p2.matches,p2.age)

player_list = []
p1 = player("rohit sharma", "india", "batsman", 5000, 37)
player_list.append(p1)

for player in player_list:
    if player.age >35:
        print(player.name,player.age)
    