# 3.5 · Fetch e pull

> **Em uma frase:** `git fetch` **baixa** as novidades do remoto sem mexer no seu trabalho; `git pull` baixa **e já junta** as novidades na sua branch.

## 📬 A analogia da caixa de correio

- **`git fetch`** é **pegar as cartas** na caixa de correio e deixá-las em cima da mesa. Você sabe que chegaram, pode lê-las, mas nada mudou na sua casa ainda.
- **`git pull`** é pegar as cartas **e já fazer o que elas pedem**.

Em termos de Git:

```text
git pull  =  git fetch  +  git merge
```

## 🔎 `git fetch`: ver antes de juntar

```bash
git fetch origin
```

O Git baixa os commits novos do remoto e guarda em **branches de rastreamento remoto**, como `origin/main`. Sua branch local `main` **não muda**.

Depois você pode inspecionar o que chegou:

```bash
# Ver os commits que estão no remoto e você ainda não tem
git log main..origin/main --oneline

# Ver as diferenças de código
git diff main origin/main
```

E, se estiver tudo certo, juntar na sua branch:

```bash
git merge origin/main
# ou, para manter o histórico linear:
git rebase origin/main
```

> [!TIP]
> Use `fetch` quando quiser **saber o que mudou** antes de misturar com o seu trabalho. É a opção mais cuidadosa.

## ⬇️ `git pull`: baixar e juntar de uma vez

```bash
git pull origin main
```

- **`origin`**: o repositório remoto.
- **`main`**: a branch remota que você quer trazer para a branch em que você está.

Se sua branch já está ligada ao remoto (foi clonada ou usou `push -u`), basta:

```bash
git pull
```

> [!WARNING]
> Como o `pull` faz um merge automático, ele pode gerar **conflitos** se você e outra pessoa alteraram as mesmas linhas. Nesse caso, resolva os conflitos (veja a aula [4.7](../04-git-avancado/07-conflitos.md)) e finalize com `git add` + `git commit`.

### Pull com rebase

Se preferir um histórico linear (sem commit de merge), use:

```bash
git pull --rebase
```

## ⚖️ Comparando

| | `git fetch` | `git pull` |
| --- | --- | --- |
| Baixa os commits do remoto? | ✅ | ✅ |
| Altera sua branch local? | ❌ | ✅ |
| Pode gerar conflito? | ❌ | ✅ |
| Quando usar | Para conferir antes de juntar | Para atualizar rapidamente |

## 📌 Resumindo

- `git fetch` baixa as novidades para `origin/<branch>`, sem tocar no seu trabalho.
- `git pull` = `fetch` + `merge`: baixa e já junta na branch atual.
- Boa prática: rode `git pull` **antes de começar a trabalhar** e **antes de fazer push**.

---

<div align="center">

[⬅️ 3.4 Clone e push](./04-clone-e-push.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [3.6 Bare repository ➡️](./06-bare-repository.md)

</div>
