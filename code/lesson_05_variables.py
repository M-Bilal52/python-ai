
"""
Create an AI model profile card and estimate chat costs.
"""

# Why: A dictionary keeps the model's profile details together.
model_profile = {
    "model_name": "llama3.2",
    "context_window": 128000,
    "price_per_1k_tokens": 0.50,  # Example price in PKR
    "runs_locally": True
}

print("--- AI Model Profile Card ---")

# Why: type() helps verify that each profile value has the correct data type.
print(f"Model: {model_profile['model_name']} {type(model_profile['model_name'])}")
print(f"Context window: {model_profile['context_window']} tokens {type(model_profile['context_window'])}")
print(f"Price per 1K tokens: {model_profile['price_per_1k_tokens']} PKR {type(model_profile['price_per_1k_tokens'])}")
print(f"Runs locally: {model_profile['runs_locally']} {type(model_profile['runs_locally'])}")

tokens_per_chat = int(input("Tokens per chat: "))

# Why: Divide by 1000 because the example price is per 1,000 tokens.
estimated_cost = round(
    (tokens_per_chat / 1000) * model_profile["price_per_1k_tokens"], 2
)

print(f"Estimated cost: {estimated_cost:.2f} PKR")

# Stretch goal: estimate the cost for 30 days.
chats_per_day = int(input("Chats per day: "))
monthly_cost = round(estimated_cost * chats_per_day * 30, 2)

print(f"Estimated monthly cost: {monthly_cost:.2f} PKR")
