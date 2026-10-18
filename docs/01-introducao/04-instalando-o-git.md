# 1.4 · Instalando e configurando o Git

> **Em uma frase:** instale o Git, diga a ele **quem você é** (nome e e-mail) e pronto: você já pode começar a versionar seus projetos.

## 1️⃣ Instalação

Baixe o instalador para o seu sistema na página oficial: **[git-scm.com/downloads](https://git-scm.com/downloads)**

| Sistema | Como instalar |
| --- | --- |
| **Windows** | Baixe o instalador e avance com as opções padrão. Ele instala também o **Git Bash**, um terminal que aceita comandos no estilo Linux. |
| **macOS** | Rode `git --version` no Terminal. Se o Git não estiver instalado, o sistema oferece instalar. Também dá para usar `brew install git`. |
| **Linux (Debian/Ubuntu)** | `sudo apt install git` |

Depois de instalar, abra o terminal e confira se deu certo:

```bash
git --version
# Exemplo de saída: git version 2.45.1
```

Se aparecer a versão, está tudo certo. ✅

## 2️⃣ Configuração inicial (obrigatória)

Todo commit que você fizer vai levar uma "assinatura" com seu **nome** e **e-mail**. Por isso, o Git pede que você configure essas informações antes do primeiro commit.

```bash
# Seu nome (como vai aparecer no histórico)
git config --global user.name "Seu Nome"

# Seu e-mail (use o mesmo da sua conta do GitHub)
git config --global user.email "seuemail@example.com"
```

> [!IMPORTANT]
> Use o **mesmo e-mail da sua conta do GitHub**. É assim que o GitHub liga os seus commits ao seu perfil (e conta os "quadradinhos verdes" de contribuição).

### O que significa o `--global`?

A opção `--global` salva a configuração para **todos os projetos** do seu usuário no computador. Você só precisa fazer isso **uma vez**. Na próxima aula você vai ver como usar uma configuração diferente para um projeto específico.

## 3️⃣ Configurações opcionais (mas úteis)

```bash
# Define o editor de texto que o Git vai abrir quando precisar
# (por exemplo, para escrever uma mensagem de commit longa).
# Para usar o VS Code:
git config --global core.editor "code --wait"
# Outras opções comuns: "vim", "nano", "notepad"

# Faz o nome da branch inicial de novos repositórios ser "main"
# (padrão usado hoje pelo GitHub)
git config --global init.defaultBranch main
```

## 4️⃣ Conferindo as configurações

```bash
# Lista todas as configurações globais
git config --global --list

# Mostra o valor de uma configuração específica
git config user.name
```

## 📌 Resumindo

| Comando | Para que serve |
| --- | --- |
| `git --version` | Ver se o Git está instalado (e qual versão) |
| `git config --global user.name "Nome"` | Definir seu nome |
| `git config --global user.email "email"` | Definir seu e-mail |
| `git config --global core.editor "code --wait"` | Definir o editor padrão |
| `git config --global --list` | Ver todas as configurações |

---

<div align="center">

[⬅️ 1.3 Git não é GitHub](./03-git-nao-e-github.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [1.5 Usuários locais ➡️](./05-usuarios-locais.md)

</div>
