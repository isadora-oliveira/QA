# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrante

- Isadora Oliveira

---

# 1. Repositório da Atividade

| Item | Descrição |
|------|-----------|
| Nome do repositório | `QA-LocalEats` |
| Link do repositório | `https://github.com/isadora-oliveira/QA-LocalEats` |

E## Estrutura de Diretórios

```text
QA-LocalEats/
├── .github/
│   └── workflows/
│       └── quality.yml
├── tests/
│   └── test_busca_categoria.py
├── busca_categoria.py
└── README.md
```

---

# 2. Planejamento da Funcionalidade

| Item | Descrição |
|------|-----------|
| Título da Issue | Implementar busca de restaurantes por categoria |
| Objetivo da funcionalidade | Permitir ao usuário filtrar restaurantes pela categoria desejada. |
| Link da Issue | `https://github.com/isadora-oliveira/QA-LocalEats/issues/1` |

---

# 3. Teste Automatizado

| Item | Descrição |
|------|-----------|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar se a função retorna apenas os restaurantes pertencentes à categoria informada. |
| Link para o arquivo do teste | `https://github.com/isadora-oliveira/QA-LocalEats/blob/main/tests/test_busca_categoria.py` |

### Código do teste

```python
from busca_categoria import buscar_por_categoria


def test_buscar_restaurantes_por_categoria():

    restaurantes = [
        {
            "nome": "Restaurante Sabor 0",
            "categoria": "Italiana"
        },
        {
            "nome": "Restaurante Sabor 2",
            "categoria": "Japonesa"
        },
        {
            "nome": "Restaurante Sabor 5",
            "categoria": "Brasileira"
        }
    ]

    resultado = buscar_por_categoria(restaurantes, "Italiana")

    assert len(resultado) == 1
    assert resultado[0]["nome"] == "Restaurante Sabor 0"
```

---

# 4. Pipeline de Integração Contínua

| Item | Descrição |
|------|-----------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | `push` e `pull_request` |
| Link para o arquivo do workflow | `https://github.com/isadora-oliveira/QA-LocalEats/blob/main/.github/workflows/quality.yml` |
| Link de uma execução do workflow | `https://github.com/isadora-oliveira/QA-LocalEats/actions` |

### Código do workflow

```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:

    runs-on: ubuntu-latest

    steps:

      - name: Baixar código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install pytest

      - name: Executar testes
        run: pytest
```

---

# 5. Indicadores de Qualidade

| Indicador | Valor |
|-----------|-------|
| Quantidade de testes executados | 1 |
| Quantidade de testes aprovados | 1 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

# 6. Registro de Defeito

| Item | Descrição |
|------|-----------|
| Título do defeito | Restaurante sem campo "categoria" gera erro na busca |
| Severidade | Média |
| Link da Issue | `https://github.com/isadora-oliveira/QA-LocalEats/issues/2` |

Foi identificado que a função pode gerar erro caso algum restaurante não possua o campo **categoria**. O defeito foi identificado durante testes de cenários alternativos. A correção consiste em validar a existência da chave antes de realizar a comparação, evitando exceções durante a execução.