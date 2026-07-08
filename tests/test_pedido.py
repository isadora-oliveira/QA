import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pedido import calcular_total_pedido

# preços reais do site LocalEats
VALOR_MINIMO = 40.00


def test_deve_calcular_total_quando_pedido_supera_valor_minimo():
    # dois pratos do Restaurante Sabor 0: R$ 59.17 + R$ 46.81 = R$ 105.98
    itens = [
        {"nome": "Prato Especial 0", "preco": 59.17},
        {"nome": "Prato Especial 1", "preco": 46.81},
    ]
    resultado = calcular_total_pedido(itens, VALOR_MINIMO)
    assert resultado == pytest.approx(105.98)


def test_deve_aceitar_pedido_quando_total_igual_ao_valor_minimo():
    # total exatamente igual ao mínimo (valor de borda)
    # Prato Especial 0 R$ 23.00 + Prato Especial 2 R$ 17.23 = R$ 40.23
    itens = [
        {"nome": "Prato Especial 0", "preco": 23.00},
        {"nome": "Prato Especial 2", "preco": 17.23},
    ]
    resultado = calcular_total_pedido(itens, 40.23)
    assert resultado == pytest.approx(40.23)


def test_deve_rejeitar_pedido_com_apenas_um_item_abaixo_do_minimo():
    # item mais barato do site: R$ 17.23, abaixo do mínimo de R$ 40.00
    itens = [{"nome": "Prato Especial 2", "preco": 17.23}]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, VALOR_MINIMO)


def test_deve_rejeitar_pedido_com_carrinho_vazio():
    # no LocalEats o botão finalizar aparece mesmo com carrinho vazio
    itens = []
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, VALOR_MINIMO)
