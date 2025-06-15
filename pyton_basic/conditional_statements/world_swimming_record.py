swimming_record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_to_swim_one_meter = float(input())

seconds_needed = distance_in_meters * seconds_to_swim_one_meter

delay_in_seconds = int(distance_in_meters // 15)
delay = delay_in_seconds * 12.5

full_swimming_time = seconds_needed + delay

if swimming_record_in_seconds > full_swimming_time :
    print(f" Yes, he succeeded! The new world record is {full_swimming_time:.2f} seconds.")
else:
    full_swimming_time = full_swimming_time - swimming_record_in_seconds
    print(f"No, he failed! He was {full_swimming_time:.2f} seconds slower.")

