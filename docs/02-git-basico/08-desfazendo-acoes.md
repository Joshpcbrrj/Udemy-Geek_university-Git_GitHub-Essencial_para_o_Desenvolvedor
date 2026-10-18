# 2.8 · Desfazendo e refazendo ações no Git

> **Em uma frase:** errou? Quase tudo no Git tem volta. O comando certo depende de **onde** está o erro: no arquivo, no staging ou em um commit.

## 🧭 Mapa rápido: qual comando usar?

| Onde está o que você quer desfazer | Comando |
| --- | --- |
| Alterei um arquivo e quero **descartar** as mudanças | `git restore <arquivo>` |
| Dei `git add` e quero **tirar do staging** | `git restore --staged <arquivo>` |
| Quero corrigir o **último commit** (mensagem ou arquivo esquecido) | `git commit --amend` |
| Quero **apagar** commits que ainda não enviei | `git reset` |
| Quero desfazer um commit que **já está no GitHub** | `git revert` |

## ♻️ `git restore`: desfazer alterações em arquivos

O `git restore` é o comando moderno (desde o Git 2.23) para restaurar arquivos.

```bash
# Descarta as alterações de um arquivo (volta ao último commit)
git restore arquivo.txt

# Descarta as alterações de TODOS os arquivos
git restore .

# Tira um arquivo do staging (as alterações continuam no arquivo)
git restore --staged arquivo.txt

# Tira todos os arquivos do staging
git restore --staged .

# Restaura um arquivo como ele estava em um commit específico
git restore --source=<hash> arquivo.txt
```

> [!WARNING]
> `git restore <arquivo>` (sem `--staged`) **apaga** as alterações não commitadas daquele arquivo. Elas não vão para a lixeira.

## ⏪ Desfazendo o último commit

O caso mais comum: você fez um commit e quer desfazê-lo, **mantendo** as alterações para ajustar e commitar de novo.

```bash
git reset --soft HEAD~1
```

O `HEAD~1` significa "um commit antes do atual". Para os outros modos do `reset` (incluindo o perigoso `--hard`), veja a aula [4.6 Revert e reset](../04-git-avancado/06-revert-e-reset.md).

## ✏️ `git commit --amend`: corrigir o último commit

### Esqueci de incluir um arquivo

```bash
git add arquivo-esquecido.txt
git commit --amend --no-edit   # --no-edit mantém a mesma mensagem
```

### Escrevi a mensagem errada

```bash
git commit --amend -m "Mensagem corrigida"
```

> [!IMPORTANT]
> O `--amend` **substitui** o último commit por um novo (com outro hash). Só use em commits que você **ainda não enviou** para o GitHub; caso contrário, vai causar conflito no histórico de quem já baixou.

## 🧩 Juntando vários commits em um (squash)

Para juntar vários commits pequenos em um só, use o **rebase interativo**:

```bash
# Abre a lista dos 3 últimos commits para edição
git rebase -i HEAD~3
```

O Git abre o editor com algo assim:

```text
pick a1b2c3d Cria formulário
pick d4e5f6a Corrige typo
pick 7a8b9c0 Ajusta espaçamento
```

1. Mantenha `pick` no **primeiro** commit (o que vai "receber" os outros).
2. Troque `pick` por `squash` (ou só `s`) nos commits que você quer juntar a ele.
3. Salve e feche. O Git vai pedir para você escrever a mensagem final do commit combinado.

```text
pick a1b2c3d Cria formulário
s    d4e5f6a Corrige typo
s    7a8b9c0 Ajusta espaçamento
```

> [!WARNING]
> Assim como o `--amend`, o rebase interativo **reescreve o histórico**. Evite usar em commits que já foram compartilhados com outras pessoas.

## 🔁 Commit que já foi para o GitHub?

Use `git revert <hash>`: ele cria um novo commit que desfaz o anterior, sem reescrever o histórico. Detalhes na aula [4.6](../04-git-avancado/06-revert-e-reset.md).

> [!NOTE]
> Em tutoriais antigos você vai ver `git checkout -- arquivo` no lugar de `git restore arquivo`. Os dois fazem a mesma coisa; a aula [4.5](../04-git-avancado/05-desfazendo-com-checkout.md) mostra as equivalências.

## 📌 Resumindo

- **Arquivos:** `git restore` (descartar) e `git restore --staged` (tirar do staging).
- **Último commit:** `git commit --amend` para corrigir mensagem ou incluir arquivo; `git reset --soft HEAD~1` para desfazê-lo.
- **Vários commits em um:** `git rebase -i`.
- **Commits já compartilhados:** `git revert`.
- `--amend`, `reset` e `rebase -i` reescrevem o histórico: use só no que ainda não foi enviado.

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Edite o `saudacao.txt` e depois descarte a alteração, voltando ao último commit.

<details>
<summary>Ver resposta</summary>

```bash
git restore saudacao.txt
```

</details>

**2.** Você deu `git add .` e incluiu um arquivo por engano. Como tirá-lo do staging sem perder a alteração?

<details>
<summary>Ver resposta</summary>

```bash
git restore --staged nome-do-arquivo
```

</details>

**3.** Você fez um commit e percebeu que esqueceu de incluir o arquivo `extra.txt`. Como colocá-lo **no mesmo commit**?

<details>
<summary>Ver resposta</summary>

```bash
git add extra.txt
git commit --amend --no-edit
```
(Só faça isso se o commit ainda **não** foi enviado ao GitHub.)

</details>

**4.** Desfaça o último commit, mas mantenha as alterações prontas para commitar de novo.

<details>
<summary>Ver resposta</summary>

```bash
git reset --soft HEAD~1
```

</details>

---

<div align="center">

[⬅️ 2.7 Comandos úteis](./07-comandos-uteis.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [3.1 Branches ➡️](../03-git-intermediario/01-branches.md)

</div>
