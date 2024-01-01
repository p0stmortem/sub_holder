from datetime import datetime, timedelta

customer_data = {
    'Flava Flave': {'subscribed': True, 'subscription_type': 'monthly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 25, 'phone_number': '123-456-7890'},
    'Jada Pickett Smith': {'subscribed': True, 'subscription_type': 'quarterly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 30, 'phone_number': '987-654-3210'},
    'William smith': {'subscribed': True, 'subscription_type': 'quarterly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 30, 'phone_number': '987-654-3210'},
    'some guy': {'subscribed': True, 'subscription_type': 'monthly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 25, 'phone_number': '987-654-3210'},
    'your mom': {'subscribed': True, 'subscription_type': 'quarterly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 30, 'phone_number': '987-654-3210'},
    'that one beatle thats still alive': {'subscribed': True, 'subscription_type': 'quarterly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 30, 'phone_number': '987-654-3210'},
    'Rick Sanchez': {'subscribed': True, 'subscription_type': 'quarterly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 30, 'phone_number': '987-654-3210'},
    'Morty Smith': {'subscribed': True, 'subscription_type': 'quarterly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 30, 'phone_number': '987-654-3210'},
    'Jane Smith': {'subscribed': True, 'subscription_type': 'quarterly', 'subscription_start_date': datetime(2023, 1, 1), 'amount_owed': 30, 'phone_number': '987-654-3210'},

    # Add more customers as needed in same format but obv change the datetime, matey
    #also probably wanna implement something that resubscribes the customer...and that would go here but meh, later time..
}

# Function to check and update subscription status based on timeout
def check_subscription_timeout(customer, data):
    subscription_start_date = data['subscription_start_date']
    current_date = datetime.now()
    subscription_duration = None

    if data['subscription_type'] == 'monthly':
        subscription_duration = timedelta(days=30)
    elif data['subscription_type'] == 'quarterly':
        subscription_duration = timedelta(days=90)
    elif data['subscription_type'] == 'yearly':
        subscription_duration = timedelta(days=365)

    if subscription_duration:
        if current_date - subscription_start_date >= subscription_duration:
            data['subscribed'] = False
            print(f"{customer} has been unsubscribed due to subscription timeout.")

# To simulate the passage of time and check for subscription timeouts
for customer, data in customer_data.items():
    check_subscription_timeout(customer, data)

# To print a table-like structure, you can iterate through the dictionary
print("| Customer Name | Subscribed | Subscription Type | Amount Owed | Phone Number |")
print("|---------------|-------------|-------------------|-------------|--------------|")
for customer, data in customer_data.items():
    print(f"| {customer} | {data['subscribed']} | {data['subscription_type']} | {data['amount_owed']} | {data['phone_number']} |")


# To mark a customer as unsubscribed, you can set the 'subscribed' key to False
customer_data['John Doe']['subscribed'] = False

# To check if a customer needs to re-subscribe based on their subscription type, you can use conditions
for customer, data in customer_data.items():
    if data['subscribed'] and data['subscription_type'] == 'monthly':
 # Check if it's time to renew the monthly subscription for this customer
 # If needed, update the subscription status and amount owed

# To print a table-like structure, you can iterate through the dictionary
print("| Customer Name | Subscribed | Subscription Type | Amount Owed | Phone Number |")
print("|---------------|-------------|-------------------|-------------|--------------|")
for customer, data in customer_data.items():
    print(f"| {customer} | {data['subscribed']} | {data['subscription_type']} | {data['amount_owed']} | {data['phone_number']} |")
