import math


def get_fare(flag_down_fare, within, beyond, distance):
    if distance < 1000:
        return flag_down_fare
    elif distance >= 1000 and distance <= 9800:
        return (within * math.ceil((distance - 1000)/400)) + flag_down_fare
    elif distance > 9800:
        first_fee = beyond * (math.ceil((distance - 9800)/350))
        remainding_fees = (distance - (distance - 9800) - 1000)
        second_fee = within * math.ceil(remainding_fees/400)
        return first_fee + second_fee + flag_down_fare


flag_down_fare = float(input("What's the flag-down fare: "))
within = float(input("What's the rate per 400 meters within 9.8km? "))
beyond = float(input("What's the rate per 350 meters beyond 9.8km? "))
distance = float(input("What's the distance traveled (in meters)? "))
peak = input("Is it peak day? [yes/no] ")

total_meter_fare = get_fare(flag_down_fare, within, beyond, distance)

if peak == "yes":
    total_meter_fare = total_meter_fare * 1.25
else:
    midnight = input("Is the ride between midnight and 6am? [yes/no] ")
    if midnight == "yes":
        total_meter_fare = total_meter_fare * 1.5

location = input("Is there any location surcharge? [yes/no]")
if location == "yes":
    total_meter_fare = total_meter_fare + \
        float(input("What's the surcharge? "))

print("The total fare is $", round(total_meter_fare, 2))
