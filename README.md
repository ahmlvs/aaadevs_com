# aaadevs_com

**aaadevs_com** is a website project built using **FastAPI**. The goal is to develop a scalable, high-performance web application with essential pages and features. Currently, the project includes the following components:

- **Home Page**: The main landing page of the website.
- **Static Files**:
  - `robots.txt`: Provides instructions for web crawlers.
  - `sitemap.xml`: Helps search engines index the site's pages.
- **Contact Form Handler**: Processes submissions from a contact form.

This project serves as a foundation for further development, including additional pages, APIs, and backend logic.

---

## How to Create and Activate a Virtual Environment

### Create the Virtual Environment

```bash
python3 -m venv env
```

### Activate the Virtual Environment

```bash
source env/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Deactivate the Virtual Environment (if needed)

```bash
deactivate
```

## Add Environment Variables (.env)

Create a .env file in the project root with the following variables:

```env
PRODUCTION=prod                                     # Use "prod" for production, "dev" for development
ALLOWED_ORIGINS=http://localhost,http://127.0.0.1   # For development
PRODUCTION_DB_URL=your_production_database_url      # Production Database URL string
```

## Run the Application

### Run Locally

```bash
python3 main.py
```

### Run in Production with Uvicorn

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```
