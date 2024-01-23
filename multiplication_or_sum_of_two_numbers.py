#define the two numbers for multiplication and sum
def multiplication_or_sum(first_number, second_number):
#calculate product and sum of first number and second number
 product = first_number * second_number
 sum = first_number + second_number
#check if product is less than 1000
 if product <= 1000:
    return product
 else:
    return sum
#conditions
#first condition
result = multiplication_or_sum(26, 31)
print("The result is", result)
#second condition
result = multiplication_or_sum(35, 35)
print("The result is", result)