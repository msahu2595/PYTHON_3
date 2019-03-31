# default parameters

# [1]
def user_info(first_name = "unknown", last_name = "unknown", age = None):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

user_info()

# [2]
def new_user_info(first_name, last_name = "unknown", age = None):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

new_user_info("manish")

# [3]
def new_2_user_info(first_name, last_name, age = None):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

new_2_user_info("manish", "sahu")

# [4]
def new_3_user_info(first_name, last_name, age):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

new_3_user_info("manish", "sahu", 23)