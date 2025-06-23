from config import app, db
from models import Episode, Guest, Appearance

def seed_database():
    db.drop_all()
    db.create_all()

    seed_data = [
        ("Michael J. Fox", "actor", "1/11/99"),
        ("Sandra Bernhard", "Comedian", "1/12/99"),
        ("Tracey Ullman", "television actress", "1/13/99"),
        ("Gillian Anderson", "film actress", "1/14/99"),
        ("David Alan Grier", "actor", "1/18/99"),
        ("William Baldwin", "actor", "1/19/99"),
        ("Michael Stipe", "Singer-lyricist", "1/20/99"),
    ]

    guests = []
    episodes = []

    for idx, (name, occupation, date) in enumerate(seed_data, start=1):
        guest = Guest(name=name, occupation=occupation)
        episode = Episode(number=idx, date=date)
        db.session.add(guest)
        db.session.add(episode)
        db.session.flush()  # Ensure they have IDs before using
        appearance = Appearance(rating=4, guest_id=guest.id, episode_id=episode.id)
        db.session.add(appearance)

    db.session.commit()
    print("Database seeded successfully.")

if __name__ == '__main__':
    with app.app_context():
        seed_database()
