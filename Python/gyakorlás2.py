import random
a=random.randint(1,100)
print("Random szám")
os=0
for x in range(1,a+1):
    if a%x==0:
        os+=1 
if os==2:
    print("prím",os,"osztója van")
else 
    print("nem prím!",os,"osztója van")
