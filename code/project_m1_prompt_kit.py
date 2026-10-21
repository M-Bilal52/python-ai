"""
AI prompt kit for a Local Business
"""
Business_name =input("Enter your business name: ")
Business_type =input("Enter your business type: ")
city =input("Enter your city: ")
Main_customer =input("Enter your main customer demographic: ")
Monthly_budget =input("Enter your monthly budget for marketing: ")
print()
print(f"Business Name: {Business_name}")
print(f"Business Type: {Business_type}")
print(f"City: {city}")
print(f"Main Customer Demographic: {Main_customer}")
print(f"Monthly Marketing Budget: {Monthly_budget}")

marketing =(
    f"Create a marketing strategy for {Business_name}, a {Business_type} located in {city}. "
    f"The main customers are {Main_customer}. The monthly budget for marketing is {Monthly_budget}. "
)

customer_service =(
    f"Create a customer service strategy for {Business_name}, a {Business_type} located in {city}. "
    f"The main customers are {Main_customer}. The monthly budget for marketing is {Monthly_budget}. "