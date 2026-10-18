---
hide:
  - navigation
  - toc
---

# Git e GitHub Essencial

**Resumo completo do curso da Geek University, escrito para quem está começando do zero.** Linguagem simples, analogias, diagramas, exercícios com respostas e alertas sobre os erros mais comuns.

[Começar pela aula 1.1](01-introducao/01-controle-de-versao.md){ .md-button .md-button--primary }
[:material-clipboard-check-outline: Fazer o simulado](simulado/index.md){ .md-button }
[:material-book-open-variant: Baixar o EPUB](downloads/git-e-github-essencial.epub){ .md-button }
[:material-lightning-bolt: Guia rápido de comandos](guia-rapido.md){ .md-button }

## Como usar este material

- **Começando do zero?** Siga as aulas na ordem. No rodapé de cada página há links para a aula anterior e a próxima.
- **Já sabe o básico?** Use o menu ou a **busca** (atalho ++s++ ou ++f++) para ir direto ao assunto.
- **Precisa só lembrar um comando?** Vá para o [guia rápido](guia-rapido.md).
- **Quer testar o que aprendeu?** Faça o [simulado](simulado/index.md), com nota automática e explicação de cada resposta.
- **Prefere ler offline?** Baixe o [EPUB](downloads/git-e-github-essencial.epub) e abra em qualquer leitor de e-books (Apple Books, Google Play Livros, Calibre ou Kindle, pelo "Enviar para Kindle").

Toda aula começa com um resumo **"Em uma frase"** e termina com **"Resumindo"** e exercícios **"🏋️ Mão na massa"**.

## O fluxo do Git em 30 segundos

```bash
git init                          # 1. Começa a versionar a pasta
git add .                         # 2. Prepara as alterações
git commit -m "Minha mensagem"    # 3. Salva um ponto no histórico
git remote add origin <url>       # 4. Conecta ao GitHub (só uma vez)
git push -u origin main           # 5. Envia para o GitHub
```

## Módulos

<div class="grid cards" markdown>

-   :material-flag-outline: **1 · Introdução**

    ---

    Controle de versão, o que é o Git, Git × GitHub e a configuração inicial.

    [:octicons-arrow-right-24: Começar](01-introducao/01-controle-de-versao.md)

-   :material-source-commit: **2 · Git básico**

    ---

    As três áreas do Git, commits, `.gitignore`, histórico e como desfazer coisas.

    [:octicons-arrow-right-24: Começar](02-git-basico/01-como-o-git-funciona.md)

-   :material-source-branch: **3 · Git intermediário**

    ---

    Branches, merge, rebase, clone, push, fetch, pull e tags.

    [:octicons-arrow-right-24: Começar](03-git-intermediario/01-branches.md)

-   :material-github: **4 · Git avançado**

    ---

    GitHub na prática, colaboradores, reset, revert e resolução de conflitos.

    [:octicons-arrow-right-24: Começar](04-git-avancado/01-repositorio-remoto.md)

-   :material-account-group-outline: **5 · Open source**

    ---

    Issues, fork e pull requests: como contribuir com projetos de outras pessoas.

    [:octicons-arrow-right-24: Começar](05-open-source/01-issues.md)

-   :material-card-account-details-outline: **6 · Currículo online**

    ---

    Um site gratuito no GitHub Pages e extensões do Git para o VS Code.

    [:octicons-arrow-right-24: Começar](06-curriculo-online/01-curriculo-e-plugins.md)

-   :material-language-markdown-outline: **7 · Markdown e Gist**

    ---

    Toda a sintaxe do Markdown, com exemplos, e como compartilhar código com Gists.

    [:octicons-arrow-right-24: Começar](07-markdown-e-gist/01-markdown.md)

-   :material-star-outline: **8 · Extras**

    ---

    Além do curso: `git stash`, chave SSH, GitHub Flow, GitHub Actions e erros comuns.

    [:octicons-arrow-right-24: Começar](08-extras/01-git-stash.md)

</div>

## Sobre

Anotações de **[Josué B. Almeida](https://github.com/Joshpcbrrj)** sobre o curso **Git e GitHub Essencial para o Desenvolvedor**, da **Geek University** (Udemy). O código-fonte deste site está no [GitHub](https://github.com/Joshpcbrrj/Udemy-Geek_university-Git_GitHub-Essencial_para_o_Desenvolvedor): encontrou um erro? Abra uma issue ou envie um pull request.

O texto está sob a licença **CC BY 4.0**. Os PDFs de material de apoio e outras imagens que vêm do curso pertencem à Geek University.
