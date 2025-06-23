# Late Show Flask API
A Flask-based RESTful API for managing episodes, guests, and appearances for a late-night show.

## Setup
1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`
4. Run migrations: `flask db init`, `flask db migrate`, `flask db upgrade`
5. Seed the database: `python seed.py`
6. Start the server: `flask run --port=5555`

## API Endpoints
- `GET /episodes`: List all episodes.
- `GET /episodes/:id`: Get episode details with appearances.
- `GET /guests`: List all guests.
- `POST /appearances`: Create a new appearance.