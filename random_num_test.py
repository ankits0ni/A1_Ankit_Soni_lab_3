# Create an empty list to store formatted numbers.
numbers = []

# Iterate through numbers from 0 to 999 (exclusive).
for num in range(1000):
    # Convert the number to a string and fill with zeros to make it three digits long.
    num = str(num).zfill(3)

    # Append the formatted number to the 'numbers' list.
    numbers.append(num)

# Print the last formatted number.
print(numbers[-1])

def test_last_number():
    # Test case: Check if the last number is '999'.
    assert numbers[-1] == '999'

def test_first_number():
    # Test case: Check if the first number is '000'.
    assert numbers[-1] == '000'
