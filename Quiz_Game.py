#Quiz Game Project

import random
import sys
import time

#Part 1: Deciding how to store Questions
#Added 3 question banks to the game
#Each Question bank consists of 20 questions each 
quiz_data = [
    {
        "Q":"How many continents are there on Earth?",
        "Options":["A) 5", "B) 6", "C) 7", "D) 8"],
        "Answer":"C"
    },

    {
        "Q":"What is the capital of France?",
        "Options":["A) London", "B) Berlin", "C) Madrid", "D) Paris"],
        "Answer":"D"
    },

    {
        "Q":"Which planet is known as the Red Planet?",
        "Options":["A) Mars", "B) Saturn", "C) Jupiter", "D) Venus"],
        "Answer":"A"
    },

    {
        "Q":"Which is the most popular sport in the world?",
        "Options":["A) Football", "B) Cricket", "C) Basketball", "D) American Football"],
        "Answer":"A"
    },

    {
        "Q":"What is the hardest natural substance in the world?",
        "Options":["A) Gold", "B) Iron", "C) Diamond", "D) Silver"],
        "Answer":"C"
    },

    {
        "Q":"Which gas do plants absorb from the atmosphere?",
        "Options":["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
        "Answer":"C"
    },

    {
        "Q": "Which element has the chemical symbol 'O'?",
        "Options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Silver"],
        "Answer": "B"
    },

    {
        "Q": "How many bones are in the adult human body?",
        "Options": ["A) 206", "B) 208", "C) 210", "D) 204"],
        "Answer": "A"
    },

    {
        "Q": "Which country is home to the kangaroo?",
        "Options": ["A) Brazil", "B) South Africa", "C) Australia", "D) India"],
        "Answer": "C"
    },

    {
        "Q": "What is the largest ocean on Earth?",
        "Options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "Answer": "D"
    },

    {
        "Q": "Who painted the Mona Lisa?",
        "Options": ["A) Vincent van Gogh", "B) Leonardo da Vinci", "C) Pablo Picasso", "D) Claude Monet"],
        "Answer": "B"
    },

    {
        "Q": "What is the hardest natural substance on Earth?",
        "Options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"],
        "Answer": "C"
    },

    {
        "Q": "Which instrument has 88 keys?",
        "Options": ["A) Violin", "B) Guitar", "C) Piano", "D) Flute"],
        "Answer": "C"
    },

    {
        "Q": "How many sides does a hexagon have?",
        "Options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "Answer": "B"
    },

    {
        "Q": "What is the fastest land animal in the world?",
        "Options": ["A) Lion", "B) Cheetah", "C) Gazelle", "D) Horse"],
        "Answer": "B"
    },

    {
        "Q": "Which gas do plants absorb from the atmosphere for photosynthesis?",
        "Options": ["A) Carbon Dioxide", "B) Oxygen", "C) Nitrogen", "D) Hydrogen"],
        "Answer": "A"
    },

    {
        "Q": "In which continent is the Sahara Desert located?",
        "Options": ["A) Asia", "B) Africa", "C) South America", "D) Australia"],
        "Answer": "B"
    },

    {
        "Q": "What is the freezing point of water in Celsius?",
        "Options": ["A) 0°C", "B) -10°C", "C) 32°C", "D) 100°C"],
        "Answer": "A"
    },

    {
        "Q": "Which primary color do you mix with Blue to get Green?",
        "Options": ["A) Red", "B) Yellow", "C) Purple", "D) White"],
        "Answer": "B"
    },

    {
        "Q": "What is the smallest prime number?",
        "Options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "Answer": "C"
    }
]

sports_quiz_data = [
    {
        "Q": "Which Argentine legend scored the infamous 'Hand of God' goal in 1986?",
        "Options": ["A) Lionel Messi", "B) Diego Maradona", "C) Sergio Agüero", "D) Mario Kempes"],
        "Answer": "B"
    },

    {
        "Q": "Which club is known as 'The Red Devils' in English football?",
        "Options": ["A) Liverpool", "B) Arsenal", "C) Manchester United", "D) AC Milan"],
        "Answer": "C"
    },

    {
        "Q": "Who was famous for his iconic 'Siuuu' celebration?",
        "Options": ["A) Cristiano Ronaldo", "B) Neymar Jr", "C) Kylian Mbappé", "D) Ronaldinho"],
        "Answer": "A"
    },

    {
        "Q": "Which country won the first-ever FIFA World Cup in 1930?",
        "Options": ["A) Brazil", "B) Uruguay", "C) Argentina", "D) Italy"],
        "Answer": "B"
    },

    {
        "Q": "Which NBA player famously scored 100 points in a single game in 1962?",
        "Options": ["A) Michael Jordan", "B) Kobe Bryant", "C) Wilt Chamberlain", "D) LeBron James"],
        "Answer": "C"
    },

    {
        "Q": "Which team did Michael Jordan win all 6 of his NBA Championships with?",
        "Options": ["A) LA Lakers", "B) Chicago Bulls", "C) Boston Celtics", "D) Miami Heat"],
        "Answer": "B"
    },

    {
        "Q": "Which NBA legend went by the nickname 'The Black Mamba'?",
        "Options": ["A) Shaquille O'Neal", "B) Kobe Bryant", "C) Allen Iverson", "D) Dwyane Wade"],
        "Answer": "B"
    },

    {
        "Q": "Which superstar player is nicknamed 'The Greek Freak'?",
        "Options": ["A) Luka Dončić", "B) Nikola Jokić", "C) Giannis Antetokounmpo", "D) Kristaps Porziņģis"],
        "Answer": "C"
    },

    {
        "Q": "Which heavyweight boxing champion famously said 'Float like a butterfly, sting like a bee'?",
        "Options": ["A) Mike Tyson", "B) Muhammad Ali", "C) Joe Frazier", "D) George Foreman"],
        "Answer": "B"
    },

    {
        "Q": "Which boxer was nicknamed 'Iron Mike' during his dominant reign?",
        "Options": ["A) Mike Tyson", "B) Evander Holyfield", "C) Floyd Mayweather", "D) Lennox Lewis"],
        "Answer": "A"
    },

    {
        "Q": "Floyd Mayweather retired with an undefeated professional record of what?",
        "Options": ["A) 40-0", "B) 50-0", "C) 60-0", "D) 45-0"],
        "Answer": "B"
    },

    {
        "Q": "Which Australian legendary batsman retired with an astonishing Test average of 99.94?",
        "Options": ["A) Shane Warne", "B) Ricky Ponting", "C) Sir Donald Bradman", "D) Allan Border"],
        "Answer": "C"
    },

    {
        "Q": "Who holds the record for the highest individual score in Test Cricket (400 not out)?",
        "Options": ["A) Sachin Tendulkar", "B) Brian Lara", "C) Chris Gayle", "D) Viv Richards"],
        "Answer": "B"
    },

    {
        "Q": "Which Indian cricketer is widely known as 'Captain Cool'?",
        "Options": ["A) Virat Kohli", "B) Rohit Sharma", "C) MS Dhoni", "D) Sourav Ganguly"],
        "Answer": "C"
    },

    {
        "Q": "Which country has won the most FIFA/ICC Men's Cricket World Cups?",
        "Options": ["A) India", "B) West Indies", "C) England", "D) Australia"],
        "Answer": "D"
    },

    {
        "Q": "Which quarterback has won the most Super Bowl rings (7) in NFL history?",
        "Options": ["A) Patrick Mahomes", "B) Peyton Manning", "C) Tom Brady", "D) Aaron Rodgers"],
        "Answer": "C"
    },

    {
        "Q": "What is the name of the annual championship game of the NFL?",
        "Options": ["A) The Rose Bowl", "B) The Super Bowl", "C) The World Series", "D) The Grey Cup"],
        "Answer": "B"
    },

    {
        "Q": "Which NFL team was the first to complete a legendary 'perfect season' (undefeated)?",
        "Options": ["A) 1972 Miami Dolphins", "B) 2007 New England Patriots", "C) Green Bay Packers", "D) San Francisco 49ers"],
        "Answer": "A"
    },

    {
        "Q": "Which hockey icon is widely referred to simply as 'The Great One'?",
        "Options": ["A) Mario Lemieux", "B) Wayne Gretzky", "C) Bobby Orr", "D) Sidney Crosby"],
        "Answer": "B"
    },

    {
        "Q": "What is the name of the famous trophy awarded to the NHL Champions?",
        "Options": ["A) Lombardi Trophy", "B) The Stanley Cup", "C) The Ashes", "D) The Claret Jug"],
        "Answer": "B"
    }
]

movies_quiz_data = [
    {
        "Q": "Which 1997 movie famously won 11 Oscars and featured the line 'I'm the king of the world!'?",
        "Options": ["A) Titanic", "B) Gladiator", "C) Braveheart", "D) Avatar"],
        "Answer": "A"
    },

    {
        "Q": "In 'The Matrix', what color pill does Neo take to wake up and see reality?",
        "Options": ["A) Blue", "B) Red", "C) Yellow", "D) Green"],
        "Answer": "B"
    },

    {
        "Q": "What is the highest-grossing film of all time (unadjusted for inflation)?",
        "Options": ["A) Avengers: Endgame", "B) Titanic", "C) Avatar", "D) Star Wars: The Force Awakens"],
        "Answer": "C"
    },

    {
        "Q": "Which actor famously played the iconic archaeologist Indiana Jones?",
        "Options": ["A) Harrison Ford", "B) Tom Cruise", "C) Mel Gibson", "D) Bruce Willis"],
        "Answer": "A"
    },

    
    {
        "Q": "Who played the Joker in the 2008 masterpiece 'The Dark Knight'?",
        "Options": ["A) Joaquin Phoenix", "B) Jared Leto", "C) Jack Nicholson", "D) Heath Ledger"],
        "Answer": "D"
    },

    {
        "Q": "In the Marvel Cinematic Universe, what is Thor’s magical hammer called?",
        "Options": ["A) Stormbreaker", "B) Mjolnir", "C) Gungnir", "D) Aegis"],
        "Answer": "B"
    },

    {
        "Q": "What iconic vehicle is used as the time machine in 'Back to the Future'?",
        "Options": ["A) Mustang", "B) Chevrolet Corvette", "C) DeLorean", "D) Dodge Charger"],
        "Answer": "C"
    },

    {
        "Q": "In 'Star Wars', what is Darth Vader’s famous reveal line to Luke Skywalker?",
        "Options": [
            "A) 'Luke, I am your father.'",
            "B) 'No, I am your father.'",
            "C) 'You are my son.'",
            "D) 'Obi-Wan never told you the truth.'"
        ],
        "Answer": "B"
    },

    
    {
        "Q": "What is the name of the toy cowboy in Disney Pixar's 'Toy Story'?",
        "Options": ["A) Buzz", "B) Woody", "C) Rex", "D) Slinky"],
        "Answer": "B"
    },

    {
        "Q": "In 'Shrek', what kind of mythical creature is Fiona secretly under a spell to become?",
        "Options": ["A) Dragon", "B) Ogre", "C) Fairy", "D) Witch"],
        "Answer": "B"
    },

    {
        "Q": "Which animated movie features the hit song 'Let It Go'?",
        "Options": ["A) Tangled", "B) Moana", "C) Frozen", "D) Brave"],
        "Answer": "C"
    },

    {
        "Q": "What is the name of the African kingdom where 'The Lion King' takes place?",
        "Options": ["A) Pride Lands", "B) Wakanda", "C) Zamunda", "D) Elephant Graveyard"],
        "Answer": "A"
    },

    {
        "Q": "What killer mask is worn by the killer in the horror movie franchise 'Scream'?",
        "Options": ["A) Michael Myers Mask", "B) Ghostface", "C) Hockey Mask", "D) Jigsaw Mask"],
        "Answer": "B"
    },

    {
        "Q": "In 'The Shining', what is the creepy word written on the door that is 'Murder' spelled backward?",
        "Options": ["A) REDRUM", "B) DRACO", "C) NOSFERATU", "D) OVERLOOK"],
        "Answer": "A"
    },

    {
        "Q": "What is the name of the puppet used by John Kramer in the 'Saw' movies?",
        "Options": ["A) Chucky", "B) Annabelle", "C) Billy", "D) Slappy"],
        "Answer": "C"
    },

    {
        "Q": "Which movie features the famous line: 'First rule of Fight Club is: You do not talk about Fight Club'?",
        "Options": ["A) Pulp Fiction", "B) Fight Club", "C) The Matrix", "D) Goodfellas"],
        "Answer": "B"
    },

    {
        "Q": "In 'The Lord of the Rings', what word does Gollum constantly use to describe the One Ring?",
        "Options": ["A) My Treasure", "B) My Dearest", "C) My Precious", "D) My Shiny"],
        "Answer": "C"
    },

    {
        "Q": "In 'Forrest Gump', what does Forrest say life is like?",
        "Options": [
            "A) A box of chocolates",
            "B) A deck of cards",
            "C) A rolling stone",
            "D) A bowl of cherries"
        ],
        "Answer": "A"
    },

    {
        "Q": "Which Quentin Tarantino movie features John Travolta and Samuel L. Jackson as hitmen?",
        "Options": ["A) Reservoir Dogs", "B) Kill Bill", "C) Pulp Fiction", "D) Django Unchained"],
        "Answer": "C"
    },

    {
        "Q": "In 'Harry Potter', what is the name of the train platform that leads to Hogwarts?",
        "Options": ["A) Platform 8 and 1/2", "B) Platform 9 and 3/4", "C) Platform 10", "D) Platform 7 and 1/4"],
        "Answer": "B"
    }
]

#Part 2: This where the game is made and controlled
#Random 6 Questions will be asked from the desired question banks
#Added a 30 second time limit for the whole quiz to make the game more fun
def game(score, quiz_data_option):
    start_time = time.time()
    for item in quiz_data_option:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= 30:
            print("\nTIME IS UP!")
            break
        else:
            print("\n")
            print(item["Q"])
            print(item["Options"])
            answer = input("Please choose the correct answer: ")
            if time.time() - start_time >= 30:
                print("\nTIME IS UP! THAT ANSWER DIDN'T COUNT")
                break
            real_answer = item["Answer"]
            if answer.upper() == real_answer:
                score = score + 10
                continue
            else:
                continue


    return score

    
#Part 3: The UI and the setup of the game
#User can choose which category they want to have a quiz for
#There total score and number of quizzez will be tracked and displayed at the end
def main():
    total_quizzez = 0
    total_score = 0
    while True:
        answer = input("Enter Q to start the game: ")
        if answer.upper() == "Q":
            while True:
                print("Welcome!")
                print("\nPlease choose the category for which you want to have a quiz for: ")
                print("1. General Quiz")
                print("2. Sports Quiz")
                print("3. Movie Quiz")
                print("0. End Game")
                reply = input("Enter your choice of quiz[1/2/3/0]: ").strip()
                if reply == "1":
                    user_score = 0
                    selected_questions = random.sample(quiz_data, 6)
                    user_score = game(user_score, selected_questions)
                    print(f"You earned: {user_score}/60")
                    total_score = total_score + user_score
                    print(f"Current Total Score: {total_score}")
                    total_quizzez += 1
                elif reply == "2":
                    user_score = 0
                    selected_questions = random.sample(sports_quiz_data, 6)
                    user_score = game(user_score, selected_questions)
                    print(f"You earned: {user_score}/60")
                    total_score = total_score + user_score
                    print(f"Current Total Score: {total_score}")
                    total_quizzez += 1
                elif reply == "3":
                    user_score = 0
                    selected_questions = random.sample(movies_quiz_data, 6)
                    user_score = game(user_score, selected_questions)
                    print(f"You earned: {user_score}/60")
                    total_score = total_score + user_score
                    print(f"Current Total Score: {total_score}")
                    total_quizzez += 1
                elif reply == "0":
                    print(f"\nYou earned a score of {total_score} points in {total_quizzez} quizzez.")
                    print("ENDING THE GAME......")
                    print("--------- THANK YOU FOR PLAYING THE GAME :) ---------------", end = "")
                    sys.exit()
                    
                else:
                    print("\nYou Chose the wrong the option. Please choose either 1(General Quiz) or 2(Game Quiz) or 3(Movie Quiz) or 0(End Game).")
                    


        else:
            print("Entered the wrong button. Please enter the correct Letter")


main()