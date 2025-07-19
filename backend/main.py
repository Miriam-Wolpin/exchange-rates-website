from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP", "CNY", "ILS"]
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise Exception("API_KEY not found. Please define it in a .env file.")

@app.get("/currencies")
def get_supported_currencies():
    return {"currencies": SUPPORTED_CURRENCIES}

@app.get("/rates")
def get_exchange_rates(base: str):
    base = base.upper()
    if base not in SUPPORTED_CURRENCIES:
        raise HTTPException(status_code=400, detail="Currency not supported")

    url = f"https://api.exchangerate.host/live?access_key={API_KEY}&base={base}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Exchange rate fetch failed: {str(e)}")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to connect to exchange rate service")

    data = response.json()

    print(data)

    if not data.get("success") or "quotes" not in data:
        raise HTTPException(status_code=500, detail="Invalid data returned from exchange rate service")

    filtered_rates = {}
    for pair, rate in data["quotes"].items():
        # לדוגמה: "USDILS" → נחלץ את "ILS"
        target_currency = pair.replace(base, "")
        if target_currency in SUPPORTED_CURRENCIES and target_currency != base:
            filtered_rates[target_currency] = rate

    return {
        "base": base,
        "rates": filtered_rates
    }
