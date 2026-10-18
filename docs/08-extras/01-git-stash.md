# 8.1 · Guardando alterações temporariamente com `git stash`

> **Em uma frase:** o `git stash` "guarda na gaveta" as alterações que você ainda não quer commitar, deixando a pasta limpa para fazer outra coisa. Depois você tira da gaveta e continua de onde parou.

> [!NOTE]
> As aulas do **Módulo 8** são **conteúdo extra**: não fazem parte do curso original da Geek University. Elas cobrem assuntos que quem está começando costuma precisar logo cedo.

## 🗄️ Para que serve?

Situação clássica: você está no meio de uma funcionalidade, com vários arquivos alterados, e chega um pedido urgente: *"corrige um bug na `main` agora!"*.

- Fazer commit do trabalho pela metade? Não é o ideal.
- Trocar de branch com tudo alterado? O Git pode não deixar ou levar as alterações junto.

O `stash` resolve isso: ele **guarda as alterações** em uma pilha separada e devolve a pasta ao estado do último commit.

```text
 Alterações em andamento ──git stash──▶ 🗄️ gaveta (pilha de stashes)
 Pasta limpa ◀─────────────────────────
 ... resolve o bug em outra branch ...
 Alterações de volta  ◀──git stash pop── 🗄️
```

## 🛠️ Comandos essenciais

```bash
# Guarda as alterações dos arquivos rastreados
git stash

# Guarda com uma descrição (recomendado, para lembrar depois)
git stash push -m "Formulário de login pela metade"

# Inclui também arquivos novos (untracked)
git stash -u

# Lista tudo o que está guardado
git stash list
# stash@{0}: On feature-login: Formulário de login pela metade
# stash@{1}: WIP on main: a1b2c3d Ajusta rodapé

# Mostra o que tem dentro de um stash
git stash show -p stash@{0}

# Tira da gaveta o mais recente e o REMOVE da lista
git stash pop

# Aplica um stash, mas o MANTÉM na lista
git stash apply stash@{1}

# Apaga um stash específico
git stash drop stash@{1}

# Apaga TODOS os stashes (cuidado!)
git stash clear
```

> [!TIP]
> `pop` = aplica **e** remove da lista. `apply` = aplica e **mantém** (útil para aplicar o mesmo stash em mais de uma branch).

## 🚑 O exemplo do bug urgente, passo a passo

```bash
# Você está na feature-login, com alterações pela metade
git stash push -m "Login pela metade"

# Vai corrigir o bug
git switch main
git switch -c corrige-bug
# ... corrige, testa ...
git commit -am "Corrige cálculo do total"

# Volta para o que estava fazendo
git switch feature-login
git stash pop
```

> [!WARNING]
> Se o `git stash pop` encontrar um conflito, o stash **não é removido** da lista. Resolva o conflito, dê `git add` e depois remova o stash com `git stash drop`.

> [!NOTE]
> O stash é **local**: não vai para o GitHub com o `git push`. Não use como backup de longo prazo; para isso, faça commits em uma branch.

## 📌 Resumindo

| Comando | O que faz |
| --- | --- |
| `git stash push -m "msg"` | Guarda as alterações com uma descrição |
| `git stash -u` | Guarda incluindo arquivos novos |
| `git stash list` | Lista os stashes |
| `git stash pop` | Aplica o mais recente e remove da lista |
| `git stash apply` | Aplica sem remover da lista |
| `git stash drop` | Apaga um stash |

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** No `treino-git`, altere um arquivo, guarde a alteração com uma descrição e confirme que a pasta ficou limpa.

<details>
<summary>Ver resposta</summary>

```bash
echo "rascunho" >> README.md
git stash push -m "Rascunho do README"
git status        # nothing to commit, working tree clean
git stash list    # stash@{0}: On main: Rascunho do README
```

</details>

**2.** Recupere a alteração e confira que o stash saiu da lista.

<details>
<summary>Ver resposta</summary>

```bash
git stash pop
git stash list    # vazio
```

</details>

**3.** Você criou o arquivo **novo** `ideia.txt` e rodou `git stash`. O arquivo foi guardado?

<details>
<summary>Ver resposta</summary>

**Não.** Por padrão, o stash só guarda arquivos **rastreados**. Para incluir arquivos novos, use `git stash -u`.

</details>

---

<div align="center">

[⬅️ 7.2 Gists](../07-markdown-e-gist/02-gists.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [8.2 Chave SSH ➡️](./02-chave-ssh.md)

</div>
