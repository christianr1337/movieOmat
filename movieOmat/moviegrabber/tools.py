'''
Created on Nov 4, 2012

@author: c1337b
'''
import os
from movies.models import Movie
import imdb


class Tools(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def get_folder_names_and_save_to_model(self):
        folderlist = open("data/folders")
        
        # Create the object that will be used to access the IMDb's database.
        ia = imdb.IMDb() # by default access the web.
        
        try:
            for moviefolder in folderlist:
                if("-" in moviefolder):
                    print
                    print "End of folders"
                    break

                print "Analyzing folders: ", moviefolder
                print "Movies: "

                for movie in os.listdir(moviefolder.rstrip()):
                    movie_content = movie.split(" ++ ")
                    print movie_content
                    
                    movie_name = movie_content[0]
                    try:
                        movie_languages = movie_content[1] 
                        movie_quality = movie_content[2]
                    except: 
                        movie_languages = "no language provided"
                        movie_quality = "no quality provided"
                    print "Name: %s  Languages: %s  Quality: %s" % (movie_name, movie_languages, movie_quality)
                    
                    #movie_db = Movie(name=movie_name, languages=movie_languages, quality=movie_quality, in_folder=moviefolder)
                    #movie_db.save()

                    ''' 
                        IMDB Access and retriving of movie data
                        TODO: auslagern
                    '''
                    # Search for a movie (get a list of Movie objects).
                    s_result = ia.search_movie(movie_name)
                    if not s_result:
                        print "LALALAL"
                        movie_db = Movie(name=movie_name, imdb_name="Kein IMDb Eintrag gefunden", languages=movie_languages, quality=movie_quality, in_folder=moviefolder)
                        movie_db.save()
                        continue
                    
                    # Print the long imdb canonical title and movieID of the results.
                    #for item in s_result:
                    #    print item['long imdb canonical title'], item.movieID
                    
                    # Retrieves default information for the first result (a Movie object).
                    imdb_movie_obj = s_result[0]
                    ia.update(imdb_movie_obj)
                    
                    # Print some information.
                    try:
                        imdb_name=imdb_movie_obj
                        print "Imdb name: ", imdb_name
                        
                    except:
                        imdb_name = "No name is found in imdb."
                    
                    try:
                        runtime=imdb_movie_obj['runtime'][0]
                        print "Imdb runtime(in min): ", runtime
                        
                    except:
                        runtime = 0
                        
                    try:
                        rating=imdb_movie_obj['rating']
                        print "Imdb rating: ", rating
                        
                    except:
                        rating = 0
                    
                    try:
                        plot=imdb_movie_obj['plot'][0]
                        print "Imdb plot: ", plot
                        
                    except:
                        plot = "No plot is found in imdb."


                    #director = imdb_movie_obj['director'] # get a list of Person objects.

                    '''
                        END OF IMDB Data migration
                    '''
                    
                    movie_db = Movie(name=movie_name,imdb_name= imdb_name, description=plot, imdb_rating=rating, length=runtime, languages=movie_languages, quality=movie_quality, in_folder=moviefolder)
                    movie_db.save()

                print
        except OSError:
            print "Wrong movie folder: ", moviefolder
