# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# print("Armstrong numbers in the given range:")
# for num in range(start, end + 1):
    # order = len(str(num))
    # sum_of_powers = sum(int(digit) ** order for digit in str(num))
    # if num == sum_of_powers:
        # print(num)
# for num in range(-1, -11, -1):
    # print(num)




    
# num = int(input("Enter a number: "))

# if num > 1:
    # for i in range(2, int(num ** 0.5) + 1):
        # if num % i == 0:
            # print(f"{num} is not a prime number.")
            # break
    # else:
        # print(f"{num} is a prime number.")
# else:
    # print(f"{num} is not a prime number.")




# def fibonacci(n):
    # a, b = 0, 1
    # for _ in range(n):
        # print(a, end=" ")
#   def print_armstrong_in_range(lower_bound,upper_bound):
    # for i in range (lower_bound,upper_bound + 1):
        # if
        # print_armstrong_in_range_(upper_bound, lower_bound)  

# for i in range(lower_bound)


def reverse_negative(num):
    if num > 0:
        raise ValueError("Number must be negative")
    reversed_num = int(str(abs(num))[::-1]) 
    return -reversed_num 

