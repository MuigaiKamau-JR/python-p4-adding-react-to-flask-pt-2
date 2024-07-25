from models import db, Movie
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add initial movies
    movie1 = Movie(title="Inception", year=2010)
    movie2 = Movie(title="The Matrix", year=1999)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.commit()
