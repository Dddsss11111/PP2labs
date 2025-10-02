movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]






# 1 Write a function that takes a single movie and returns True if its IMDB score is above 5.5

# def check(index):
#     return True if(movies[index]["imdb"] > 5.5) else False

# print(check(2))



# 2 Write a function that returns a sublist of movies with an IMDB score above 5.5.

# def cool():
#     li = []
#     for i in movies:
#         if(i["imdb"] > 5.5):
#             li.append(i)
#     return li

# print(cool())




# 3 Write a function that takes a category name and returns just those movies under that category.

# def sort_movies(categ):
#     li = []
#     for i in movies:
#         if(i["category"] == categ):
#             li.append(i)
#     return li

# print(sort_movies("Romance"))

# sorted_movies = filter(lambda x : x["category"] == "Drama", movies)
# print(list(sorted_movies))



# 4 Write a function that takes a list of movies and computes the average IMDB score.

# def av():
#     count = 0
#     for i in movies:
#         count += i["imdb"]
#     return count / len(movies)
# print(av())




# 5 Write a function that takes a category and computes the average IMDB score.

# def av_cat(categ):
#     count = 0
#     score = 0
#     for i in movies:
#         if i["category"] == categ:
#             score += i["imdb"]
#             count += 1
#     return score / count

# print(av_cat("Thriller"))