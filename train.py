class train:
    def __init__(self,n,num,s,d,p):
        self.name = n
        self.num = num
        self.source = s
        self.destination = d
        self.price = p

t1 = train("intercity express", 12128, "solapur","mumbai", 390)
t2 = train("deccan express", 11007, "pune", "mumbai", 200)
t3 = train("sinhgad express", 11010, "pune", "mumbai",180)
t4 = train("indryani express", 22106, "hydrabad", "mumbai", 500)
t5 = train("garibrath express",12026, "pune", "nagpur", 850)

print(t4.name)
print(t4.num)
print(t4.source)
print(t4.destination)
print(t4.price)

train_list = []
t5 = train("garibrath express",12026, "pune", "nagpur", 850) 
train_list.append(t5)     
        
    
for train in train_list:
    if train.price<1000:
        print(train.name,train.price)
    
    