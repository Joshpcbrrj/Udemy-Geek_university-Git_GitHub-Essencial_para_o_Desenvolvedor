<div align="center">

<img src="Conteúdo%20do%20curso/1%20-%20Introducao%20ao%20git%20e%20preparacao%20do%20ambiente/img/1.png" alt="Banner do curso Git e GitHub da Geek University" width="720">

# Git e GitHub Essencial para o Desenvolvedor

**Resumo completo do curso da Geek University (Udemy), escrito para quem está começando do zero.**

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=udemy&logoColor=white)

[📜 Certificado](Conteúdo%20do%20curso/Certificado/Certificado.pdf) ·
[📋 Conteúdo programático](Conteúdo%20do%20curso/Certificado/Conteudo.png) ·
[⚡ Guia rápido de comandos](Guia%20rápido%20de%20comandos.md)

</div>

---

## 👋 Sobre este repositório

Este repositório reúne as minhas anotações do curso **Git e GitHub Essencial para o Desenvolvedor**, da **Geek University**. A ideia é que ele sirva como um **material de estudo e consulta** para qualquer pessoa que esteja aprendendo Git e GitHub.

As explicações foram escritas em **linguagem simples**, com analogias, exemplos práticos e alertas sobre os erros mais comuns. Além do Git, o curso cobre **colaboração em projetos open source**, criação de um **currículo online** com GitHub Pages e **Markdown**.

## 🧭 Como usar este material

- **Começando do zero?** Siga as aulas **na ordem**. Cada aula tem links de "Anterior" e "Próximo" no final.
- **Já sabe o básico?** Use o índice abaixo para ir direto ao assunto.
- **Precisa só lembrar um comando?** Vá para o **[⚡ Guia rápido de comandos](Guia%20rápido%20de%20comandos.md)**.

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
| 1.1 | [O que é controle de versão?](Conteúdo%20do%20curso/1%20-%20Introducao%20ao%20git%20e%20preparacao%20do%20ambiente/1.1%20-%20O%20que%20é%20controle%20de%20versão%20do%20código.md) | Por que versionar código; modelos centralizado x distribuído |
| 1.2 | [O que é Git?](Conteúdo%20do%20curso/1%20-%20Introducao%20ao%20git%20e%20preparacao%20do%20ambiente/1.2%20-%20O%20que%20é%20Git.md) | História e principais recursos do Git |
| 1.3 | [Git não é GitHub](Conteúdo%20do%20curso/1%20-%20Introducao%20ao%20git%20e%20preparacao%20do%20ambiente/1.3%20-%20Git%20não%20é%20Github.md) | A diferença entre a ferramenta e a plataforma |
| 1.4 | [Instalando e configurando o Git](Conteúdo%20do%20curso/1%20-%20Introducao%20ao%20git%20e%20preparacao%20do%20ambiente/1.4%20-%20Instalando%20o%20Git.md) | Instalação e configuração de nome e e-mail |
| 1.5 | [Registrando múltiplos usuários locais](Conteúdo%20do%20curso/1%20-%20Introducao%20ao%20git%20e%20preparacao%20do%20ambiente/1.5%20-%20Registrando%20usuários%20locais%20no%20Git.md) | Configuração global x local e credenciais |

### 2️⃣ Git básico

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 2.1 | [Entendendo como o Git funciona](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.1%20-%20Entendendo%20como%20o%20Git%20funciona.md) | Repositório, snapshots e as três áreas do Git |
| 2.2 | [Ciclo de vida dos arquivos](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.2%20-%20O%20ciclo%20de%20vida%20dos%20status%20de%20arquivos%20no%20Git.md) | Untracked, modified, staged e o fluxo completo |
| 2.3 | [Usando o .gitignore](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.3%20-%20Fazendo%20uso%20do%20gitignore.md) | Como ignorar arquivos e pastas |
| 2.4 | [Como fazer commits](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.4%20-%20Como%20fazer%20os%20commits.md) | Criar commits e escrever boas mensagens |
| 2.5 | [Consultando o histórico](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.5%20-%20Como%20consultar%20o%20histórico%20do%20projeto.md) | `git log` e seus filtros |
| 2.6 | [Voltando no tempo](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.6%20-%20Voltando%20no%20tempo%20com%20o%20Git.md) | Visão geral de checkout, reset e revert |
| 2.7 | [Comandos úteis](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.7%20-%20Conhecendo%20alguns%20comandos%20úteis.md) | `git mv`, `git rm` e `git diff` |
| 2.8 | [Desfazendo e refazendo ações](Conteúdo%20do%20curso/2%20-%20Git%20basico/2.8%20-%20Desfazendo%20e%20refazendo%20ações%20no%20Git.md) | `restore`, `reset`, `--amend`, squash e `revert` |

### 3️⃣ Git intermediário

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 3.1 | [Branches](Conteúdo%20do%20curso/3%20-%20Git%20intermediario/3.1%20-%20Branches.md) | Criar, trocar, renomear e excluir branches |
| 3.2 | [Merge](Conteúdo%20do%20curso/3%20-%20Git%20intermediario/3.2%20-%20Merge.md) | Juntar branches; fast-forward x commit de merge |
| 3.3 | [Rebase](Conteúdo%20do%20curso/3%20-%20Git%20intermediario/3.3%20-%20Rebase.md) | Histórico linear, rebase interativo e a regra de ouro |
| 3.4 | [Clone e push](Conteúdo%20do%20curso/3%20-%20Git%20intermediario/3.4%20-%20Clone%20e%20push.md) | Baixar repositórios e enviar commits |
| 3.5 | [Fetch e pull](Conteúdo%20do%20curso/3%20-%20Git%20intermediario/3.5%20-%20Fetch%20e%20pull.md) | Trazer as novidades do repositório remoto |
| 3.6 | [Bare repository](Conteúdo%20do%20curso/3%20-%20Git%20intermediario/3.6%20-%20Bare%20repository.md) | O que é um repositório central |
| 3.7 | [Trabalhando com tags](Conteúdo%20do%20curso/3%20-%20Git%20intermediario/3.7%20-%20Trabalhando%20com%20tags.md) | Marcar versões do projeto |

### 4️⃣ Git avançado

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 4.1 | [Repositório remoto no GitHub](Conteúdo%20do%20curso/4%20-%20Git%20avancado/4.1%20-%20Repositório%20remoto%20Github.md) | Conectar um projeto local ao GitHub |
| 4.2 | [Usando clone e pull](Conteúdo%20do%20curso/4%20-%20Git%20avancado/4.2%20-%20Usando%20clone%20e%20pull.md) | Rotina de trabalho com o remoto |
| 4.3 | [Adicionando colaboradores](Conteúdo%20do%20curso/4%20-%20Git%20avancado/4.3%20-%20Adicionando%20colaboradores%20no%20meu%20projeto.md) | Convidar pessoas e níveis de permissão |
| 4.4 | [Consultando o histórico de commits](Conteúdo%20do%20curso/4%20-%20Git%20avancado/4.4%20-%20Consultando%20histórico%20de%20commits.md) | Terminal, interfaces gráficas e GitHub |
| 4.5 | [Desfazendo ações com checkout](Conteúdo%20do%20curso/4%20-%20Git%20avancado/4.5%20-%20Desfazendo%20ações%20com%20checkout.md) | Descartar alterações e visitar commits |
| 4.6 | [Desfazendo ações com revert e reset](Conteúdo%20do%20curso/4%20-%20Git%20avancado/4.6%20-%20Desfazendo%20ações%20com%20revert%20e%20reset.md) | Os três modos do reset e quando usar revert |
| 4.7 | [Resolvendo conflitos](Conteúdo%20do%20curso/4%20-%20Git%20avancado/4.7%20-%20Resolvendo%20conflitos.md) | Entender e resolver conflitos passo a passo |

### 5️⃣ Colaborando com projetos open source

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 5.1 | [O que são issues?](Conteúdo%20do%20curso/5%20-%20Colaborando%20com%20projetos%20open%20source/5.1%20-%20O%20que%20são%20issues.md) | Relatar bugs e fechar issues por commit |
| 5.2 | [Trabalhando com fork](Conteúdo%20do%20curso/5%20-%20Colaborando%20com%20projetos%20open%20source/5.2%20-%20Trabalhando%20com%20fork.md) | Copiar projetos e manter o fork atualizado |
| 5.3 | [Pull requests](Conteúdo%20do%20curso/5%20-%20Colaborando%20com%20projetos%20open%20source/5.3%20-%20Realizando%20e%20aceitando%20pull%20requests.md) | Enviar, revisar, testar e aceitar PRs |

### 6️⃣ Criação de currículo online

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 6.1 | [Currículo online + plugins do VS Code](Conteúdo%20do%20curso/6%20-%20Criacao%20de%20curriculo%20online/6.1%20-%20Projeto%20de%20curriculo%20original%20e%20plugins%20do%20Git%20para%20Vscode.md) | GitHub Pages, GitLens e Git History |

### 7️⃣ Markdown, README e Gist

| Aula | Assunto | O que você vai aprender |
| --- | --- | --- |
| 7.1 | [Entendendo o Markdown](Conteúdo%20do%20curso/7%20-%20Markdown%20readme%20e%20gist/7.1%20-%20Entendendo%20markdown.md) | Toda a sintaxe, com exemplos e resultado |
| 7.2 | [Entendendo Gists](Conteúdo%20do%20curso/7%20-%20Markdown%20readme%20e%20gist/7.2%20-%20Entendendo%20Gists.md) | Compartilhar trechos de código rapidamente |
| 📄 | [Modelo de README](Conteúdo%20do%20curso/7%20-%20Markdown%20readme%20e%20gist/README/README.md) | Um template para usar nos seus projetos |

---

## 🤝 Encontrou um erro ou quer sugerir uma melhoria?

Fique à vontade para contribuir! É uma ótima forma de praticar o que está no [Módulo 5](Conteúdo%20do%20curso/5%20-%20Colaborando%20com%20projetos%20open%20source/5.1%20-%20O%20que%20são%20issues.md):

- abra uma **[issue](https://github.com/Joshpcbrrj/Udemy-Geek_university-Git_GitHub-Essencial_para_o_Desenvolvedor/issues)** descrevendo o problema ou a sugestão; ou
- faça um **fork**, corrija e envie um **pull request**.

## 🙏 Créditos

- Curso: **Git e GitHub Essencial para o Desenvolvedor**, da **Geek University**, na Udemy.
- Anotações e resumo: **[Josué B. Almeida](https://github.com/Joshpcbrrj)**.

<div align="center">

Se este material te ajudou, deixe uma ⭐ no repositório!

</div>
