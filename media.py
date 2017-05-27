import webbrowser  #import the function "webbrowser"

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  #Define the class "Movie"
        self.title = movie_title  #the followeing line create the instance variables for title, storyline, poster and trailer
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
