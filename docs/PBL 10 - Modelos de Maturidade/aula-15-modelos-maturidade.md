# Aula 15 – Modelos de Maturidade

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante:  
> - Isadora Oliveira

---

## 🔹 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|---|:---:|:---:|:---:|
| Os requisitos são documentados? | | X | |
| Existe controle de mudanças? | | | X |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | X | |
| O processo de desenvolvimento é conhecido por toda a equipe? | | X | |
| As tarefas são planejadas e acompanhadas regularmente? | | | X |
| Existe padronização para implementação de funcionalidades? | | X | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | | X |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | X | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | X | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | X | |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | | X |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | X |

### Nível de maturidade estimado

**CMMI Nível 1 – Inicial / MPS.BR Nível G (Parcialmente Gerenciado)**

### Justificativa

O processo tem algumas coisas boas: os testes sempre foram rodados antes de entregar, o repositório está organizado com pastas e os arquivos `.md` explicam o que foi feito. Mas faltam várias coisas que um processo mais maduro teria. Não tem controle de mudanças, então quando algo era alterado dependia de lembrar de atualizar tudo na mão. Não tem métricas nem planejamento formal. O processo foi sendo descoberto ao longo das atividades, sem uma definição antes de começar. Por isso o nível é inicial, com alguns elementos gerenciados de forma pontual.

---

## 🔹 2. Lacunas Identificadas

| Lacuna | Impacto |
|---|---|
| Não tem controle de mudanças | Quando algo mudava, era fácil esquecer de atualizar algum arquivo e ficar com informação errada |
| Não tem métricas | Não dá pra saber se o processo melhorou ou piorou de uma atividade pra outra |
| Sem revisão de outra pessoa | Erros que passam despercebidos quando se trabalha sozinho ficam na entrega |
| Rastreabilidade parcial | Não é fácil saber se todos os comportamentos importantes do sistema estão sendo testados |
| Planejamento informal | Algumas etapas só eram descobertas no meio da atividade, gerando retrabalho |

---

## 🔹 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| Criar um checklist de entrega por atividade | Evita esquecer de validar os testes ou atualizar o `.md` |
| Anotar os defeitos encontrados em algum lugar (arquivo ou issue do GitHub) | Permite ver se os mesmos problemas se repetem |
| Definir pelo menos uma métrica simples | Torna o progresso mais fácil de acompanhar |
| Revisar o trabalho com outro colega antes de entregar | Aumenta a chance de pegar erros que passam batido |
| Usar issues no GitHub pra registrar mudanças | Ajuda a entender o que mudou e por quê |

---

## ✅ Conclusão

O processo utilizado nas atividades do LocalEats ainda é inicial, mas já tem algumas coisas boas, como os testes organizados e o repositório com os arquivos separados por PBL. Pra evoluir de nível, o principal seria formalizar o que já funciona e adicionar coisas simples como um checklist e o registro dos problemas encontrados. 
