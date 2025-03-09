

question = [
    {
        "prompt" : "What is the capital of India?",
        "options" : ["A. Delhi", "B. Gujrat", "C. Rajsthan", "D. Goa"],
        "answers" : "A"
    },
    {
        "prompt" : "What is the national Bird of India?",
        "options" : ["A. Parrot", "B. Sparrow", "C. Peacock", "D. Duck"],
        "answers" : "C"
    },
    {
        "prompt" : "What is the full form DDL",
        "options" : ["A. (Data Definition Language)", "B. (Data Design Language)", "C. (Delete Data Language)", "D. None of this"],
        "answers" : "A"
    },
    {
        "prompt" : "How many types of looping statement in C language?",
        "options" : ["A. 4", "B. 3", "C. 2", "D. 1"],
        "answers" : "B"
    },
    {
        "prompt" : "What is the full form of CSS?",
        "options" : ["A. Control Space Service", "B. Control Style Sheet", "C. Cascading Style Sheet", "D. None of this"],
        "answers" : "C"
    }
]
def run_quiz(question):
    while True:
        score = 0
        for que in question:
            print("\n"+que['prompt'])
            for option in que['options']:
                print(option)
            answer = input("Enter your answer (A,B,C or D): ").upper()
            if answer == que['answers']:
                print("Correct ✅")
                score += 1
            else:
                print("Wrong! The correct answer is = ", que['options'][0])

        print(f"\nyou correct the {score} answers out of {len(question)} questions")

        option = input("\nTo play again, type 'Yes'. To exit, type 'No': ")
        if option != 'yes':
            print("Thanks for playing! 👋")
            break  # Exit the loop and end the game


run_quiz(question)