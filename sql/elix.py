from elixir import *

metadata.bind = "mysql://root@localhost/movies"
metadata.bind.echo = True

class Movie(Entity):
    
    using_options(tablename='movies')
    
    title = Field(Unicode(30), primary_key=True)   # <-- modify this line
    year = Field(Integer, primary_key=True)
    description = Field(UnicodeText)
    director = ManyToOne('Director')
    genres = ManyToMany('Genre')                   # <-- and add this one
    
    def __repr__(self):
        return '<Movie "%s" (%d)>' % (self.title, self.year)
    

class Director(Entity):
    
    using_options(tablename='director')
    
    name = Field(Unicode(60))
    movies = OneToMany('Movie')
    
    def __repr__(self):
        return '<Director "%s">' % self.name


class Genre(Entity):
    
    using_options(tablename='genre')
    
    name = Field(Unicode(15), primary_key=True)
    movies = ManyToMany('Movie')
    
    def __repr__(self):
        return '<Genre "%s">' % self.name


setup_all(True)

scifi = Genre(name=u"Science-Fiction")
rscott = Director(name=u"Ridley Scott")
glucas = Director(name=u"George Lucas")
alien = Movie(title=u"Alien", year=1979, director=rscott, genres=[scifi, Genre(name=u"Horror")])
brunner = Movie(title=u"Blade Runner", year=1982, director=rscott, genres=[scifi])
swars = Movie(title=u"Star Wars", year=1977, director=glucas, genres=[scifi])

#rscott = Director(name=u"Ridley Scott")
#glucas = Director(name=u"George Lucas")
#alien = Movie(title=u"Alien", year=1979)
#swars = Movie(title=u"Star Wars", year=1977)
#brunner = Movie(title=u"Blade Runner", year=1982)
#rscott.movies.append(brunner) 
#rscott.movies.append(alien)
#swars.director = glucas
#
#print glucas.movies

session.commit()
#create_all()


#a = Movie(title=u"Blade Runner", year = 1982)
#print a
#
#session.commit()
#print Movie.query.all()
#
#movie = Movie.query.first()
#movie.year = 1983
#session.commit()
#print Movie.query.all()
#
#for i in Movie.query.all():
#    i.delete()
#
#session.commit()
#
#print Movie.query.all()

