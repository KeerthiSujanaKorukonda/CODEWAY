#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using a list comprehension
    password_list = [random.choice(characters) for _ in range(length)]

    # Convert the list of characters into a string
    password = ''.join(password_list)
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Invalid input! Length must be a positive integer.")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()


# In[ ]:




