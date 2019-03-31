# looping in tuples
mixed = (1,2,3,4.0)
for i in mixed:
    print(i)
# we can use while loop too


# tuple with one element (with/without paraenthesis)
nums = (1)
nums1 = (1,)
words = 'word1'
words1 = 'word1',
print(type(nums))
print(type(nums1))
print(type(words))
print(type(words1))


# tuple without paraenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))


# tuple unpacking
guitarists = ('maneli jamal', 'eddie van der meer', 'andrew foy')
guitarist1, guitarist2, guitarist3 = guitarists
print(guitarist1)


# list inside tuple
favourites = ('southern mangolia', ['tokyo ghoul theme', 'landscape'])
string_1 = favourites[1].pop()
favourites[1].append('we made it')
print(string_1)
print(favourites)


# min, max and sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))


