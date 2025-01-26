# # Guess the number
# import random #(its a library which can generate random charecter)
# target_num=random.randint(1,100)#randint function gives a random number which is btw the given range of 1-100
# while True:#loop end na hoa obdi number same thakbe as kaj loop er modhey cholche so jotokhon na randint function abar call hochee totokhon number will same loop end hole abar prothome cursor giye randit call hbe and then number change before that  number will be same.

    # guess_num=input("write your guessed number or Quit(type Q):")
    # if (guess_num=="Q"):
    #     break
    # guess_num=int(guess_num)
    # if(target_num==guess_num):
    #     print("sucess")
    #     break#as soon as break execute loop will break
    # elif(target_num>guess_num):
    #     print("guess a big number")
    # else:
    #     print("guess a small number")
    
# print("Game over") 

#Random Password Generator
import random
import string #this have different type charecter inside it.
letters=string.ascii_letters#this variable have all a-z and A-Z letters and we get the value in the form of string.
# print(letters)
digits=string.digits#it give all 0-9 digits
# print(digits)
puncutaion=string.punctuation #it gives all special charecter
# print(puncutaion)
charvalues=puncutaion+letters+digits
value=random.choice(charvalues)#whenever this choice function will be called it will generate a random charecter from the non empty data(in form of list or tuple or string etc) of random charecter we will give inside the it=>()
password_len=12
password=""
for i in range(password_len):
    # print(random.choice(charvalues))# we have to write full function then only function will call for every iteration otherwise if we write value then opore ekbar function call hoye just oi ekta value ie 12 bar print hoe jbe because loop er vetorey kaj chole baire giye function statement read hbe na during loop running, we know we have to write the exact function to call the functin otherwise it will not callled
    password=password+random.choice(charvalues)
print(password) 

