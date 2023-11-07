#Say hello to the user Y
#Ask them to enter in their daily caloric intake limit Y
#Ask them to enter in the food they ate that day and add it to a list Y
#Ask them how many calories it was Y
#add both to their own lists Y
#Then at the end the amount of calories up and print if they went over the limit or not Y

print("Hello user!! Welcome to The #1 Calorie Counter! Let's get started with your daily caloric intake")

caloricLimit = int(input("What is your caloric intake limit? ")) #stores the caloric limit for the day 

sentinel = input("Okay, now for the food. Would you like to continue? ")
sentinel.lower() #converts answer to lowercase

food = [] #stores food answers
calories = [] #stores calories
while(sentinel != "no"): #sentinel control loop
    question1 = input("Food: ")
    food.append(question1) #adds answer to food list

    question2 = int(input("Calories: "))
    calories.append(question2) #adds answer to calories list

    question3 = input("Would you like to add more items? (y/n) ")
    question3.lower()
    if question3 != "y":
        sentinel = "no"

totalCalories = 0 
for i in range(len(calories)): 
   totalCalories += calories[i]

limitReached = False
if totalCalories > caloricLimit:
    limitReached = True
    print ("You exceeded your daily calorie goal of "+ str(caloricLimit) + " calories. It's alright, we'll get 'em tomorrow!")
else:
    print("You consumed " + str(totalCalories) + " calories today. Great job staying in a deficit!!")
    
