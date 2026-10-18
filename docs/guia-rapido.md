# ⚡ Guia rápido de comandos e glossário

> Uma "cola" com os comandos mais usados e os termos que aparecem no curso. Para a explicação completa, siga os links para as aulas.

[🏠 Voltar ao índice](../README.md)

## Sumário

- [Configuração](#configuração)
- [Começando um projeto](#começando-um-projeto)
- [Dia a dia](#dia-a-dia)
- [Histórico](#histórico)
- [Branches](#branches)
- [Repositório remoto](#repositório-remoto)
- [Desfazendo coisas](#desfazendo-coisas)
- [Tags](#tags)
- [Glossário](#glossário)

## Configuração

| Comando | O que faz | Aula |
| --- | --- | --- |
| `git --version` | Mostra a versão instalada | [1.4](./01-introducao/04-instalando-o-git.md) |
| `git config --global user.name "Nome"` | Define seu nome para todos os projetos | [1.4](./01-introducao/04-instalando-o-git.md) |
| `git config --global user.email "email"` | Define seu e-mail para todos os projetos | [1.4](./01-introducao/04-instalando-o-git.md) |
| `git config user.email "email"` | Define o e-mail só para o projeto atual | [1.5](./01-introducao/05-usuarios-locais.md) |
| `git config --list` | Lista as configurações | [1.4](./01-introducao/04-instalando-o-git.md) |

## Começando um projeto

| Comando | O que faz | Aula |
| --- | --- | --- |
| `git init` | Transforma a pasta atual em um repositório Git | [2.2](./02-git-basico/02-ciclo-de-vida-dos-arquivos.md) |
| `git clone <url>` | Baixa um repositório remoto completo | [3.4](./03-git-intermediario/04-clone-e-push.md) |

## Dia a dia

| Comando | O que faz | Aula |
| --- | --- | --- |
| `git status` | Mostra o status dos arquivos | [2.2](./02-git-basico/02-ciclo-de-vida-dos-arquivos.md) |
| `git add <arquivo>` | Prepara um arquivo para o commit | [2.2](./02-git-basico/02-ciclo-de-vida-dos-arquivos.md) |
| `git add .` | Prepara todas as alterações | [2.2](./02-git-basico/02-ciclo-de-vida-dos-arquivos.md) |
| `git commit -m "msg"` | Cria um commit com as alterações preparadas | [2.4](./02-git-basico/04-commits.md) |
| `git commit -am "msg"` | Prepara e commita arquivos já rastreados | [2.4](./02-git-basico/04-commits.md) |
| `git diff` | Mostra alterações ainda não preparadas | [2.7](./02-git-basico/07-comandos-uteis.md) |
| `git diff --staged` | Mostra o que vai entrar no próximo commit | [2.7](./02-git-basico/07-comandos-uteis.md) |
| `git mv <antigo> <novo>` | Renomeia ou move um arquivo | [2.7](./02-git-basico/07-comandos-uteis.md) |
| `git rm <arquivo>` | Apaga um arquivo e registra a remoção | [2.7](./02-git-basico/07-comandos-uteis.md) |
| `git rm --cached <arquivo>` | Para de rastrear o arquivo, sem apagá-lo do disco | [2.3](./02-git-basico/03-gitignore.md) |

## Histórico

| Comando | O que faz | Aula |
| --- | --- | --- |
| `git log` | Lista os commits | [2.5](./02-git-basico/05-historico-do-projeto.md) |
| `git log --oneline` | Lista resumida, uma linha por commit | [2.5](./02-git-basico/05-historico-do-projeto.md) |
| `git log --graph --oneline --all` | Desenha o gráfico de branches | [2.5](./02-git-basico/05-historico-do-projeto.md) |
| `git show <hash>` | Mostra os detalhes de um commit | [3.2](./03-git-intermediario/02-merge.md) |
| `git blame <arquivo>` | Mostra quem alterou cada linha | [4.4](./04-git-avancado/04-historico-de-commits.md) |

## Branches

| Comando | O que faz | Aula |
| --- | --- | --- |
| `git branch` | Lista as branches | [3.1](./03-git-intermediario/01-branches.md) |
| `git switch -c <nome>` | Cria uma branch e troca para ela | [3.1](./03-git-intermediario/01-branches.md) |
| `git switch <nome>` | Troca de branch | [3.1](./03-git-intermediario/01-branches.md) |
| `git branch -d <nome>` | Exclui uma branch já mesclada | [3.1](./03-git-intermediario/01-branches.md) |
| `git merge <branch>` | Junta a branch indicada na branch atual | [3.2](./03-git-intermediario/02-merge.md) |
| `git rebase <branch>` | Reaplica seus commits no topo da branch indicada | [3.3](./03-git-intermediario/03-rebase.md) |
| `git cherry-pick <hash>` | Copia um commit específico para a branch atual | [3.2](./03-git-intermediario/02-merge.md) |

## Repositório remoto

| Comando | O que faz | Aula |
| --- | --- | --- |
| `git remote add origin <url>` | Conecta o repositório local ao remoto | [4.1](./04-git-avancado/01-repositorio-remoto.md) |
| `git remote -v` | Lista os remotos configurados | [4.1](./04-git-avancado/01-repositorio-remoto.md) |
| `git push -u origin <branch>` | Primeiro envio de uma branch | [3.4](./03-git-intermediario/04-clone-e-push.md) |
| `git push` | Envia os commits da branch atual | [3.4](./03-git-intermediario/04-clone-e-push.md) |
| `git fetch` | Baixa as novidades sem alterar seu trabalho | [3.5](./03-git-intermediario/05-fetch-e-pull.md) |
| `git pull` | Baixa e junta as novidades na branch atual | [3.5](./03-git-intermediario/05-fetch-e-pull.md) |
| `git remote add upstream <url>` | Conecta o repositório original de um fork | [5.2](./05-open-source/02-fork.md) |

## Desfazendo coisas

| Situação | Comando | Aula |
| --- | --- | --- |
| Descartar alterações de um arquivo | `git restore <arquivo>` | [2.8](./02-git-basico/08-desfazendo-acoes.md) |
| Tirar um arquivo do staging | `git restore --staged <arquivo>` | [2.8](./02-git-basico/08-desfazendo-acoes.md) |
| Corrigir a mensagem do último commit | `git commit --amend -m "nova msg"` | [2.8](./02-git-basico/08-desfazendo-acoes.md) |
| Desfazer o último commit (mantendo as alterações) | `git reset --soft HEAD~1` | [4.6](./04-git-avancado/06-revert-e-reset.md) |
| Voltar tudo para um commit (⚠️ apaga alterações) | `git reset --hard <hash>` | [4.6](./04-git-avancado/06-revert-e-reset.md) |
| Desfazer um commit já enviado | `git revert <hash>` | [4.6](./04-git-avancado/06-revert-e-reset.md) |
| Cancelar um merge com conflito | `git merge --abort` | [4.7](./04-git-avancado/07-conflitos.md) |
| Ver tudo por onde o HEAD passou (resgatar commits) | `git reflog` | [4.6](./04-git-avancado/06-revert-e-reset.md) |

## Tags

| Comando | O que faz | Aula |
| --- | --- | --- |
| `git tag -a v1.0.0 -m "msg"` | Cria uma tag anotada | [3.7](./03-git-intermediario/07-tags.md) |
| `git tag` | Lista as tags | [3.7](./03-git-intermediario/07-tags.md) |
| `git push origin --tags` | Envia as tags para o remoto | [3.7](./03-git-intermediario/07-tags.md) |

## Glossário

| Termo | Significado |
| --- | --- |
| **Repositório (repo)** | Pasta de projeto acompanhada pelo Git, com todo o histórico guardado na pasta `.git`. |
| **Commit** | Um "ponto de salvamento" do projeto, com autor, data, mensagem e um identificador (hash). |
| **Hash** | Código único de cada commit (ex.: `a1b2c3d`). Usado para se referir a ele. |
| **Working directory** | A pasta do projeto, onde você edita os arquivos. |
| **Staging area (index)** | Área de preparação: onde ficam as alterações que vão entrar no próximo commit. |
| **Untracked** | Arquivo que o Git ainda não rastreia. |
| **Branch** | Linha de desenvolvimento independente. A principal costuma se chamar `main`. |
| **HEAD** | Ponteiro que indica em qual commit/branch você está agora. |
| **Detached HEAD** | Quando você está em um commit específico, fora de qualquer branch. |
| **Merge** | Juntar o trabalho de uma branch em outra. |
| **Fast-forward** | Merge em que o Git só avança o ponteiro, sem criar commit de merge. |
| **Rebase** | Reaplicar commits em cima de outra branch, deixando o histórico linear. |
| **Conflito** | Quando duas alterações mexem na mesma linha e o Git precisa que você decida. |
| **Remoto (remote)** | Cópia do repositório em um servidor, como o GitHub. |
| **origin** | Apelido padrão do repositório remoto principal. |
| **upstream** | Apelido comum para o repositório original de um fork. |
| **Push** | Enviar commits locais para o remoto. |
| **Pull** | Trazer commits do remoto e juntar na branch atual (`fetch` + `merge`). |
| **Fetch** | Baixar commits do remoto sem alterar seu trabalho. |
| **Clone** | Baixar uma cópia completa de um repositório. |
| **Fork** | Cópia de um repositório de outra pessoa na sua conta do GitHub. |
| **Pull request (PR)** | Pedido para que suas alterações sejam revisadas e incorporadas a um projeto. |
| **Issue** | "Ticket" no GitHub para relatar bugs, pedir melhorias ou organizar tarefas. |
| **Tag** | Etiqueta fixa em um commit, usada para marcar versões (ex.: `v1.0.0`). |
| **Bare repository** | Repositório só com o histórico, sem arquivos de trabalho; usado como servidor central. |
| **`.gitignore`** | Arquivo que lista o que o Git deve ignorar. |
| **Gist** | Pequeno repositório do GitHub para compartilhar trechos de código. |

---

<div align="center">

[🏠 Voltar ao índice](../README.md)

</div>
