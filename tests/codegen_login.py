# Esse é o código gerado pelo Playwright Codegen — sem nenhuma alteração
# Comando: playwright codegen https://local-eats-unisenac.vercel.app/static/login.html
#
# Problemas que percebi no código gerado:
# - O seletor input[type='email'] pega dois campos (login + cadastro) e quebra o teste
# - Tem um clique desnecessario antes de digitar o e-mail
# - Usa .press("Tab") em vez de ir direto pro próximo campo
# - Importou o 're' sem usar em lugar nenhum
# - Misturou a interação com a UI e as verificações no mesmo lugar

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
