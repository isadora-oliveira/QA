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
