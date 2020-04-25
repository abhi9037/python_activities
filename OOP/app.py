import os
import json
from user import User


def menu():
    name = input("Enter user name: ")
    filename = "{}.txt".format(name)
    if file_exist(filename):
        with open(filename, "r") as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    selection = input("A. Add movie\n"
                      "S. Set the list of movies\n"
                      "W. Set movie as watched\n"
                      "D. Delete a movie\n"
                      "L. See the list of watched movies\n"
                      "F. Save\n"
                      "Q. Quit\n"
                      "Select an option:")
    while selection!= "Q":
        if selection == 'A' or selection == 'a':
            movie_name = input("Enter movie name: ")
            movie_genre = input("Enter movie genre: ")
            user.addMovie(movie_name, movie_genre)
        elif selection == 'S' or selection == 's':
            for movie in user.movies:
                print("Name:{}, Genre :{}, Watched:{}".format(movie.name, movie.genre, movie.watched))
        elif selection == 'W' or selection == 'w':
            movie_name = input("Enter movie name to set watched: ")
            user.setWatched(movie_name)
        elif selection == 'D' or selection == 'd':
            movie_name = input("Enter movie name to delete: ")
            user.deleteMovie(movie_name)
        elif selection == 'L' or selection == 'l':
            for movie in user.watchedMovies():
                if movie.watched:
                    print("Name:{}, Genre :{}".format(movie.name, movie.genre))
        elif selection == "F" or selection == "f":
            with open(filename, "w") as f:
                json.dump(user.json(),f)
        else:
            print("Wrong input !!!!!")
        selection = input("A. Add movie\n"
                          "S. Set the list of movies\n"
                          "W. Set movie as watched\n"
                          "D. Delete a movie\n"
                          "L. See the list of watched movies\n"
                          "F. Save\n"
                          "Q. Quit\n"
                          "Select an option:")


def file_exist(filename):
    return os.path.isfile(filename)

menu()
