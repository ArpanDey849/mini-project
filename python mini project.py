#Guess the number
import random #(its a library which can generate random charecter)
target_num=random.randint(1,100)#randint function gives a random number which is btw the given range of 1-100
while True:

    guess_num=input("write your guessed number or Quit(type Q):")
    if (guess_num=="Q"):
        break
    guess_num=int(guess_num)
    if(target_num==guess_num):
        print("sucess")
        break#as soon as break execute loop will break
    elif(target_num>guess_num):
        print("guess a big number")
    else:
        print("guess a small number")
    
print("Game over") 
