# 📦 Zero Mile Delivery System – Backend (FastAPI)

This project is a backend API built using **FastAPI** and **SQLite**, designed to simulate a logistics company's last-mile parcel delivery system. It supports creating parcels, listing all parcels, and tracking parcels by a unique ID.

---

## 🚀 Features

- Create a new parcel with auto-generated tracking ID
- Get all saved parcels
- Get parcel details by tracking ID
- In-memory database (SQLite) for fast development
- Fully tested using Swagger Docs and Postman

---

## 🛠️ Tech Stack

- 💻 Python 3.10+
- ⚡ FastAPI – Web framework
- 🛢️ SQLite – Lightweight DB (file-based)
- 🔧 SQLAlchemy – ORM
- 🔁 Uvicorn – ASGI server
- 📬 Postman – API testing

---

## 📦 API Endpoints

| Method | Endpoint                 | Description                      |
| ------ | ------------------------ | -------------------------------- |
| POST   | `/parcels/`              | Create a new parcel              |
| GET    | `/parcels/`              | Get a list of all parcels        |
| GET    | `/parcels/{tracking_id}` | Get details of a specific parcel |

---

## Create a virtual environment

- python -m venv venv
- source venv/bin/activate # On Windows: venv\Scripts\activate

---

## Install dependencies:

- pip install -r requirements.txt

---

## Run the server

- uvicorn main:app --reload

---

## Open the API docs in browser:

- Swagger UI: http://localhost:8000/docs

---
