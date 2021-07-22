import random

control = 0 #Soul Reducing Controller
soul = 9
restart = "Y"
word_list_2 = []
word_list_1 = ["apologise", "crocodile", "education", "abounding", "beginning", "christmas", "fireboard", "identical", "chocolate", "challenge", "important",
             "consonant", "dangerous", "australia", "irregular", "knowledge", "macaronic", "pineapple", "secretary", "halloween", "alligator", "seventeen",
             "different", "vegetable", "structure", "wonderful", "provoking", "crocodile", "abounding", "beginning", "brainless", "breathing", "september",
             "imperfect", "xylophone", "integrity", "blessings", "charlotte", "afterlife", "everybody", "louisiana", "celebrity", "delicious", "attention",
             "elocution", "difficult", "necessary", "recycling", "treatment", "billboard", "territory", "architect", "ecosystem", "twentieth", "caribbean",
             "generator", "kamasutra", "amphibian", "addiction", "radiation", "innocence", "nightmare", "abundance", "direction", "reference", "Sunflower"] #Word Store

while True:
    if (restart == "y" or restart == "Y"):
        word = word_list_1[random.randint(0,67)] #(0, 67] random number
        for element in word:
            word_list_2.append(element)
        global_list = ["-","-","-","-","-","-","-","-","-"]
        name = input("Name : ")
        print(f"Hello {name} time to play hangman!")


        while True:
            choice = input("You wanna guess the word?(Y/n) ")
            if (choice == "Y"): #If you guess the word
                guess = input("Your Prediction(Word) : ")
                if (guess == word): #If your guess is equal the word
                    control = 1
                    guess_list = []
                    for event in guess:
                        guess_list.append(event)

                    for i in range(9):
                        if (word_list_2[i] == guess_list[i]):
                            global_list[i] = word_list_2[i]
                        print(f"{global_list[i]}\n")

                    print(f"Congratulations! You find the secret word! The word is {word}")
                    break
                else:
                    soul -= 1
                    print(f"The soul that left behind : {soul}")

            elif (choice == "n"): #If you guess the letter
                prdctn = input("Your Prediction(Letter) : ")
                for i in range(9): #Control every letter
                    if (word_list_2[i] == prdctn): #If your letter guess is equal the letter
                        control += 1
                        global_list[i] = prdctn
                    print(f"{global_list[i]}\n")

                if (control == 0): #If there is not any correct letter
                   soul -= 1
                   print(f"The soul that left behind : {soul}")
                else: #If there is at least 1 correct letter
                    print(f"The soul that left behind : {soul}")

                control = 0
            if (soul <= 0):
                print(f"You Lose! I'm sorry! The word is {word}\nMaybe next time?")
                break
        restart = input("You wanna try again? Y/N")
    else:
        print("Have nice day :)")
        break
