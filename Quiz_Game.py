#Quiz Game Project

#Part 1: Deciding how to store Questions
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
    }
]

def game(score):
    for item in quiz_data:
        print(item["Q"])
        print(item["Options"])
        answer = input("Please choose the correct answer: ")
        real_answer = item["Answer"]
        if answer.upper() == real_answer:
            score = score + 10
            continue
        else:
            continue

    return score

    

def main():
    while True:
        answer = input("Enter Q to start the game: ")
        if answer.upper() == "Q":
            user_score = 0
            user_score = game(user_score)
            print(f"You earned: {user_score}/30")

        else:
            print("Pressed the wrong button. Restart the game")
            break


main()