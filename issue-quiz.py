score = 1

questionOne = input("Renewable Energy has seen dramatic growth in the U.S. over the past decade. For the following quiz, enter 'T' for true and 'F' for false.\nQuestion 1: There has been a 4-fold growth in annual Wind generation? ")

if questionOne == "F":
  questionTwo = input("CORRECT! There's actually been a 5 FOLD annual increase in Wind generation.\nQuestion 2: There has been a 39-folk growth in annual Solar generation? ")
  score = score + 1
else:
  questionTwo = input("Actually, there's been a 5 FOLD annual increase in Wind generation.\nQuestion 2: There has been a 39-fold growth in annual Solar generation? ")

if questionTwo == "T":
  questionThree = input("CORRECT! That's an incredible increase in Solar generation.\nQuestion 3: There have been 200,050 Electric Vehicles sold through 2017? ")
  score = score +1
else:
  questionThree = input("It's actually TRUE, there has been a 39-fold growth in annual solar generation.\nQuestion 3: There have been 200,050 Electric Vehicles sold through 2017? ")

if score == 1:
    question = " question"
else:
    question = " questions"

if questionTwo == "T":
  print("Correct. In fact, there have been 395,270 Electric Vehicles sold through 2017.\nYou got " + str(score) + question + " right.")
else:
  print("Correct. There have been 395,270 Electric Vehicles sold through 2017.\nYou got " + str(score) + question + " right.")
