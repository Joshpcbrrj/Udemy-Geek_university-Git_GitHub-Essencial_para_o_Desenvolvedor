# 3.4 · Clone e push

> **Em uma frase:** `git clone` **baixa** um repositório remoto inteiro para o seu computador; `git push` **envia** seus commits locais para o repositório remoto.

```text
           git clone (baixa tudo, uma vez)
 Remoto  ─────────────────────────────────▶  Seu computador
 (GitHub) ◀─────────────────────────────────
           git push (envia seus commits)
```

## 📥 `git clone`: baixando um repositório

```bash
git clone <URL-do-repositório>
```

O `clone` cria uma pasta com:

- **todos os arquivos** do projeto;
- **todo o histórico** de commits;
- uma conexão já configurada com o repositório de origem, chamada **`origin`**.

### Exemplo de clone

```bash
git clone https://github.com/usuario/meu-projeto.git

# Entre na pasta criada
cd meu-projeto
```

### Escolhendo o nome da pasta

```bash
git clone https://github.com/usuario/meu-projeto.git minha-pasta
```

Se você não informar o nome, o Git usa o nome do repositório.

> [!TIP]
> A URL fica no botão verde **"<> Code"** da página do repositório no GitHub. Ela pode ser **HTTPS** (`https://github.com/...`), mais fácil para começar, ou **SSH** (`git@github.com:...`), que exige configurar uma chave SSH.

## 📤 `git push`: enviando seus commits

```bash
git push <nome-do-remoto> <nome-da-branch>
```

- **`<nome-do-remoto>`**: o "apelido" do repositório remoto. Quase sempre é **`origin`**.
- **`<nome-da-branch>`**: a branch local que você quer enviar.

### Exemplo de push

```bash
git push origin main
```

### Enviando uma branch nova pela primeira vez

Se a branch só existe no seu computador, use `-u` (ou `--set-upstream`) no primeiro push:

```bash
git push -u origin minha-branch
```

O `-u` cria a branch no remoto e "liga" as duas. A partir daí, basta digitar:

```bash
git push
```

> [!IMPORTANT]
> Se alguém enviou commits para a mesma branch antes de você, o GitHub **recusa** o seu push (erro `rejected`). Isso protege o trabalho da outra pessoa. A solução é primeiro **trazer** as novidades com `git pull` e depois fazer o push novamente.

## 📌 Resumindo

| Comando | O que faz |
| --- | --- |
| `git clone <url>` | Baixa o repositório completo (arquivos + histórico) |
| `git clone <url> pasta` | Baixa em uma pasta com o nome que você escolher |
| `git push origin main` | Envia os commits da `main` para o remoto |
| `git push -u origin branch` | Envia uma branch nova e liga ela ao remoto |
| `git push` | Envia a branch atual (depois de já ter usado `-u`) |

---

<div align="center">

[⬅️ 3.3 Rebase](./03-rebase.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [3.5 Fetch e pull ➡️](./05-fetch-e-pull.md)

</div>
