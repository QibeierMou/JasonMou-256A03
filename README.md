
# Happy Camp Django Application

## 📌 Project Description
This is a Django web application for managing events, positions, and user registrations.  
Users can register for events, select volunteer positions, and view reports based on their role.

---

## 🚀 How to Run the Application (Docker)

### Build Docker Image
```bash
docker build -t happy_camp .


---

## 2. 🧪 How to Run Tests (VERY IMPORTANT for marking)

Add:

```md
## 🧪 Run Tests

```bash
python manage.py test


---

## 3. 📊 Run Coverage (REQUIRED BY YOUR REQUIREMENT)

Add:

```md
## 📊 Test Coverage

```bash
coverage run manage.py test
coverage report


---

## 4. ⚙️ CI/CD Pipeline Info (REQUIRED MARKING POINT)

Add:

```md
## ⚙️ CI/CD Pipeline

This project includes a GitHub Actions CI/CD pipeline that:

- Runs automated tests
- Checks code coverage
- Builds Docker image if tests pass
- Ensures minimum 50% test coverage requirement

## 🐳 Docker Notes

- Application runs inside Docker container
- Database is NOT containerized (runs separately or locally)
- Default port: 8000

## 👥 User Roles

- Admin: Manage events, positions, and reports
- Member: Join and update events
- Volunteer: Register for events and choose positions

## 🛠 Tech Stack

- Django 6
- Python 3.12+
- SQLite (testing)
- MySQL (production optional)
- Docker
- GitHub Actions (CI/CD)