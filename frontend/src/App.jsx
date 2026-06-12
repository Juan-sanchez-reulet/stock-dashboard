import { useState, useEffect } from "react"
import {
  LineChart, Line, XAxis, YAxis,
  CartesianGrid, Tooltip, ResponsiveContainer,
  BarChart, Bar
} from "recharts"

const TICKERS = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOGL"]
const PERIODOS = ["1mo", "3mo", "6mo", "1y"]

function App() {
  const [datos, setDatos] = useState([])
  const [cargando, setCargando] = useState(true)
  const [ticker, setTicker] = useState("AAPL")
  const [periodo, setPeriodo] = useState("3mo")

  useEffect(() => {
    setCargando(true)
    fetch(`http://localhost:8000/api/stock/${ticker}?period=${periodo}`)
      .then(res => res.json())
      .then(data => {
        setDatos(data)
        setCargando(false)
      })
  }, [ticker, periodo])  // se re-ejecuta cuando cambia ticker O periodo

  return (
    <div style={{ padding: "2rem", maxWidth: "1100px", margin: "0 auto" }}>

      {/* Selectores */}
      <div style={{ display: "flex", gap: "1rem", marginBottom: "1.5rem", alignItems: "center" }}>
        <h2 style={{ margin: 0 }}>{ticker}</h2>

        {TICKERS.map(t => (
          <button
            key={t}
            onClick={() => setTicker(t)}
            style={{
              padding: "6px 14px",
              borderRadius: "6px",
              border: "none",
              cursor: "pointer",
              background: ticker === t ? "#6366f1" : "#27272a",
              color: "#fff",
              fontWeight: ticker === t ? "600" : "400"
            }}
          >
            {t}
          </button>
        ))}

        <select
          value={periodo}
          onChange={e => setPeriodo(e.target.value)}
          style={{ marginLeft: "auto", padding: "6px 10px", borderRadius: "6px", background: "#27272a", color: "#fff", border: "none" }}
        >
          {PERIODOS.map(p => (
            <option key={p} value={p}>{p}</option>
          ))}
        </select>
      </div>

      {cargando ? <p>Cargando...</p> : <>

        {/* Gráfico precio + MA20 */}
        <p style={{ color: "#a1a1aa", marginBottom: "0.5rem" }}>Precio de cierre + Media móvil 20 días</p>
        <ResponsiveContainer width="100%" height={350}>
          <LineChart data={datos}>
            <CartesianGrid strokeDasharray="3 3" stroke="#3f3f46" />
            <XAxis dataKey="fecha" tick={{ fontSize: 10, fill: "#a1a1aa" }} />
            <YAxis domain={["auto", "auto"]} tick={{ fill: "#a1a1aa" }} />
            <Tooltip
              contentStyle={{ background: "#18181b", border: "1px solid #3f3f46" }}
            />
            <Line type="monotone" dataKey="precio" stroke="#6366f1" dot={false} strokeWidth={2} />
            <Line type="monotone" dataKey="ma20" stroke="#f59e0b" dot={false} strokeWidth={1.5} strokeDasharray="4 4" />
          </LineChart>
        </ResponsiveContainer>

        {/* Gráfico volumen */}
        <p style={{ color: "#a1a1aa", margin: "1.5rem 0 0.5rem" }}>Volumen</p>
        <ResponsiveContainer width="100%" height={150}>
          <BarChart data={datos}>
            <CartesianGrid strokeDasharray="3 3" stroke="#3f3f46" />
            <XAxis dataKey="fecha" tick={{ fontSize: 10, fill: "#a1a1aa" }} />
            <YAxis tick={{ fill: "#a1a1aa" }} />
            <Tooltip
              contentStyle={{ background: "#18181b", border: "1px solid #3f3f46" }}
            />
            <Bar dataKey="volumen" fill="#6366f1" opacity={0.7} />
          </BarChart>
        </ResponsiveContainer>

      </>}
    </div>
  )
}

export default App
