class farm:
    def __init__(self,c,a,s,l,m):
        self.crop_name = c
        self.acres = a
        self.season = s
        self.location = l 
        self.month = m

f1 = farm("wheat", 5, "winter", "baramati" , 6)
f2 = farm("soyabean" ,4 , "mansoon", "solapur" , 4)
f3 = farm("sugarcane", 7 ,"all season", "pune" ,11)
f4 = farm("mug", 2, "mansoon", "beed" , 5)
f5 = farm("rice", 1 ,"mansoon", "maval" , 4) 
print(f1.crop_name)
print(f1.acres)
print(f1.season)
print(f1.location)
print(f1.month)

farm_list = []
f1 = farm("wheat", 5, "winter", "baramati" , 6)
farm_list.append(f1)

for farm in farm_list:
    print(f1.crop_name,f1.month,f1.location)
    

