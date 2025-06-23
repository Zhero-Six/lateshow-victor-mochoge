from config import app, db, api
from models import Episode, Guest, Appearance
from flask_restful import Resource
from flask import request  # Needed for AppearanceCreate
from sqlalchemy.exc import IntegrityError

# --- Root Route ---
@app.route('/')
def index():
    return {"message": "Welcome to the Late Show API"}, 200

# --- Resources ---
class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [episode.to_dict() for episode in episodes], 200

class EpisodeDetail(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {'error': 'Episode not found'}, 404
        return {
            'id': episode.id,
            'date': episode.date,
            'number': episode.number,
            'appearances': [
                {
                    'id': appearance.id,
                    'episode_id': appearance.episode_id,
                    'guest_id': appearance.guest_id,
                    'rating': appearance.rating,
                    'guest': appearance.guest.to_dict()
                } for appearance in episode.appearances
            ]
        }, 200

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {'error': 'Episode not found'}, 404
        db.session.delete(episode)
        db.session.commit()
        return {}, 204

class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict() for guest in guests], 200

class AppearanceCreate(Resource):
    def post(self):
        data = request.get_json()
        try:
            appearance = Appearance(
                rating=data['rating'],
                episode_id=data['episode_id'],
                guest_id=data['guest_id']
            )
            db.session.add(appearance)
            db.session.commit()
            return appearance.to_dict(), 201
        except (ValueError, IntegrityError):
            db.session.rollback()
            return {'errors': ['validation errors']}, 400

# --- Register Resources ---
api.add_resource(EpisodeList, '/episodes')
api.add_resource(EpisodeDetail, '/episodes/<int:id>')
api.add_resource(GuestList, '/guests')
api.add_resource(AppearanceCreate, '/appearances')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
