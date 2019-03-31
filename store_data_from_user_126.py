# store data from user

user = {}

name = input('what is your name : ')
age = input('what is your age : ')
fav_movies = input('what is your favourate movies saperated by comma : ').split(",")
fav_songs = input('what is your favourate songs : ').split(",")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
print(user)

for key, value in user.items():
    print(f"{key} : {value}")


