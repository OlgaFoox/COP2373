# List of common spam words and phrases
spam_words = [
    "free", "100% free", "act now", "limited time", "special promotion",
    "money back", "winner", "cash bonus", "earn money", "risk-free",
    "incredible deal", "free gift", "order now", "click here", "unsecured credit",
    "instant approval", "congratulations", "free access", "lower your interest rate",
    "best price", "satisfaction guaranteed", "full refund", "costly", "free trial",
    "no fees", "easy money", "million dollars", "save big", "guarantee",
    "double your income"
]


def scan_email(email_message):
    spam_score = 0
    found_words = []

    for word in spam_words:
        # Check for the occurrence of each spam word/phrase
        if word.lower() in email_message.lower():
            spam_score += 1
            found_words.append(word)

    return spam_score, found_words


def rate_spam_score(spam_score):
    if spam_score >= 10:
        return "Very Likely Spam"
    elif spam_score >= 5:
        return "Possible Spam"
    elif spam_score > 0:
        return "Low Likelihood of Spam"
    else:
        return "Not Spam"


# Main application logic
user_input = input("Enter your email message: ")
spam_score, found_words = scan_email(user_input)
spam_rating = rate_spam_score(spam_score)

# Display results
print(f"Spam Score: {spam_score}")
print(f"Likelihood of Spam: {spam_rating}")
if found_words:
    print(f"Words/Phrases Causing Spam Score: {', '.join(found_words)}")
else:
    print("No spam-related words/phrases found.")
