# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:15:36 2023

@author: david
"""

def calculate_final_amount(allocations, returns, monthly_payment, time_period):
    num_months = time_period * 12
    portfolio_value = 0

    for month in range(num_months):
        for allocation, asset_return in zip(allocations, returns):
            portfolio_value += allocation * (portfolio_value + monthly_payment) * (1 + asset_return / 12)

    return portfolio_value


import matplotlib.pyplot as plt

def get_user_allocations(num_assets):
    allocations = []
    total_allocation = 0
    investments = []

    while total_allocation != 1:
        allocations = []  # Reset the allocations
        total_allocation = 0  # Reset the total allocation
        investments = []  # Reset the investments

        for i in range(num_assets):
            investment_type = input(f"Enter the type of investment for Asset {i+1}: ")
            allocation = float(input(f"Enter allocation for {investment_type} [0,1]: "))

            while allocation < 0 or allocation > 1:
                allocation = float(input(f"Enter allocation for {investment_type} [0,1]: "))

            total_allocation += allocation
            allocations.append(allocation)
            investments.append(investment_type)

        if total_allocation != 1:
            print("Warning: Total allocation does not equal 1.")

    
    fig, ax = plt.subplots()
    ax.pie(allocations, labels=investments, autopct='%1.1f%%')
    ax.set_title("Your investment allocation")
    plt.show()

    return allocations

def generate_csv(amounts):
    with open('portfolio_amounts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Year', 'Amount'])
        for i, amount in enumerate(amounts):
            writer.writerow([i + 1, amount])
        
    
a = int(input('Give me the number of allocations:'))
print(get_user_allocations(a))

def get_user_returns(num_assets):
    returns = []

    for i in range(num_assets):
        asset_return = float(input(f"Enter return for Asset {i+1}: "))
        while asset_return < 0:
            asset_return = float(input(f"Enter return for Asset {i+1}: "))
            
        returns.append(asset_return)

    return returns

def main():
    num_assets = int(input("Enter the number of assets in the portfolio: "))
    allocations = get_user_allocations(num_assets)
    returns = get_user_returns(num_assets)

    monthly_payment = float(input("Enter the monthly payment amount: "))
    time_period = float(input("Enter the time period in years: "))

    final_amount = calculate_final_amount(allocations, returns, monthly_payment, time_period)

    print(f"\nThe final amount after {time_period} years is: ${final_amount:.2f}")


if __name__ == '__main__':
    main()
    