# python custom exceptions
# Q - Why custom exceptions ?
# A - To increse the readability of code.

# Example

class NameToShortError(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameToShortError("name is too short")
    
username = input("Enter your name : ")
validate(username)
print(f'hello {username}')




