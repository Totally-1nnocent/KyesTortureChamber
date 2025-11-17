#####  Autism Quiz  #####
import random

questions = {
    "When did the first Transformers Movie release?":{"Answer":"1986", "Category":"Transformers", "Hint":"It was released in the 80's", "Asked":False, 
                                                      "Possible Answers":["1982", "2000", "1992", "1986"]},
    "What is the name of the main character of Tron: Uprising?":{"Answer":"Beck", "Category":"Tron", "Hint":"The female version of this name would be Rebecca", "Asked":False, 
                                                                 "Possible Answers":["Charlie", "Megan", "Beck", "Penny"]},
    "Which year was Tron: Legacy released?":{"Answer":"2010", "Possible Answers":["2010", "2008", "1996", "2018"], "Category":"Tron", "Hint":"It was released in the 2010's.", "Asked":False},
    "How old were Dante and Vergil when their house burnt down?":{"Answer":"8", "Possible Answers":["16", "18", "8", "10"], "Category":"Devil May Cry", "Hint":"They were considered minors.", "Asked":False,
                                                                 "Possible Answers":["16", "18", "8", "10"]},
    "Which transformer gained the matrix of leadership after Optimus Prime?":{"Answer":"Hot Rod", "Category":"Transformers", "Hint":"His name became Rodimus Prime.", "Asked":False, 
                                                                              "Possible Answers":["Ultra Magnus", "Bumblebee", "Hot Rod", "Orion Pax"]},
    "In the transformers show Transformers: Prime, the character Smokescreen was supposed to be which other character?":{"Answer":"Hot Rod", "Category":"Transformers", "Hint":"In the show, he almost becomes a prime.", "Asked":False,
                                                                                                                         "Possible Answers":["Hot Rod", "Elita-1", "Ironhide", "Bluestreak"]},
    "In the IDW Transformers comics, Rodimus Prime is the captain of what ship?":{"Answer":"Lost Light", "Category":"Transformers", "Hint":"It does not appear in any other iteration of Transformers.", "Asked":False,
                                                                                  "Possible Answers":["USS Enterprise", "The Ark", "Lost Light", "Serenity"]},
    "In the IDW Transformers comics, which character buys Rodimus' ship for him?":{"Answer":"Drift", "Category":"Transformers", "Hint":"He is an ex - decepticon.", "Asked":False,
                                                                                   "Possible Answers":["Drift", "Tarn", "Soundwave", "Ultra Magnus"]},
    "In Transformers, what is the name of the leader of the Decepticon Justice Division":{"Answer":"Tarn", "Category":"Transformers", "Hint":"He is named after a pre-war Decepticon city-state.", "Asked":False,
                                                                                          "Possible Answers":["Vos", "Helex", "Megatron", "Tarn"]},
    "In Devil May Cry, who does the character Trish strongly resemble?":{"Answer":"Eva", "Category":"Devil May Cry", "Hint":"She is Dante and Vergil's mother.", "Asked":False,
                                                               "Possible Answers":["Nico", "Lady", "Eva", "Patty"]},
    }

askedQuestions = {}

def ask_question(questions, askedQuestions, questionNum):
    chosenQuestion = random.choice(list(questions.keys())) #choses random question
    while questions[chosenQuestion]["Asked"] == True: # checks if the question had already been asked
        chosenQuestion = random.choice(list(questions.keys())) 
    counter = 0
    flag = True
    print("")
    print("#####################")
    print("")
    print(chosenQuestion)
    for answer in questions[chosenQuestion]["Possible Answers"]: # print all possible answers
        counter = counter + 1
        print(f"{counter}. {answer}")
    chosenAnswer = input("Enter your answer or 'hint' for a hint: ")
    while flag: # ensure valid input
        if chosenAnswer.lower() == "hint":
            print(questions[chosenQuestion]["Hint"])
            chosenAnswer = input("Enter your answer: ")
        try:
            int(chosenAnswer)
        except:
            print("That is an invalid input.")
            chosenAnswer = input("Enter your answer: ")
        else:
            if int(chosenAnswer) > 0 and int(chosenAnswer) < 5:
                flag = False
            else:
                print("That is an invalid input.")
                chosenAnswer = input("Enter your answer: ")

    questions[chosenQuestion]["Asked"] = True #so the question isnt repeated
    # record question
    askedQuestions.update({chosenQuestion:{"Correct Answer": questions[chosenQuestion]["Answer"], "QuestionNumber": questionNum, "Chosen Answer": questions[chosenQuestion]["Possible Answers"][(int(chosenAnswer)-1)]}})

def play_game(questions, askedQuestions):
    for i in range(0, 10):
        ask_question(questions, askedQuestions, 1)


def summary(askedQuestions):
    print("")
    print("###############################")
    print("")
    for i in range(0, len(askedQuestions)):
        print(askedQuestions)

play_game(questions, askedQuestions)