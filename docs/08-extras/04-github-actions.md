# 8.4 · Introdução ao GitHub Actions

> **Em uma frase:** o GitHub Actions é um "robô" do GitHub que executa tarefas automaticamente (testar o código, publicar um site, gerar um arquivo) sempre que algo acontece no repositório, como um `push`.

> [!NOTE]
> Conteúdo extra: esta aula não faz parte do curso original.

## 🤖 O que é CI/CD?

- **CI (Integração Contínua):** a cada alteração enviada, o código é **testado automaticamente**. Se algo quebrou, você descobre na hora.
- **CD (Entrega/Implantação Contínua):** se os testes passaram, o projeto é **publicado automaticamente**.

O **GitHub Actions** é a ferramenta de CI/CD do próprio GitHub. É gratuito para repositórios públicos (e tem uma cota gratuita para os privados).

> [!TIP]
> Este próprio repositório usa GitHub Actions para publicar o site e gerar o EPUB do material sempre que há um `push` na `main`.

## 📖 Vocabulário

| Termo | O que é |
| --- | --- |
| **Workflow** | Um processo automatizado, descrito em um arquivo `.yml` na pasta `.github/workflows/` |
| **Evento** (`on`) | O que dispara o workflow: `push`, `pull_request`, um horário, um clique manual... |
| **Job** | Um conjunto de passos que roda em uma máquina |
| **Runner** | A máquina virtual que executa o job (ex.: `ubuntu-latest`) |
| **Step** | Um passo: um comando (`run`) ou uma ação pronta (`uses`) |
| **Action** | Um "bloco" reutilizável, criado pela comunidade (ex.: `actions/checkout`) |

## 🛠️ Seu primeiro workflow

Crie o arquivo **`.github/workflows/ola.yml`** no seu repositório:

```yaml
name: Olá, Actions

# Quando rodar: a cada push na main e a cada pull request
on:
  push:
    branches: [main]
  pull_request:

jobs:
  cumprimentar:
    runs-on: ubuntu-latest      # máquina Linux fornecida pelo GitHub

    steps:
      - name: Baixar o código do repositório
        uses: actions/checkout@v4

      - name: Listar os arquivos
        run: ls -la

      - name: Dizer olá
        run: echo "Olá! Este workflow foi disparado por ${{ github.actor }}."
```

Faça commit e push:

```bash
git add .github/workflows/ola.yml
git commit -m "Adiciona primeiro workflow do GitHub Actions"
git push
```

### Vendo o resultado

1. No GitHub, abra a aba **Actions** do repositório.
2. Clique na execução mais recente.
3. Clique no job `cumprimentar` para ver a saída de cada passo.

Um ✅ verde significa que tudo deu certo; um ❌ vermelho mostra em qual passo falhou.

> [!IMPORTANT]
> A indentação importa no YAML! Use **espaços** (nunca tab) e mantenha o alinhamento. Um espaço fora do lugar faz o workflow falhar.

## 🧪 Um exemplo mais real: testes automáticos

Em um projeto Node.js, um workflow típico de CI fica assim:

```yaml
name: Testes

on: [push, pull_request]

jobs:
  testar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm test
```

Combinado com as [regras de proteção da `main`](./03-github-flow.md), dá para **impedir o merge** de pull requests cujos testes falharam.

## 🔐 Segredos (secrets)

Nunca escreva senhas ou tokens no arquivo do workflow. Cadastre-os em **Settings → Secrets and variables → Actions** e use no workflow assim:

```yaml
- run: ./publicar.sh
  env:
    TOKEN: ${{ secrets.MEU_TOKEN }}
```

## 🛒 Marketplace

Existem milhares de actions prontas no **[GitHub Marketplace](https://github.com/marketplace?type=actions)**: publicar em servidores, enviar mensagens, verificar código, gerar documentação etc.

## 📌 Resumindo

- GitHub Actions executa tarefas automaticamente quando eventos acontecem no repositório.
- Workflows ficam em `.github/workflows/*.yml`.
- Estrutura: `on` (quando) → `jobs` (o quê) → `steps` (passo a passo).
- Resultados na aba **Actions**; segredos em **Settings → Secrets and variables → Actions**.

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Adicione o workflow `ola.yml` desta aula ao seu `treino-git` e veja a execução na aba **Actions**.

<details>
<summary>Ver resposta</summary>

Crie a pasta `.github/workflows/` na raiz do repositório, salve o arquivo `ola.yml` com o conteúdo da aula e faça commit e push. Em alguns segundos, a execução aparece na aba **Actions**.

</details>

**2.** Altere o workflow para rodar **só** quando houver push na branch `main` (e não em pull requests).

<details>
<summary>Ver resposta</summary>

```yaml
on:
  push:
    branches: [main]
```

</details>

**3.** Quebre o workflow de propósito (por exemplo, adicione um passo `run: exit 1`) e veja o que aparece no GitHub.

<details>
<summary>Ver resposta</summary>

A execução fica com um ❌ vermelho, e o passo que falhou aparece destacado nos logs. O GitHub também pode enviar um e-mail avisando da falha. Remova o passo para voltar ao ✅.

</details>

---

<div align="center">

[⬅️ 8.3 GitHub Flow](./03-github-flow.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [8.5 Erros comuns ➡️](./05-erros-comuns.md)

</div>
