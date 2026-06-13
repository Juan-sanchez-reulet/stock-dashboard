# Stock Dashboard

![Tests](https://github.com/Juan-sanchez-reulet/stock-dashboard/actions/workflows/test.yml/badge.svg)

Dashboard financiero en tiempo real construido con FastAPI y React.

## ¿Qué hace?

Conecta con Yahoo Finance, procesa los datos en el backend con pandas, y los visualiza en el frontend con Recharts. Soporta múltiples tickers y períodos, con media móvil de 20 días calculada en servidor.

## Stack

| Capa | Tecnología |
|------|-----------|
| Backend | FastAPI + pandas + yfinance |
| Frontend | React + Recharts |
| Testing | pytest + httpx |
| CI | GitHub Actions |
| Linting | ruff |

## Arquitectura
React (Vite) → GET /api/stock/{symbol}?period={period}
↓
FastAPI
↓
yfinance → pandas → JSON

## Decisiones técnicas

- **Lógica en el backend:** la media móvil se calcula en pandas, no en el frontend. El frontend solo renderiza.
- **Separación de responsabilidades:** `data.py` maneja datos, `main.py` maneja HTTP. Cambiar la fuente de datos no toca el servidor.
- **NaN → null:** los primeros 19 días no tienen MA20 por definición estadística. Se convierten explícitamente a `null` para que el JSON sea válido.

## Correr en local

**Backend**
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install fastapi uvicorn pandas yfinance
uvicorn main:app --reload
```

**Frontend**
```bash
cd frontend
npm install && npm run dev
```

**Tests**
```bash
cd backend && pytest -v
```

## API

`GET /api/stock/{symbol}?period={period}`

```json
[
  { "fecha": "01 Mar 2026", "precio": 170.73, "volumen": 54321000, "ma20": null },
  { "fecha": "04 Mar 2026", "precio": 169.00, "volumen": 48200000, "ma20": 171.50 }
]
```

Documentación interactiva disponible en `http://localhost:8000/docs`.
