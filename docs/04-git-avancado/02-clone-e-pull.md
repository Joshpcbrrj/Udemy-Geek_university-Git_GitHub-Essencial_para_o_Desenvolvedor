# 4.2 · Usando clone e pull

> **Em uma frase:** use `git clone` **uma vez** para baixar o projeto do GitHub e `git pull` **sempre** que quiser trazer as novidades que outras pessoas enviaram.

## 📥 Clonando um repositório do GitHub

1. Abra a página do repositório no GitHub.
2. Clique no botão verde **"<> Code"** e copie a URL.
3. No terminal, vá até a pasta onde quer guardar o projeto e rode:

```bash
git clone https://github.com/usuario/repositorio.git
```

O Git cria uma pasta com todos os arquivos, todas as branches e todo o histórico, e já configura o remoto `origin`. (Mais opções do `clone` na aula [3.4](../03-git-intermediario/04-clone-e-push.md).)

## 🔄 Mantendo o projeto atualizado com `git pull`

Enquanto você trabalha, outras pessoas podem estar enviando commits para o GitHub. O `git pull` (que é um `fetch` + `merge`, como visto na aula [3.5](../03-git-intermediario/05-fetch-e-pull.md)) traz essas novidades para a sua máquina.

```bash
# 1. Confira se você está na branch certa
git switch main      # ou: git checkout main

# 2. Traga as novidades do remoto para essa branch
git pull
```

Se a branch não estiver ligada a uma branch remota, informe o remoto e a branch:

```bash
git pull origin main
```

> [!NOTE]
> O `git pull origin main` traz a `main` do remoto **para a branch em que você está agora**. Ele não atualiza outra branch "à distância". Por isso, sempre confira em qual branch você está antes de rodar o comando.

> [!WARNING]
> Se você e outra pessoa alteraram as **mesmas linhas**, o pull vai parar com um **conflito**. Você precisa resolvê-lo manualmente; veja a aula [4.7 Resolvendo conflitos](./07-conflitos.md).

## 💡 Rotina recomendada

```bash
git pull                     # 1. Atualiza antes de começar
# ... trabalha nos arquivos ...
git add .                    # 2. Prepara
git commit -m "Mensagem"     # 3. Registra
git pull                     # 4. Atualiza de novo (alguém pode ter enviado algo)
git push                     # 5. Envia
```

## 📌 Resumindo

- `git clone <url>`: baixa o projeto completo (só uma vez).
- `git pull`: traz as novidades do remoto para a branch atual (= `fetch` + `merge`).
- Sempre confira a branch atual antes do `pull` e faça `pull` antes do `push`.

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Edite o `README.md` do seu `treino-git` **pelo site do GitHub** (ícone de lápis) e depois traga essa alteração para o seu computador.

<details>
<summary>Ver resposta</summary>

```bash
git switch main
git pull
```

</details>

**2.** Você rodou `git pull` e apareceu `Already up to date.` O que isso significa?

<details>
<summary>Ver resposta</summary>

Que não há nada novo no remoto: sua branch local já tem todos os commits da branch remota.

</details>

**3.** Coloque a rotina na ordem certa: `git push`, `git commit`, `git pull` (antes de começar), `git add`, `git pull` (antes de enviar).

<details>
<summary>Ver resposta</summary>

`git pull` → (trabalhar) → `git add` → `git commit` → `git pull` → `git push`.

</details>

---

<div align="center">

[⬅️ 4.1 Repositório remoto](./01-repositorio-remoto.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [4.3 Colaboradores ➡️](./03-colaboradores.md)

</div>
