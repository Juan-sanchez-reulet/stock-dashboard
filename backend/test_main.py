from fastapi.testclient import TestClient
from main import app

# TestClient simula peticiones HTTP sin levantar servidor real
client = TestClient(app)

def test_endpoint_devuelve_200():
    response = client.get("/api/stock/AAPL")
    assert response.status_code == 200

def test_endpoint_devuelve_json():
    response = client.get("/api/stock/AAPL")
    datos = response.json()
    assert isinstance(datos, list)

def test_endpoint_con_period():
    response = client.get("/api/stock/AAPL?period=1mo")
    assert response.status_code == 200

def test_endpoint_ticker_distinto():
    response = client.get("/api/stock/TSLA")
    assert response.status_code == 200
    datos = response.json()
    assert isinstance(datos, list)

def test_estructura_respuesta():
    response = client.get("/api/stock/AAPL")
    datos = response.json()
    primer_elemento = datos[0]
    assert "fecha" in primer_elemento
    assert "precio" in primer_elemento
    assert "ma20" in primer_elemento
    assert "volumen" in primer_elemento
    