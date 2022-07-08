"""
print("Hello World")
print("Luyanda Madonsela")
print("Success " * 3)
print("Success" + " Yes")

price = 10

price_Yes = True

if price<100:
    print(price)
    
elif price_Yes==True:
    print('Yes it is true')
    
name = input("what is your name? ")
color = input("What is your favourite color? " )
print(name + " loves " + color)

weight_lbs = input("Please enter your weight in pounds ")
weight_kgs = int(weight_lbs) * 0.6
print("You are " + str(weight_kgs)) #have to convert weight_kgs back to string type in order to concatenate


print('''  Hot Day today       
      
      Please drink plenty of water   
                              ''')



name = input("Please enter your name: ")

if len(name)<3:
    print("Name must be at least 3 characters long")
elif len(name)>=50:
    print("Name has to have a maximum of  50 characters")
else:
    print("Name looks good")
    

    
prices = [10,20,30]  
total = 0 
for i in prices:
    
    total+=i
    
print(f'Total price is {total}')
"""

numbers = [1,2,3,4,5]
numbers.insert(-1,6)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers2.reverse()
numbers2.pop()
print(numbers2)
print(len(numbers))

for i in range(1,5):
    for j in range(1,5):
        if j>2 and i<2:
            print(f'({i},{j})')

for i in range(len(numbers)):
        if numbers[i]<3:
            numbers[i]+=2

print(numbers)           

if 12 in numbers2:
    print(numbers2)       
    
