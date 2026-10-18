# 2.3 · Fazendo uso do `.gitignore`

> **Em uma frase:** o `.gitignore` é um arquivo de texto onde você lista os arquivos e pastas que o Git deve **fingir que não existem**.

## 🤔 Para que serve?

Nem tudo o que está na pasta do projeto deve ir para o histórico. Exemplos clássicos:

- 🔑 **Arquivos sensíveis:** senhas, chaves de API, arquivos `.env`.
- 📦 **Dependências baixadas:** pastas como `node_modules/` ou `venv/`, que podem ser reinstaladas a qualquer momento.
- ⚙️ **Arquivos gerados automaticamente:** builds, `*.log`, arquivos compilados.
- 💻 **Arquivos do seu sistema/editor:** `.DS_Store` (macOS), `Thumbs.db` (Windows), `.vscode/`.

Listando esses itens no `.gitignore`, eles **não aparecem** no `git status` e **não entram** no `git add .` por acidente.

## 📝 Como criar

1. Na **raiz do projeto** (mesma pasta onde está a `.git`), crie um arquivo chamado exatamente **`.gitignore`** (com o ponto no começo e sem extensão).
2. Escreva um padrão por linha.
3. Faça commit do `.gitignore`, assim todo mundo do projeto usa as mesmas regras.

## 🔣 Regras básicas dos padrões

| Padrão | O que ignora |
| --- | --- |
| `arquivo.txt` | Qualquer arquivo com esse nome, em qualquer pasta |
| `*.log` | Todos os arquivos que terminam com `.log` (`*` = "qualquer coisa") |
| `pasta/` | A pasta inteira (a barra `/` no final indica que é uma pasta) |
| `/config.ini` | Só o `config.ini` que está na **raiz** do projeto (a barra no início fixa a raiz) |
| `**/temp` | Qualquer arquivo ou pasta `temp`, em **qualquer nível** de subpasta |
| `!importante.log` | **Exceção:** não ignore este arquivo, mesmo que outra regra o pegue |
| `# texto` | Comentário (o Git ignora a linha) |

## 💡 Exemplo de `.gitignore`

```gitignore
# Logs gerados automaticamente
*.log

# Mas este log específico deve ser versionado
!importante.log

# Dependências (podem ser reinstaladas)
node_modules/
/libs/

# Arquivos de configuração com senhas
.env
config.ini

# Tudo dentro da pasta "temp" da raiz
temp/*

# Pastas "cache" em qualquer nível do projeto
**/cache/

# Arquivos do sistema operacional
.DS_Store
Thumbs.db
```

> [!WARNING]
> O `.gitignore` só funciona para arquivos que **ainda não são rastreados**. Se você já fez commit de um arquivo e depois o colocou no `.gitignore`, o Git continua acompanhando. Para parar de rastrear (sem apagar do seu computador), use:
>
> ```bash
> git rm --cached nome_do_arquivo
> git commit -m "Para de rastrear nome_do_arquivo"
> ```

> [!TIP]
> Não precisa escrever tudo do zero! O site **[gitignore.io](https://www.toptal.com/developers/gitignore)** e o repositório **[github/gitignore](https://github.com/github/gitignore)** têm modelos prontos para cada linguagem (Node, Python, Java etc.). O GitHub também oferece esses modelos quando você cria um repositório novo.

## 📌 Resumindo

- `.gitignore` lista o que o Git deve ignorar: senhas, dependências, arquivos gerados e de sistema.
- Use `*` para "qualquer coisa", `/` no fim para pastas, `**/` para qualquer nível e `!` para exceções.
- Arquivos que já foram commitados precisam de `git rm --cached` para deixarem de ser rastreados.

---

<div align="center">

[⬅️ 2.2 Ciclo de vida dos arquivos](./02-ciclo-de-vida-dos-arquivos.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [2.4 Commits ➡️](./04-commits.md)

</div>
