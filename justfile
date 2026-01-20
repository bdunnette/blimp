# Justfile for BLIMP

# Linux/MacOS shell
set shell := ["bash", "-c"]
# Windows PowerShell shell
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

# Run the development server
dev:
    uv run python manage.py runserver

# Run migrations
migrate:
    uv run python manage.py migrate

# Create a superuser
superuser:
    uv run python manage.py createsuperuser

# Run Huey worker
huey:
    uv run python manage.py run_huey

# Run tests
test:
    uv run pytest

# Open Django shell
shell:
    uv run python manage.py shell

# Linting and formatting
lint:
    uv run ruff check .
    uv run ruff format .

# Run a manage.py command
manage *args:
    uv run python manage.py {{args}}
