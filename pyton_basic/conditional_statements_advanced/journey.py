budget = float(input())
season = input()
destination = 0
place = 0
total_budget = 0

if budget <= 100:
  if season == 'summer':
      total_budget = budget * 0.30
      place = 'Camp'
      destination = 'Bulgaria'
  elif season == 'winter':
      total_budget = budget * 0.70
      place = 'Hotel'
      destination = 'Bulgaria'
elif 100 < budget <= 1000:
  if season == 'summer':
      total_budget = budget * 0.40
      place = 'Camp'
      destination = 'Balkans'
  elif season == 'winter':
      total_budget = budget * 0.80
      place = 'Hotel'
      destination = 'Balkans'
else:
  place = 'Hotel'
  total_budget = budget * 0.90
  destination = 'Europe'
print(f'Somewhere in {destination}')
print(f'{place} - {total_budget:.2f}')