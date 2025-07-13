cake_length = int(input())
cake_width = int(input())
cake_size = cake_length * cake_width


while True:
    command = input()

    if command == 'STOP':
        print(f'{cake_size} pieces are left.')
        break

    pice_taken = int(command)
    cake_size -= pice_taken

    if cake_size <= 0:
        print(f'No more cake left! You need {abs(cake_size)} pieces more.')
        break
        
