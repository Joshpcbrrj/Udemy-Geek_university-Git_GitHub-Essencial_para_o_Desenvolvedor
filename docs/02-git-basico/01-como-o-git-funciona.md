# 2.1 · Entendendo como o Git funciona

> **Em uma frase:** o Git tira "fotos" (snapshots) do seu projeto sempre que você pede, e guarda essas fotos em ordem dentro de uma pasta escondida chamada `.git`.

<img src="./img/1.png" alt="Diagrama do funcionamento do Git" width="850">

📄 [Material de apoio em PDF](./img/pdf-como-o-git-funciona.pdf)

## 📦 1. Repositório

Um **repositório** (ou "repo") é simplesmente uma pasta de projeto que o Git está acompanhando. Você transforma qualquer pasta em repositório com:

```bash
git init
```

Esse comando cria uma pasta oculta chamada **`.git`**. É lá dentro que o Git guarda **todo o histórico** do projeto.

> [!WARNING]
> Nunca apague nem edite a pasta `.git` manualmente. Se ela for apagada, o histórico do projeto vai junto (os arquivos atuais continuam, mas o Git "esquece" tudo).

## 📸 2. Snapshots (commits)

Cada vez que você faz um **commit**, o Git tira uma **foto do estado de todos os arquivos** naquele momento e guarda essa foto no histórico.

- Arquivos que **não mudaram** não são copiados de novo: o Git só aponta para a versão que já tinha guardado. Por isso ele é tão leve.
- Cada commit recebe um **identificador único** (um *hash*, como `a1b2c3d`), usado para encontrar aquele ponto no histórico.
- Cada commit sabe qual foi o commit **anterior**, formando uma "linha do tempo".

```text
(commit 1) ← (commit 2) ← (commit 3)   ← você está aqui
```

## 🗃️ 3. As três áreas do Git

Este é o conceito mais importante para entender o Git. Todo arquivo passa por três "lugares":

| Área | Também chamada de | O que é |
| --- | --- | --- |
| **Working Directory** | Diretório de trabalho | A pasta do projeto, onde você edita os arquivos normalmente. |
| **Staging Area** | Área de preparação, *index* | Uma "sala de espera" onde você coloca as alterações que vão entrar no próximo commit. |
| **Repository** | Repositório local, `.git` | Onde os commits ficam guardados para sempre. |

```text
 Working Directory  ──git add──▶  Staging Area  ──git commit──▶  Repositório
   (você edita)                (você escolhe)              (fica registrado)
```

> [!TIP]
> **Analogia da mudança de casa:** a casa é o *working directory*; a caixa de papelão onde você vai colocando os itens é a *staging area*; quando você fecha a caixa com fita e escreve uma etiqueta, isso é o *commit*.

## 🌿 4. Branches (ramificações)

Uma **branch** é uma linha de desenvolvimento independente. Você pode criar uma branch para testar uma nova funcionalidade sem afetar a versão principal (normalmente chamada de `main`). Depois, se der certo, você junta essa branch na principal.

## 🔀 5. Merge (mesclagem)

**Merge** é o ato de juntar o trabalho de uma branch em outra. Na maioria das vezes o Git faz isso sozinho. Quando duas pessoas alteram **a mesma linha** do mesmo arquivo, acontece um **conflito**, que você resolve manualmente.

## ☁️ 6. Repositórios remotos

Até aqui, tudo acontece **no seu computador**. Um **repositório remoto** é uma cópia do projeto em um servidor (como o GitHub). Você usa:

- `git push` para **enviar** seus commits para o remoto;
- `git pull` para **trazer** os commits de outras pessoas para a sua máquina.

## 🕵️ 7. Histórico e rastreamento

Como cada commit guarda autor, data e mensagem, o Git consegue mostrar **toda a evolução do projeto**: quem mudou o quê, quando e por quê. Isso ajuda a encontrar a origem de bugs e a entender decisões antigas.

## 📌 Resumindo

- `git init` transforma uma pasta em repositório (cria a pasta `.git`).
- O Git guarda o projeto como uma sequência de **snapshots** chamados **commits**.
- Todo arquivo passa por três áreas: **Working Directory → Staging Area → Repositório**.
- **Branches** permitem trabalhar em paralelo; **merge** junta esse trabalho; **remotos** permitem compartilhar.

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** Na pasta `treino-git`, confirme que existe a pasta oculta `.git`.

<details>
<summary>Ver resposta</summary>

```bash
ls -a                  # Git Bash, Linux ou macOS
Get-ChildItem -Force   # PowerShell
```
A pasta `.git` deve aparecer na lista. (Se você ainda não rodou `git init` nela, rode antes.)

</details>

**2.** Explique as três áreas do Git (working directory, staging area e repositório) usando uma analogia **sua**, diferente da caixa de mudança.

<details>
<summary>Ver resposta</summary>

Um exemplo: **fazer compras**. O *working directory* são as prateleiras do mercado, onde você escolhe os produtos; a *staging area* é o carrinho, onde ficam os itens que você decidiu levar; o *commit* é passar no caixa e receber o cupom fiscal, que fica registrado para sempre.

</details>

**3.** Quando você faz um commit, o Git guarda uma cópia nova de **todos** os arquivos do projeto?

<details>
<summary>Ver resposta</summary>

Não. Ele guarda uma "foto" do estado do projeto, mas os arquivos que **não mudaram** não são copiados de novo: o Git só aponta para a versão que já tinha. Por isso o histórico ocupa pouco espaço.

</details>

---

<div align="center">

[⬅️ 1.5 Usuários locais](../01-introducao/05-usuarios-locais.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [2.2 Ciclo de vida dos arquivos ➡️](./02-ciclo-de-vida-dos-arquivos.md)

</div>
