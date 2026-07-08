# Aula 10 – Testes Funcionais Automatizados

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante:  
> - Isadora Oliveira

---

## 📁 Estrutura do Projeto

```
.
├── pages/
│   └── login_page.py
├── src/
│   └── pedido.py
├── tests/
│   ├── codegen_login.py
│   ├── test_login.py
│   └── test_pedido.py
├── pytest.ini
└── README.md
```

---

## 🔹 1. Fluxo Funcional Escolhido

**Fluxo:** Login de usuário

**Arquivo da Page Object:** `/pages/login_page.py`  
**Arquivo de testes:** `/tests/test_login.py`  
**Código gerado pelo Codegen:** `/tests/codegen_login.py`

**Descrição:** Permite que o usuário faça login no sistema. Ele preenche e-mail e senha e, se estiver certo, vai pra tela principal.

**Por que esse fluxo?**

O login é a porta de entrada do sistema. Se ele quebrar, ninguém consegue usar nada. Além disso, no diagnóstico da Aula 3 identifiquei que o LocalEats não tem página de administração do usuário e vários fluxos dependem de estar logado, então faz sentido garantir que isso funciona automaticamente.

**Cenários testados:**

| Cenário | Entrada | Resultado esperado |
|---|---|---|
| Login válido | E-mail e senha corretos | Vai pra `index.html` + mostra "Olá, Isadora" |
| Senha incorreta | E-mail correto + senha errada | Permanece em `login.html` + mensagem "Invalid credentials" |
| Campos vazios | Nenhum dado preenchido | Formulário não submete, permanece em `login.html` |

---

## 🔹 2. Teste com Codegen

### Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/static/login.html
```

### Código gerado (`/tests/codegen_login.py`)

```python
import re
from playwright.sync_api import Page, expect


def test_login(page: Page) -> None:
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_text("Entrar").first.click()
    page.locator("input[type='email']").click()
    page.locator("input[type='email']").fill("teste@localeats.com")
    page.locator("input[type='email']").press("Tab")
    page.locator("input[type='password']").fill("123456")
    page.get_by_role("button", name="Entrar").click()
    page.wait_for_timeout(1000)
    expect(page.locator("body")).to_contain_text("Explorar")
```

### Observações sobre o código gerado

**O que o Codegen fez bem:**
- Capturou toda a sequência de ações em segundos, sem escrever nenhuma linha manualmente
- Gerou automaticamente a estrutura de teste com `from playwright.sync_api import Page, expect`
- Identificou os campos de e-mail e senha e registrou os valores preenchidos

**O que gerou problemas:**
- Usou `page.locator("input[type='email']")` — esse seletor pega dois campos ao mesmo tempo porque a página tem dois formulários (Entrar e Criar Conta), então o teste quebra na hora
- Adicionou um clique desnecessário antes de digitar o e-mail, que não precisava estar lá
- Usou `.press("Tab")` pra ir pro próximo campo em vez de ir direto
- Importou `re` sem usar em lugar nenhum
- Misturou tudo no mesmo lugar, sem separar o que é interação com a tela do que é verificação

---

## 🔹 3. Teste Automatizado com Pytest

O teste do Codegen **quebra** quando rodado porque o seletor pega dois campos ao mesmo tempo. O erro foi:

```
playwright._impl._errors.Error: Locator.fill: Error: strict mode violation:
locator("input[type='email']") resolved to 2 elements:
  1) <input id="loginEmail" .../>
  2) <input id="regEmail" .../>
```

Por isso o código do Codegen não dá pra usar direto sem revisar.

---

## 🔹 4. Refatoração com Page Object Model (POM)

### Por que refatorar?

O código do Codegen coloca tudo no mesmo lugar, misturando a parte de clicar nos campos com as verificações. Com o Page Object Model, a interação com a tela fica só na `LoginPage` e os testes ficam mais simples de ler e de mudar.

### Page Object (`/pages/login_page.py`)

```python
class LoginPage:
    URL = "https://local-eats-unisenac.vercel.app/static/login.html"

    def __init__(self, page):
        self.page = page
        # a página tem dois formulários então uso o ID pra não pegar o campo errado
        self.email = page.locator("#loginEmail")
        self.senha = page.locator("#loginPassword")
        self.botao_entrar = page.locator("#loginForm button[type='submit']")

    def acessar(self):
        self.page.goto(self.URL)

    def realizar_login(self, email, senha):
        self.email.fill(email)
        self.senha.fill(senha)
        self.botao_entrar.click()

    def clicar_entrar(self):
        self.botao_entrar.click()

    def mensagem_visivel(self, texto):
        return self.page.get_by_text(texto).is_visible()
```

### Teste refatorado (`/tests/test_login.py`)

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pages.login_page import LoginPage

# usuário cadastrado no LocalEats pra usar nos testes
EMAIL_VALIDO = "isadora.qa.teste@localeats.com"
SENHA_VALIDA = "Teste@123"


def test_login_com_credenciais_validas(page):
    # testa se o login funciona com e-mail e senha corretos
    login = LoginPage(page)
    login.acessar()
    login.realizar_login(EMAIL_VALIDO, SENHA_VALIDA)

    page.wait_for_url("**/index.html", timeout=5000)
    assert "index.html" in page.url
    assert login.mensagem_visivel("Olá, Isadora")


def test_login_com_senha_incorreta(page):
    # testa se o sistema bloqueia quando a senha está errada
    login = LoginPage(page)
    login.acessar()
    login.realizar_login(EMAIL_VALIDO, "senha_errada")

    page.wait_for_timeout(1000)
    assert "login.html" in page.url
    assert login.mensagem_visivel("Invalid credentials")


def test_login_com_campos_vazios(page):
    # testa se o sistema impede o login com campos vazios
    login = LoginPage(page)
    login.acessar()
    login.clicar_entrar()

    page.wait_for_timeout(500)
    assert "login.html" in page.url
```

### Melhorias realizadas

| Aspecto | Código Codegen | Após Refatoração |
|---|---|---|
| **Seletores** | `input[type='email']` — pega 2 campos e quebra o teste | `#loginEmail` — ID único, sem conflito |
| **Organização** | tudo misturado no mesmo lugar | UI separada na `LoginPage` |
| **Manutenção** | mudar seletor = alterar vários arquivos | mudar seletor = alterar só `login_page.py` |
| **Leitura** | `page.locator("...").fill(...)` repetido | `login.realizar_login(email, senha)` |
| **Ações extras** | `.first.click()` + `.press("Tab")` desnecessários | só o que precisa |
| **Import sobrando** | `import re` sem usar | removido |

---

## 🔹 5. Execução dos Testes

### Comando

```bash
pytest tests/test_login.py -v
```

### Evidência (saída real do pytest)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- python.exe
cachedir: .pytest_cache
rootdir: C:\Users\isado\OneDrive\Área de Trabalho\QA
configfile: pytest.ini
plugins: base-url-2.1.0, playwright-0.8.0
collected 3 items

tests/test_login.py::test_login_com_credenciais_validas[chromium]  PASSED [ 33%]
tests/test_login.py::test_login_com_senha_incorreta[chromium]      PASSED [ 66%]
tests/test_login.py::test_login_com_campos_vazios[chromium]        PASSED [100%]

============================= 3 passed in 13.22s ==============================
```

### Resumo

| Métrica | Resultado |
|---|---|
| Total de testes | 3 |
| Passaram | 3 ✅ |
| Falharam | 0 ❌ |
| Tempo de execução | 13,22s |
| Navegador | Chromium (headless) |

---

## 🔹 6. Análise Crítica dos Testes

**O teste quebrou em algum momento? Por quê?**

Sim. Na primeira versão o teste quebrou porque o Codegen gerou o seletor `input[type='email']`, que pega dois campos ao mesmo tempo (a página tem formulário de login e de cadastro juntos). O Playwright não deixa isso acontecer e dá erro. A solução foi usar `#loginEmail`, que é o ID específico do campo certo.

**Quais seletores foram mais difíceis?**

O botão "Entrar" foi o mais complicado. Tinha dois botões com esse nome na página e dois botões de submit. Tive que usar `#loginForm button[type='submit']` pra pegar exatamente o certo.

**O Codegen ajudou ou gerou problemas?**

Ajudou pra começar rápido, mas o código gerado não funcionou direto. Precisou de vários ajustes porque os seletores pegavam o campo errado. É útil pra explorar, mas não dá pra entregar o código sem revisar.

**O teste é confiável? Por quê?**

Mais ou menos. Os três testes passam sempre, mas o de login válido depende de um usuário cadastrado no site. Se o banco resetar, o teste quebra. Não é algo que eu consiga controlar no LocalEats.

**O que tornaria o teste mais robusto?**

Criar e deletar o usuário de teste automaticamente antes e depois dos testes. Também trocaria o `wait_for_timeout` por algo que espera o elemento aparecer de verdade.

**Quais são os riscos de manutenção?**

Se o LocalEats mudar os IDs dos campos ou o texto da mensagem de erro, os testes quebram. Com o POM pelo menos a correção é feita em um só lugar.

---

## 🔹 7. Reflexão no Contexto do LocalEats

**Testes automatizados substituem testes manuais?**

Não. Os testes automatizados são bons pra verificar fluxos que já funcionavam antes e garantir que continuam funcionando. Mas não enxergam problemas visuais, tipo a foto do restaurante não combinar com o tipo de comida, que só percebi na Aula 3 testando manualmente.

**Vale a pena automatizar todos os fluxos?**

Não, porque dá trabalho criar e manter os testes. Faria sentido focar nos fluxos mais importantes, como login, busca e finalizar pedido.

**Qual tipo de teste deve ser priorizado?**

Como vimos na pirâmide de testes: primeiro os unitários, depois os de integração, e por último os funcionais E2E. Os E2E são mais lentos e dão mais trabalho, então não dá pra ter muito.

**Como isso ajuda no projeto?**

Se o LocalEats mudar alguma coisa no login e quebrar, os testes automatizados já avisam antes de precisar testar manualmente. Isso seria bem útil porque o sistema muda bastante e tem muitos bugs desde o início.

---

🚀 **Conclusão**

Nessa atividade automatizei o fluxo de login do LocalEats usando Playwright + Pytest com Page Object Model. O Codegen ajudou a começar, mas o código gerado precisou de ajustes porque os seletores pegavam os campos errados. Depois da refatoração os 3 testes passaram sem problema. O mais importante foi entender que testes E2E quebram mais fácil que os unitários e precisam de cuidado com os seletores.
