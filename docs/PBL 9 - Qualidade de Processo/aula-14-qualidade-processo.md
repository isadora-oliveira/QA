# Aula 14 – Qualidade de Processo

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante:  
> - Isadora Oliveira

---

## 🔹 1. Mapeamento do Processo

### Fluxo de trabalho utilizado nas atividades do LocalEats

```
Recebimento da Demanda
          ↓
   Análise do Sistema
          ↓
  Desenvolvimento e Testes
          ↓
     Validação e Ajustes
          ↓
  Documentação e Entrega
```

**Descrição do fluxo:**

Em cada atividade PBL, o processo começa com o recebimento do enunciado do professor. Depois, o sistema LocalEats é explorado para entender o comportamento esperado. Em seguida, os testes ou artefatos são desenvolvidos e executados. Se alguma coisa quebra ou não funciona, os ajustes são feitos antes de documentar tudo no arquivo `.md` e entregar no repositório.

---

## 🔹 2. Entradas, Atividades e Saídas

| Etapa | Entrada | Atividade | Saída |
|---|---|---|---|
| Recebimento da demanda | Enunciado do PBL | Leitura e entendimento da tarefa | Tarefa definida |
| Análise do sistema | Acesso ao LocalEats | Exploração do sistema e identificação de fluxos | Fluxo escolhido para testar |
| Desenvolvimento e testes | Fluxo definido | Escrita de testes e código | Testes implementados |
| Validação e ajustes | Testes escritos | Execução dos testes e correção de erros | Testes passando |
| Documentação e entrega | Testes validados | Escrita do arquivo `.md` com evidências | Documento entregue no repositório |

---

## 🔹 3. Reflexão sobre o Processo

**O processo utilizado estava claramente definido?**

Mais ou menos. O enunciado de cada PBL diz o que precisa ser entregue, mas não detalha como chegar lá. A ordem das etapas foi sendo descoberta ao longo das atividades. Nas primeiras foi mais difícil, porque eu ainda não sabia o que esperar do sistema.

**Todos os integrantes seguem o mesmo fluxo de trabalho?**

Como foi trabalho individual, o fluxo foi só o meu. Mas percebi que, dependendo do PBL, eu invertia às vezes as etapas — por exemplo, no PBL 6 comecei escrevendo o teste antes do código por causa do TDD, o que foi diferente do que fazia antes.

**Em quais etapas a qualidade é verificada?**

Principalmente na etapa de validação, quando os testes são executados. Mas também na análise do sistema, quando identifico comportamentos inesperados (como o botão de finalizar pedido aparecer com carrinho vazio, ou o seletor do Playwright pegar dois campos ao mesmo tempo).

**Quais melhorias poderiam tornar o processo mais eficiente?**

- Explorar o sistema antes de começar a escrever qualquer teste, pra não descobrir problemas de seletor no meio da implementação.
- Criar um checklist simples antes de cada entrega pra não esquecer de atualizar o `.md` com os caminhos e logs corretos.
- Separar melhor o tempo de implementação do de documentação, porque às vezes a documentação ficava pra última hora.

**Como a qualidade do processo impacta a qualidade do produto final?**

Bastante. Nas atividades em que eu seguia as etapas na ordem certa (entender o fluxo → implementar → validar → documentar), o resultado ficou mais organizado e com menos retrabalho. Nas que pulei etapas ou documentei sem validar direito, apareceram inconsistências nos caminhos de arquivo ou nos logs mostrados no `.md`. Um processo bem definido desde o começo economiza tempo e reduz erros no final.
