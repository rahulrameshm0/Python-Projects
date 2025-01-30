
question = [
    {"Prompt": "What is the capital of India?",
    "option": ["A.Rajasthan", "B.Delhi", "C.Gujarat", "D.Punjab"],
    "answer":"B"},

    {"Prompt": "What is the capital of Australia??",
    "option": ["A.Sydney", "B.Canberra", "C.Melbourne", "D.Brisbane"],
    "answer":"B"},

    {"Prompt": "Which planet is known as the Red Planet?",
    "option": ["A.Venus", "B.Mars", "C.Jupiter", "D.Mercury"],
    "answer": "B"},

    {"Prompt": "Who painted the Mona Lisa?",
    "option": ["A.Vincent van Goghn", "B.Michelangelo", "C.Leonardo da Vinci", "D.Pablo Picasso"],
    "answer": "C"}
    ]

def run_quiz(question):
    count = 0
    for i in question:
        print(f"{i['Prompt']}")
        for option in i['option']:
            print(option)
        option = input("Enter your option: ").upper()

        if option == i['answer']:
            count += 1
        else:
            print("Wrong answer!")
    print(f"You got {count} out of {len(i)}")

run_quiz(question)