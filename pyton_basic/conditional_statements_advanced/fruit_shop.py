fruit = input()
day_of_the_week = input()
number_of_fruits = float(input())
price = 0

if fruit == 'banana' and (day_of_the_week == 'Monday' or
   day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or
          day_of_the_week == 'Friday'):
              price = 2.50
elif fruit == 'apple' and (day_of_the_week == 'Monday' or
day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or
          day_of_the_week == 'Friday'):
              price = 1.20
elif fruit == 'orange' and (day_of_the_week == 'Monday' or  day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or
          day_of_the_week == 'Friday'):
              price = 0.85
elif fruit == 'grapefruit' and (day_of_the_week == 'Monday' or
   day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or
          day_of_the_week == 'Friday'):
              price = 1.45
elif fruit == 'kiwi' and (day_of_the_week == 'Monday' or
   day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or
          day_of_the_week == 'Friday'):
              price = 2.70
elif fruit == 'pineapple' and (day_of_the_week == 'Monday' or
   day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or
          day_of_the_week == 'Friday'):
              price = 5.50
elif fruit == 'grapes' and (day_of_the_week == 'Monday' or
   day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or
          day_of_the_week == 'Friday'):
              price = 3.85
elif (day_of_the_week == 'Saturday' or day_of_the_week =='Sunday') and fruit == 'banana':
    price = 2.70
elif (day_of_the_week == 'Saturday' or day_of_the_week =='Sunday') and fruit == 'grapes':
    price = 4.20
elif (day_of_the_week == 'Saturday' or day_of_the_week =='Sunday') and fruit == 'apple':
    price = 1.25
elif (day_of_the_week == 'Saturday' or day_of_the_week =='Sunday') and fruit == 'orange':
    price = 0.90
elif (day_of_the_week == 'Saturday' or day_of_the_week =='Sunday') and fruit == 'grapefruit':
    price = 1.60
elif (day_of_the_week == 'Saturday' or day_of_the_week =='Sunday') and fruit == 'kiwi':
    price = 3.00
elif (day_of_the_week == 'Saturday' or day_of_the_week =='Sunday') and fruit == 'pineapple':
    price = 5.60
total = number_of_fruits * price
if total > 0 :
    print(f'{total:.2f}')
else:
    print('error')