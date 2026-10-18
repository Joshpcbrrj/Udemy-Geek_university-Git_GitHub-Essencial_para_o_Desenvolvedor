# 4.5 · Desfazendo ações com checkout

> **Em uma frase:** o `git checkout` pode **descartar alterações** que ainda não foram commitadas e também **visitar** um commit antigo.

> [!NOTE]
> Nas versões mais novas do Git, essas tarefas ganharam comandos mais claros: `git restore` (para arquivos) e `git switch` (para branches). O `checkout` continua funcionando e aparece em muitos tutoriais, por isso vale conhecer os dois. A tabela no final da aula mostra as equivalências.

## 🧹 Descartando alterações que ainda NÃO foram para o staging

Você editou arquivos, **não** deu `git add` e quer voltar como estava no último commit.

```bash
# Um arquivo específico
git checkout -- nome-do-arquivo

# Todos os arquivos da pasta atual
git checkout -- .
```

O `--` serve para dizer ao Git "o que vem depois é um **arquivo**, não uma branch". O `.` significa "todos os arquivos da pasta atual (e subpastas)".

> [!WARNING]
> As alterações descartadas **não vão para a lixeira**: são perdidas de vez.

## 🧹 Descartando alterações que JÁ foram para o staging

Você editou, deu `git add` e agora quer **jogar tudo fora** e voltar ao último commit:

```bash
# Um arquivo específico
git checkout HEAD -- nome-do-arquivo

# Todos os arquivos
git checkout HEAD -- .
```

O `HEAD` significa "o último commit". Esse comando restaura o arquivo como estava no último commit, **tanto no staging quanto na pasta**, ou seja, apaga as alterações dos dois lugares.

> [!TIP]
> Se você só quer **tirar do staging** mas **manter** as alterações no arquivo, o comando certo é `git restore --staged nome-do-arquivo`.

## 🕰️ Visitando um commit antigo

```bash
git checkout <hash-do-commit>
```

Seus arquivos voltam a ficar exatamente como estavam naquele commit. Você entra no modo **"detached HEAD"** (HEAD desanexado), ou seja, não está em nenhuma branch.

- Para **voltar ao presente**: `git checkout main` (ou `git switch main`).
- Para **trabalhar a partir dali**, crie uma branch:

  ```bash
  git switch -c nova-branch
  ```

> [!IMPORTANT]
> Esse comando **não apaga** nenhum commit. Ele só muda o que você está vendo. Os commits mais novos continuam na branch `main`.

## 🔁 Equivalências: `checkout` × comandos modernos

| Objetivo | Com `checkout` | Forma moderna |
| --- | --- | --- |
| Descartar alterações de um arquivo | `git checkout -- arquivo` | `git restore arquivo` |
| Descartar alterações de todos os arquivos | `git checkout -- .` | `git restore .` |
| Descartar alterações do staging e da pasta | `git checkout HEAD -- arquivo` | `git restore --staged --worktree arquivo` |
| Só tirar do staging (mantendo as alterações) | — | `git restore --staged arquivo` |
| Trocar de branch | `git checkout main` | `git switch main` |
| Criar e trocar de branch | `git checkout -b nova` | `git switch -c nova` |
| Visitar um commit antigo | `git checkout <hash>` | `git switch --detach <hash>` |

## 📌 Resumindo

- `git checkout -- arquivo`: descarta alterações **fora** do staging.
- `git checkout HEAD -- arquivo`: descarta alterações do staging **e** da pasta.
- `git checkout <hash>`: visita um commit antigo (detached HEAD) sem apagar nada.
- Prefira `git restore` e `git switch` no dia a dia: são mais claros.

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Edite o `README.md` (sem dar `git add`) e descarte a alteração usando `checkout`.

<details>
<summary>Ver resposta</summary>

```bash
git checkout -- README.md
```

</details>

**2.** Edite o `README.md`, dê `git add` e depois descarte a alteração **do staging e da pasta** usando `checkout`.

<details>
<summary>Ver resposta</summary>

```bash
git checkout HEAD -- README.md
```

</details>

**3.** Escreva o equivalente moderno (com `restore` ou `switch`) de cada comando: `git checkout -- arquivo`, `git checkout main` e `git checkout -b nova`.

<details>
<summary>Ver resposta</summary>

`git restore arquivo` · `git switch main` · `git switch -c nova`.

</details>

---

<div align="center">

[⬅️ 4.4 Histórico de commits](./04-historico-de-commits.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [4.6 Revert e reset ➡️](./06-revert-e-reset.md)

</div>
