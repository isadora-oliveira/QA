🧪 Aula 5 – Testes Funcionais vs Estruturais - LocalEats

👥 Integrantes do Grupo
Isadora Oliveira

🎯 1. Funcionalidade escolhida
Funcionalidade selecionada: Busca de restaurantes

Descrição da funcionalidade: Permite que o usuário procure restaurantes usando filtros como tipo de comida, localização e faixa de preço.

O que o usuário espera: Que ao buscar, apareçam restaurantes corretos, rápidos e de acordo com o filtro selecionado.

🔍 2. Testes Caixa-Preta (Visão do Usuário)
Quais testes vocês fariam sem conhecer o código?

🔹 Cenários de teste
Cenário 1: Buscar restaurante por tipo de comida e verificar se os resultados são corretos

Cenário 2: Buscar por localização e verificar se aparecem restaurantes próximos

Cenário 3: Tentar buscar sem preencher nada e ver o comportamento do sistema

Cenário 4: Usar o campo de busca pelo celular e verificar se funciona corretamente

🔹 Possíveis erros identificados
- Resultados incorretos na busca
- Falha ao usar o botão “Enter”
- Filtro não funcionando corretamente
- Sistema não atualizando resultados corretamente

🔧 3. Testes Caixa-Branca (Visão do Sistema)
Como essa funcionalidade poderia estar implementada internamente?

🔹 Lógica hipotética (pseudo-código ou descrição)
- O sistema pode usar condições (if/else) para aplicar filtros
- Pode existir validação de campos obrigatórios
- Pode haver consulta ao banco de dados para retornar restaurantes
- Pode existir ordenação dos resultados antes de exibir

🔹 Situações a serem testadas
- Se o filtro de tipo está sendo aplicado corretamente no código
- Se a consulta ao banco está retornando dados certos
- Se a validação impede buscas vazias
- Se a ordenação dos resultados está funcionando

🔹 Possíveis erros identificados
- Falha na lógica de filtros
- Consulta errada ao banco de dados
- Falta de validação de entrada
- Erro na ordenação dos resultados

⚖️ 4. Comparação entre as abordagens
Qual a principal diferença entre testar sem ver o código e com acesso ao código? 
A principal diferença é que, ao testar sem ver o código (caixa-preta), o foco está no comportamento do sistema do ponto de vista do usuário, se ele funciona corretamente na prática. Já com acesso ao código (caixa-branca), o foco está na lógica interna, analisando como o sistema foi implementado e se o código está correto.

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-preta:
- Erros de usabilidade
- Resultados incorretos visíveis
- Problemas na experiência do usuário

Caixa-branca:
- Erros de lógica
- Problemas no código
- Falhas em regras internas

💡 5. Reflexão no contexto do LocalEats
Qual abordagem parece mais importante neste momento do projeto?
Na minha opinião, as duas abordagens são importantes. A caixa-preta ajuda a identificar os problemas que o usuário realmente vê, que são muitos no atualmente. Já a caixa-branca ajuda a entender onde o erro pode estar no código.

Apenas uma abordagem seria suficiente? Por quê?
Apenas uma das abordagens não seria suficiente, pois o sistema tem problemas tanto na experiência do usuário quanto na parte interna.


🚀 Conclusão
Com essa atividade, eu entendi melhor que os testes funcionais e estruturais se complementam. Um ajuda a ver o problema pelo lado do usuário e o outro ajuda a encontrar a causa dentro do sistema. No caso do LocalEats, os dois seriam necessários para melhorar a qualidade do sistema.