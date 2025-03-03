import time

#1 String comparison for uppercase

phrase = input("Enter a phrase: ")
upper_phrase = input("Enter a phrase: ")

if upper_phrase == phrase.upper():
    print("Stop shouting please!")

#2 Vowel counter
string = input("Enter a string: ")
vowels = "aeiou"
count = 0

for vowel in vowels:
    if vowel in string.lower():
        count += 1

print(f"{string} has {count} different vowels")

#3 Alphabetical order
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

if str1 < str2:
    print(f"{str1} comes before {str2}")
else:
    print(f"{str2} comes before {str1}")

#4 Email verification
while True:
    email1 = input("Enter your email address: ")
    email2 = input("Enter your email address again: ")

    if email1 != email2:
        print("The two inputs did not match.")
    else:
        print("Thank you!")
        break

# 5: Factorial calculations with performance measurement


#Calculate factorial using iteration
def factorial_iterative(recur_vvv):
    result = 1
    for i in range(1, recur_vvv + 1):
        result *= i
    return result


#Calculate factorial using recursion
def factorial_recursive(recur_vvv):
    if recur_vvv <= 1:
        return 1
    return recur_vvv * factorial_recursive(recur_vvv - 1)


# Measure and display performance
print("Input             Iterative          Recursive")

results = []
test_numbers = [3, 10, 25]

for recur_vvv in test_numbers:
    # Time for iterative implementation
    start = time.perf_counter_ns()
    iter_result = factorial_iterative(recur_vvv)
    stop = time.perf_counter_ns()
    iterative_time = stop - start

    # Time for recursive implementation
    start = time.perf_counter_ns()
    recur_result = factorial_recursive(recur_vvv)
    stop = time.perf_counter_ns()
    recursive_time = stop - start

    # Store results
    results.append(
        (recur_vvv, iterative_time, recursive_time, iter_result, recur_result))

# Display all results together
for result in results:
    recur_vvv, iterative_time, recursive_time, iter_result, recur_result = result
    print(f"{recur_vvv:5d}       {iterative_time:14d}    {recursive_time:14d}")

user_input = int(input("\nEnter a number to calculate factorial: "))
if user_input >= 0:
    print(
        f"Factorial of {user_input} (iterative): {factorial_iterative(user_input)}"
    )
    if user_input <= 900:
        print(
            f"Factorial of {user_input} (recursive): {factorial_recursive(user_input)}"
        )
    else:
        print("input too large")
