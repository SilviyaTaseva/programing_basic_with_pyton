deposit_sum = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())/100
monthly_rate = annual_interest_rate/12
end_sum = deposit_sum + deposit_term * (deposit_sum * monthly_rate)

print(f"{end_sum :.2f}")