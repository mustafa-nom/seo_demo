# Example 2: User Input Validation with Error Handling
def get_valid_age():
    """
    Prompts user for their age and validates the input.
    Demonstrates handling user input errors with retry logic.
    """
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        age_input = input("Please enter your age: ")
        try:
            age = int(age_input)

            # this is a nice place to check and raise any for errors...
            if age <= 0:
                print('age cant be less than/equal 0')
                attempts += 1
                continue
            return age
            
            # here is a good place to catch errors...
        except ValueError: 
            print('invalid input, use a valid int')
            attempts += 1
print('max attempts reached, gl bro')
return None

# Example usage
print("=== Example 2: User Input Validation ===")
user_age = get_valid_age()
if user_age is not None:
    print(f"Valid age entered: {user_age}")
    if user_age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
else:
    print("Could not get valid age input")

print()
