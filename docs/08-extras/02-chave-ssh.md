# 8.2 · Conectando ao GitHub com chave SSH

> **Em uma frase:** uma chave SSH é um par de "chaves digitais" que prova para o GitHub que você é você, sem precisar digitar senha ou token a cada `push`.

> [!NOTE]
> Conteúdo extra: esta aula não faz parte do curso original.

## 🔑 Como funciona?

O SSH usa **duas chaves** que só funcionam juntas:

| Chave | Arquivo | Pode compartilhar? |
| --- | --- | --- |
| 🔓 **Pública** | `id_ed25519.pub` | ✅ Sim, é ela que você cadastra no GitHub |
| 🔐 **Privada** | `id_ed25519` | ❌ **Nunca!** Fica só no seu computador |

> [!TIP]
> **Analogia:** a chave pública é um **cadeado** que você entrega ao GitHub; a privada é a **única chave** que abre esse cadeado. O GitHub tranca uma "mensagem" com o cadeado, e só quem tem a chave privada consegue abrir, provando que é você.

### HTTPS ou SSH?

| | HTTPS | SSH |
| --- | --- | --- |
| URL | `https://github.com/usuario/repo.git` | `git@github.com:usuario/repo.git` |
| Autenticação | Login pelo navegador / token | Chave SSH |
| Configuração | Quase nenhuma | Uma vez só (esta aula) |

Os dois funcionam bem. Muita gente prefere SSH porque, depois de configurado, nunca mais pede nada.

## 🛠️ Passo a passo

> [!IMPORTANT]
> No **Windows**, use o **Git Bash** para os comandos abaixo. No macOS e no Linux, use o Terminal.

### 1. Verifique se você já tem uma chave

```bash
ls ~/.ssh
```

Se aparecerem `id_ed25519` e `id_ed25519.pub`, você já tem uma chave e pode pular para o passo 3.

### 2. Gere uma chave nova

```bash
ssh-keygen -t ed25519 -C "seuemail@example.com"
```

- Quando perguntar onde salvar, aperte **Enter** para usar o local padrão.
- Quando pedir uma *passphrase* (senha da chave), você pode criar uma (mais seguro) ou apertar **Enter** para deixar sem.

### 3. Adicione a chave ao ssh-agent

O *ssh-agent* é um programa que guarda sua chave carregada na memória.

```bash
# Git Bash (Windows) e Linux
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# macOS (guarda a passphrase no Keychain)
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

### 4. Copie a chave **pública**

```bash
# Git Bash (Windows)
clip < ~/.ssh/id_ed25519.pub

# macOS
pbcopy < ~/.ssh/id_ed25519.pub

# Linux (ou qualquer sistema): mostre e copie manualmente
cat ~/.ssh/id_ed25519.pub
```

O texto copiado começa com `ssh-ed25519 ...` e termina com o seu e-mail.

### 5. Cadastre no GitHub

1. No GitHub, clique na sua foto → **Settings**.
2. No menu lateral, clique em **SSH and GPG keys**.
3. Clique em **New SSH key**.
4. Dê um título (ex.: "Notebook pessoal"), cole a chave no campo **Key** e clique em **Add SSH key**.

### 6. Teste a conexão

```bash
ssh -T git@github.com
```

Na primeira vez, aparece uma pergunta sobre a "autenticidade do host". Digite **`yes`**. Se der tudo certo, você verá:

```text
Hi seu-usuario! You've successfully authenticated, but GitHub does not provide shell access.
```

### 7. Use URLs SSH

Para novos clones, escolha a aba **SSH** no botão **"<> Code"** do GitHub:

```bash
git clone git@github.com:usuario/repositorio.git
```

Para um repositório que já usa HTTPS, troque a URL do remoto:

```bash
git remote set-url origin git@github.com:usuario/repositorio.git
git remote -v
```

> [!CAUTION]
> **Nunca** compartilhe, envie por mensagem ou faça commit da chave **privada** (o arquivo **sem** `.pub`). Se ela vazar, apague a chave em **Settings → SSH and GPG keys** e gere outra.

## 📌 Resumindo

- Chave **pública** vai para o GitHub; chave **privada** nunca sai do seu computador.
- Fluxo: `ssh-keygen` → `ssh-add` → copiar a `.pub` → **Settings → SSH and GPG keys** → `ssh -T git@github.com`.
- Use URLs no formato `git@github.com:usuario/repo.git`.

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Configure uma chave SSH e teste a conexão com o GitHub.

<details>
<summary>Ver resposta</summary>

Siga os passos 2 a 6 desta aula. O teste final é:

```bash
ssh -T git@github.com
# Hi seu-usuario! You've successfully authenticated...
```

</details>

**2.** Troque o remoto do seu `treino-git` de HTTPS para SSH e faça um push.

<details>
<summary>Ver resposta</summary>

```bash
git remote set-url origin git@github.com:SEU-USUARIO/treino-git.git
git push
```

</details>

**3.** Qual dos dois arquivos você cola no GitHub: `id_ed25519` ou `id_ed25519.pub`?

<details>
<summary>Ver resposta</summary>

O **`id_ed25519.pub`**, a chave **pública**. O arquivo sem `.pub` é a chave privada e nunca deve ser compartilhado.

</details>

---

<div align="center">

[⬅️ 8.1 git stash](./01-git-stash.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [8.3 GitHub Flow ➡️](./03-github-flow.md)

</div>
