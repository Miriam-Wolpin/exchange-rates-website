// src/App.jsx
import React, { useState, useEffect } from "react";
import ExchangeTable from "./components/ExchangeTable";
import "./App.css";

const SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP", "CNY", "ILS"];

function App() {
  const [baseCurrency, setBaseCurrency] = useState("USD");
  const [rates, setRates] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchRates() {
      setLoading(true);
      try {
        const res = await fetch(`http://localhost:8000/rates?base=${baseCurrency}`);
        const data = await res.json();

        const formatted = Object.entries(data.rates).map(([target, rate]) => ({
          base: baseCurrency,
          target,
          rate,
        }));

        setRates(formatted);
      } catch (error) {
        console.error("Error fetching exchange rates:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchRates();
  }, [baseCurrency]);

  return (
    <div className="App">
      <h1>Exchange Rates</h1>

      <label>
        Choose base currency:{" "}
        <select
          value={baseCurrency}
          onChange={(e) => setBaseCurrency(e.target.value)}
        >
          {SUPPORTED_CURRENCIES.map((curr) => (
            <option key={curr} value={curr}>
              {curr}
            </option>
          ))}
        </select>
      </label>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <ExchangeTable data={rates} baseCurrency={baseCurrency} />
      )}
    </div>
  );
}

export default App;
