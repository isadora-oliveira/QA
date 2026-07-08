def calcular_total_pedido(itens, valor_minimo):
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Pedido não atingiu o valor mínimo do restaurante")

    return total
