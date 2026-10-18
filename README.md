<div align="center">

<img src="./docs/01-introducao/img/1.png" alt="Banner do curso Git e GitHub da Geek University" width="720">

# Git e GitHub Essencial para o Desenvolvedor

**Resumo completo do curso da Geek University (Udemy), escrito para quem está começando do zero.**

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=udemy&logoColor=white)

[📜 Certificado](./docs/certificado/certificado.pdf) ·
[📋 Conteúdo programático](./docs/certificado/conteudo-programatico.png) ·
[⚡ Guia rápido de comandos](./docs/guia-rapido.md)

</div>

---

## 👋 Sobre este repositório

Este repositório reúne as minhas anotações do curso **Git e GitHub Essencial para o Desenvolvedor**, da **Geek University**. A ideia é que ele sirva como um **material de estudo e consulta** para qualquer pessoa que esteja aprendendo Git e GitHub.

As explicações foram escritas em **linguagem simples**, com analogias, exemplos práticos e alertas sobre os erros mais comuns. Além do Git, o curso cobre **colaboração em projetos open source**, criação de um **currículo online** com GitHub Pages e **Markdown**.

## 🧭 Como usar este material

- **Começando do zero?** Siga as aulas **na ordem**. Cada aula tem links de "Anterior" e "Próximo" no final.
- **Já sabe o básico?** Use o índice abaixo para ir direto ao assunto.
- **Precisa só lembrar um comando?** Vá para o **[⚡ Guia rápido de comandos](./docs/guia-rapido.md)**.

Todas as aulas seguem o mesmo formato:

| Seção | O que tem |
| --- | --- |
| **Em uma frase** | O resumo da ideia principal, logo no começo |
| **Explicação** | O conceito com analogias e diagramas |
| **Na prática** | Os comandos, com comentários explicando cada um |
| **Alertas** | 💡 Dicas, ⚠️ cuidados e ❗ pontos importantes |
| **Resumindo** | Uma revisão rápida (geralmente uma tabela de comandos) |

## ⚡ O fluxo do Git em 30 segundos

```bash
git init                          # 1. Começa a versionar a pasta
git add .                         # 2. Prepara as alterações
git commit -m "Minha mensagem"    # 3. Salva um ponto no histórico
git remote add origin <url>       # 4. Conecta ao GitHub (só uma vez)
git push -u origin main           # 5. Envia para o GitHub
```

```text
 Pasta do projeto ──git add──▶ Staging ──git commit──▶ Repositório local ──git push──▶ GitHub
```

---

## 📚 Índice do conteúdo

### 1️⃣ Introdução ao Git e preparação do ambiente

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 1.1 | [O que é controle de versão?](./docs/01-introducao/01-controle-de-versao.md) | Por que versionar código; modelos centralizado x distribuído |
| 1.2 | [O que é Git?](./docs/01-introducao/02-o-que-e-git.md) | História e principais recursos do Git |
| 1.3 | [Git não é GitHub](./docs/01-introducao/03-git-nao-e-github.md) | A diferença entre a ferramenta e a plataforma |
| 1.4 | [Instalando e configurando o Git](./docs/01-introducao/04-instalando-o-git.md) | Instalação e configuração de nome e e-mail |
| 1.5 | [Registrando múltiplos usuários locais](./docs/01-introducao/05-usuarios-locais.md) | Configuração global x local e credenciais |

### 2️⃣ Git básico

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 2.1 | [Entendendo como o Git funciona](./docs/02-git-basico/01-como-o-git-funciona.md) | Repositório, snapshots e as três áreas do Git |
| 2.2 | [Ciclo de vida dos arquivos](./docs/02-git-basico/02-ciclo-de-vida-dos-arquivos.md) | Untracked, modified, staged e o fluxo completo |
| 2.3 | [Usando o .gitignore](./docs/02-git-basico/03-gitignore.md) | Como ignorar arquivos e pastas |
| 2.4 | [Como fazer commits](./docs/02-git-basico/04-commits.md) | Criar commits e escrever boas mensagens |
| 2.5 | [Consultando o histórico](./docs/02-git-basico/05-historico-do-projeto.md) | `git log` e seus filtros |
| 2.6 | [Voltando no tempo](./docs/02-git-basico/06-voltando-no-tempo.md) | Visão geral de checkout, reset e revert |
| 2.7 | [Comandos úteis](./docs/02-git-basico/07-comandos-uteis.md) | `git mv`, `git rm` e `git diff` |
| 2.8 | [Desfazendo e refazendo ações](./docs/02-git-basico/08-desfazendo-acoes.md) | `restore`, `reset`, `--amend`, squash e `revert` |

### 3️⃣ Git intermediário

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 3.1 | [Branches](./docs/03-git-intermediario/01-branches.md) | Criar, trocar, renomear e excluir branches |
| 3.2 | [Merge](./docs/03-git-intermediario/02-merge.md) | Juntar branches; fast-forward x commit de merge |
| 3.3 | [Rebase](./docs/03-git-intermediario/03-rebase.md) | Histórico linear, rebase interativo e a regra de ouro |
| 3.4 | [Clone e push](./docs/03-git-intermediario/04-clone-e-push.md) | Baixar repositórios e enviar commits |
| 3.5 | [Fetch e pull](./docs/03-git-intermediario/05-fetch-e-pull.md) | Trazer as novidades do repositório remoto |
| 3.6 | [Bare repository](./docs/03-git-intermediario/06-bare-repository.md) | O que é um repositório central |
| 3.7 | [Trabalhando com tags](./docs/03-git-intermediario/07-tags.md) | Marcar versões do projeto |

### 4️⃣ Git avançado

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 4.1 | [Repositório remoto no GitHub](./docs/04-git-avancado/01-repositorio-remoto.md) | Conectar um projeto local ao GitHub |
| 4.2 | [Usando clone e pull](./docs/04-git-avancado/02-clone-e-pull.md) | Rotina de trabalho com o remoto |
| 4.3 | [Adicionando colaboradores](./docs/04-git-avancado/03-colaboradores.md) | Convidar pessoas e níveis de permissão |
| 4.4 | [Consultando o histórico de commits](./docs/04-git-avancado/04-historico-de-commits.md) | Terminal, interfaces gráficas e GitHub |
| 4.5 | [Desfazendo ações com checkout](./docs/04-git-avancado/05-desfazendo-com-checkout.md) | Descartar alterações e visitar commits |
| 4.6 | [Desfazendo ações com revert e reset](./docs/04-git-avancado/06-revert-e-reset.md) | Os três modos do reset e quando usar revert |
| 4.7 | [Resolvendo conflitos](./docs/04-git-avancado/07-conflitos.md) | Entender e resolver conflitos passo a passo |

### 5️⃣ Colaborando com projetos open source

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 5.1 | [O que são issues?](./docs/05-open-source/01-issues.md) | Relatar bugs e fechar issues por commit |
| 5.2 | [Trabalhando com fork](./docs/05-open-source/02-fork.md) | Copiar projetos e manter o fork atualizado |
| 5.3 | [Pull requests](./docs/05-open-source/03-pull-requests.md) | Enviar, revisar, testar e aceitar PRs |

### 6️⃣ Criação de currículo online

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 6.1 | [Currículo online + plugins do VS Code](./docs/06-curriculo-online/01-curriculo-e-plugins.md) | GitHub Pages, GitLens e Git History |

### 7️⃣ Markdown, README e Gist

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 7.1 | [Entendendo o Markdown](./docs/07-markdown-e-gist/01-markdown.md) | Toda a sintaxe, com exemplos e resultado |
| 7.2 | [Entendendo Gists](./docs/07-markdown-e-gist/02-gists.md) | Compartilhar trechos de código rapidamente |
| 📄 | [Modelo de README](./docs/07-markdown-e-gist/modelo-readme/modelo-de-readme.md) | Um template para usar nos seus projetos |

---

## 🤝 Encontrou um erro ou quer sugerir uma melhoria?

Fique à vontade para contribuir! É uma ótima forma de praticar o que está no [Módulo 5](./docs/05-open-source/01-issues.md):

- abra uma **[issue](https://github.com/Joshpcbrrj/Udemy-Geek_university-Git_GitHub-Essencial_para_o_Desenvolvedor/issues)** descrevendo o problema ou a sugestão; ou
- faça um **fork**, corrija e envie um **pull request**.

## 🙏 Créditos

- Curso: **Git e GitHub Essencial para o Desenvolvedor**, da **Geek University**, na Udemy.
- Anotações e resumo: **[Josué B. Almeida](https://github.com/Joshpcbrrj)**.

<div align="center">

Se este material te ajudou, deixe uma ⭐ no repositório!

</div>
