import time
print("3 viruses")
Number = input("Your Friend's Number: ")

LoginTime = input("Login first(hint: Broken): ")
if LoginTime == "Broken":
    print("Select the virus")
    print("1. Data Eater")
    print("2. Phone Heater")
    print("3. Phone Broker In 1 Month")
    print("(phone heater is faster and phone breaker takes only 30 seconds but the process is 1 month.)")
    Choser = input("Choose One(Only type 1, 2 or 3.): ")
    if Choser == "1":
        time.sleep(5)
        print("Detecting Number...")
        time.sleep(4)
        print("Locating Number...")
        time.sleep(4)
        print("Searching Number...")
        time.sleep(8)
        print("Processing...(this might takes 30 seconds)")
        time.sleep(17)
        print("Sending Virus...")
        time.sleep(6)
        print("Detecting Antivirus...")
        time.sleep(2)
        print("Virus Sent!")
        time.sleep(4)
    elif Choser == "2":
        time.sleep(3)
        print("Searching Number...")
        time.sleep(6)
        print("Detecting...")
        time.sleep(3)
        Celc = input("How Many Celcius Degrees You Want? ")
        time.sleep(7)
        print("Heating Phone Untill", + Celc,"Degrees...")
        time.sleep(10)
        print("Phone Heated To", + Celc,"Degrees.")
        time.sleep(3)
    elif Choser == "3":
        print("Locating Number...")
        time.sleep(2)
        print("Breaking Phone...")
        time.sleep(8)
        print("Done, Wait for 1 month.")
        print("Prediction:")
        time.sleep(1)
        print("Day 1: Nothing Happens")
        time.sleep(1)
        print("Week 1: Logged Out From Some Accounts")
        time.sleep(1)
        print("Week 3: Phone Battery Exhaust Faster")
        time.sleep(1)
        print("Month 1: Phone Broken")
    else:
        print("Only Number 1, 2 or 3!")
        time.sleep(3)
else:
    print("Wrong Password")
    time.sleep(3)