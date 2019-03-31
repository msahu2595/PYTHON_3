# dictionary comprehension
# square = {1:1, 2:4, 3:9}
square = {f"Square of {num} is":num**2 for num in range(1,11)}
print(square)
for k,v in square.items():
    print(f"{k} : {v}")

# word count in string
str_1 = "manish kumar sahu"
word_count = {i:str_1.count(i) for i in str_1.replace(' ','')}
print(str_1)
print(word_count)



