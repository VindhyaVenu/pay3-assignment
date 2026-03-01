
This project implements a REST API deployed on AWS EC2, connected to an AWS RDS PostgreSQL database. The application is containerized and designed following secure configuration best practices.

The API:
- Creates entries in a PostgreSQL database
- Retrieves all stored entries
- Requires Authorization header: `pay3-assignment`

---

## 🏗 Tech Stack

- FastAPI (Python)
- PostgreSQL (AWS RDS)
- AWS EC2
- Docker (for containerization)
- GitHub (source control)

---

## 🌍 Live Deployment URL

```
http://13.201.48.175:8000/docs
```

Swagger UI is available at the above URL.

---

## 🔐 Authorization

All endpoints require:

```
Authorization: Bearer pay3-assignment
```

If the header is missing or incorrect, the API returns `401 Unauthorized`.

---

## ⚙️ Environment Variables

Before running the application, set the following environment variables:

```bash
export DB_HOST=database-1.chswc4ickuyj.ap-south-1.rds.amazonaws.com
export DB_PORT=5432
export DB_NAME=postgres
export DB_USER=postgres
export DB_PASSWORD=<your_master_password>
```

⚠️ Credentials are NOT hardcoded in source code.

---

## ▶️ Run Application Locally

1. Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 🧪 API Endpoints

### 1️⃣ Create Item

```bash
curl -X POST "http://13.201.48.175:8000/items?name=TestItem1" \
-H "Authorization: Bearer pay3-assignment"
```

Response:

```json
{
  "message": "Item created"
}
```

---

### 2️⃣ Get All Items

```bash
curl -X GET "http://13.201.48.175:8000/items" \
-H "Authorization: Bearer pay3-assignment"
```

Response:

```json
[
  {
    "id": 1,
    "name": "TestItem1"
  }
]
```

---

## 🗄 Database

- AWS RDS PostgreSQL (Free Tier)
- Database and table created dynamically via SQLAlchemy
- EC2 allowed access via Security Group rules


## 🔒 Security

- Database credentials stored as environment variables
- No secrets committed to GitHub
- Authorization header required for all endpoints

## 🚀 Deployment Architecture

Client → EC2 (FastAPI) → RDS PostgreSQL

