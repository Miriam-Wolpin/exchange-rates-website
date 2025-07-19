# HOW TO RUN – Exchange Rates Website

This guide explains how to run the fullstack app both locally and using Docker.

---

## Option 1: Run Locally (without Docker)

### Prerequisites:
- Python 3.10+ installed
- Node.js (v18+ recommended)
- Git

---

### 1. Clone the project

```bash
git clone https://github.com/YOUR_USERNAME/exchange-rates-website.git
cd exchange-rates-website
```

---

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/Scripts/activate       # On Windows
# or: source venv/bin/activate     # On macOS/Linux

pip install -r requirements.txt
```
To use the API, you must create an account at [https://exchangerate.host](https://exchangerate.host/) and generate a free API key.
  
Then, add a `.env` file under `backend/` with:
 ```
API_KEY=your_exchangerate_api_key
 ```

Then run the server:
```bash
uvicorn main:app --reload
```

Accessible at: [http://localhost:8000](http://localhost:8000)

---

### 3. Frontend Setup (React + Vite)

Open a new terminal window:

```bash
cd frontend
npm install
npm run dev
```

Visit: [http://localhost:5173](http://localhost:5173)

---

## Option 2: Run with Docker (Recommended)

### Requirements:
- Docker Desktop installed and running
- WSL 2 (updated – run `wsl --update` if needed)

---

### Run both apps

```bash
docker compose up --build
```

- Frontend: [http://localhost:5173](http://localhost:5173)
- Backend: [http://localhost:8000](http://localhost:8000)

To use the API, you must create an account at [https://exchangerate.host](https://exchangerate.host/) and generate a free API key.
  
Then, add a `.env` file under `backend/` with:
 ```
API_KEY=your_exchangerate_api_key
 ```

---

Enjoy this app!

