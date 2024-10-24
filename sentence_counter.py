import re

def main():
    print("Enter sentences one by one. Type 'END' to finish input.")
    user_input = []
    
    #Sentences from the user
    while True:
        sentence = input("Enter a sentence: ")
        if sentence.strip().upper() == 'END':
            break
        user_input.append(sentence)

    # Combine all sentences into a single string
    full_text = ' '.join(user_input)
    
    # Regular expression to find sentences
    # Using re.MULTILINE to consider new lines properly and re.DOTALL to match newline as part of '.'
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z]|$)'
    sentences = re.findall(pat, full_text, flags=re.DOTALL | re.MULTILINE)
    
    # Display the sentences and their count
    print("\nYou entered the following sentences:")
    for index, sentence in enumerate(sentences, start=1):
        print(f"{index}: {sentence.strip()}")
    
    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()
