print("Please tell us your monthly usage requirements.")
print("")

calls = int(input("Minimum outgoing calls you need? : "))
sms = int(input("Minimum SMS messages you need? : "))
data = float(input("Minimum amount of data (in GB) you need?: "))

if calls <= 80 and sms <= 300 and data <= 0.1:
    print("We recommend Combo 1")
elif calls <= 200 and sms <= 500 and data <= 2:
    print("We recommend Combo 2")
elif 200 <= calls <= 300 and sms <= 1000 and data <= 3:
    print("We recommend Combo 3")
elif 300 <= calls <= 400 and 1500 and data <= 4:
    print("We recommend Combo 4")
elif 400 <= calls <= 800 and 2000 and data <= 10:
    print("We recommend Combo 5")
else:
    print("Sorry, we don't have a plan that fits your requirements.")