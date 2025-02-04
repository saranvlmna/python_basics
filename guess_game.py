secret_word = "hey"
guess = ""
num_of_try = 0
     
try:
 while guess != secret_word:
    guess = input("Enter guess: ")
    
    if guess == secret_word:
        print("You Win!")
        break
    
    num_of_try += 1
    
    if num_of_try == 3:
        retry = input("Need more tries? (yes/no): ")
        if retry.lower() == "yes":
            num_of_try = 0
        else:
            print("You lose!")
            break

except:
   print("Error")