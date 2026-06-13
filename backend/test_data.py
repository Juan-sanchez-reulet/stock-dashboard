from data import get_stock_data

def test_devuelve_lista():
    resultado = get_stock_data("AAPL", "3mo")
    assert isinstance(resultado, list)

def test_lista_no_vacia():
    resultado = get_stock_data("AAPL", "3mo")
    assert len(resultado) > 0

def test_campos_correctos():
    resultado = get_stock_data("AAPL", "3mo")
    primer_elemento = resultado[0]
    # Verificamos que los campos que espera Recharts existen
    assert "fecha" in primer_elemento
    assert "precio" in primer_elemento
    assert "volumen" in primer_elemento
    assert "ma20" in primer_elemento

def test_precio_es_numero():
    resultado = get_stock_data("AAPL", "3mo")
    for fila in resultado:
        assert isinstance(fila["precio"], float)

def test_ma20_null_primeros_dias():
    # Los primeros 19 días no tienen suficientes datos para MA20
    resultado = get_stock_data("AAPL", "1y")
    primeros = resultado[:19]
    for fila in primeros:
        assert fila["ma20"] is None

def test_ma20_tiene_valores_despues():
    # A partir del día 20 ma20 debe tener valores reales
    resultado = get_stock_data("AAPL", "1y")
    assert resultado[20]["ma20"] is not None

def test_ticker_invalido_no_rompe():
    # Un ticker que no existe debe devolver lista vacía, no explotar
    resultado = get_stock_data("TICKERINVALIDO123", "3mo")
    assert isinstance(resultado, list)