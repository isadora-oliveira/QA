# Aula 12 – BDD e Automação Orientada a Comportamento

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante:  
> - Isadora Oliveira

---

## 📁 Estrutura do Projeto

```
.
├── features/
│   └── filtro_categoria.feature
├── tests/
│   └── test_filtro_categoria.py
├── pages/
│   └── login_page.py
├── src/
│   └── pedido.py
└── pytest.ini
```

---

## 🔹 1. Fluxo escolhido

**Integrante:** Isadora Oliveira

| Item | Descrição |
|---|---|
| **Fluxo** | Filtro por categoria |
| **Objetivo** | Validar se o filtro de culinária funciona corretamente na página inicial |

**Descrição do fluxo:**

Na página inicial do LocalEats tem uma barra com botões de filtro: Todos, Italiana, Japonesa, Brasileira e Mexicana. Quando o usuário clica num desses botões, a lista de restaurantes atualiza e mostra só os que combinam com aquela culinária. Se clicar em Todos, volta a mostrar tudo.

Achei interessante esse fluxo porque é algo que qualquer usuário usa na hora de procurar um restaurante e dá pra testar vários comportamentos diferentes.

---

## 🔹 2. Cenários BDD

**Arquivo:** `features/filtro_categoria.feature`

```gherkin
Feature: Filtro por categoria

  Scenario: Filtrar por culinária Italiana
    Given que o usuário está na página inicial do LocalEats
    When clica no filtro de culinária Italiana
    Then a lista exibe apenas restaurantes com culinária Italiana

  Scenario: Filtro Todos mostra todos os restaurantes
    Given que o usuário aplicou o filtro Italiana na página inicial
    When clica no filtro Todos
    Then a lista exibe todos os 15 restaurantes disponíveis

  Scenario: Botão do filtro ativo fica destacado
    Given que o usuário está na página inicial do LocalEats
    When clica no filtro de culinária Japonesa
    Then o botão Japonesa aparece como selecionado
```

**Descrição dos cenários:**

| Cenário | Dado | Quando | Então |
|---|---|---|---|
| Filtrar por Italiana | usuário na página inicial | clica em Italiana | só aparece 3 restaurantes italianos |
| Filtro Todos | filtro Italiana aplicado | clica em Todos | volta a mostrar os 15 restaurantes |
| Botão ativo | usuário na página inicial | clica em Japonesa | botão Japonesa fica com classe `active` |

---

## 🔹 3. Automação com pytest-bdd

### Estrutura do projeto

```
.
├── features/
│   └── filtro_categoria.feature
└── tests/
    └── test_filtro_categoria.py
```

### Arquivo: `tests/test_filtro_categoria.py`

```python
import os
from pathlib import Path
from pytest_bdd import scenarios, given, when, then

# carrega os cenários do arquivo .feature
scenarios(str(Path(__file__).parent.parent / "features" / "filtro_categoria.feature"))

EMAIL = "isadora.qa.teste@localeats.com"
SENHA = "Teste@123"


def fazer_login(page):
    # faz login antes de acessar a página principal
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.wait_for_load_state("networkidle")
    page.fill("#loginEmail", EMAIL)
    page.fill("#loginPassword", SENHA)
    page.click("#loginForm button[type='submit']")
    page.wait_for_timeout(2000)


@given("que o usuário está na página inicial do LocalEats")
def acessar_pagina(page):
    fazer_login(page)


@given("que o usuário aplicou o filtro Italiana na página inicial")
def acessar_com_filtro(page):
    fazer_login(page)
    page.click('.filter-btn[data-cuisine="Italiana"]')
    page.wait_for_timeout(1000)


@when("clica no filtro de culinária Italiana")
def clicar_italiana(page):
    page.click('.filter-btn[data-cuisine="Italiana"]')
    page.wait_for_timeout(1000)


@when("clica no filtro Todos")
def clicar_todos(page):
    page.click('.filter-btn[data-cuisine=""]')
    page.wait_for_timeout(1000)


@when("clica no filtro de culinária Japonesa")
def clicar_japonesa(page):
    page.click('.filter-btn[data-cuisine="Japonesa"]')
    page.wait_for_timeout(1000)


@then("a lista exibe apenas restaurantes com culinária Italiana")
def validar_italiana(page):
    cards = page.locator(".rest-card")
    assert cards.count() == 3
    for i in range(3):
        assert "Italiana" in cards.nth(i).locator(".card-meta").inner_text()


@then("a lista exibe todos os 15 restaurantes disponíveis")
def validar_todos(page):
    assert page.locator(".rest-card").count() == 15


@then("o botão Japonesa aparece como selecionado")
def validar_botao_ativo(page):
    btn = page.locator('.filter-btn[data-cuisine="Japonesa"]')
    assert "active" in btn.get_attribute("class")
```

### Decisões tomadas

- Usei `Path(__file__)` pra montar o caminho do `.feature` de forma que funcione em qualquer máquina, sem precisar de caminho fixo.
- Criei a função `fazer_login()` pra não repetir o código de login em cada cenário.
- Os seletores usam `data-cuisine` porque o HTML do LocalEats usa esse atributo nos botões de filtro. É mais estável do que pegar pelo texto do botão.
- A verificação de cada card checa se o texto "Italiana" aparece dentro da `.card-meta`, que é onde fica o nome da culinária.

---

## 🔹 5. Execução dos testes

### Comando utilizado

```bash
pytest tests/test_filtro_categoria.py -v
```

### Log do console

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\isado\OneDrive\Área de Trabalho\QA
configfile: pytest.ini
plugins: base-url-2.1.0, bdd-8.1.0, playwright-0.8.0
collected 3 items

tests/test_filtro_categoria.py::test_filtrar_por_culinária_italiana PASSED [ 33%]
tests/test_filtro_categoria.py::test_filtro_todos_mostra_todos_os_restaurantes PASSED [ 66%]
tests/test_filtro_categoria.py::test_botão_do_filtro_ativo_fica_destacado PASSED [100%]

============================= 3 passed in 18.42s ==============================
```

| Cenários | Resultado |
|---|---|
| Total coletados | 3 |
| Passaram | 3 |
| Falharam | 0 |

---

## 🔹 6. Análise crítica

**O cenário escrito ficou compreensível?**

Sim. A estrutura Given-When-Then deixa bem claro o que o teste faz sem precisar ler o código. Dá pra entender só lendo o `.feature` que o teste vai clicar em Italiana e checar se a lista mudou.

**O teste automatizado ficou legível?**

Mais ou menos. O arquivo Python tem algumas partes que só quem conhece pytest-bdd entende, como o `scenarios()` e os decoradores `@given`, `@when`, `@then`. Mas o corpo de cada função ficou bem simples.

**O BDD ajudou a entender o comportamento?**

Sim. Antes de escrever o teste eu precisei pensar em como o filtro deveria se comportar do ponto de vista do usuário, não só tecnicamente. Isso ajudou a escolher melhor o que verificar.

**Quais dificuldades surgiram?**

A maior dificuldade foi entender o caminho do arquivo `.feature`. Tentei com caminho relativo e não funcionou de primeira, tive que usar `Path(__file__)` pra resolver. Também tive que instalar o `pytest-bdd` que não estava instalado ainda.

**Os seletores foram frágeis?**

Os seletores usam `data-cuisine`, que é um atributo do HTML e tende a ser mais estável que texto visível. Mas se o time de desenvolvimento mudar o nome do atributo, os testes quebram.

**O teste ficou dependente da interface?**

Sim. O teste abre o navegador e interage com a tela. Se o layout mudar ou se o filtro passar a funcionar de outro jeito, os testes precisariam ser atualizados.

**O cenário representa realmente uma regra de negócio?**

Sim. O filtro por categoria é uma funcionalidade principal do sistema que afeta diretamente a experiência do usuário ao procurar restaurantes.

**O que tornaria o teste mais robusto?**

Usar `data-testid` nos elementos HTML em vez de classes CSS ou atributos de negócio. Assim, mesmo que o visual mude, os seletores continuariam funcionando.

---

## 🔹 7. Reflexão no contexto do LocalEats

**BDD melhora a comunicação entre a equipe?**

Sim. O arquivo `.feature` pode ser lido por qualquer pessoa da equipe, mesmo sem saber programar. Isso facilita alinhar o que o sistema deve fazer antes de começar a desenvolver.

**Todo teste deve ser escrito em BDD?**

Não. BDD faz mais sentido para fluxos importantes do negócio, onde é preciso que desenvolvimento, QA e produto falem a mesma língua. Para testes unitários simples, como os da Aula 9, BDD seria exagero.

**Quando vale a pena usar BDD?**

Quando o comportamento do sistema precisa ser documentado de um jeito que todos entendam. No caso do LocalEats, os filtros de categoria são uma funcionalidade visível para o usuário final, então BDD faz sentido.

**O comportamento ficou mais claro?**

Sim. Escrever o cenário em Gherkin me fez pensar melhor nos casos de uso antes de automatizar. Percebo que é mais fácil discutir o que o sistema deve fazer quando está escrito assim do que lendo código Python.

**Como isso ajuda no projeto do grupo?**

Ajuda a documentar os comportamentos esperados do sistema de um jeito que qualquer integrante consegue entender e revisar, mesmo sem ter escrito o teste.

---

## ✅ Conclusão

Nessa atividade aprendi a:

- Escrever cenários BDD em Gherkin com a estrutura Given-When-Then
- Usar `pytest-bdd` para conectar os cenários com a automação
- Integrar `pytest-bdd` com `playwright` para testar comportamentos reais no navegador
- Organizar o projeto separando os cenários (`.feature`) da implementação (`.py`)

A parte mais importante foi perceber que BDD não é só sobre automação, é sobre comunicação. O arquivo `.feature` funciona como uma documentação viva do sistema que qualquer pessoa consegue entender.
