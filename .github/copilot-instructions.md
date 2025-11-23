# Copilot Instructions for companyf25v2

## Project Overview
A Django 5.1 web application for managing employees and their project assignments. The main task is to implement forms for adding employees and projects through the web interface.

## Architecture

### App Structure
- **compapp**: Main Django app with three views for employee management
  - URL namespace: `/comp/`
  - Database: SQLite (`db.sqlite3`)

### Data Model
**Employee** (models.py):
- Core fields: `name`, `date_of_birth`, `date_joined`, `phone_number`, `position`
- Relationships: One-to-many with Project via `projects` related name
- Display: Uses `__str__` to show "Name - Position"

**Project** (models.py):
- Linked to Employee via ForeignKey (`on_delete=CASCADE`)
- Fields: `name`, `start_date`, `end_date`, `amount` (decimal, optional)
- Used to track assignments assigned to each employee

## Critical Patterns & Workflows

### Date Filtering in Views
`employee_detail` view filters projects by active date range:
```python
projects = employee.projects.filter(start_date__lte=today, end_date__gte=today)
```
This shows only projects where the current date falls within `start_date` and `end_date`. When adding/editing projects, respect this business logic.

### URL Routing
- Views are accessible at: `/comp/employeeslist/`, `/comp/employee/<id>/`, `/comp/engineers/`
- Main project URL config includes app URLs via `include('compapp.urls')`
- Use Django's `{% url %}` template tag with named routes for links (see `employee_list.html`)

### Forms Convention
**EmployeeForm** (forms.py) is a ModelForm using Django's form generation:
- Field order in Meta.fields list determines form field order
- When creating ProjectForm (currently missing), follow this pattern
- Forms automatically validate based on model field types (DateField, DecimalField, etc.)

### Template Structure
Templates expect context variables directly (e.g., `{{ employee.name }}`, `{{ projects }}`):
- `employee_list.html`: Iterates over employees, sorted by name in view
- `employee_detail.html`: Shows employee details + related projects from context
- Use `{% empty %}` blocks for no-data states (see employee_list.html)

## Development Workflow

### Running the Project
```bash
python manage.py runserver
```
Accessible at `http://localhost:8000/comp/employeeslist/`

### Database Management
```bash
python manage.py makemigrations  # After model changes
python manage.py migrate          # Apply migrations
python manage.py createsuperuser  # Create admin user
```

Existing migrations tracked in `compapp/migrations/`:
- `0001_initial.py`: Employee model
- `0002_project.py`: Project model and FK relationship

### Admin Interface
Register models in `admin.py` to allow CRUD operations at `/admin/`. Currently no admin customization—models use default representation.

## Key Development Notes

1. **Missing Project Form**: The README mentions "create a form to add projects" but `ProjectForm` doesn't exist. When implementing, follow the `EmployeeForm` pattern as a ModelForm.

2. **Phone Number Validation**: Phone field is `CharField(max_length=8)`—no format validation. Consider if this should accept international formats or if validation is needed.

3. **Amount Field**: Project.amount allows null/blank—useful for projects without budgets. Preserve this in forms.

4. **Position Filtering**: The `employee_engineers` view filters by `position__icontains="engineer"`. This is case-insensitive substring matching; note for form validation if position field gets a choices list.

5. **Template Styling**: Minimal inline CSS in templates—consider if these should be extracted to static files for larger changes.

## File Reference Guide
- **Models**: `compapp/models.py` — Core data structures
- **Views**: `compapp/views.py` — Three views for employee filtering/display
- **Forms**: `compapp/forms.py` — EmployeeForm only; ProjectForm to be added
- **URLs**: `compapp/urls.py` → routes to views; `companyproj/urls.py` → includes app
- **Templates**: `compapp/templates/` — Two HTML files for list and detail views
