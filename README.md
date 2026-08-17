# LMCX-25

Website for the Lower Mainland Cyclocross series — a Django-based site for managing cyclocross events and announcements.

## Prerequisites

- Python 3.10+ (check with `python --version`)
- PostgreSQL (required for local development)
- Git

## Local Setup

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd lmcx-25
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv site/venv

# Activate it (Windows)
site\venv\Scripts\activate

# Activate it (macOS/Linux)
source site/venv/bin/activate
```

### 3. Install Dependencies

```bash
cd site
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the `site/` directory with the following required variables:

```
SECRET_KEY=<your-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
PGDATABASE=lmcx_db
PGUSER=postgres
PGPASSWORD=<your-postgres-password>
PGHOST=localhost
PGPORT=5432
CLOUDINARY_CLOUD_NAME=<your-cloudinary-cloud-name>
CLOUDINARY_API_KEY=<your-cloudinary-api-key>
CLOUDINARY_API_SECRET=<your-cloudinary-api-secret>
```

**Note:** You can generate a `SECRET_KEY` using:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Database Setup

Ensure PostgreSQL is running, then apply migrations:

```bash
cd site
python manage.py migrate
```

Create a superuser for the Django admin:

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
cd site
python manage.py runserver
```

Visit http://localhost:8000 in your browser.

Access the admin panel at http://localhost:8000/admin/ with your superuser credentials.

## Common Commands

All commands run from the `site/` directory:

```bash
# Apply database migrations
python manage.py migrate

# Create new migrations from model changes
python manage.py makemigrations

# Django shell for interactive testing
python manage.py shell

# Collect static files (required before deployment)
python manage.py collectstatic --no-input

# Run tests
python manage.py test
```

## Project Structure

```
site/
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .env               # Environment configuration (create this)
├── events/            # Django app for races, practices, clinics
│   ├── models.py      # Event model
│   ├── views/         # List and detail views
│   └── urls.py
├── announcements/     # Django app for news/announcements
│   ├── models.py      # Announcement model
│   ├── views/         # List and detail views
│   └── urls.py
├── lmcx/              # Main project settings
│   ├── settings.py    # Django configuration
│   ├── urls.py        # Root URL configuration
│   └── views.py       # Custom 404/500 handlers
├── static/            # CSS, fonts, images
├── media/             # Uploaded images (Cloudinary in production)
└── templates/         # HTML templates
```

## Key Technologies

- **Django** — Web framework
- **PostgreSQL** — Database
- **TinyMCE** — Rich text editor for event/announcement descriptions
- **Cloudinary** — Image hosting and CDN
- **WhiteNoise** — Static file serving

## Debugging

VS Code includes a "Python Debugger: Django" launch configuration. Press F5 to start debugging the development server.

## Deployment

The project uses Railway for deployment. See `Procfile` for the deployment configuration.

