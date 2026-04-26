# Diagnóstico de Qualidade – Startup Local Eats

> Disciplina: Qualidade de Software  
> Aula 3 – Papéis, Responsabilidades e Práticas de QA  
> Equipe: 1SÓ 
> Integrantes: Isadora Oliveira
---

# 1. Diagnóstico da Situação Atual


## 1.1 Papéis atuais identificados

- Desenvolvedor
- Gerente de produto
- Possível analista de sistemas (não formalizado)
- Não tem um papel claro de QA


## 1.2 Quem é responsável pela qualidade hoje?

Descreva como vocês acreditam que a qualidade está sendo tratada atualmente.

> Resposta: Parece que a qualidade fica principalmente na responsabilidade dos desenvolvedores, sem um processo definido ou uma pessoa específica cuidando disso.

---

## 1.3 Problemas identificados

Liste os principais problemas relacionados à falta de organização da qualidade.

- Não possui app para iOS
- Mesma descrição para todos os restaurantes
- Fotos dos restaurantes não condizem com o tipo de comida vendida
- Filtro de busca não funciona corretamente
- Necessidade de clicar no botão “buscar” (Enter não funciona)
- Após busca, precisa apagar e buscar novamente para atualizar resultados
- Não possui filtro de ordenação dos restaurantes
- Não existe página de administração do usuário
- Botão “Favoritar” não mantém o estado após atualizar a página
- Botões “Cardápio” e “Avaliações” não funcionam
- Não possui endereço, telefone ou contato dos restaurantes
- Pedido é enviado sem confirmação de forma de pagamento
- Pedido não sai do status “pending”
- Página “orders.html” apresenta ID no lugar do nome do restaurante
- Itens do pedido aparecem como ID ao invés do nome
- Não é possível realizar pagamento pelo site
- Tela de pedido sobrepõe os itens no navegador do celular
- Não possui SAC (atendimento ao cliente)

---

## 1.4 Impactos desses problemas

Explique quais são as consequências desses problemas para o sistema e para os usuários.

> Resposta: Esses problemas impactam diretamente a experiência do usuário, porque dificultam o uso da plataforma e deixam o sistema pouco confiável. A falta de funcionamento correto de funções como busca, pedidos e pagamentos pode fazer o usuário desistir de usar o serviço.

Além disso erro como status incorreto gera problemas também para os restaurantes, que podem ter prejuízos e retrabalho. No geral isso afeta a credibilidade da plataforma e pode prejudicar o crescimento da startup.

---

## 1.5 A qualidade é responsabilidade de quem?

Explique se a qualidade deve ser responsabilidade de uma pessoa ou de toda a equipe.

> Resposta: Na minha opinião, a qualidade deve ser responsabilidade de toda a equipe, não apenas de uma pessoa. Mesmo com um profissional de QA, todos devem se preocupar com a qualidade desde o início do desenvolvimento, para evitar que erros cheguem até o usuário final.

---

# 2. Papéis da Equipe Propostos

Definam quais papéis deveriam existir na equipe da Local Eats.

---

## 2.1 Lista de papéis

- Desenvolvedor
- Analista de Sistemas
- QA / Analista de Qualidade
- DevOps
- Gerente de Produto

---

## 2.2 Descrição dos papéis

Preencha a tabela abaixo:

| Papel | Responsabilidades principais | Relação com a qualidade |
| Desenvolvedor | Criar e corrigir funcionalidades do sistema | Ajuda na qualidade ao evitar e corrigir erros no código |
| Analista de Sistemas | Definir regras e requisitos do sistema | Evita erros de entendimento e funcionalidades mal implementadas |
| QA / Analista de Qualidade | Testar o sistema e identificar problemas  | Garante que as funcionalidades funcionem corretamente antes de ir para produção |
| DevOps | Fazer deploy e manter o sistema funcionando | Ajuda a garantir estabilidade e evitar falhas em produção |
| Gerente de Produto | Organizar prioridades e funcionalidades | Garante que o sistema atenda às necessidades do usuário |

---

# 3. Práticas de QA Sugeridas

Sugira práticas que a startup pode adotar para melhorar a qualidade.

---

## 3.1 Lista de práticas

- Testes manuais das funcionalidades principais
- Registro e acompanhamento de bugs
- Testes em diferentes dispositivos (web e mobile)
- Revisão das funcionalidades antes do deploy
- Testes de usabilidade com foco na experiência do usuário

---

## 3.2 Explicação das práticas

Explique brevemente cada prática sugerida.

### Prática 1: Testes manuais
> Descrição: Testar o sistema antes de liberar para os usuários, verificando funções como busca, pedidos e favoritos.

### Prática 2: Registro de bugs
> Descrição: Anotar todos os erros encontrados para acompanhar e corrigir depois.

### Prática 3: Testes em diferentes dispositivos
> Descrição: Verificar se o sistema funciona bem em celular e computador, já que foram encontrados problemas no mobile.

### Prática 4: Revisão antes do deploy
> Descrição: Conferir se tudo está funcionando corretamente antes de colocar no ar.

### Prática 5: Testes de usabilidade
> Descrição: Avaliar se o sistema é fácil de usar e se o usuário consegue realizar tarefas sem dificuldade.
---

# 4. Anúncios de Contratação

A startup decidiu contratar novos profissionais. Crie anúncios de vagas.

> Mínimo: 2 vagas

---

## 4.1 Vaga 1 – [Título da vaga]

### Descrição da vaga
> A Local Eats está buscando um profissional de QA para ajudar a melhorar a qualidade do sistema e reduzir falhas em produção.

### Responsabilidades
- Testar funcionalidades do sistema
- Identificar e registrar bugs
- Validar entregas antes do lançamento
- Trabalhar junto com desenvolvedores

### Requisitos obrigatórios
- Conhecimento básico em testes de software
- Atenção a detalhes
- Boa comunicação

### Requisitos desejáveis
- Experiência com testes web e mobile
- Conhecimento em ferramentas de bug tracking

### Certificações desejáveis
- ISTQB (básico)

---

## 4.2 Vaga 2 – [Título da vaga]

### Descrição da vaga
> A Local Eats busca um desenvolvedor para atuar na criação e melhoria da plataforma.

### Responsabilidades
- Desenvolver novas funcionalidades
- Corrigir erros do sistema
- Trabalhar junto com QA
- Garantir funcionamento das funções principais

### Requisitos obrigatórios
- Conhecimento em programação
- Lógica de programação
- Noção de desenvolvimento web

### Requisitos desejáveis
- Experiência com sistemas web e mobile
- Conhecimento em Git

### Certificações desejáveis
- Cursos na área de desenvolvimento de software
---

# 5. Conclusão da Equipe

Descreva brevemente:

- O que a equipe aprendeu com a atividade
- Principais dificuldades encontradas
- Principais melhorias propostas para a startup

> Resposta: Com essa atividade, eu consegui entender melhor como a falta de organização na qualidade pode gerar vários problemas em um sistema real. Percebi que muitos erros acontecem por falta de testes e de responsabilidades bem definidas.

A principal dificuldade foi relacionar os problemas do sistema com os atributos de qualidade corretos.

Como melhoria, acredito que a startup deveria ter um QA dedicado, mais testes antes de liberar o sistema e uma organização melhor entre as equipes para evitar erros em produção.

---

# 📌 Observações (opcional)

Espaço livre para comentários adicionais da equipe.

> Essa análise ajudou a entender na prática a importância da qualidade de software e como ela impacta diretamente o usuário final.