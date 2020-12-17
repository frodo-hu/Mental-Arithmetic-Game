
#The time module is needed to set a timer or to measure the time during the exercises
import time
#operator and functools modules are needed to multiply the random numbers in the exersises
import functools
import operator
#the random function module gives random numbers in the exersises which allow different sets of calculations in every round
import random
print("Welcome to the mental arithmetic game")
time.sleep(1)
#here the leaderboards are created
o = open("leaderboardspeedrunkl1x1.txt", "a")
oo = open("leaderboardtimer1x1.txt", "a")
o.close()
oo.close()

#This is the main loop in which the whole game mechanics are included
while True:
    try:
        #This part is the main menu in which the user can select the gamemode, the leaderboard or can quit the program
        print("Main Menu" + "\n")
        print("1 - Gamemode Timer")
        print("2 - Gamemode Speedrun")
        print("3 - Leaderboard")
        print("4 - Quit")
        gm = int(input("Enter 1 - 4 to proceed: "))
        #if function if input is 1 for first gamemode
        if gm == 1:
            print("\n", "Difficulty level", "\n", "1 - easy (small 1x1)", "\n", "2 - hard (big 1x1)", "\n", "3 - Quit")
            #This next loop is for the game mode Timer
            while True:
                #first of the user can choose between the different difficulty settings
                try:
                    dl = int(input("which level? "))
                    if dl == 1:
                        #Next the user gets a quick explanation about the game mode and after the count down the timer is started
                        print("try to solve as many calculations as you can in 60 seconds")
                        time.sleep(2)
                        print("Ready")
                        time.sleep(1)
                        print("Set")
                        time.sleep(1)
                        print("Go")
                        #use of time module to set start time at users local time
                        start_time = time.time()
                        score = 0
                        #Game mechanics
                        while True:
                            #The program constructs a numbers list with two random variables in the given range
                            numbers_list = []
                            for x in range(2):
                                value = random.randint(2, 10)
                                numbers_list.append(value)
                            #The program multiplies the numbers and cunstructs the answer
                            answer = functools.reduce(operator.mul, numbers_list, 1)
                            #The program shows the numbers two the user and gives him an oportunity to make a guess
                            print("Multiple these numbers", numbers_list)
                            guess = input()
                            #after the guess the program checks the time that has passed since the game started
                            elapsed_time = time.time() - start_time
                            #The program checks if the guess fits the answer and if the time is still under the limit set
                            #Since the answer is a integer it has to be converted to a string for the comparison this
                            #allows the user to enter a string without the program breaking down
                            if guess == str(answer) and elapsed_time < 60:
                                #if the time has not expired and the guess is right the score is increased by one and the loop continues to run
                                score = score + 1
                                #after every answer the program shows the user the remaining time after every guess
                                print(int(60 - elapsed_time), "seconds remaining")
                                continue
                            elif guess != str(answer) and elapsed_time < 60:
                                #if the guess is wrong and the time hasn't expired the score will stay the same and the loop continues to run
                                score = score
                                print(int(60 - elapsed_time), "seconds remaining")
                                continue
                            else:
                                #if the time expires the guess won't count, the loop stops to run and the program shows the user his score
                                print("Game Over")
                                time.sleep(0.5)
                                print("You solved", score, "calculations right in 60 seconds")
                                break
                        break
                    if dl == 2:
                        #The hard difficulty runs approximately the same, that's why only the differences will be explained
                        #The user has more time since the calculations will me more difficult
                        print("try to solve as many calculations as you can in 90 seconds")
                        time.sleep(2)
                        print("Ready")
                        time.sleep(1)
                        print("Set")
                        time.sleep(1)
                        print("Go")
                        start_time = time.time()
                        score = 0
                        while True:
                            numbers_list = []
                            for x in range(2):
                                #The range of numbers from which two randomly will be chosen is higher since the multiplications should be more difficult
                                value = random.randint(10, 30)
                                numbers_list.append(value)
                            answer = functools.reduce(operator.mul, numbers_list, 1)
                            print("Multiple these numbers", numbers_list)
                            guess = input()
                            elapsed_time = time.time() - start_time
                            if guess == str(answer) and elapsed_time < 90:
                                score = score + 1
                                print(int(90 - elapsed_time), "seconds remaining")
                                continue
                            elif guess != str(answer) and elapsed_time < 90:
                                score = score
                                print(int(90 - elapsed_time), "seconds remaining")
                                continue
                            else:
                                print("Game Over")
                                time.sleep(0.5)
                                print("You solved", score, "calculations right in 90 seconds")
                                break
                        score = str(score)
                        #The user is able to save his score in leaderboard file
                        s = input("\nDo you want to safe your score in the Leaderboard? \n\nInput -1- for yes or input else if you don't want to save: ")
                        if s == str(1):
                            #The user can enter his name and the program will save the name and result in the leaderboard that has been created in the beginning
                            user = input("username: ")
                            x = open("leaderboardtimer1x1.txt", "a")
                            x.writelines('\n')
                            x.writelines([user, ", ", score])
                            x.close()
                            print("\nscore saved... returning to main menu\n")
                            time.sleep(1)
                        else:
                            print("\nscore not saved... returning to main menu")
                            time.sleep(1)
                        break
                    break
                except ValueError:
                    print("Error")
                continue
            continue
        #if function if input is 2 for second gamemode
        if gm == 2:
            #The user can choose the difficulty level
            print("\n", "Difficulty level", "\n", "1 - easy (kleines 1x1)", "\n", "2 - hard (grosses 1x1)", "\n",
                  "3 - Quit")
            while True:
                try:
                    dl = int(input("which level? "))
                    if dl == 1:
                        #The game mechanics are again similar to the game mode timer the differences will be explained
                        print("try to solve 10 calculations right as fast as you can")
                        time.sleep(2)
                        print("Ready")
                        time.sleep(1)
                        print("Set")
                        time.sleep(1)
                        print("Go")
                        start_time = time.time()
                        score = 0
                        while True:
                            numbers_list = []
                            for x in range(2):
                                value = random.randint(2, 10)
                                numbers_list.append(value)
                            answer = functools.reduce(operator.mul, numbers_list, 1)
                            print("Multiple these numbers", numbers_list)
                            guess = input()
                            #the time won't be calculate after every guess since the user has no time limit
                            #instead the program will check if the user has reached 10 right answers already, if not the loop will continue running
                            if guess == str(answer) and score < 9:
                                score = score + 1
                                continue
                            elif guess != str(answer):
                                score = score
                                continue
                            else:
                                #if the user reached 10 correct guesses the program will calculate the time it took and show the result to the user
                                print("Game Over")
                                elapsed_time = time.time() - start_time
                                time.sleep(0.5)
                                print("You had", elapsed_time, "for solving 10 calculations right")
                                #the loop will stop running and the user gets back to the main menue
                                break
                        break
                    if dl == 2:
                        #the hard difficulty level is similar to the easy one that's why only the differences will be explained
                        print("try to solve 10 calculations right as fast as you can")
                        time.sleep(2)
                        print("Ready")
                        time.sleep(1)
                        print("Set")
                        time.sleep(1)
                        print("Go")
                        start_time = time.time()
                        score = 0
                        while True:
                            numbers_list = []
                            for x in range(2):
                                #the range includes higher numbers to give the user more difficult calculations
                                value = random.randint(10, 30)
                                numbers_list.append(value)
                            answer = functools.reduce(operator.mul, numbers_list, 1)
                            print("Multiple these numbers", numbers_list)
                            guess = input()
                            if guess == str(answer) and score < 9:
                                score = score + 1
                                continue
                            elif guess != str(answer):
                                score = score
                                continue
                            else:
                                print("Game Over")
                                elapsed_time = time.time() - start_time
                                time.sleep(0.5)
                                print("You had", elapsed_time, "for solving 10 calculations right")
                                break
                    score = str(elapsed_time)
                    # the user can again save his result in a leaderboard but this time the score is the time in which the user was able to
                    # solve 10 calculations right and not the amount of calculations the user solved in the given time
                    s = input("\nDo you want to safe your time in the Leaderboard? \n\nInput -1- for yes or input else if you don't want to save: ")
                    if s == str(1):
                        user = input("username: ")
                        x = open("leaderboardspeedrunkl1x1.txt", "a")
                        x.writelines("\n")
                        x.writelines([user, ", ", score])
                        x.close()
                        print("\ntime saved... returning to main menu\n")
                        time.sleep(1)
                    else:
                        print("\ntime not saved... returning to main menu")
                        time.sleep(1)
                        break
                    break
                except ValueError:
                    print("Error")
                continue
            continue
        if gm == 3:
            #every score for score time is connected to a username
            #for gamemode 1 it is organized as a dictionary with key = username and value = score
            a_dictionary = {}
            a_file = open("leaderboardtimer1x1.txt")
            #programm starts to read file from second line because if user saves score there is always a \n
            try:
                next(a_file)
            #If file is empty (user has not saved a score) it skips the error with stopiteration: pass
            except StopIteration:
                pass
            #for every line it reads username as key and score as value
            for line in a_file:
                key, value = line.split()
                a_dictionary[key] = int(value)
            #sorting of the dictionary after score (reversed to have the highest score at the top)
            sorted_a_dict = {}
            sorted_a_keys = sorted(a_dictionary, key=a_dictionary.get, reverse=True)
            for w in sorted_a_keys:
                sorted_a_dict[w] = a_dictionary[w]

            print("leaderboard Gamemode Timer")
            print(sorted_a_dict)

            # for gamemode 2 it is organized as a dictionary with key = username and value = time/float
            b_dictionary = {}
            b_file = open("leaderboardspeedrunkl1x1.txt")
            try:
                next(b_file)
            except StopIteration:
                pass
            for line in b_file:
                key, value = line.split()
                b_dictionary[key] = float(value)
            sorted_b_dict = {}
            #sorted that fastest time is at the top
            sorted_b_keys = sorted(b_dictionary, key=b_dictionary.get)
            for w in sorted_b_keys:
                sorted_b_dict[w] = b_dictionary[w]
            print("\nleaderboard Gamemode Speedrun")
            print(sorted_b_dict)
            t = input("\nto go back to main menu press enter! \n")
            continue
        if gm == 4:
            #if the user chooses to quit the loop will stop
            break
        else:
            #if the user chooses a number that is not in the range 1 - 4 the program will tell the user to choose a number in the given range and the loop will run again
            print("that is not a mode!")
            continue
    except ValueError:
            #if the user enters a non integer the program will tell the the user to enter a number in the given range and the loop will run again
        print("This is not 1 - 4! Choose a Mode!")
        continue
