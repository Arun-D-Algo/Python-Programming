#Program to generate COMPOUND INTEREST from given input.

principle = 0
time = 0
rate = 0

principle = float(input("Enter the principle amount : "))
while principle<0:
    print("The principle cannot be a negative amount!")
    principle = float(input("Enter a valid principle amount : "))

time = float(input("Enter the time period in years : "))
while time<0:
    print("The time cannot be a negative value!")
    time = float(input("Enter a valid time in years : "))

rate = float(input("Enter the rate of interest : "))

total_interest = principle*pow((1+ (rate/100)), time)
print(f"Balance after {time} years is {total_interest:.2f} .")