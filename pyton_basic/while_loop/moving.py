room_length = int(input())
room_width = int(input())
room_high = int(input())
total_room_space = room_width * room_high * room_length

while True :
    command = input()
    if command == 'Done':
        print(f'{total_room_space} Cubic meters left.')
        break

    room_space = int(command)
    total_room_space -= room_space

    if total_room_space < 0:
        print(f'No more free space! You need {abs(total_room_space)} Cubic meters more.')
        break
