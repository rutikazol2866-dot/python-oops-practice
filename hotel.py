class hotel:
    def __init__(self,n,i,p,l,r):
        self.name = n
        self.items = i
        self.price = p
        self.location = l
        self.rating = r

r1 = hotel("ashirvad hotel", "mutton", 300, "narhe", 4.5) 
r2 = hotel("ekadashi pure veg", "panner patiyala", 450, "katraj", 5.3)
r3 = hotel("sainath", "chiken", 299, "karve nagar", 4.2)
r4 = hotel("supream hotel", 350, "pulav", "kumbhej", 3.5)
r5 = hotel("swarana", 499, "veg maratha", "warje", 3.3)  

print(r1.name)
print(r1.items)
print(r1.price)
print(r1.location)
print(r1.rating)

hotel_list = []
r2 = hotel("ekadashi pure veg", "panner patiyala", 450, "katraj", 5.3)
hotel_list.append(r2)

for hotel in hotel_list:
    print(r1.price,r1.name,r1.rating)

        
