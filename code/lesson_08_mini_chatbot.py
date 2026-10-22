
"""
Lesson 08: Build a rule-based chatbot for City Care Clinic.
The chatbot answers common questions and tracks unanswered messages.
"""

print(
    "City Care Bot: Hi! Ask about timings, fees, location or appointments. "
    "Type 'bye' to exit."
)

# Why: Ask for the name once, before the loop, so we can personalize replies.
customer_name = input("City Care Bot: What is your name? ").strip().title()

message_count = 0
unanswered_count = 0
complaint_count = 0

while True:
    raw_message = input(f"{customer_name}: ")
    user_message = raw_message.strip().lower()

    # Why: Count every message, including "bye", for an accurate summary.
    message_count += 1

    if user_message == "bye":
        print(f"City Care Bot: Take care, {customer_name}!")
        break

    # Why: Handle complaints and human requests before normal questions.
    complaint_keywords = ["late", "complaint", "problem", "unhappy"]
    human_keywords = ["agent", "human"]

    if any(word in user_message for word in complaint_keywords):
        complaint_count += 1
        print(
            "City Care Bot: Sorry about that. "
            "The clinic manager will call you today."
        )

    elif any(word in user_message for word in human_keywords):
        print("City Care Bot: Connecting you to a human...")
        break

    elif (
        user_message == "hi"
        or user_message == "hello"
        or user_message == "hey"
        or user_message.startswith("hi ")
    ):
        print("City Care Bot: Hello! How can I help you today?")

    elif any(word in user_message for word in [
        "timing", "timings", "hours", "open"
    ]):
        print(
            "City Care Bot: We are open 10 am to 8 pm, "
            "Monday to Saturday."
        )

    elif any(word in user_message for word in [
        "fee", "fees", "price", "cost"
    ]):
        print("City Care Bot: Consultation fee is 2,000 PKR.")

    elif any(word in user_message for word in [
        "location", "address", "where"
    ]):
        print(
            "City Care Bot: We are located at Main Market, Lahore."
        )

    elif any(word in user_message for word in [
        "appointment", "booking", "book"
    ]):
        print(
            "City Care Bot: Please call the clinic "
            "to book an appointment."
        )
    else:
        unanswered_count += 1

        # Why: Keep unknown questions for the future AI module to answer.
        ai_prompt = (
            "You are the friendly assistant of City Care Clinic. "
            f"Answer in 2 lines: {user_message[:150]}"
        )

        print(
            "City Care Bot: I am not sure yet. "
            f"In Module 2, an AI will answer: {ai_prompt}"
        )

print("=" * 40)
print(
    f"Chat summary: {message_count} messages, "
    f"{unanswered_count} unanswered."
)
print(f"Complaints received: {complaint_count}")
