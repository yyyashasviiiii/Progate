# PREPARING THE ITEMS


# Create a dictionary with keys and values, and assign it to the items variable
items = {'apple':2,'banana':4,'orange':6}
# Create a for loop that gets the keys of items
for item_name in items:
    # Print '--------------------------------------------------'
    print("--------------------------------------------")
    # Print 'Each ___ costs ___ dollars'
    print("Each "+item_name+" costs "+str(items[item_name])+" dollars")
    
    
# BUYING AN ITEM


items = {'apple': 2, 'banana': 4, 'orange': 6}
for item_name in items:
    print('--------------------------------------------------')
    print('Each ' + item_name + ' costs ' + str(items[item_name]) + ' dollars')
    
    # Receive a value by using input(), and assign it to the input_count variable
    input_count = input('How many '+item_name+'s do you want?: ')
    # Print 'You will buy ___ ___s' by using input_count and item_name
    print("You will buy "+input_count+" "+item_name+" s")
    
    # Convert input_count to an integer and assign it to the count variable
    count = int(input_count)
    # Multiply the price of each item and the count variable, and assign it to the total_price variable
    total_price = items[item_name] * count
    # By using total_price and type conversion, print 'The total price is ___ dollars'
    print("The total price is "+str(total_price)+" dollars")
    
    
    # CONTROL FLOW
    
    
    # Assign 20 to the money variable
money = 20

items = {'apple': 2, 'banana': 4, 'orange': 6}
for item_name in items:
    print('--------------------------------------------------')
    # Using the money variable, print 'You have ___ dollars in your wallet'
    print("You have "+str(money)+" dollars in your wallet")
    print('Each ' + item_name + ' costs ' + str(items[item_name]) + ' dollars')
    
    input_count = input('How many ' + item_name + 's do you want?: ')
    print('You will buy ' + input_count + ' ' + item_name + 's')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('The total price is ' + str(total_price) + ' dollars')
    
    # Add control flow based on the comparison of money and total_price
    if money >= total_price:
        print("You have bought "+input_count+" "+item_name+" s")
        money -= total_price
    else:
        print("You do not have enough money")
        print("You cannot buy that many "+item_name+"s")
        
  
  # THE REMAINING MONEY
  
  
  money = 20
items = {'apple': 2, 'banana': 4, 'orange': 6}
for item_name in items:
    print('--------------------------------------------------')
    print('You have ' + str(money) + ' dollars in your wallet')
    print('Each ' + item_name + ' costs ' + str(items[item_name]) + ' dollars')
    
    input_count = input('How many ' + item_name + 's do you want?: ')
    print('You will buy ' + input_count + ' ' + item_name + 's')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('The total price is ' + str(total_price) + ' dollars')
    
    if money >= total_price:
        print('You have bought ' + input_count + ' ' + item_name + 's')
        money -= total_price
        # When money is equal to 0, print 'Your wallet is now empty' and stop the loop
        if money == 0:
            print("Your wallet is now empty")
            break
        
        
    else:
        print('You do not have enough money')
        print('You cannot buy that many ' + item_name + 's')
# Using the money variable and type conversion, print 'You have ___ dollars left'
print("You have "+str(money)+" dollars left")


#<--------------------------------------END------------------------------------------------>
