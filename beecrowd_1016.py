def time_to_overtake(distance_km):
    speed_x = 60
    speed_y = 90

    relative_speed = speed_y - speed_x

    time_hours = distance_km / relative_speed

    time_minutes = time_hours * 60

    return time_minutes


distance_km = int(input())

time_minutes = time_to_overtake(distance_km)

print(int(time_minutes), "minutes")
