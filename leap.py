# def next_leap_year(year):
    # while True:
        # year += 1
        # if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # return year
    
         num = int(input("Enter a number: "))

divisors = [i for i in range(1, num) if num % i == 0]

if sum(divisors) == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

 