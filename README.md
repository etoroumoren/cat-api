# Profile API - Backend Wizards Stage 0

A simple RESTful API endpoint that returns profile information along with a dynamic cat fact fetched from an external API.

## Live Demo
**Deployed URL:** []

**Test it:**
```bash
curl https://your-deployed-url.com/me
```

## Features
- Returns personal profile information
- Fetches random cat facts from Cat Facts API
- Dynamic UTC timestamps in ISO 8601 format
- Error handling for external API failures
- Built with Django REST Framework

## Tech Stack
- **Language:** Python 3.x
- **Framework:** Django 5.2.7
- **API Framework:** Django REST Framework 3.16.1
- **HTTP Client:** requests 2.32.4

## API Endpoint

### GET /me

Returns profile information with a random cat fact.

**Response Format:**
```json
{
  "status": "success",
  "user": {
    "email": "torohkiss@gmail.com",
    "name": "Etoro Umoren",
    "stack": "django"
  },
  "timestamp": "2025-10-21T23:51:19.123456+00:00",
  "fact": "Cats sleep 70% of their lives."
}
```

**Response Fields:**
- `status`: Always returns "success"
- `user.email`: Developer's email address
- `user.name`: Developer's full name
- `user.stack`: Backend technology stack
- `timestamp`: Current UTC time in ISO 8601 format
- `fact`: Random cat fact from Cat Facts API

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/etoroumoren/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   
   # On Linux/Mac:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Test the endpoint:**
   ```bash
   curl http://127.0.0.1:8000/me
   ```
   
   Or visit in browser: `http://127.0.0.1:8000/me/`

## Dependencies

The project requires the following Python packages (see `requirements.txt`):

```
Django==5.2.7
djangorestframework==3.16.1
requests==2.32.4
gunicorn
```

**Install all dependencies:**
```bash
pip install -r requirements.txt
```

## Environment Variables

No environment variables are required for this project. All configuration is handled in `catapi/settings.py`.

## Project Structure

```
catapi/
├── catapi/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myprofile/           # App containing the /me endpoint
│   ├── views.py         # API endpoint logic
│   └── urls.py          # URL routing
├── manage.py
├── requirements.txt
└── README.md
```

## Testing

### Manual Testing

**Using curl:**
```bash
curl http://127.0.0.1:8000/me
```

**Using curl with pretty print:**
```bash
curl http://127.0.0.1:8000/me | python -m json.tool
```

**Using browser:**
Visit `http://127.0.0.1:8000/me/` to see the Django REST Framework browsable API.

### Verify Dynamic Data

Run the curl command multiple times to verify:
- Timestamp changes with each request
- Cat fact changes with each request

## Error Handling

The API gracefully handles external API failures:
- If the Cat Facts API is unreachable, a fallback message is returned
- Network timeouts are set to 5 seconds
- The endpoint always returns HTTP 200 OK with valid JSON

## Deployment

This API is deployed on Railway.

**Deployment platforms used:**
- Railway / PythonAnywhere / Heroku / AWS (specify which one)

## API Documentation

### Endpoint Details

- **URL:** `/me`
- **Method:** `GET`
- **Auth Required:** No
- **Permissions:** Public

### Success Response

- **Code:** 200 OK
- **Content-Type:** `application/json`
- **Content:** JSON object with status, user, timestamp, and fact fields

### External API Integration

**Cat Facts API:**
- **URL:** https://catfact.ninja/fact
- **Timeout:** 5 seconds
- **Fallback:** "Unable to fetch cat fact at this time"

## Author

**Etoro Umoren**
Backend Developer  
Email: torohkiss@gmail.com  
Stack: Python/Django
