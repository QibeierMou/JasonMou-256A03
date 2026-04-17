# 🎪 Happy Camp Django Application

## 🌐 Live Application

Access the deployed app here:
👉 http://143.198.40.218:15317/

---

## 📌 Project Description

Happy Camp is a Django-based web application for managing events, positions, and user registrations.

Users can:

* Register and log in
* Browse and join events
* Select positions for events
* View reports based on their role

---

## 👥 User Roles

* **Admin**

  * Create, update, delete events
  * Manage positions
  * View all reports (users, events, registrants)

* **Member**

  * View events
  * Register/unregister
  * View reports (including event participants)

* **Volunteer**

  * Register for events
  * Choose positions
  * View personal event registrations

---

## 📊 Reports Implemented

* ✅ List of Users (Admin only)
* ✅ Upcoming Events (All roles)
* ✅ All Events (Admin only)
* ✅ My Registered Events (Member & Volunteer)
* ✅ Event + Registrants (Admin & Member)

All reports are sorted and clearly presented.

---

## 🚀 Run with Docker

### 1. Build Image

```bash
docker build -t happy_camp .
```

### 2. Run Container

```bash
docker run -p 15317:8000 happy_camp
```

### 3. Open in Browser

```
http://localhost:15317/
```

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 📊 Test Coverage

```bash
coverage run manage.py test
coverage report
```

✔ Current coverage: **68%** (above required 50%)

---

## ⚙️ CI/CD Pipeline

This project includes a GitHub Actions pipeline that:

* ✅ Runs automated Django tests
* ✅ Measures code coverage
* ✅ Uses SQLite for isolated test environment
* ✅ Builds Docker container if tests pass

Pipeline file location:

```
.github/workflows/ci.yml
```

---

## 🐳 Docker Notes

* Application runs inside Docker container

* Database is **NOT containerized** (as required)

* Uses:

  * SQLite for testing
  * External MySQL (optional for production)

* Default Django port inside container: **8000**

* Exposed port: **15317**

---

## ⚙️ Environment Variables

Create a `.env` file (NOT committed to Git):

Example:

```
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=3306
```

---

## 🛠 Tech Stack

* Django 6
* Python 3.12+
* SQLite (testing)
* MySQL (optional production)
* Docker
* GitHub Actions (CI/CD)

---

## 📁 Project Structure

```
accounts/      # User management
events/        # Event system
positions/     # Volunteer roles
reports/       # Reporting system
happy_camp/    # Main project settings
```

---

## ✅ Requirements Checklist

✔ Dockerized application
✔ Database NOT in Docker
✔ CI/CD pipeline implemented
✔ Test coverage ≥ 50%
✔ Multiple role-based reports
✔ Clean UI with CSS styling

---