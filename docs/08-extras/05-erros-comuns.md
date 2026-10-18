# 8.5 · Erros comuns e como resolver

> **Em uma frase:** um guia de "primeiros socorros" com as mensagens de erro que quem está começando mais encontra, o que cada uma significa e como resolver.

> [!NOTE]
> Conteúdo extra: esta aula não faz parte do curso original.

> [!TIP]
> Use `Ctrl+F` e procure por um trecho da mensagem de erro que apareceu no seu terminal.

## 📁 Repositório e configuração

### `fatal: not a git repository (or any of the parent directories): .git`

**Causa:** você está em uma pasta que não é um repositório Git.

**Solução:** entre na pasta certa com `cd caminho/do/projeto` ou, se for um projeto novo, rode `git init`.

### `Author identity unknown` / `Please tell me who you are`

**Causa:** você ainda não configurou nome e e-mail.

**Solução:**

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

### `warning: in the working copy of '...', LF will be replaced by CRLF`

**Causa:** o Windows usa um caractere de fim de linha diferente do Linux/macOS (CRLF × LF). O Git está avisando que vai converter automaticamente.

**Solução:** **nenhuma, é só um aviso.** Seu arquivo não foi danificado. (Esse comportamento é controlado pela configuração `core.autocrlf`.)

### Abriu uma tela estranha e não consigo sair (Vim)

**Causa:** você rodou `git commit` sem `-m` (ou um merge abriu o editor), e o editor padrão é o **Vim**.

**Solução:** aperte `Esc`, digite **`:wq`** e aperte `Enter` (salva e sai). Para sair sem salvar: `Esc`, `:q!`, `Enter`. Para não passar mais por isso, configure outro editor:

```bash
git config --global core.editor "code --wait"
```

## ☁️ Push, pull e autenticação

### `! [rejected] main -> main (fetch first)` ou `(non-fast-forward)`

**Causa:** o repositório remoto tem commits que você ainda não tem (alguém enviou antes, ou você editou pelo site).

**Solução:** traga as novidades e envie de novo:

```bash
git pull          # ou: git pull --rebase
git push
```

### `fatal: The current branch minha-branch has no upstream branch`

**Causa:** a branch existe só no seu computador e ainda não está ligada a uma branch remota.

**Solução:**

```bash
git push -u origin minha-branch
```

### `error: src refspec main does not match any`

**Causa:** você tentou dar push na `main`, mas ela não existe, porque ainda não há nenhum commit ou porque a branch se chama `master`.

**Solução:** confira com `git branch`. Se não houver commits, faça o primeiro commit. Se a branch se chamar `master` e você quiser renomeá-la:

```bash
git branch -M main
git push -u origin main
```

### `Support for password authentication was removed` / `Authentication failed`

**Causa:** o GitHub não aceita mais a senha da conta no terminal.

**Solução:** use o login pelo navegador (Git Credential Manager), um **Personal Access Token** no lugar da senha ou uma [chave SSH](./02-chave-ssh.md). Veja também a [aula 1.5](../01-introducao/05-usuarios-locais.md).

### `git@github.com: Permission denied (publickey)`

**Causa:** você está usando uma URL SSH, mas sua chave SSH não está configurada ou não está cadastrada no GitHub.

**Solução:** siga a [aula 8.2](./02-chave-ssh.md) e teste com `ssh -T git@github.com`.

### `fatal: refusing to merge unrelated histories`

**Causa:** o repositório local e o remoto começaram separados. Isso acontece muito quando você cria o repositório no GitHub **com README** e também roda `git init` no computador.

**Solução:**

```bash
git pull origin main --allow-unrelated-histories
# resolva conflitos, se houver
git push -u origin main
```

> [!TIP]
> Para evitar esse erro, crie o repositório no GitHub **vazio** quando você já tem o projeto no computador.

## 🌿 Branches e merge

### `CONFLICT (content): Merge conflict in arquivo.txt`

**Causa:** duas alterações mexeram na mesma linha.

**Solução:** veja o passo a passo na [aula 4.7 Resolvendo conflitos](../04-git-avancado/07-conflitos.md). Para desistir: `git merge --abort`.

### `error: Your local changes to the following files would be overwritten by checkout` (ou `by merge`)

**Causa:** você tem alterações não commitadas que seriam perdidas ao trocar de branch ou fazer o merge.

**Solução:** faça commit das alterações ou guarde-as temporariamente com o [`git stash`](./01-git-stash.md):

```bash
git stash
git switch outra-branch
# ... depois, de volta à branch original:
git stash pop
```

### `You are in 'detached HEAD' state`

**Causa:** você fez checkout de um commit ou de uma tag, e não de uma branch.

**Solução:** para voltar, use `git switch main`. Para continuar trabalhando a partir dali, crie uma branch com `git switch -c nova-branch`.

## 😬 "Fiz besteira"

### Fiz commit na branch errada (ex.: direto na `main`)

Se ainda **não** deu push:

```bash
git branch nova-branch       # cria uma branch apontando para o commit atual
git reset --hard HEAD~1      # tira o commit da main (o commit continua na nova-branch)
git switch nova-branch       # continue trabalhando aqui
```

> [!WARNING]
> O `reset --hard` apaga alterações **não commitadas**. Confira o `git status` antes.

### Escrevi a mensagem do commit errada

Se ainda não deu push: `git commit --amend -m "Mensagem correta"`.

### Fiz commit de uma senha ou de um arquivo sensível

1. Pare de rastrear o arquivo: `git rm --cached arquivo` e adicione-o ao `.gitignore`.
2. Faça um novo commit.
3. Se o commit **já foi para o GitHub**, considere a senha **vazada**: **troque-a imediatamente**. Ela continua no histórico, e remover do histórico exige ferramentas específicas (como o `git filter-repo`).

### Apaguei um commit com `reset --hard` sem querer

```bash
git reflog                    # encontre o hash do commit perdido
git reset --hard <hash>       # volte para ele
```

## 📌 Resumindo

- Leia a mensagem de erro com calma: quase sempre ela diz o que fazer (muitas vezes com o comando pronto).
- `git status` é o melhor primeiro passo para entender qualquer situação.
- Quase tudo no Git tem volta, especialmente o que já foi commitado (`git reflog`).

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** No `treino-git`, crie uma branch nova sem dar push e rode `git push`. Qual erro aparece e como resolver?

<details>
<summary>Ver resposta</summary>

Aparece `fatal: The current branch ... has no upstream branch`. Resolva com `git push -u origin nome-da-branch`.

</details>

**2.** Simule um "commit na branch errada": faça um commit na `main` e depois mova-o para uma branch nova.

<details>
<summary>Ver resposta</summary>

```bash
echo "teste" >> README.md && git commit -am "Commit na branch errada"
git branch branch-certa
git reset --hard HEAD~1
git switch branch-certa
git log --oneline -1    # o commit está aqui
```

</details>

**3.** Rode `git commit` sem `-m` para abrir o editor padrão. Se for o Vim, saia sem salvar.

<details>
<summary>Ver resposta</summary>

Aperte `Esc`, digite `:q!` e aperte `Enter`. O commit é cancelado, porque a mensagem ficou vazia.

</details>

---

<div align="center">

[⬅️ 8.4 GitHub Actions](./04-github-actions.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md)

</div>
