# 4.1 · Repositório remoto no GitHub

> **Em uma frase:** um repositório remoto é uma cópia do seu projeto guardada em um servidor (como o GitHub), e o comando `git remote` é o que conecta o seu repositório local a ela.

## ☁️ O que é um repositório remoto?

Até agora, tudo estava **só no seu computador**. Um **repositório remoto** é uma versão do projeto hospedada na internet que serve para:

- 💾 ter um **backup** do seu código;
- 👥 **compartilhar** e trabalhar em equipe;
- 🌍 **mostrar** seus projetos (portfólio).

Cada remoto tem um **apelido** e uma **URL**. O apelido padrão é **`origin`**.

> [!NOTE]
> Quando você **clona** um repositório, o Git já cria o remoto `origin` automaticamente, apontando para o endereço de onde você clonou. Você só precisa configurar manualmente quando criou o projeto do zero com `git init`.

## 🚀 Passo a passo: enviando um projeto local para o GitHub

### 1. Crie o repositório no GitHub

No GitHub, clique em **"+" → "New repository"**, dê um nome e clique em **"Create repository"**.

> [!TIP]
> Se você já tem o projeto no computador, crie o repositório no GitHub **vazio** (sem marcar README, `.gitignore` ou licença). Assim você evita um conflito logo no primeiro push.

### 2. Conecte o repositório local ao remoto

```bash
# Formato
git remote add <apelido> <URL-do-repositório>

# Na prática
git remote add origin https://github.com/seu-usuario/meu-repositorio.git
```

### 3. Envie seus commits

```bash
git push -u origin main
```

O `-u` liga a sua branch `main` local à `main` do GitHub. Nas próximas vezes, basta usar `git push`.

Pronto! Atualize a página do repositório no GitHub e seus arquivos estarão lá. 🎉

## 🛠️ Gerenciando remotos

```bash
# Lista os remotos configurados e suas URLs
git remote -v

# Exemplo de saída:
# origin  https://github.com/seu-usuario/meu-repositorio.git (fetch)
# origin  https://github.com/seu-usuario/meu-repositorio.git (push)

# Troca a URL de um remoto (ex.: você renomeou o repositório no GitHub)
git remote set-url origin https://github.com/seu-usuario/novo-nome.git

# Renomeia o apelido de um remoto
git remote rename origin github

# Remove a conexão com um remoto (não apaga nada no GitHub)
git remote remove origin
# ou, abreviado:
git remote rm origin
```

> [!IMPORTANT]
> Para enviar código (`push`), você precisa ter **permissão** no repositório e estar **autenticado**. Na primeira vez, o Git vai pedir login; veja como funciona na aula [1.5](../01-introducao/05-usuarios-locais.md).

## 📌 Resumindo

| Comando | O que faz |
| --- | --- |
| `git remote add origin <url>` | Conecta o repositório local a um remoto |
| `git remote -v` | Lista os remotos |
| `git remote set-url origin <url>` | Muda a URL do remoto |
| `git remote remove origin` | Remove a conexão com o remoto |
| `git push -u origin main` | Primeiro envio da branch `main` |

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Crie um repositório **vazio** no GitHub chamado `treino-git` e envie para ele o seu repositório local de treino.

<details>
<summary>Ver resposta</summary>

```bash
git remote add origin https://github.com/SEU-USUARIO/treino-git.git
git push -u origin main
```
Atualize a página do repositório no GitHub para ver seus arquivos.

</details>

**2.** Você renomeou o repositório no GitHub para `meu-treino`. Como atualizar o endereço no seu computador?

<details>
<summary>Ver resposta</summary>

```bash
git remote set-url origin https://github.com/SEU-USUARIO/meu-treino.git
git remote -v
```

</details>

**3.** Rodar `git remote remove origin` apaga o repositório no GitHub?

<details>
<summary>Ver resposta</summary>

**Não.** Ele só remove a "ligação" no seu computador. O repositório no GitHub continua intacto.

</details>

---

<div align="center">

[⬅️ 3.7 Tags](../03-git-intermediario/07-tags.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [4.2 Clone e pull ➡️](./02-clone-e-pull.md)

</div>
