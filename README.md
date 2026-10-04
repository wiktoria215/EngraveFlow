# EngraveFlow – Jewelry & Workshop Order Management System

A dedicated Django-based web management system designed for artisanal jewelry and engraving workshops. The application tracks custom ring production, technical metallurgical parameters, and client records.

## Features

- **Relational Data Architecture:** Client entity management (`Klient`) linked via Foreign Key relations to custom workshop orders (`Obraczka`).
- **Complete CRUD Workflow:** Comprehensive operations to create, inspect, modify, and delete manufacturing orders.
- **Dynamic Query Filtering:** Search engine leveraging Django `Q` objects across raw material types and customer names.
- **Automated Parameter Auditing:** Tracking manufacturing tolerances (diameter, thickness, total weight, stone mounts).
- **Session Notifications:** User feedback integration via the Django messaging framework.

## Project Structure

```text
├── core/                   # Project configuration and routing
├── warsztat/               # Workshop management domain app
│   ├── models.py           # Domain models (Klient, Obraczka)
│   ├── views.py            # Business logic and query filtering
│   ├── forms.py            # ModelForm implementations
│   └── templates/warsztat/ # UI layout and order views
├── manage.py
├── requirements.txt
└── .gitignore

Tech Stack

    Backend: Python 3.11+, Django 5.x

    Database: SQLite (Development) / PostgreSQL compatible

    Frontend: Django Templates, HTML5, CSS

Setup & Local Execution
1. Clone the repository:
    Bash

git clone [https://github.com/wiktoria215/EngraveFlow.git](https://github.com/wiktoria215/EngraveFlow.git)
cd EngraveFlow

2. Create and activate a virtual environment:
    Bash

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

3. Install dependencies:
    Bash

pip install -r requirements.txt

4. Apply database migrations:
    Bash

python manage.py migrate

5. Run development server:
    Bash

python manage.py runserver