
"""
Lesson 07: Route AI tasks to models based on task type and cost.
"""

task_type = input("Task (code / private / chat): ").strip().lower()
estimated_tokens = int(input("Estimated tokens: "))

# Why: Different tasks need different models for privacy, quality, and cost.
if task_type == "private":
    model_name = "llama3.2 (local, Ollama)"
    price = 0.0

elif task_type == "code":
    model_name = "claude (cloud, strong at code)"
    price = 0.80

else:
    model_name = "cheap chat model (cloud)"
    price = 0.10

# Why: Long requests may use more resources and cost more.
if estimated_tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# Stretch: Check both conditions using and.
paid_user = input("Is this a paid user? (yes/no): ").strip().lower()

if paid_user == "no" and estimated_tokens > 2000:
    print("Upgrade to send long requests.")

# Why: A local model has zero example per-token API cost.
estimated_cost = (estimated_tokens / 1000) * price

print(f"Chosen model: {model_name}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")
