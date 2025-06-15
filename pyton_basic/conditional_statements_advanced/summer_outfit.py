celsius = int(input())
time_of_the_day = input()

outfit = ''
shoes = ''

if time_of_the_day not in ['Morning', 'Afternoon', 'Evening']:
  print('Error')
elif celsius <= 0:
  print('Error')
else:
  if time_of_the_day == 'Morning':
      if 10 <= celsius <= 18:
          outfit = 'Sweatshirt'
          shoes = 'Sneakers'
      elif 18 < celsius <= 24:
          outfit = 'Shirt'
          shoes = 'Moccasins'
      elif celsius >= 25:
          outfit = 'T-Shirt'
          shoes = 'Sandals'
  elif time_of_the_day == 'Afternoon':
      if 10 <= celsius <= 18:
          outfit = 'Shirt'
          shoes = 'Moccasins'
      elif 18 < celsius <= 24:
          outfit = 'T-Shirt'
          shoes = 'Sandals'
      elif celsius >= 25:
          outfit = 'Swim Suit'
          shoes = 'Barefoot'
  elif time_of_the_day == 'Evening':
      if 10 <= celsius <= 18:
          outfit = 'Shirt'
          shoes = 'Moccasins'
      elif 18 < celsius <= 24:
          outfit = 'Shirt'
          shoes = 'Moccasins'
      elif celsius >= 25:
          outfit = 'Shirt'
          shoes = 'Moccasins'

print(f'It\'s {celsius} degrees, get your {outfit} and {shoes}.')   