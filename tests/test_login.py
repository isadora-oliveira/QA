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
