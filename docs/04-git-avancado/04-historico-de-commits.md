# 4.4 · Consultando o histórico de commits

> **Em uma frase:** você pode ver o histórico do projeto de três jeitos: pelo **terminal** (`git log`), por **interfaces gráficas** no editor ou pela **página do GitHub**.

## 💻 1. Pelo terminal: `git log`

```bash
git log
```

Mostra os commits do mais recente para o mais antigo, com hash, autor, data e mensagem.

### Variações mais usadas

```bash
# Uma linha por commit (visão geral rápida)
git log --oneline

# Filtrar por autor
git log --author="Maria"

# Filtrar por período (formato AAAA-MM-DD)
git log --since=2023-01-01
git log --until=2023-07-01

# Filtrar por palavra na mensagem
git log --grep="login"

# Combinar filtros
git log --oneline --author="João"

# Ver o histórico de um arquivo específico
git log --oneline -- caminho/do/arquivo.txt

# Ver quem alterou cada linha de um arquivo (e em qual commit)
git blame caminho/do/arquivo.txt
```

> [!TIP]
> Para todas as opções, consulte `git help log` ou revise a aula [2.5 Como consultar o histórico](../02-git-basico/05-historico-do-projeto.md).

## 🖼️ 2. Por interfaces gráficas

Muitas ferramentas desenham o histórico como um **gráfico colorido**, onde cada linha vertical é uma branch e cada bolinha é um commit. Fica muito mais fácil enxergar quando as branches foram criadas e mescladas.

<img src="./img/2.png" alt="Histórico de commits exibido em gráfico por uma interface gráfica" width="900">

Algumas opções populares:

- Extensões do VS Code como **Git Graph**, **GitLens** e **Git History** (veja a [aula 6.1](../06-curriculo-online/01-curriculo-e-plugins.md));
- **GitHub Desktop**, **GitKraken**, **Sourcetree**;
- No próprio terminal: `git log --graph --oneline --all`.

## 🌐 3. Pela página do GitHub

No GitHub (e também no GitLab e no Bitbucket), dá para navegar pelo histórico direto no navegador:

1. Abra o repositório.
2. Clique no link de **commits** (ícone de relógio 🕒, perto do botão "Code").
3. Clique em qualquer commit para ver **exatamente** quais linhas foram adicionadas (verde) e removidas (vermelho).

<img src="./img/3.png" alt="Lista de commits na interface web do GitHub" width="600">

> [!TIP]
> Dentro de um arquivo no GitHub, o botão **History** mostra só os commits que mexeram naquele arquivo, e o botão **Blame** mostra quem alterou cada linha.

## 📌 Resumindo

- **Terminal:** `git log` (e suas variações) e `git blame`.
- **Interfaces gráficas:** visualização em gráfico das branches e commits.
- **GitHub:** aba de commits, com o "diff" colorido de cada alteração.

---

<div align="center">

[⬅️ 4.3 Colaboradores](./03-colaboradores.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [4.5 Desfazendo com checkout ➡️](./05-desfazendo-com-checkout.md)

</div>
