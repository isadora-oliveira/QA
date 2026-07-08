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
