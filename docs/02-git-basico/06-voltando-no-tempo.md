# 2.6 · Voltando no tempo com o Git

> **Em uma frase:** existem três formas principais de "voltar no tempo" no Git: **visitar** um commit antigo (`checkout`), **apagar** commits do histórico (`reset`) ou **desfazer** um commit criando outro (`revert`).

Antes de qualquer coisa, descubra o **hash** do commit para onde você quer voltar:

```bash
git log --oneline
# a1b2c3d Adiciona rodapé
# 9f8e7d6 Cria página inicial   ← quero voltar para cá
# 1234abc Commit inicial
```

Você só precisa dos primeiros caracteres do hash (ex.: `9f8e7d6`).

## 1️⃣ `git checkout <hash>`: só olhar o passado

```bash
git checkout 9f8e7d6
```

Seus arquivos voltam a ficar **exatamente como estavam** naquele commit. É como abrir um álbum de fotos antigo: você pode olhar, rodar o projeto, testar... sem apagar nada.

Você fica em um estado chamado **"detached HEAD"** (HEAD desanexado), ou seja, não está em nenhuma branch.

- Para **voltar ao presente**: `git checkout main` (ou `git switch main`).
- Se quiser **trabalhar a partir daquele ponto**, crie uma branch nova:

  ```bash
  git switch -c minha-correcao
  ```

> [!WARNING]
> Commits feitos em "detached HEAD" sem criar uma branch ficam "soltos" e podem ser perdidos quando você voltar para a `main`.

## 2️⃣ `git reset <hash>`: voltar e tirar commits do histórico

```bash
git reset 9f8e7d6
```

A branch volta para o commit indicado e os commits que vieram depois **saem do histórico**. Dependendo da opção (`--soft`, `--mixed` ou `--hard`), as alterações desses commits são mantidas ou **apagadas**.

## 3️⃣ `git revert <hash>`: desfazer de forma segura

```bash
git revert a1b2c3d
```

Em vez de apagar, o Git cria um **novo commit que faz o contrário** daquele. O histórico fica intacto, por isso é a forma mais segura de desfazer algo que **já foi enviado** para o GitHub.

> [!TIP]
> `reset` e `revert` são explicados em detalhes, com diagramas e os três modos do reset, na aula [4.6 Revert e reset](../04-git-avancado/06-revert-e-reset.md).

## 🧭 Qual usar?

| Situação | Comando |
| --- | --- |
| Só quero **ver** como o projeto estava | `git checkout <hash>` |
| Quero desfazer commits que **ainda não enviei** para o GitHub | `git reset` |
| Quero desfazer um commit que **já está no GitHub** / compartilhado | `git revert` |

> [!TIP]
> Antes de operações que mexem no histórico (como `reset --hard`), crie uma branch de backup: `git branch backup-antes-do-reset`. Se algo der errado, seus commits continuam lá.

## 📌 Resumindo

- `checkout <hash>`: visita o passado sem alterar nada (detached HEAD).
- `reset`: volta a branch e remove commits do histórico.
- `revert`: cria um commit que desfaz outro, preservando o histórico (ideal para o que já foi compartilhado).
- Próximos passos: desfazer alterações em arquivos na [2.8](./08-desfazendo-acoes.md); `reset` e `revert` a fundo na [4.6](../04-git-avancado/06-revert-e-reset.md).

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** No `treino-git`, visite o **primeiro** commit, veja como os arquivos estavam e volte para o presente.

<details>
<summary>Ver resposta</summary>

```bash
git log --oneline        # copie o hash do primeiro commit (o último da lista)
git checkout <hash>      # os arquivos voltam no tempo (detached HEAD)
git switch main          # volta ao presente
```

</details>

**2.** Você descobriu um erro em um commit que **já está no GitHub**. Qual comando é o mais seguro para desfazê-lo?

<details>
<summary>Ver resposta</summary>

`git revert <hash>`. Ele cria um novo commit que desfaz o anterior, sem reescrever o histórico que outras pessoas já baixaram.

</details>

**3.** Você visitou um commit antigo com `git checkout <hash>` e quer corrigir algo a partir dali, sem perder o trabalho. O que faz antes de commitar?

<details>
<summary>Ver resposta</summary>

Cria uma branch a partir daquele ponto, para os commits não ficarem "soltos" no detached HEAD:

```bash
git switch -c correcao-antiga
```

</details>

---

<div align="center">

[⬅️ 2.5 Histórico do projeto](./05-historico-do-projeto.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [2.7 Comandos úteis ➡️](./07-comandos-uteis.md)

</div>
