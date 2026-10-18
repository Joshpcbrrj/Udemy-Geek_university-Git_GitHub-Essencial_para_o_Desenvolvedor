# 3.6 · Bare repository

> **Em uma frase:** um repositório *bare* ("vazio") é um repositório **só com o histórico**, sem os arquivos de trabalho. Ele serve como o "ponto central" para onde todo mundo envia e de onde todo mundo baixa código.

## 📦 Repositório normal x bare

| | Repositório normal | Repositório bare |
| --- | --- | --- |
| Tem os arquivos do projeto para editar? | ✅ Sim | ❌ Não |
| Tem o histórico (conteúdo da pasta `.git`)? | ✅ Sim | ✅ Sim (é só isso que ele tem) |
| Dá para editar arquivos e commitar nele? | ✅ Sim | ❌ Não |
| Recebe `push` com segurança? | ⚠️ Não é recomendado | ✅ Feito para isso |
| Uso típico | Seu computador | Servidor compartilhado |

> [!TIP]
> **Analogia:** pense em um repositório bare como um **cofre** de um banco. Ninguém trabalha dentro do cofre; as pessoas só **depositam** (`push`) e **retiram** (`pull`/`clone`).

## 🤔 Por que ele existe?

Se você enviasse commits (`push`) para um repositório normal onde alguém está editando arquivos, os arquivos dessa pessoa ficariam inconsistentes com o histórico. Como o repositório bare **não tem arquivos de trabalho**, esse problema não existe.

É por isso que servidores Git usam repositórios bare.

> [!NOTE]
> Quando você cria um repositório no **GitHub**, por baixo dos panos ele funciona como um repositório bare: é o ponto central para onde todo mundo faz push e de onde todo mundo faz pull.

## 🛠️ Criando um repositório bare

```bash
git init --bare meu-projeto.git
```

Por convenção, o nome de um repositório bare termina com **`.git`**.

### Exemplo prático: um "servidor" na sua própria máquina

Dá para simular um GitHub localmente usando uma pasta como servidor:

```bash
# 1. Cria o repositório central (o "servidor")
git init --bare /caminho/servidor/meu-projeto.git

# 2. Em outra pasta, clona como se fosse do GitHub
git clone /caminho/servidor/meu-projeto.git

# 3. Trabalha normalmente: commit, push, pull...
cd meu-projeto
git push origin main
```

Repositórios bare também podem ser acessados pela rede usando **HTTP/HTTPS** ou **SSH**.

## 📌 Resumindo

- Repositório bare = só o histórico, sem os arquivos de trabalho.
- Serve como repositório **central** para receber `push` e fornecer `pull`/`clone`.
- Criado com `git init --bare nome.git`.
- O GitHub funciona como um grande servidor de repositórios centrais.

---

<div align="center">

[⬅️ 3.5 Fetch e pull](./05-fetch-e-pull.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [3.7 Tags ➡️](./07-tags.md)

</div>
