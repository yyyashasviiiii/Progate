# CALCULATING PRICES
#<----------------->

# Assign 2 to the apple_price variable
apple_price = 2

# Assign 5 to the count variable
count = 5

# Assign the result of apple_price * the count variable to the total_price variable
total_price = apple_price * count

# By using the count variable, print 'You will buy .. apples'
print("You will buy" + str(count)+ "apples")

# By using the total_price variable, print 'The total price is .. dollars'
print("The total price is "+str(total_price)+" dollars")


# GETTING INPUT
#<------------->

apple_price = 2

# Receive the number of apples by using input(), and assign it to the input_count variable 
input_count = input("How many apples do you want?: ")

# Convert the input_count variable to an integer, and assign it to the count variable
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')

# CONTROL FLOW
#<------------>

apple_price = 2
# Assign 10 to the money variable
money = 10

input_count = input('How many apples do you want?: ')
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')

# Add control flow based on the comparison of money and total_price
if(money > total_price):
    print("You have bought "+str(count)+" apples")
    print("You have"+str(total_price-money)+" dollars left")
elif money == total_price:
    print("You have bought "+str(count)+" apples")
    print("Your wallet is now empty")
else:
    print("You do not have enough money")
    print("You cannot buy that many apples")
    
    
