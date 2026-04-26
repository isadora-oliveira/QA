# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrantes do grupo:  
> - Isadora Oliveira

---

# 1. Plano de Testes

## 1.1 Objetivo
Descreva o objetivo do plano de testes.

> Exemplo: Validar as principais funcionalidades do sistema LocalEats, verificando se elas funcionam corretamente e se o comportamento do sistema está consistente durante o uso.

---

## 1.2 Escopo

### O que será testado
- Login
- Busca de restaurantes
- Visualização de restaurantes
- Sistema de favoritos
- Realização de pedidos

### O que NÃO será testado
- Performance avançada de infraestrutura
- Testes automatizados

---

## 1.3 Funcionalidades selecionadas
Liste as funcionalidades que serão foco dos testes:

- Login
- Busca de restaurantes
- Visualização de restaurantes
- Favoritos
- Pedido

---

## 1.4 Estratégia de Testes

Descreva como os testes serão realizados.

- Tipos de teste:
  - (X) Funcional
  - (X) Usabilidade
  - (X) Outros: Sistema


- Abordagem:
  > Exemplo: Testes manuais baseados em cenários reais de uso, simulando o comportamento do usuário no sistema LocalEats.

---

## 1.5 Responsáveis

Defina os papéis na equipe:

| Nome | Responsabilidade |
|------|----------------|
|  Isadora    |    Planejamento e execução dos testes          |
|  Isadora    |    Registro de resultados e análise            |

---

# 2. Casos de Teste


---

## CT-01 – Login com sucesso

**Pré-condição:**  
Usuário cadastrado

**Passos:**  
1. Acessar página de login
2. Inserir usuário válido
3. Inserir senha válida
4. Clicar em entrar

**Dados de entrada (se aplicável):**  
usuário e senha corretos

**Resultado esperado:**  
usuário acessa o sistema com sucesso

---

## CT-02 – Login com erro

**Pré-condição:**  
Usuário cadastrado

**Passos:**  
1. Inserir usuário correto
2. Inserir senha incorreta 
3. Clicar em entrar 

**Dados de entrada (se aplicável):**  
senha inválida

**Resultado esperado:**  
sistema bloqueia acesso e mostra erro
---

## CT-03 – Busca de restaurantes com sucesso

**Pré-condição:**  
usuário logado

**Passos:**  
1. Ir para busca
2. Inserir tipo de comida 
3. Clicar em buscar 

**Dados de entrada (se aplicável):**  
tipo de restaurante válido

**Resultado esperado:**  
lista de restaurantes aparece corretamente
---

## CT-04 – Busca sem resultado

**Pré-condição:**  
usuário logado

**Passos:**  
1. Ir para busca 
2. Inserir filtro inexistente 
3. Clicar em buscar 

**Dados de entrada (se aplicável):**  
termo inválido

**Resultado esperado:**  
sistema informa que não há resultados
---

## CT-05 – Favoritar restaurante

**Pré-condição:**  
usuário logado

**Passos:**  
1. Acessar restaurante
2. Clicar em “favoritar” 
3. Atualizar página 

**Dados de entrada (se aplicável):**  
restaurante selecionado

**Resultado esperado:**  
restaurante continua salvo nos favoritos
---

# 3. Execução dos Testes

Preencha a tabela com os resultados obtidos.

| ID     | Resultado (Passou/Falhou) | Evidência (descrição ou print) |
|--------|--------------------------|---------------------------------|
| CT-01  |      Passou              |  /artefatos/CT-01.png           |
| CT-02  |      Passou              |  /artefatos/CT-02.png           |
| CT-03  |      Falhou              |  /artefatos/CT-03.png           |
| CT-04  |      Passou              |  /artefatos/CT-04.png           |
| CT-05  |    Falhou parcialmente   |  /artefatos/CT-05.png           |

---

# 4. Análise dos Resultados
- Quantidade de testes executados: 5 
- Quantidade de testes que passaram: 3 
- Quantidade de testes que falharam: 2 

## Principais problemas encontrados
- Falha na busca de restaurantes
- Instabilidade no sistema de favoritos

---

# 5. Reflexão

Responda às questões abaixo:

- O plano de testes ajudou a organizar melhor o processo? Por quê? 
O plano de testes ajudou a organizar melhor o processo, porque definiu o que testar antes de executar.

- Algum problema só foi identificado durante a execução? Explique.
Alguns problemas, como favoritos não salvando e busca inconsistente, só apareceram durante a execução.

- O que o grupo melhoraria no processo de testes?
Eu melhoraria o processo incluindo mais testes de integração e testes em diferentes dispositivos, principalmente mobile.
---

## Conclusão

No geral, o sistema ainda apresenta inconsistências importantes, principalmente na busca e nos favoritos. A qualidade ainda não está estável o suficiente para uso confiável.
---

# 6. Conclusão Geral

Faça um resumo final:

O sistema LocalEats apresenta problemas de qualidade que impactam diretamente a experiência do usuário.

Pontos positivos:
- Interface simples
- Funcionalidades principais existem

Principais problemas:
- Falhas na busca
- Erros em favoritos

Impressão geral:
O sistema ainda precisa de melhorias significativas em testes e validação antes de ser considerado estável.