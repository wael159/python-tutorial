
#exercise 1
print('Enter your name:')
x = input()
print('Hello, ' + x)

#exercise 2
print('first user enter your name:')
x1 = input()
print('second user enter your name:' + x)
x2=input()
if (len(x1)>len(x2)):
    print(x1," "  +  'has the longest name')
else:
    print(x2, " " + 'has the longest name')


#exercise 3
print('first user enter your name:')
x1 = input()
vowel_list=["A", "E" ,"I", "U","a","e","i","u"]
if x1[0] in vowel_list:
    print("Hello, " + x1)

#exercise 4
#Ask the user for his name, and tell him if the last letter is a vowel or a consonant
print('first user enter your name:')
x1 = input()
vowel_list=["A", "E","I","U","a","e","i","u"]
if x1[-1] in vowel_list:
    print("your last letter is vowel")
else:
    print("your last letter is constant")

#exercise 5
#Ask the user for two numbers (one after the other) and then print their sum
num1 = int(input(' please enter the first number here'))
num2 = int(input(' please enter the second number here'))
print(num1+num2)


#exercise 6
sentence=str(input (" print the longest sentence without any A" ))
if  'A' and 'a' not in sentence:
    print("the number of the letter that you write is", len(sentence)-sentence.count(" "))
else:
    print("fail")

#exercise 7
name=str(input ("enter you full name" ))
print(name.split())
if name.replace(" ", "").isalpha()==False:
   print("you must enter just letters")
if name.count(" ")!=1:
    print("you must enter your name with last name with just one space")
if name.split()[0].islower() or name.split()[1].islower() :
    print("your fisrt name  and last name must start with capital letters")

# Ask the user for a sentence, and then tell him how many words are in it.
sentence=str(input ("please enter a sentence" ))
print("the number of the words here is ," ,len(sentence.split()))

#Write a python program to get a string made of the first 2 and the last 2 chars from a given string, if the string length is less than 2, return instead the empty string.
#For example: "Helloworld" output "Held", while "Sik" returns ""
sentence=str(input ("please enter a sentence" ))
if len(sentence)<4:
    print("")
else:
    sub=sentence[0:2]+sentence[-2:]
    print(sub)

#Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then tell him how old he turnt/will turn this year.
import datetime
#x = datetime.datetime.now()
#print(x)
date_entry = input('Enter your birthday in DD/MM/YYYY format')
day, month,year= map(int,date_entry.split('/'))
print("in 2020 you will be {} years old".format(2020-year))


#for loops
name = ['Alex', 'Mike', 'Dylan', 'Yossi']
count=0
for i in name:
    count+=1
print("the number of the words here is {}".format(count))

#Write a program that print every name that starts by ‘a’
name=['Alex','Mike','Dylan','yossi','Alan']
count=0
for i in name:
    if i[0]=="A":
        count+=1
print(count)

#Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.
for i in range(11):
    if i not in [3,6]:
        print(i)

names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
for name in names:
    age=int(input("{} , please enter your agre here".format(name)))
    if age<16:
        print("we r so sorry we must delete your name")
        names.remove(name)
print("the final list is", names)

#Use a for loop to print the numbers from 1 to 20, inclusive.
for i in range(21):
    print(i)

#Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers
million=range(1,1000001)
print(min(million))
print(max(million))
print(sum(million))

#Write a program that returns the index of the first occurrence of an item in a list.
list1=['Rick', 'Morty', 'Rick', 'Jerry', 'Summer']
check='Rick'
for idx, val  in enumerate(list1):
    if val==check:
        print("the first ocuurence is ih the {} index".format(idx))
        break

# concatenate two lists withot + sign
list1=[0,1,0,2,3,0,3,1]
list2=[1,5,6,9,8,2,3]
for i in list1:
    list2.append(i)
print("the concatenated list is look like these {} ".format(list2))

#Create a board as following by using for loops:
for i in range(0,7):
    print("X"*i)
for i in reversed(range(0,6)):
    print("X"*i)

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

for i in range(3,31):
    if(i%3==0):
        print(i)

#Write a program that insert an item at a defined index. #todo

#________________________________________________________________________________________
#current_players = ['Mario', 'Luigi', 'Peach']
#new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
#i=0
#print(len(new_players))
#while i<len(new_players):
#    current_players.append(new_players[i])
#print(current_players)
#---------------------------------------------------------------------------------------------
count=1
for i in reversed(range(0, 5)):
    print(" "*i+"*"*count)
    count=count+1

#_______________________
#What is the output of the following?
x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

#--------------
print("hello world")

#------------------------------------------------------------------
count=1
for i in reversed(range(0, 5)):
    print("*"*count+" "*i)
    count=count+1
    if i==0:
        count = 0
        for i in reversed(range(0, 6)):
            print(" " * count + "*" * i)
            count = count + 1


#-------------------------------------------------------------------------------
count=1
for i in reversed(range(0,5,2)):
        print(int(i / 2) * (" ") + "*" * count + int(i / 2) * (" "))
        count = count + 2
#---------------------------------------------------------------------------
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if my_list[j] < my_list[minimum]:
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
#-----------------------------------------------------------------------
my_str = "I do"
my_text = "What I can't build, I do not understand."
found   = False
index = 0
for letter in my_text:
    if letter == my_str[index]:
        index += 1
        if index == len(my_str):
            found = True
            break
    else:
        index = 0

if found:
    print("<{}> was found in the text !".format(my_str))
else:
    print("<{}> is not in the text".format(my_str))
#---------------------------------------------------------------------------------------
#Write a program that prints the longest word in a list.
mylist='hey to all how are you'
mylist=mylist.split()

max_len=0
for idx,word in enumerate(mylist):
    length=len(word)
    if length>max_len:
        max_len=length
        word_idx=idx
print("the longest word is {}".format((mylist[word_idx])))

#------------------------------------------------------------------------------------------

#while loops
#pizza exersize
topping=input("please inser a topping to your pizza")
print("you’ll add that {} to your pizza".format(topping))
while topping!='quit':
    topping=input("please inser a topping to your pizza")
    if topping=='quit':
        print("thank you")
        break
    else:
        print("you’ll add that {} to your pizza".format(topping))
#--------------------------------------------------------------------------------------------------------
#Given a list, use a while loop to print out every elements from the end to the beginning.
mylist1=[1,2,3,4,5,6,6]
i=len(mylist1)
while i>0:
    print(mylist1[i-1])
    i=i-1
#------------------------------------------------------------------------------
#Use a while loop to print every number from 5 to 100
num=5
while(num<=100):
    print(num)
    num=num+1
#----------------------------------------------------------------
user_input = input("Password: ")
while user_input != "my_password":
    print("Access denied.")
    user_input = input("> ")
print("Access granted")

#it is an unlimited while loop

#-----------------------------------------

#Take the last exercise, and apply it to a family, ask every member of the family their age, and at the end of the loop, tell them the cost of the tickets for the whole family.
family_list=['Rick', 'Morty', 'Rick', 'Jerry', 'Summer']
total_price=0
i=0
while i<len(family_list):
    age=int(input("{} , please insert your age here".format(family_list[i])))

    if age<3:
        price=0
    elif age>3 and age<=12:
        price=10
    elif age>12:
        price=12
    i+=1
    total_price=price+total_price
print("the total price for your family is {}$".format(total_price))

#-----------------------------------------------------------------------------------------
#A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.

#Write a program that ask every user their age, and then tell them which can see the movie.
family_list=['Rick', 'Morty', 'Rick', 'Jerry', 'Summer']
new_list=[]
i=0
while i<len(family_list):
    age=int(input("{} , please insert your age here".format(family_list[i])))
    if age<16 or age>21:
        new_list=family_list.remove(family_list[i])
    i+=1
print("peopele who can enter to the cinema is {} ".format(new_list))

#----------------------------------------------------------------------------------------------------
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

num3=1500
while num3<2700:
    if num3%7==0 and num3%5==0:
        print(num3)
    num3=num3+1

#----------------------------------
#Count the number of spaces in a string.
string1='hey how are you'
i=0
count=0
while i<len(string1):
    if string1[i]==" ":
        count=count+1
        i=i+1
print("the number of spaces is {}".format(count))


#----------------------------------------------------
#Count the number of words in a string.
str1=input("Please Enter a string as you wish\n")
print(len(str1))
tot=1;
i=0
while i<len(str1):
    if(str1[i]==' ' or str1 == '/n' or str1 == '\t'):
        tot=tot+1
print("Total number of words in the given string= ",tot)

#------------------------------------------------------------------
# exercises of tthe while loop with hard level is not done yet

#________________________________________________________________________

#Dectionary
#creating a dictionary
dict_ages={"wael":28,"rabea":25,"hassan":18}
print(dict_ages)
#-------------------
#transforming dict
dict1={0: 10, 1: 20}
dict1[2]=30
print(dict1)
#--------------
# the max value in the dict
print("the max value in the dic is {} ".format(max(dict1.values())))
print("the min value is {} ".format(min(dict1.values())))

#--------------------------------------------------------
products = {
'SMART WATCH': 550,
'PHONE' : 1000,
'PLAYSTATION': 500,
'LAPTOP' : 1550,
'MUSIC PLAYER' : 600,
'TABLET' : 400
}
# foor loop with dict
for key,value in products.items():
    print(key,'-',value)

#------------------------------------------------------------------
#Write a Python program to remove duplicates values from Dictionary.
for key,value in products.items():
    if value not in products.values():
        products[key]=value
print(products)

#------------------------------------------------------
#Write a Python script to check if a given key already exists in a dictionary.
key_tocheck=input("please insert the key that you want to check")
for key,value in products.items():
    if key_tocheck in products.keys():
        print("the key is found in the dict")
        break
#another solution
if key_tocheck in products:
    print("the key is found")
#------------------------------------------------------------------------------
#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
new_dic={}
for d in [dic1,dic2,dic3]:
    new_dic.update(d)
print(new_dic)

#-------------------------------
list1 = ['Rick', 'Donald', 'Mickey' , 'Mario']
list2 = ['Sanchez', 'Duck', 'Mouse', 'Kart']
new_dict={}
i=0
for idx,value in enumerate(list1):
    new_dict[value]=list2[idx]
print(new_dict)


#----------------------------------------------
#Ask the user how many money he got, then display products that he can afford.
products = {
'SMART WATCH': 550,
'PHONE' : 1000,
'PLAYSTATION': 500,
'LAPTOP' : 1550,
'MUSIC PLAYER' : 600,
'TABLET' : 400

}
money=int(input("how many money you get?"))
if money<min(products.values()):
    print("you cant afford any thing")
else:
    for key, value in products.items():
        if money >= value:
            print("you can buy {} , it costs {} ".format(key,value))

#------------------------------------------------------------------
#Get a number from the user, and then spell each number in words, for example, if the user input 1234:
num_dict={0:"zero",1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', }
num_to_word=input("insert a number and you will get the words")
for i in num_to_word:
    print(num_dict[int(i)])
#----------------------------------------------------------------------------
#Get a number from the user and create a dictionnary where the keys are every number from 1 to this number, and values are the square of keys.
num_to_square=int(input("please inser a number"))
dict_power={}
for i in range(1,num_to_square+1):
    dict_power[i]=i**2
print(dict_power)
#--------------------------------------------------------------------------------
#Make a dictionnary called contacts and add three of your friends with their phone number
contacts={"Eyal":"0586878399",
"John":"0542815674",
"Mario":"0512345678"}
#adding another contact
contacts["wael"]="0502165547"

#print all te contacts
[print(key,"-",value) for key,value in contacts.items()]

#search if a given name exists:
name=input("enter a name to search if it is in te contacts")
if name in contacts.keys():
        print("the name is in the contacts")
else:
    print("the name is not in the contacts")

#Write a code that searches if a given number exists in the contacts, if it exist, then print his name.
number=input("enter a number to search if it is in te contacts")
if number in contacts.values():
        print("the number is in the contacts, his name is {}".format(list(contacts.keys())[list(contacts.values()).index(number)]))
else:
    print("the number is not in the contacts")

#Given another dictionnary of contacts, add it to your dictionnary
contact2={"Eyal2":"0546878399",
"John2":"0522815674",
"Mario2":"0212345678"}
contacts.update(contact2)
print(contacts)

#Count how many contacts are in your dictionnary
print(len(contacts))

#sorted items
print(sorted(contacts.items()))

#-------------------------------------------------------------------------------------------------------
#Write a Python program to combine two dictionary adding values for common keys. Go to the editor
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for key, value in d1.items():
    if key in d2:
        d3[key]=d1[key]+d2[key]
    else:
        d3[key]=value
        for key1, value1 in d2.items():
            if key1 not in d1.items():
                d3[key1]=value1

print(d3)

#--------------------------------------------------------------------------------------------------------
#function

def display_message():
    print("hey my name is wael")
display_message()

#--------------------------------
def favorite_book(title):
    print("one of my favorite book is {} ".format(title))
favorite_book("hello world")
#---------------------------------------
def make_shirt(size, text):
    print("the size of the t shirt is {}".format(size))
    print(text)
make_shirt(15, "hello to all")

#--------------------------------------------
def get_age(year, month, day):
    import datetime
    date_birth=datetime.date(year,month,day)
    date_now=datetime.datetime.now().date()
    return  date_now-date_birth

print(get_age(1992,9,24))
