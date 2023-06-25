# Currency Converter

def convert_currency(amount, rate):
    converted_amount = amount * rate
    return converted_amount

# Exchange rates (as of a certain date)
exchange_rates = {
    'USD': 1.0,    # 1 USD = 1 USD
    'GBP': 0.72,   # 1 GBP = 0.72 USD
    'EUR': 0.82,   # 1 EUR = 0.82 USD
    'INR': 74.92   # 1 INR = 74.92 USD
}

# Test the currency converter
amount = float(input("Enter the amount: "))
source_currency = input("Enter the source currency: ").upper()
target_currency = 'INR'

if source_currency in exchange_rates and target_currency in exchange_rates:
    rate = exchange_rates[target_currency] / exchange_rates[source_currency]
    converted_amount = convert_currency(amount, rate)
    print("Converted amount:", converted_amount, target_currency)
else:
    print("Invalid currency provided.")

'''
=================================
Test Case:
=================================

Enter the amount: 100
Enter the source currency: USD 
Converted amount: 7492.0 INR

'''