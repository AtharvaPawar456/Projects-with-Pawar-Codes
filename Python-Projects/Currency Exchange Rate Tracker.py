# Currency Exchange Rate Tracker

# pip install requests

import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][target_currency]
        return rate
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

# Test the Currency Exchange Rate Tracker
base_currency = input("Enter the base currency: ").upper()
target_currency = input("Enter the target currency: ").upper()

exchange_rate = get_exchange_rate(base_currency, target_currency)
if exchange_rate is not None:
    print(f"1 {base_currency} = {exchange_rate} {target_currency}")


'''
=================================
Test Case:
=================================

Test1:
Enter the base currency: INR
Enter the target currency: USD
1 INR = 0.0122 USD

---------------------------------

Test2:
Enter the base currency: USD
Enter the target currency: INR
1 USD = 82.02 INR

'''