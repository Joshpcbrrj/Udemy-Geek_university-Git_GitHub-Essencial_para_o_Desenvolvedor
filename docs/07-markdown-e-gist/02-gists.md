# 7.2 · Entendendo Gists

> **Em uma frase:** um *Gist* é um jeito rápido de guardar e compartilhar **pequenos trechos de código ou anotações** no GitHub, sem precisar criar um repositório inteiro.

<img src="./img/1.webp" alt="Logo do GitHub Gist" width="800">

## 📌 O que é um Gist?

Pense no Gist como um **post-it virtual para programadores**. Ele é perfeito para:

- 💡 guardar um **trecho de código** que você sempre esquece (um comando, uma função, uma configuração);
- 🤝 **compartilhar** uma solução rápida com alguém;
- 📝 fazer **anotações** em Markdown;
- 🧪 mostrar um **exemplo** em uma pergunta ou em um post.

Acesse em: **[gist.github.com](https://gist.github.com)**

> [!NOTE]
> Por baixo dos panos, **todo Gist é um repositório Git**. Ele tem histórico de versões (cada edição vira uma revisão), pode receber comentários, estrelas e até ser clonado com `git clone`.

## 🛠️ Como criar um Gist

1. Faça login no GitHub.
2. Clique no **+** no canto superior direito e escolha **New gist** (ou acesse [gist.github.com](https://gist.github.com)).
3. Escreva uma **descrição** curta sobre o que é o Gist.
4. Dê um **nome ao arquivo** **com a extensão** (ex.: `comandos-git.md`, `script.py`). A extensão define as cores do código.
5. Escreva ou cole o conteúdo.
6. (Opcional) Clique em **Add file** para incluir mais arquivos no mesmo Gist.
7. Escolha a visibilidade:
   - **Create public gist**: aparece no seu perfil e qualquer pessoa pode encontrar;
   - **Create secret gist**: não aparece em buscas, só quem tiver o link consegue ver.

Pronto! Você recebe um **link exclusivo** para compartilhar.

> [!WARNING]
> Um Gist **secreto não é privado**. Qualquer pessoa com o link consegue abrir. Nunca coloque senhas, tokens ou dados pessoais em um Gist.

## 💡 Dicas

- Adicione um arquivo **`README.md`** ao Gist para explicar o conteúdo com mais detalhes.
- Use o botão **Embed** para incorporar o Gist em um blog ou site.
- Em [gist.github.com/seu-usuario](https://gist.github.com) você vê todos os seus Gists.

## ⚖️ Gist x Repositório

| | Gist | Repositório |
| --- | --- | --- |
| Tamanho ideal | Trechos pequenos, poucos arquivos | Projetos completos |
| Pastas | ❌ Não suporta | ✅ Suporta |
| Issues e pull requests | ❌ Não | ✅ Sim |
| Histórico de versões | ✅ Sim | ✅ Sim |
| Criação | Rápida, direto no navegador | Um pouco mais de configuração |

## 📌 Resumindo

- Gist = pequeno repositório para trechos de código e anotações.
- Pode ser **público** ou **secreto** (secreto ≠ privado!).
- Tem histórico, comentários e pode ter vários arquivos, incluindo um `README.md`.

---

<div align="center">

[⬅️ 7.1 Markdown](./01-markdown.md) &nbsp;|&nbsp; [🏠 Índice](../../README.md)

</div>
