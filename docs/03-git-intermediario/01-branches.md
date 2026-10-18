# 3.1 · Branches

> **Em uma frase:** uma branch é uma "linha do tempo paralela" do projeto, onde você pode trabalhar à vontade sem mexer na versão principal.

<img src="./img/1.jpg" alt="Diagrama de branches no Git" width="800">

## 🌳 O que é uma branch?

Imagine que seu projeto é um livro. A branch `main` é a versão oficial. Você quer testar um final alternativo, mas sem estragar o livro original. Então você faz uma **cópia de rascunho**, escreve o final novo nela e, se ficar bom, incorpora ao livro oficial. Se ficar ruim, é só jogar o rascunho fora.

Uma branch é esse rascunho, com uma grande vantagem: ela é **leve e instantânea**. Por baixo dos panos, uma branch é só um **ponteiro** (uma etiqueta) que aponta para um commit. Quando você faz um novo commit na branch, a etiqueta avança junto.

```text
main:     A ── B ── C
                     \
feature:              D ── E   ← você está trabalhando aqui
```

### Quando usar branches?

- Desenvolver uma **nova funcionalidade** sem afetar o código que já funciona.
- **Corrigir um bug** de forma isolada.
- **Experimentar** uma ideia sem compromisso.
- Permitir que **várias pessoas** trabalhem ao mesmo tempo, cada uma na sua branch.

> [!NOTE]
> A branch principal costuma se chamar **`main`** (em projetos mais antigos, **`master`**). É a versão "oficial" do projeto.

## 🛠️ Comandos essenciais

### Ver as branches

```bash
# Lista as branches locais (a atual aparece com * na frente)
git branch

# Lista também as branches do repositório remoto
git branch -a

# Mostra só o nome da branch atual
git branch --show-current
```

### Criar uma branch

```bash
git branch nome-da-branch
```

Isso **só cria** a branch. Você continua na branch em que estava.

### Trocar de branch

```bash
# Forma moderna (recomendada)
git switch nome-da-branch

# Forma tradicional (ainda muito usada)
git checkout nome-da-branch
```

### Criar e já trocar para a nova branch

```bash
# Forma moderna
git switch -c nome-da-branch

# Forma tradicional
git checkout -b nome-da-branch
```

> [!TIP]
> Antes de trocar de branch, faça commit (ou guarde) suas alterações. Se houver mudanças não salvas que conflitem com a outra branch, o Git não deixa trocar, para você não perder trabalho.

### Renomear uma branch

```bash
# Renomeia uma branch específica
git branch -m nome-atual novo-nome

# Renomeia a branch em que você está
git branch -m novo-nome
```

### Excluir uma branch

```bash
# Exclui apenas se ela já foi mesclada (seguro)
git branch -d nome-da-branch

# Força a exclusão, mesmo sem merge (cuidado!)
git branch -D nome-da-branch
```

> [!NOTE]
> Você não consegue excluir a branch em que está. Troque para outra antes.

### Ver o histórico de uma branch

```bash
git log nome-da-branch

# Visualizar todas as branches em forma de gráfico
git log --graph --oneline --decorate --all
```

### Juntar uma branch na atual

```bash
# Estando na main, traz as alterações da feature
git switch main
git merge nome-da-branch
```

Isso é o **merge**, assunto da [próxima aula](./02-merge.md).

## 📌 Resumindo

| Comando | O que faz |
| --- | --- |
| `git branch` | Lista as branches |
| `git branch nome` | Cria uma branch |
| `git switch nome` | Troca de branch |
| `git switch -c nome` | Cria e troca de branch |
| `git branch -m novo-nome` | Renomeia a branch atual |
| `git branch -d nome` | Exclui uma branch já mesclada |
| `git merge nome` | Junta a branch `nome` na branch atual |

---

<div align="center">

[⬅️ 2.8 Desfazendo ações](../02-git-basico/08-desfazendo-acoes.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [3.2 Merge ➡️](./02-merge.md)

</div>
