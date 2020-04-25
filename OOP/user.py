from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "User : {} ".format(self.name)

    def addMovie(self, name, genre, watched=False):
        movie = Movie(name, genre, watched)
        self.movies.append(movie)

    def deleteMovie(self,name):
        self.movies = list(filter(lambda x:x.name != name, self.movies))

    def watchedMovies(self):
        return list(filter(lambda x: x.watched, self.movies))

    def setWatched(self, name):
        for movie in self.movies:
            if name == movie.name:
                movie.watched = True

    def json(self):
        return {
            'name':self.name,
            'movies': [movie.json() for movie in self.movies]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.fromJson(movie_data))
        user.movies = movies
        return user
