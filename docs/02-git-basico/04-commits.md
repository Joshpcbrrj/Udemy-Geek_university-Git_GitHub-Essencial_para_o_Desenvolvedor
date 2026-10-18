# 2.4 · Como fazer os commits

> **Em uma frase:** um commit é um "ponto de salvamento" do seu projeto, com uma mensagem explicando o que mudou.

## 🎮 O que é um commit?

Pense nos *checkpoints* de um videogame. Cada vez que você passa de uma fase importante, o jogo salva seu progresso e, se algo der errado depois, você pode voltar para lá.

O commit é exatamente isso para o seu código. Cada commit guarda:

- uma **foto (snapshot)** de como os arquivos estavam;
- o **autor** (nome e e-mail que você configurou);
- a **data e hora**;
- uma **mensagem** descrevendo a alteração;
- um **identificador único** chamado *hash* (ex.: `3f9a2c1...`), usado para encontrar esse commit depois.

## 🛠️ Como fazer um commit (2 passos)

### 1. Escolha o que vai entrar no commit (`git add`)

```bash
# Um arquivo
git add index.html

# Vários arquivos
git add index.html style.css

# Tudo o que mudou na pasta atual
git add .
```

### 2. Registre o commit (`git commit`)

```bash
git commit -m "Adiciona página de login"
```

O `-m` significa *message*: a mensagem vai direto no comando. Se você rodar só `git commit` (sem `-m`), o Git abre o editor de texto configurado para você escrever a mensagem.

Pronto! O commit foi criado e agora faz parte do histórico.

## ⚡ Atalho: `git commit -a`

```bash
git commit -a -m "Corrige cor do botão"
# ou, juntando as opções:
git commit -am "Corrige cor do botão"
```

A opção `-a` faz o `git add` **automaticamente** de todos os arquivos **já rastreados** que foram modificados.

> [!WARNING]
> O `-a` **não inclui arquivos novos** (untracked). Para arquivos novos, você continua precisando do `git add`.

## ✍️ Como escrever boas mensagens de commit

A mensagem é para o "você do futuro" e para as outras pessoas do time. Algumas dicas:

- ✅ Seja **curto e específico** (até ~50 caracteres na primeira linha).
- ✅ Diga **o que** a alteração faz, de preferência com verbo no presente/imperativo: *"Adiciona"*, *"Corrige"*, *"Remove"*.
- ✅ Faça **um commit por assunto**. Não misture "corrige bug do login" com "muda a cor do rodapé".
- ❌ Evite mensagens genéricas como `"update"`, `"ajustes"`, `"aaaa"`.

| ❌ Ruim | ✅ Bom |
| --- | --- |
| `update` | `Atualiza instruções de instalação no README` |
| `arrumei umas coisas` | `Corrige cálculo de frete para o Norte` |
| `teste` | `Adiciona testes do formulário de cadastro` |

> [!TIP]
> Muitos projetos usam o padrão **[Conventional Commits](https://www.conventionalcommits.org/pt-br/)**, com prefixos como `feat:` (nova funcionalidade), `fix:` (correção) e `docs:` (documentação). Ex.: `fix: corrige validação de e-mail`.

## 📌 Resumindo

- Commit = ponto de salvamento com foto dos arquivos + autor + data + mensagem + hash.
- Fluxo: `git add` (escolher) → `git commit -m "mensagem"` (salvar).
- `git commit -am` adiciona e commita arquivos **já rastreados** de uma vez.
- Boas mensagens são curtas, específicas e falam de um assunto só.
- Todos os commits podem ser consultados depois com `git log` (próxima aula).

## 🏋️ Mão na massa

> Tente resolver antes de abrir a resposta. Os exercícios práticos usam a pasta `treino-git`, criada na aula 1.5.

**1.** No `treino-git`, faça três commits diferentes, cada um com uma alteração pequena e uma boa mensagem.

<details>
<summary>Ver resposta</summary>

Exemplo:
```bash
echo "Linha 1" >> ola.txt && git add ola.txt && git commit -m "Adiciona primeira linha em ola.txt"
echo "# Treino" > README.md && git add README.md && git commit -m "Cria README do projeto de treino"
echo "Linha 2" >> ola.txt && git commit -am "Adiciona segunda linha em ola.txt"
```

</details>

**2.** Reescreva estas mensagens de commit ruins para que fiquem claras: `update`, `fix`, `coisas`.

<details>
<summary>Ver resposta</summary>

Depende do que foi feito, mas, por exemplo: `Atualiza instruções de instalação no README`, `Corrige validação do campo de e-mail`, `Remove arquivos de teste não utilizados`. O importante é dizer **o que** mudou.

</details>

**3.** Você criou um arquivo **novo** e rodou `git commit -am "Adiciona arquivo"`. O arquivo entrou no commit?

<details>
<summary>Ver resposta</summary>

**Não.** O `-a` só inclui arquivos que **já são rastreados**. Para um arquivo novo, você precisa rodar `git add` antes.

</details>

---

<div align="center">

[⬅️ 2.3 .gitignore](./03-gitignore.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md) &nbsp;|&nbsp; [2.5 Histórico do projeto ➡️](./05-historico-do-projeto.md)

</div>
