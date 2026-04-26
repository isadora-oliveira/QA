# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades

- Busca de restaurantes
- Visualização de restaurantes (cardápio, fotos e avaliações)
- Sistema de favoritos
- Realização de pedidos
- Avaliações de usuários
---

## 2. Níveis de Teste

### Funcionalidade: Busca de restaurantes
- Unitário: validar filtros de busca (tipo, localização e preço)
- Integração: verificar comunicação entre busca e banco de dados
- Sistema: usuário realiza busca e vê resultados corretos
- Aceitação: usuário encontra restaurantes facilmente

### Funcionalidade: Visualização de restaurantes
- Unitário: validar exibição de informações (nome, fotos, cardápio)
- Integração: verificar conexão entre API e interface
- Sistema: usuário acessa restaurante e vê todas as informações
- Aceitação: usuário consegue entender informações corretamente

### Funcionalidade: Sistema de favoritos
- Unitário: salvar e remover favoritos
- Integração: verificar conexão com banco de dados
- Sistema: usuário salva e acessa favoritos
- Aceitação: usuário consegue favoritar e ver depois

### Funcionalidade: Realização de pedidos
- Unitário: validar itens do pedido
- Integração: conectar carrinho com sistema de pedidos
- Sistema: usuário monta e envia pedido
- Aceitação: usuário consegue finalizar pedido com sucesso


### Funcionalidade: Avaliações de usuários
- Unitário: salvar e exibir avaliações
- Integração: conectar avaliações ao restaurante
- Sistema: usuário avalia restaurante
- Aceitação: usuário consegue avaliar e visualizar avaliações


---

## 3. Prioridades e Riscos

Alta prioridade:
- Busca de restaurantes
- Realização de pedidos

Justificativa:
Essas funcionalidades são essenciais para o funcionamento do sistema. Se falharem, o usuário não consegue usar a plataforma corretamente ou finalizar um pedido.

Baixa prioridade: 
- Sistema de favoritos
- Avaliações de usuários

Justificativa:
Essas funções melhoram a experiência, mas não impedem o uso principal do sistema.

---

## 4. Pirâmide de Testes

- Maior foco: testes unitários
- Médio foco: testes de integração
- Menor foco: testes de sistema e aceitação

Justificativa:
Testes unitários são mais rápidos e ajudam a evitar erros básicos. Integração garante que os sistemas funcionam juntos. Testes de sistema e aceitação são importantes, mas mais lentos e devem ser usados em menor quantidade..

---

## 5. Testes em Produção

- Uso de testes controlados em produção
- Aplicar em novas funcionalidades e melhorias de busca e pedidos

Justificativa:
Pode ser útil testar algumas funções em produção para validar comportamento real, mas deve ser feito com cuidado para não afetar os usuários. Ideal usar em pequenas mudanças ou testes controlados.