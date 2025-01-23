
##40 CHALLENGES BY SIDAKBIR SINGH


# Level 2 challenges

# C5

#first number asked , interpreted as a float
a= float(input("enter a number"))

#second number asked , same conditions.
b = float(input("enter another number"))
#alg for the sum of the numbers
add= a+b
# outputting the value
print ( add)

#C6

#first number asked , interpreted as a float
a= float(input("enter a number"))

#second number asked , same conditions.
b = float(input("enter another number"))
#alg for the sum of the numbers
add= a+b
#alg for the multiplication of the numbers
multiply= a*b
# outputting the values
print ( add)
print ( multiply)

#C7 
#opening sentence outputed to inform the user what the program is about
print("to calculate the speed we would require some values-")
#var inputing the distance in meters
distance= float(input("enter the distance (in meters)"))
#var inputing the time in seconds
time= float(input("enter the time (in seconds)"))
#alg to calculate the speed
speed= distance/time
#outputing speed
print('here is the speed', speed,"mps")


#LEVEL 3 CHALLENGES

#C8

#opening sentence outputed to inform the user what the program is about
print("to calculate the total bill we need some values-")
#inputing the minutes 
minutes= float(input('enter the minutes used in the last month'))
#finding the cost
cost_minutes=minutes *0.10
#inputing the amount of texts sent 
texts= float(input("enter the number of texts sent last month"))
#finding the cost
cost_texts=texts*0.05
#alg to calculate the bill without additional monthly charge (amc)
bill_no_amc= cost_minutes+cost_texts
print("The bill without addtitional charge(£10.00)=","£",bill_no_amc)
#alg to calculate the bill with additional monthly charge (amc)
total_bill= bill_no_amc + 10.00
print("The bill with addtitional charge(£10.00)=","£",total_bill)


#C9
#not sure how to get a random first name (only way i can think to do this is by making a list and using random)
#but that would be me giving the names in the list so that is not random


#C10
#asking the input from the user
user_ans= int(input('how many letters in the alphabet?'))
#if statement to decide if they got it correct
if user_ans==26:
    print('correct!')
else:
    print('WRONG!')


#LEVEL 4 CHALLENGES
    

#C11
#asking the first number
num1=float(input('enter a number'))
#asking the second number
num2=float(input('enter a different number'))
#alg if num1 is greater then print num1, num2 greater then num2 or if they're the same say none
if num1>num2:
    print(num1)
elif num2>num1:
    print(num2)
elif num1==num2:
    print('no number is greater, they are the same')    


#C12
import random

num=random.randint(1,10)
#asking for the input
user_num= input('enter an integer between 1-10')
#if statement to decide if they got it correct
if num==user_num:
    print('CORRECT!')
else:
    print('not what I was thinking')
    print('my number was',num)


#C13

#total amount of holidays given= 28
#asking the amount of days they work 
employee=int(input('how many days does the employee work?'))
#setting vars for the holiday allowance of people who work the respective days
one_day_employee_holidays= 28 *(1/5)
two_day_employee_holidays= 28 *(2/5)
three_day_employee_holidays= 28 *(3/5)
four_day_employee_holidays= 28 *(4/5)

#if elif condition to determine and print the holiday allowance
#round() used to round the decimal holidays
if employee==5:
    print('The employee gets',28 ,'holidays')
elif employee==4:
    print('The employee gets',round(four_day_employee_holidays) ,'holidays')
elif employee==3:
    print('The employee gets',round(three_day_employee_holidays),'holidays')
elif employee==2:
    print('The employee gets',round(two_day_employee_holidays) ,'holidays')
elif employee==1:
    print('The employee gets',round(one_day_employee_holidays) ,'holidays')


#LEVEL 5 CHALLENGES
    
#C14

traffic_light= input('what color is the traffic light? Red, amber or green?')

if traffic_light=='amber' or traffic_light=='Amber' or traffic_light=='AMBER':
    print('get ready')
elif traffic_light=='green'or traffic_light=='Green' or traffic_light=='GREEN':
    print('go')
else:
    print('stop')

#C15
#asking the question for a response
user_response = input('enter one of the olympic values')
#if statement(to decide the correct answer) with 'or' operator to make the the code more robust/efficient 
if user_response=='Respect' or user_response=='Excellence' or user_response=='Friendship':
    print('Thats correct!')
else:
    print('Incorrect')


#C16

#asking the question for a response
hours_watched= float(input('how many hours do you spend on the TV on average'))
#if statement(to decide the correct answer) with 'and' operator to make the the code more robust/efficient 
if hours_watched<2:
    print('that should be okay')
elif hours_watched>=2 and hours_watched<4:
    print('that will rot your brain')
else:
    print('That is too much TV!')


#C17
    
#setting var
digits=1
#while loop, as long as 'digit' is less than or equal to 10 it will increase by 1(starting from 1)
while digits<= 10:
    print(digits)
    digits+=1


#C18
    
#setting var
digits=1
#while loop, as long as 'digit' is less than or equal to 20 it will increase by 2 to stay odd(starting from 1)
while digits<= 20:
    print(digits)
    digits+=2


#C19

#var to ask the number
user_guess= int(input('enter a number, try to guess what im thinking (hint 1-15)'))
# used later in the while loop as a condition
message='try again'
#  I think I made it a bit complicated.
#while loop repeats until the message is not 'try again'
while message=='try again':
    if user_guess!=7 :
        print(message)
        user_guess= int(input('enter a number, try to guess what im thinking (hint 1-15)'))
    elif user_guess==7: 
        message= 'well done'
        print(message)

#OCR CHALLENGES
#C20
#Not sure how to do it without having the list
        
#C21

#asking for age
member_age= int(input('what is the age of the member?'))
#if, elif, else conditions to decide the discount
if member_age>=13 and member_age<=15:
    #and used to make it between 13 and 15
    print('you will get a 30 percent discount')
elif member_age>= 16 and member_age<=17:
    #and used to make it between 16 and 17
    print('you will get a 20 percent discount')
elif member_age>=50:
    #over 50 members
    print('you will get a 40 percent discount')
else:
    #none meet criteria
    print('no discount')


#C22


#asking for the marks
marks=float(input('enter the amaount of marks you got'))

#making a function not needed at all but why not :)
def grade():
    if marks<10:
        print('U')
    elif marks >= 10 and marks<20:
        print('1')
    elif marks >= 20 and marks<30:
        print('2')
    elif marks >= 30 and marks<40:
        print('3')
    elif marks >= 40 and marks<50:
        print('4')    
    elif marks >= 50 and marks<60:
        print('5')
    elif marks >= 60 and marks<70:
        print('6')
    elif marks >= 70 and marks<80:
        print('7')
    elif marks >= 80 and marks<90:
        print('8')
    elif marks >= 90 and marks<100:
        print('9')

#calling the function so it is initiated
grade()


#C23

#var to ask for the amount they need to convert to coins
user_money_to_convert=float(input('enter the amount of money you want to convert to coins'))
#var to store what type of coversion takes place 
user_convert_to=input('What type of coin do you want to convert to: £1, 50p, 20p, 10p, 2p?')
#function that determines what type it is based on the var, calculates the ammount of coins returned in the the conversion value
def conversionValue():
    ##print(user_convert_to)
    if user_convert_to =='1':
        #rounding the value to get how many pounds are in the user_money_to_convert var
        one_conversion=round(user_money_to_convert)
        print('Amount of £1 coins are', one_conversion,'the decimal values cannot be returned as 1 pound(if relevant)')
    elif user_convert_to=='50':
        #rounding the value and using a multiplier to get how many 50p are in the user_money_to_convert var
        fifty_conversion=round(user_money_to_convert*2)
        print('Amount of 50p coins are',fifty_conversion,'the other decimal values cannot be returned as 50 p(if relevant)')
    elif user_convert_to=='20':
        #rounding the value and using a multiplier to get how many 20p are in the user_money_to_convert var
        twenty_conversion=round(user_money_to_convert*5)
        print('Amount of 20p coins are',twenty_conversion,'the other decimal values cannot be returned as 20 p(if relevant)')
    elif user_convert_to=='10':
        #rounding the value and using a multiplier to get how many 10p are in the user_money_to_convert var
        ten_conversion=round(user_money_to_convert*10)
        print('Amount of 10p coins are',ten_conversion,'the other decimal values cannot be returned as 10 p(if relevant)')
    elif user_convert_to=='2':
        #rounding the value and using a multiplier to get how many 2p are in the user_money_to_convert var
        two_conversion=round(user_money_to_convert*50)
        print('Amount of 2p coins are',two_conversion,'the other decimal values cannot be returned as 2 p(if relevant)')

#calling the function so it is initiated
conversionValue()


#C24

#importing the module just in case
import random
#creating an array to work with the random.choice so the computer can generate rock, paper or scissors
RPS_list=['rock','paper','scissors']
#function to choose randomly RPS from the array
comp_choice= random.choice(RPS_list)
#asking the user for their input
user_RPS= input('choose rock, paper or scissors')
#converting the users input into lowercase to preven any errors
user_RPS.lower()
def decideWin():
    if user_RPS==comp_choice:
        #game tied outcome
        print('game tied')
        #outputing what the computer generated
        print('I chose', comp_choice)

    elif user_RPS=='scissors' and comp_choice=='rock':
        #computer wins outcome
        print('computer wins')
        #outputing what the computer generated
        print('I chose', comp_choice)

    elif user_RPS=='rock' and comp_choice=='paper':
        #computer wins outcome
        print('computer wins')
        #outputing what the computer generated
        print('I chose', comp_choice)

    elif user_RPS=='paper' and comp_choice=='scissors':
        #computer wins outcome
        print('computer wins')
        #outputing what the computer generated
        print('I chose', comp_choice)

    else:
        #user wins outcome
        print('YOU WIN!')
        #outputing what the computer generated
        print('I chose', comp_choice)

#calling the function so it is initiated
decideWin()

#C25
#not sure how to do this without the RaceFile , the questions I didnt do definitly need to work on

#C26

#asking the user to input the do age
user_input_dog_age=int(input('enter the dog age in years'))
#making the human age var outside the if statement(global)
human_age=0
#the additional years to be added to convert the age after 2 years of dog age
aditional_years=(user_input_dog_age*6)-12
#if statement to decide and covert the age
if user_input_dog_age<= 2:
    #human age if dog age is below or equal 2
    human_age=user_input_dog_age*12
elif user_input_dog_age>2:
    #dog age if dog age is above 2
    human_age=24+aditional_years
#finally printing the age 
print('The human equivalent age is',human_age)


#C27

#inputing the amount of passengers
passengers=int(input('how many passengers are going'))
#inputing the distance
distance_journey=int(input('whats the distance'))
#function to find cost
def findCost():
    #maths for finding the distance without there being any additional charge for amount of passengers
    cost_distance=(distance_journey*2)+1
    if passengers>=5:
        #adding additional charge for 5 passengers or more using a multiplier 1.5 (50% increase)
        cost_distance=cost_distance*1.5
        #outputing the cost
        print('your total cost is',cost_distance)
    else:
        #outputing the cost without added charge
        print('your total cost is',cost_distance)
#calling the function so it is initiated
findCost()


#LEVEL 6 CHALLENGES

#C28

#importing the module 'math' as we would need it for pi
import math
#a sentence outputed to tell the user abbout the program
print('To find how much turf you need we need some values')
#asking for the length of the rect
rect_length=float(input('enter the length of the lawn(in meters)'))
#asking for the width of the rect
rect_width=float(input('enter the width of the lawn(in meters)'))
#finding the area of the rect
rect_area=rect_length*rect_width
#asking the radius of the flowerbed
flower_bed_radius=float(input('enter the radius of the circular flower bed in the middle(in meters)'))
##print(rect_area)
#finding the area of the circle using math.pi
flower_bed_area=math.pi*(flower_bed_radius**2)
##print(flower_bed_area)
#finding the amount of turf
turf_needed=rect_area-flower_bed_area
#outputing the amount of turf in metres
print('You would need',turf_needed,'meters of turf!')

## lines of code is just me logging some values to test if the program is working :)

#C29

#asking the numbers of teddy bears
number_teddy= int(input('how many teddy bears were sold'))
#finding the wage with the teddy bears
wage_bear= number_teddy*2
#asking the numbers of hours
number_hours= float(input('how many hours did they work'))
#finding the wage with the hours
wage_hours=number_hours*5
#if statement to find which is greater
if wage_bear>wage_hours:
    #wage from the bears is bigger so thats being outputed
    print('the wage is £',wage_bear)
else:
    #wage from the bears is bigger so thats being outputed
    print('the wage is £',wage_hours)


#C30

#asking one side
side1=float(input('enter one side'))
#asking another side
side2=float(input('enter the second side'))
#asking another side
side3=float(input('enter the third side'))
#easy and simple if statement to compare every case of the sides being the same to determine if its an isosceles triangle
if side1==side2 or side1==side3 or side2==side3:
    #true
    print('Isosceles Triangle')
else:
    #false
    print('Not Isosceles')


#C31

# the number of weights asked the user
weights=int(input('enter the number of weights'))
#used in the while loop later
i=0
#and array/list for all the weights entered
weights_list=[]
#while loop to keep asking the question until the number of weights is the number of weights they will input
while i< weights:
    #var that will ask the weight
    a=int(input('enter a weight'))
    #.append(one of my fav functions:)) this adds the value to the list/array
    weights_list.append(a)
    print(weights_list)
    #var for the counter ask the question the right amount of times
    i+=1
##print(weights_list)

##print(sum(weights_list))
#sum used to add all the values in the list/array
mean=sum(weights_list)/weights
#outputing the final value and rounding it to 2 decimal places
print('the average weight is',round(mean,2))

#C32

##sorry for the long code, I was trying something new, prob used lists and vars that were not really required
#Starting line to tell what the program is about
print('This program will help you invest in the bank account that will maximise your savings! ')
#var to ask for initial money she/he wants to save
money_to_be_saved= float(input('enter the amount of money you want to save '))
# var number of banks she wants to compare to
banks_amount=int(input('enter the amount of banks you want to compare (max 10) '))
#function to just print the right amount of banks with their interest rates as asked by the user 
def returnBanks():
    # array/list containing 10 of the best banks with highest rates, I researched
    # \n just used for a new line to clear the clutter
    banks=["1. First Direct: 7% fixed for one year \n",'2. Co-operative Bank: 7 % variable for one year \n','3. Nationwide 6.5 % variable for one year \n',
        '4. Lloyds Bank(needs a club Lloyds account) 6.25 % fixed one year \n','5. Natwest/RBS: 6.17% variable up to £5000 \n',
        '6. TSB: 6% fixed for one year \n','7. Bank of Scotland: 5.5% fixed for one year \n','8. Halifax: 5.5% fixed for one year \n','9. Lloyds Bank: 5.25% fixed for one year\n',
        '10. HSBC: 5% fixed for one year']
    #this line of code only prints the amount of banks required(it takes the number of banks from the list and just does'nt print the rest that are not required)
    number_of_banks=banks[0:banks_amount]
    #this converts/joins the indexes from the list and makes it a string, easier to read for the user
    banks_string=''.join(number_of_banks)
    #outputs the interest rates with names to user
    print(banks_string)
#another array/list is declared, named interest
interest=[]
#function that finds the total money after interest for ALL the banks
def findInterest():
    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*7
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*7
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*6.5
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*6.25
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*6.17
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*6
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*5.5
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*5.5
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*5.25
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))

    #i is made a local var just to be used to find the interest
    i=(money_to_be_saved/100)*5
    #total is made a local var to find interest+money saved at start
    total=i+money_to_be_saved
    #.append() :) , adds the total value to interest[] list
    interest.append(str(total))
#function called from before
returnBanks()
#function is finished and is called
findInterest()
#now this line takes the interest[] and prints the only total values for amount of banks to be compared
print('interests in order of banks printed £',interest[0:banks_amount])

#sorry again for the long code, could be shorter

##LEVEL 7 CHALLENGES

#C33

#var to ask amount of gcses they did
num_gcses=int(input("enter the number of GCSE's you have "))
#list/array for all the results they give
gcses_add=[]
#global var
i=0
#while loop to ask them their grade the same amount of times as the amount of gcses they did
while i<num_gcses:
    a=int(input('Enter the grade you got for your gcses '))
    #adding grade to list
    gcses_add.append(a)
    #looping
    i+=1
#adding all the values in the array/list
score= sum(gcses_add)
#if the sum is above or equal to 40 they can go sixth form
if score>= 40:
    print('You can go sixth form! \n Your score was:- ',score)
#discussion can be needed if in a specific range
elif score>=35 and score<=39:
    print('A discussion is needed. \n Your score was:- ',score)
#not eligible
else:
    print('Sorry not enough points! \n Your score was:- ',score)

#34

#array/list to hold all elec values
elec_week=[]
#global var
i=0
#asking 7 times for each day(elec)
while i<7:
    a=float(input('enter the elec for the days of the week'))
    #.append()  :)
    elec_week.append(a)
    i+=1
#var that finds the smallest number in the list using min()
smallest= min(elec_week)
#var that finds the position(index) of that smallest number in the list
place_of_smallest=elec_week.index(smallest)
##print(smallest)
#adding 1 to make it easier as the first number in the list is actualy the '0' position
day=place_of_smallest+1

#easy if-elif-else selection to determine the day of the week and outputing it
if day==1:
    print('The day free of charge is Monday!')
elif day==2:
    print('The day free of charge is Tuesday!')
elif day==3:
    print('The day free of charge is Wednesday!')
elif day==4:
    print('The day free of charge is Thursday!')
elif day==5:
    print('The day free of charge is Friday!')
elif day==6:
    print('The day free of charge is Saturday!')
else:
    print('The day free of charge is Sunday!')


#35

#just thought to use round up .ceil()
import math
#asking num of cars available
num_cars=int(input('Enter the number of cars available '))
#calculating total amount of people that can sit
num_ppl_cars_can_hold=num_cars*5
#asking for amount of people
num_ppl=int(input('Enter the number of people going '))
#if to decide is enough cars or if not how many needed
if num_ppl_cars_can_hold>=num_ppl:
    print('We have enough seats ')
else:
    #finding the people that are left/extra
    diff=num_ppl-num_ppl_cars_can_hold
    ##print(diff)
    #dividing the diff by amount of people that can sit in the car
    more_cars=diff/5
    #rounding it UP to find the amount of cars needed. math.ceil()
    print(math.ceil(more_cars),'more car(s)')



##LEVEL 8 CHALLENGES

#36

#Importing Math for rounding down .floor()
import math
#declaring values
petrol=1.40
diesel= 1.55
lpg=0.95
#function to find the price of the fuel and change given back
def priceFuel():
    type_fuel=input('what type of fuel is your car? Petrol, Diesel or LPG ')
    type_fuel.lower()
    #global var declared as I will need it later
    global litres
    litres=float(input('enter the amount of litres you put into your car '))
    #simple if-elif-else function which askes the money that user gives after telling them the price and gives change if any
    if type_fuel=='petrol':
        price=litres*1.40
        print('The total price is £',price)
        #global var declared as I will need it later
        global user_money_given
        user_money_given=float(input('How much money have you given to the machine? '))
        change=user_money_given-price
        print('Your change is £',change)

    elif type_fuel=='diesel':
        price=litres*1.55
        print('The total price is £',price)
        user_money_given=float(input('How much money have you given to the machine? '))
        change=user_money_given-price
        print('Your change is £',change)
    else:
        price=litres*0.95
        print('The total price is £',price)
        user_money_given=float(input('How much money have you given to the machine? '))
        change=user_money_given-price
        print('Your change is £',change)
#calling function so its initiated
priceFuel()
##print(litres,user_money_given)
def loyaltyPoints():
    #could have used bool but decided not to
    loyalty_card=input('Do you have a loyalty card? ')
    loyalty_card.lower()
    #nested loops to add loyalty points to loyalty card if applicable
    if loyalty_card=='no':
        print('Thats all then, Thank You!')
    elif loyalty_card=='yes':
        l_points=(math.floor(litres))+(math.floor(user_money_given))
        if l_points>100:
            additional_l_points=l_points/10
            print('You gained ',round(l_points+additional_l_points),'points!')
        else :
            print('You gained ',l_points,'points!')
#calling function so its initiated
loyaltyPoints()

#C37

#i var declared that has a set value that will not change as i dont change it after
#used as a constant
i=0
#while loop that loops the process if you press cancel(infinitly)
while i<10:
    #var to ask their choice
    choice=int(input('Please enter your choice \nBetween 1-20 '))
    #confirmation
    confirm=input('Please confirm, \nPress Okay to continue. \nPress Cancel to start again. ')
    confirm.lower()
    #if-else to do confirmation
    if confirm=='okay':
        print('Please collect your drink')
        #breaks the loop and does not repeat again :)
        break
    else:
        #i=0 to keep i constant
        i=0

## LEVEL 9 CHALLENGES

#C38

#Starting statement to tell what the program is about
print('This program will calculate your growth of the savings plan')
#setting i as a counter
i=0
#final list that contains the final value for each year
final=[0]
#asking amount of years they are saving for 
years_of_s=float(input('Enter the amount of years you are saving for- '))
#setting indx as a counter to fetch the indx value from the final list
indx=0
#looping the code for amount of years
while i<years_of_s:
    #asking the amount of money paid each year
    paid_in=float(input('Enter the amount of money you have paid in for each year- '))
    #this line fetches the value from the final list that is at the 'indx' index
    start=final[indx]
    #printing start value
    print('This is the start value this year:- £',start)
    #dividing the start by ten to find 10% of the start value and adding 10
    interest_add=((start/10)+10)
    #printing added interest
    print('This is the added interest this year:- £',interest_add)
    #appending the sum of all the values to find final price
    a=final.append((paid_in+start+interest_add))
    #changing indx by adding one so it gets to the next index
    indx+=1
    #converting an interger list to string by converting every integer to a string then joining the by ''
    final_string=''.join(str(final[indx]))
    #printing the final value
    print('This is the final value this year:- £',final_string)
    #adding one to the i counter so the code repeats again for the same amount of times as the number of years inputed
    i+=1



#C39

#importing random
import random
#starting statement to tell what the program is about
print('This is a test with 10 questions \nMarks at end')
#array that holds the points they get after each question(correct=1, wrong =0)
scores=[]

operators=['+','*','/','-']
#asking the name
name=input('enter name ')
for i in range(0,10):
    #two random integers
    digit_one=random.randint(0,100)
    digit_two=random.randint(0,100)
    #list with the four operators
    #random operator
    operator=random.choice(operators)
    #creating the question
    question=(digit_one,operator,digit_two)
    #printing it
    print(question)
    #global vars just in case
    global answer
    global comp_answer
    #converter for operators(pretty inefficient but yh)
    if operator=='+':
        comp_answer=digit_one+digit_two
    elif operator=='-':
        comp_answer=digit_one-digit_two
    elif operator=='*':
        comp_answer=digit_one*digit_two
    elif operator=='/':
        comp_answer=digit_one/digit_two
    #inputs the students answer
    answer=float(input('enter your answer '))
    #checking if answer is correct 
    if answer==comp_answer:
        print('correct')
        #.append() :) to add 1 mark if correct ,0 if not
        scores.append(1)
    else:
        print('wrong')
        print('The answer was= ',comp_answer)
        scores.append(0)
    #increasing the counter
    i+=1
#priting the final score by adding the scores list/array
print('Your score was= ',sum(scores),'out of 10!')













