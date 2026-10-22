
"""
Lesson 06: Clean user input and build a safe AI prompt.
"""

user_name = input("Your name: ")
messy_question = input("Your question: ")

# Why: strip() removes extra spaces before formatting the input.
cleaned_name = user_name.strip().title()
cleaned_question = messy_question.strip().capitalize()

# Stretch: Replace a bad word before sending the question to AI.
cleaned_question = cleaned_question.replace("stupid", "***")

character_count = len(cleaned_question)
estimated_tokens = round(character_count / 4)

# Why: lower() makes the keyword check case-insensitive.
mentions_python = "python" in cleaned_question.lower()

# Why: Slicing limits the question to 150 characters.
safe_question = cleaned_question[:150]

prompt = f"""
You are a friendly Python tutor.
Greet {cleaned_name} by name and answer in 3 short lines.
Question: {safe_question}
"""

print("=" * 40)
print(f"Cleaned question: {cleaned_question}")
print(f"Characters: {character_count}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print("=" * 40)
print(prompt)

# Stretch: Example cost only, not an actual provider price.
price_per_1k_tokens = 0.50
estimated_cost = (estimated_tokens / 1000) * price_per_1k_tokens

print(f"Estimated cost: {estimated_cost:.2f} PKR")