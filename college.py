class college:
    def __init__(self,n,c,s,f,l):
        self.name = n
        self.course = c
        self.student = s
        self.fees = f
        self.location = l

c1 = college("sinhgad college", "bca", 150, 31000, "warje")
c2 = college("trinity acedamy", "entc", 180, 60000, "yewalewadi")
c3 = college("vishwakarma university", "bcs", 200, 120000, "kondhawa")
c4 = college("rajgad dyanpeeth", "cs", 120, 11000, "bhor")
c5 = college("shardabai pawar", "science", 300, 11800, "baramati")   

print(c5.name)
print(c5.course)
print(c5.student)
print(c5.fees)
print(c5.location)

college_list = []
c4 = college("rajgad dyanpeeth", "cs", 120, 11000, "bhor")
college_list.append(c4)

for college in college_list:
    if college.fees >50000:
        print(college.name,college.fees)