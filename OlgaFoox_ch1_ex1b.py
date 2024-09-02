import random

def create_responses_file():
    # Create a file and write predefined responses
    with open('8ball_responses.txt', 'w') as my_file:
        responses = [
            "Yes, of course!",
            "Without a doubt, yes.",
            "You can count on it.",
            "For sure!",
            "Ask me later!",
            "I'm not sure.",
            "I can't tell you right now.",
            "I'll tell you after my nap.",
            "No way!",
            "I don't think so.",
            "Without a doubt, no.",
            "The answer is clearly NO!"
        ]
        for response in responses:
            # Write each response to a new line
            my_file.writelines(response + "\n")

    print("Responses written to 8ball_responses.txt.")

def read_responses():
    # Read responses from the file into a list
    responses = []
    with open('8ball_responses.txt', 'r') as my_file:
        responses = [line.strip() for line in my_file]
    return responses

def magic_8_ball():
    # Function to interact with the magic 8-ball
    # Get responses from the file
    responses = read_responses()

    while True:
        question = input("Ask me a question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Goodbye!")
            break

        # Randomly select a response
        answer = random.choice(responses)
        print("Magic 8-ball says:", answer)

def main():
    # First, create the responses file
    create_responses_file()
    # Then, run the magic 8-ball functionality
    magic_8_ball()

if __name__ == '__main__':
    main()
