from cupom import desconto_valido

def test_rf01_limite_exato():
    assert desconto_valido(20) is True

def test_rf02_acima_limite():
    assert desconto_valido(21) is False

def test_rf03_percentual_zero():
    assert desconto_valido(0) is False