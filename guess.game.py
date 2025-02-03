secreat_word= "hey"
guess = ""
num_of_try=0

while guess != secreat_word:
      guess = input("Enter guess: ")
      if(num_of_try==3):
       print("You lose!")
       break
      if(guess == secreat_word):
       print("You Win!")
       break
      num_of_try +=1
      
