# Aula 9 – Testes Unitários Automatizados e TDD

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante:  
> - Isadora Oliveira

---

## � Estrutura do Projeto

```
.
├── src/
│   └── pedido.py
└── tests/
    └── test_pedido.py
```

---

## 🔹 1. Funcionalidade Escolhida

**Arquivo da implementação:** `/src/pedido.py`  
**Arquivo de testes:** `/tests/test_pedido.py`

**Descrição:** Soma os preços dos itens do carrinho e verifica se o total é maior ou igual ao valor mínimo do restaurante.

**Por que essa funcionalidade?**

Ao abrir qualquer restaurante no [LocalEats](https://local-eats-unisenac.vercel.app/), o botão **"Finalizar Pedido"** aparece mesmo com o carrinho vazio (Total: R$ 0,00). Isso é o problema que identifiquei na Aula 3: dá pra mandar pedido sem nenhuma validação e os pedidos ficam presos em *"pending"*.

Qualquer app de delivery tipo iFood tem um valor mínimo. No LocalEats isso não existe. Criar esse teste garante que, se alguém implementar essa regra, ela vai funcionar certo.

**Dados reais do site**:

| Restaurante | Tipo | Faixa | Item | Preço |
|---|---|---|---|---|
| Restaurante Sabor 0 | Italiana – Zona Sul | $$$$ | Prato Especial 0 | R$ 59,17 |
| Restaurante Sabor 0 | Italiana – Zona Sul | $$$$ | Prato Especial 1 | R$ 46,81 |
| Restaurante Sabor 3 | Italiana – Zona Norte | $ | Prato Especial 0 | R$ 23,00 |
| Restaurante Sabor 7 | Italiana – Centro | $ | Prato Especial 2 | R$ 17,23 |

**Valor mínimo adotado:** R$ 40,00 (igual ao iFood)

**Regras:**

| Regra | Detalhe |
|---|---|
| `total = soma dos preços` | Cada item tem `nome` e `preco` |
| `total < valor_minimo` | Dá erro |
| `total >= valor_minimo` | Retorna o total |

---

## 🔹 2. Testes Unitários

> Ferramenta utilizada: **pytest** (Python 3.12)  
> Arquivo: `tests/test_pedido.py`

---

### Teste 1 — Happy Path ✅

**Nome descritivo:**  
`test_deve_calcular_total_quando_pedido_supera_valor_minimo`

**Cenário testado:**  
Dois pratos do Restaurante Sabor 0. Total fica bem acima do mínimo, deve passar.

**Dados de entrada:**
- `itens = [{"nome": "Prato Especial 0", "preco": 59.17}, {"nome": "Prato Especial 1", "preco": 46.81}]`
- `valor_minimo = 40.00`

**Resultado esperado:**  
Retornar `105.98` sem dar erro.

```python
def test_deve_calcular_total_quando_pedido_supera_valor_minimo():
    # dois pratos do Restaurante Sabor 0: R$ 59.17 + R$ 46.81 = R$ 105.98
    itens = [
        {"nome": "Prato Especial 0", "preco": 59.17},
        {"nome": "Prato Especial 1", "preco": 46.81},
    ]
    valor_minimo = 40.00
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == pytest.approx(105.98)
```

---

### Teste 2 — Happy Path / Borda ✅

**Nome descritivo:**  
`test_deve_aceitar_pedido_quando_total_igual_ao_valor_minimo`

**Cenário testado:**  
Total exatamente igual ao mínimo. Tem que aceitar porque a regra é `>=`.

**Dados de entrada:**
- Prato Especial 0 do **Restaurante Sabor 3** (R$ 23,00) + Prato Especial 2 do **Restaurante Sabor 7** (R$ 17,23) = R$ 40,23
- `valor_minimo = 40.23` (exatamente igual ao total)

**Resultado esperado:**  
Retornar `40.23` sem dar erro.

```python
def test_deve_aceitar_pedido_quando_total_igual_ao_valor_minimo():
    # total exatamente igual ao mínimo (valor de borda)
    # Prato Especial 0 R$ 23.00 + Prato Especial 2 R$ 17.23 = R$ 40.23
    itens = [
        {"nome": "Prato Especial 0", "preco": 23.00},
        {"nome": "Prato Especial 2", "preco": 17.23},
    ]
    resultado = calcular_total_pedido(itens, 40.23)
    assert resultado == pytest.approx(40.23)
```

---

### Teste 3 — Cenário de Erro ❌

**Nome descritivo:**  
`test_deve_rejeitar_pedido_com_apenas_um_item_abaixo_do_minimo`

**Cenário testado:**  
Só um item no carrinho e ele custa menos que o mínimo. Deve dar erro.

**Dados de entrada:**
- `itens = [{"nome": "Prato Especial 2", "preco": 17.23}]`
- `valor_minimo = 40.00`

**Resultado esperado:**  
Dar erro (R$ 17,23 < R$ 40,00).

```python
def test_deve_rejeitar_pedido_com_apenas_um_item_abaixo_do_minimo():
    # item mais barato do site: R$ 17.23, abaixo do mínimo de R$ 40.00
    itens = [{"nome": "Prato Especial 2", "preco": 17.23}]
    valor_minimo = 40.00
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)
```

---

### Teste 4 — Borda / Erro ❌

**Nome descritivo:**  
`test_deve_rejeitar_pedido_com_carrinho_vazio`

**Cenário testado:**  
Carrinho vazio. No LocalEats o botão "Finalizar" aparece mesmo assim, mas devia dar erro.

**Dados de entrada:**
- `itens = []`
- `valor_minimo = 40.00`

**Resultado esperado:**  
Dar erro (R$ 0,00 < R$ 40,00).

```python
def test_deve_rejeitar_pedido_com_carrinho_vazio():
    # no LocalEats o botão finalizar aparece mesmo com carrinho vazio
    itens = []
    valor_minimo = 40.00
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)
```

---

## 🔹 3. Aplicação do TDD

### 🔴 Red — Escrevendo o teste antes do código

O primeiro passo é criar o arquivo de testes **antes de escrever qualquer código**. O `src/pedido.py` ainda não existe nesse momento.

```python
# tests/test_pedido.py — criado ANTES de src/pedido.py

import pytest
from pedido import calcular_total_pedido  # ← módulo ainda inexistente

def test_deve_calcular_total_quando_pedido_supera_valor_minimo():
    # Restaurante Sabor 0 — dados reais do LocalEats
    itens = [
        {"nome": "Prato Especial 0", "preco": 59.17},
        {"nome": "Prato Especial 1", "preco": 46.81},
    ]
    resultado = calcular_total_pedido(itens, 40.00)
    assert resultado == pytest.approx(105.98)
```

**O que apareceu no terminal (sem o `src/pedido.py`):**

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1
collected 0 items / 1 error

=================================== ERRORS ====================================
___________________ ERROR collecting tests/test_pedido.py ___________________
ImportError while importing test module 'tests/test_pedido.py'.
tests/test_pedido.py:6: in <module>
    from pedido import calcular_total_pedido
E   ModuleNotFoundError: No module named 'pedido'
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.28s ==============================
```

> ✅ O teste falhou como esperado. O código ainda não existe, então faz sentido.

---

### 🟢 Green — Implementando o mínimo necessário

Com o teste falhando, escrevo o mínimo de código possível pra ele passar.

```python
# src/pedido.py — versão mínima (Green)

def calcular_total_pedido(itens, valor_minimo):
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total
```

**Depois de criar o `src/pedido.py` mínimo:**

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1
collected 4 items

tests/test_pedido.py::test_deve_calcular_total_quando_pedido_supera_valor_minimo          PASSED
tests/test_pedido.py::test_deve_aceitar_pedido_quando_total_igual_ao_valor_minimo         PASSED
tests/test_pedido.py::test_deve_rejeitar_pedido_com_apenas_um_item_abaixo_do_minimo      PASSED
tests/test_pedido.py::test_deve_rejeitar_pedido_com_carrinho_vazio                       PASSED

============================== 4 passed in 0.07s ==============================
```

> ✅ Todos passaram. O código mínimo já foi suficiente.

---

### 🔵 Refactor — Melhorando o código

Com os testes passando, melhoro o código sem medo de quebrar nada.

```python
# src/pedido.py — versão refatorada (Refactor)

def calcular_total_pedido(itens, valor_minimo):
    # soma os itens e verifica se atingiu o mínimo
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Pedido não atingiu o valor mínimo do restaurante")

    return total
```

**Depois de melhorar o código:**

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- python.exe
cachedir: .pytest_cache
rootdir: C:\Users\isado\OneDrive\Área de Trabalho\QA
collected 4 items

tests/test_pedido.py::test_deve_calcular_total_quando_pedido_supera_valor_minimo         PASSED [ 25%]
tests/test_pedido.py::test_deve_aceitar_pedido_quando_total_igual_ao_valor_minimo        PASSED [ 50%]
tests/test_pedido.py::test_deve_rejeitar_pedido_com_apenas_um_item_abaixo_do_minimo     PASSED [ 75%]
tests/test_pedido.py::test_deve_rejeitar_pedido_com_carrinho_vazio                      PASSED [100%]

============================== 4 passed in 0.08s ==============================
```

> ✅ Continuaram passando. O código mudou mas o resultado é o mesmo.

---

## 🔹 4. Refatoração

### Comparação: Green → Refactor

| Aspecto | Versão Green (mínima) | Versão Refatorada |
|---|---|---|
| **Comentario** | Sem nenhum | Linha explicando o que a função faz |
| **Mensagem de erro** | Genérica: `"Valor mínimo do pedido não atingido"` | Mesma, mas o código ficou mais organizado |

### Justificativa das melhorias

A versão Green foi escrita só pra fazer os testes passarem, sem se preocupar com organização. Na refatoração adicionei um comentário explicando o que a função faz, o que ajuda quem for ler o código depois.

A mensagem de erro ficou simples e direta. Em um sistema maior daria pra melhorar mais, mas pra esse caso já está claro o suficiente.

> Os testes garantiram que nada quebrou durante a refatoração.

---

## 🔹 5. Execução dos Testes

### Arquivo completo: `tests/test_pedido.py`

```python
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
```

### Evidência de execução (saída real do pytest)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- python.exe
cachedir: .pytest_cache
rootdir: C:\Users\isado\OneDrive\Área de Trabalho\QA
collected 4 items

tests/test_pedido.py::test_deve_calcular_total_quando_pedido_supera_valor_minimo         PASSED [ 25%]
tests/test_pedido.py::test_deve_aceitar_pedido_quando_total_igual_ao_valor_minimo        PASSED [ 50%]
tests/test_pedido.py::test_deve_rejeitar_pedido_com_apenas_um_item_abaixo_do_minimo     PASSED [ 75%]
tests/test_pedido.py::test_deve_rejeitar_pedido_com_carrinho_vazio                      PASSED [100%]

============================== 4 passed in 0.08s ==============================
```

### Resumo

| Métrica | Resultado |
|---|---|
| Total de testes | 4 |
| Passaram | 4 ✅ |
| Falharam | 0 ❌ |
| Cenários testados | funcionando, limite, erro, carrinho vazio |

---

## 🔹 6. Reflexão no Contexto do LocalEats

**Foi difícil escrever testes antes do código?**

Sim, foi estranho no começo. A vontade é sempre de escrever o código primeiro e só depois ver se funciona. Mas escrever o teste antes força a pensar o que a função precisa fazer antes de começar a implementar.

**O TDD ajudou no desenvolvimento?**

Sim. Saber que o teste já estava lá me ajudou a não ficar com dúvida se o código estava certo ou não. Quando os testes passaram, eu sabia que estava funcionando.

**Os testes aumentaram a confiança no código?**

Sim. Se eu mudar alguma coisa na função, os testes avisam na hora se quebrou alguma coisa. Isso é bem melhor do que ficar testando manualmente toda vez.

**O que melhoraria?**

Adicionaria mais cenários, como testar o que acontece se passar um preço negativo ou um item sem o campo `preco`. Também testaria o fluxo inteiro do pedido e não só o cálculo.

**Como isso ajuda no projeto?**

No LocalEats os pedidos ficam presos em "pending" e dá pra finalizar sem nenhuma validação. Com os testes automatizados, qualquer alteração no código que quebre essa regra seria detectada antes de chegar pro usuário.

---

🚀 **Conclusão**

Nessa atividade apliquei o TDD na prática: escrevi o teste antes (Red), implementei o mínimo pra passar (Green) e depois melhorei o código (Refactor). Foi interessante ver como os testes dão segurança pra mexer no código sem medo de quebrar. No contexto do LocalEats, onde o sistema tem vários problemas de validação, usar testes automatizados ajudaria muito a manter a qualidade.
