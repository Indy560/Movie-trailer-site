import fresh_tomatoes  #import the file "fresh_tomatoes.py"
import media  #import the file "media.py"

grosse_pointe_blank = media.Movie("Grosse Pointe Blank", "A hitman goes to his"
                                  "10 year high school reunion",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/Grosse_Pointe_Blank_poster.jpg/215px-Grosse_Pointe_Blank_poster.jpg",#NOQA Link to movie poster image
                        "https://www.youtube.com/watch?v=IJ7AXKWmWOg") #Link to movie trailer

blade_runner = media.Movie("Blade Runner", "A police officer hunts down human"
                           "killer cyborgs",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",#NOQA Link to movie poster image
                           "https://www.youtube.com/watch?v=eogpIG53Cis") #Link to movie trailer
                           
fight_club = media.Movie("Fight Club", "Two frustrated men start an underground"
                         "fight club",
                             "http://www.imfdb.org/images/thumb/1/12/FightClubCover.jpg/301px-FightClubCover.jpg",#NOQA Link to movie poster image
                             "https://www.youtube.com/watch?v=BdJKm16Co6M") #Link to movie trailer

the_dark_knight = media.Movie("The Dark Knight", "The Batman faces the Joker "
                              "and organized crime",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",#NOQA Link to movie poster image
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY") #Link to movie trailer

master_and_commander = media.Movie("Master and Commander", "A British navy "
                                   "ship chases a French privateer in the "
                                   "Napoleanic war",
                                "https://upload.wikimedia.org/wikipedia/en/b/bf/Master_and_Commander-The_Far_Side_of_the_World_poster.png",#NOQA Link to movie poster image
                                "https://www.youtube.com/watch?v=KpNhN-L9L-g") #Link to movie trailer

holy_grail = media.Movie("Monty Python and ", "A comedy about King Arthur "
                         "and the Holy Grail",
                           "http://vignette1.wikia.nocookie.net/filmguide/images/c/c1/Holy_grail_2001_poster.jpg/revision/latest?cb=20130724175811",#NOQA Link to movie poster image
                           "https://www.youtube.com/watch?v=urRkGvhXc8w") #Link to movie trailer

movies = [grosse_pointe_blank, blade_runner, fight_club, the_dark_knight,  #The array "movies" input list of data for the function open_movies_page in the "fresh_tomatoes" file.
          master_and_commander, holy_grail]
fresh_tomatoes.open_movies_page(movies)  #Call the function "open_movies_page" from the "fresh_tomatoes.py" file
