# Kannada Learning Portal - Backend API

This is the backend API for the Kannada Learning Portal, built with Flask.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Directory Structure

```
Backend_Flask/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── word.py
│   │   ├── group.py
│   │   ├── study_session.py
│   │   └── word_review.py
│   ├── routes/
│   │   ├── words.py
│   │   ├── groups.py
│   │   ├── sessions.py
│   │   └── dashboard.py
│   └── schemas.py
├── config.py
├── .env
└── README.md
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd Lang-Portal/Backend_Flask
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install Flask==3.0.0 Flask-SQLAlchemy==3.1.1 Flask-Migrate==4.0.5 Flask-Marshmallow==0.15.0 marshmallow-sqlalchemy==0.29.0 Flask-CORS==4.0.0 python-dotenv==1.0.0
```

4. Set up environment variables:
```bash
# Windows (PowerShell)
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"

# Linux/Mac
export FLASK_APP=app
export FLASK_ENV=development
```

5. Initialize and set up the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask seed
```

6. Run the application:
```bash
flask run
```

## API Endpoints

The API will be available at `http://127.0.0.1:5000/`

### Available Endpoints:

1. Words API:
   - GET `/api/words` - Get all words
   - GET `/api/words?search=<term>` - Search words
   - GET `/api/words?group_id=<id>` - Filter by group
   - GET `/api/words?page=1&limit=10` - Pagination

2. Groups API:
   - GET `/api/groups` - Get all groups
   - GET `/api/groups/<id>` - Get specific group

3. Study Sessions API:
   - POST `/api/sessions` - Create new session
   - GET `/api/sessions/<id>` - Get session details

4. Dashboard API:
   - GET `/api/dashboard/stats` - Get learning statistics

## Testing the API

You can test the API using:

1. Web Browser:
   - Visit `http://127.0.0.1:5000/` for the welcome page
   - Visit `http://127.0.0.1:5000/api/words` to see all words
   - Visit `http://127.0.0.1:5000/api/groups` to see all groups

2. Postman:
   - Import the API collection (if available)
   - Test different endpoints with various parameters

3. cURL:
```bash
# Get all words
curl http://127.0.0.1:5000/api/words

# Get all groups
curl http://127.0.0.1:5000/api/groups

# Create a new session
curl -X POST http://127.0.0.1:5000/api/sessions \
  -H "Content-Type: application/json" \
  -d '{"group_id": 1, "activity_type": "flashcards"}'
```

## Common Issues and Solutions

1. **Module Not Found Error**:
   - Make sure you're in the correct directory
   - Ensure virtual environment is activated
   - Verify all packages are installed

2. **Database Errors**:
   - Delete the `migrations` folder and `instance/words.db`
   - Run the database initialization commands again

3. **404 Errors**:
   - Check if you're using the correct URL with `/api/` prefix
   - Verify the endpoint exists in the routes

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

