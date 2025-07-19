# Exchange Rates Website

A fullstack application displaying real-time currency exchange rates.

Built with:

- ⚛️ React (Vite)
- 🐍 FastAPI (Python)
- 🐳 Docker & Docker Compose
- 📊 TanStack Table
- 🔗 exchangerate.com API

---

## Features

- Select base currency from dropdown (USD, EUR, GBP, CNY, ILS)
- View exchange rates to other currencies in a sortable table
- Data fetched from real external API (exchangerate)
- Fully dockerized and ready to deploy

---

## Run the App

### With Docker

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

## Local Run

For manual setup without Docker, see HOW\_TO\_RUN.md.

---

Good luck!