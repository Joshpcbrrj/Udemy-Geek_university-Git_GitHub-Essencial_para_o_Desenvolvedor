# 1.5 · Registrando múltiplos usuários locais no Git

> **Em uma frase:** além da configuração global, você pode definir um nome e e-mail **diferentes para um projeto específico**, o que é útil quando você usa uma conta pessoal e outra do trabalho no mesmo computador.

## 🌍 Global x 📁 Local

O Git tem níveis de configuração. Os dois que você mais vai usar são:

| Nível | Comando | Vale para | Onde fica salvo |
| --- | --- | --- | --- |
| **Global** | `git config --global ...` | Todos os projetos do seu usuário | Arquivo `.gitconfig` na sua pasta de usuário |
| **Local** | `git config ...` (sem `--global`) | Só o repositório atual | Arquivo `.git/config` dentro do projeto |

> [!TIP]
> A configuração **local sempre vence** a global. Então você pode deixar sua conta pessoal como global e sobrescrever só nos projetos do trabalho (ou o contrário).

## 💻 Configurando um usuário só para um projeto

Abra o terminal **dentro da pasta do projeto** (que já precisa ser um repositório Git) e rode os comandos **sem** o `--global`:

```bash
git config user.name "Seu Nome do Trabalho"
git config user.email "voce@empresa.com"
```

Para conferir qual usuário está valendo naquele projeto:

```bash
git config user.name
git config user.email

# Mostra todas as configurações e de qual arquivo cada uma veio
git config --list --show-origin
```

Para remover a configuração local (e voltar a usar a global):

```bash
git config --unset user.name
git config --unset user.email
```

## 🔐 E o login no GitHub? (credenciais)

Nome e e-mail servem só para **assinar os commits**. Eles **não** são o seu login. Quando você envia código para o GitHub (`git push`), o GitHub precisa saber se você tem permissão, e para isso pede uma **credencial**.

> [!IMPORTANT]
> Desde 2021 o GitHub **não aceita mais a senha da conta** no terminal. Você precisa usar um **Personal Access Token (PAT)**, uma chave SSH ou o login pelo navegador.

### Opção recomendada: Git Credential Manager

No **Windows** e no **macOS**, o instalador do Git já vem com o **Git Credential Manager**. Na primeira vez que você fizer `git push`, ele abre o navegador para você fazer login no GitHub e guarda a credencial de forma segura. Depois disso, não pergunta mais.

### O "helper" de credenciais

O Git usa um *credential helper* para decidir **como guardar** suas credenciais:

| Helper | O que faz |
| --- | --- |
| `manager` | Usa o Git Credential Manager (seguro, recomendado). |
| `cache` | Guarda na memória por um tempo (padrão: 15 minutos). Só Linux/macOS. |
| `store` | Guarda em um arquivo de texto **sem criptografia** no seu disco. |
| `osxkeychain` | Usa o Keychain do macOS. |

```bash
# Definir o helper (exemplo usando o "store", só para aquele repositório)
git config credential.helper store

# Remover o helper configurado
git config --unset credential.helper
```

> [!WARNING]
> Evite colocar usuário e senha/token **dentro da URL** do repositório, como em
> `https://usuario:token@github.com/...`. Isso deixa sua credencial salva em texto puro no arquivo `.git/config` e ela pode vazar facilmente. Prefira o Git Credential Manager ou SSH.

## 📌 Resumindo

- `git config --global` vale para todos os projetos; `git config` (sem `--global`) vale só para o projeto atual.
- A configuração local tem prioridade sobre a global.
- Nome/e-mail **assinam** os commits; **credenciais** (token, SSH, login no navegador) dão **permissão** para enviar código ao GitHub.

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Crie uma pasta chamada `treino-git` (vamos usá-la nos próximos exercícios), transforme-a em repositório e configure um e-mail **só para ela**. Depois prove que a configuração local "vence" a global.

<details>
<summary>Ver resposta</summary>

```bash
mkdir treino-git
cd treino-git
git init
git config user.email "trabalho@empresa.com"

git config user.email            # mostra trabalho@empresa.com (local)
git config --global user.email   # mostra o seu e-mail global
```

</details>

**2.** Agora remova a configuração local, voltando a usar a global.

<details>
<summary>Ver resposta</summary>

```bash
git config --unset user.email
```

</details>

**3.** Por que não é uma boa ideia usar uma URL como `https://usuario:token@github.com/...`?

<details>
<summary>Ver resposta</summary>

Porque o token fica salvo **em texto puro** no arquivo `.git/config`. Qualquer pessoa ou programa com acesso à pasta consegue ler e usar sua credencial. Prefira o Git Credential Manager ou uma chave SSH.

</details>

---

<div align="center">

[⬅️ 1.4 Instalando o Git](./04-instalando-o-git.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [2.1 Como o Git funciona ➡️](../02-git-basico/01-como-o-git-funciona.md)

</div>
