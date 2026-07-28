# Publicação do portfólio

Roteiro de deploy: GitHub → Vercel → domínio próprio. Execute os comandos no PowerShell, dentro de `C:\Projetos\Portfolio`.

---

## Etapa 1 · Commit inicial (local)

O `.gitignore` já está criado. Ele exclui `node_modules/`, `dist/`, `.astro/`, `.vercel/`, arquivos `.env`, `*.zip` e o `HANDOFF_PORTFOLIO.md` (documento interno, não vai para um repo público).

```powershell
cd C:\Projetos\Portfolio

# remove um lock órfão do git deixado por uma sessão anterior
Remove-Item .git\index.lock -Force -ErrorAction SilentlyContinue

git config user.name "Jonatan Jamar"
git config user.email "jjamarmartins@gmail.com"

git add -A
git status --short
```

Confira a saída de `git status`. Devem aparecer apenas: `.gitignore`, `README.md`, `PUBLICACAO.md`, `astro.config.mjs`, `bun.lock`, `package.json`, `tsconfig.json`, `public/`, `src/`.

Se `node_modules/`, `.astro/` ou o `.zip` aparecerem, pare: o `.gitignore` não foi lido. Rode `git rm -r --cached .` e repita o `git add -A`.

```powershell
git commit -m "Portfolio: site completo em Astro 5 + React 19"
git branch -M main
```

## Etapa 2 · Criar o repositório no GitHub

1. Acesse https://github.com/new (logado como **jjamar**).
2. Repository name: `portfolio`
3. Description: `Portfólio profissional · Astro 5 + React 19`
4. Visibilidade: **Public**
5. **Não** marque "Add a README file", "Add .gitignore" nem "Choose a license". O repositório precisa nascer vazio, senão o push é rejeitado.
6. Clique em **Create repository**.

## Etapa 3 · Push

```powershell
git remote add origin https://github.com/jjamar/portfolio.git
git push -u origin main
```

Na primeira vez o Git Credential Manager abre uma janela do navegador pedindo autorização do GitHub. Autorize e o push continua sozinho. Se ele pedir usuário e senha no terminal, a senha **não** é a da conta: é um Personal Access Token (github.com/settings/tokens, escopo `repo`).

## Etapa 4 · Deploy na Vercel

1. Acesse https://vercel.com/new e entre com o GitHub.
2. Importe o repositório `jjamar/portfolio`.
3. A Vercel detecta Astro sozinha. Framework Preset: `Astro`. Build Command: `astro build`. Output Directory: `dist`. Não altere nada.
4. **Deploy**.

Em 1 a 2 minutos o site sobe em `portfolio-xxxx.vercel.app`. Abra e valide antes de mexer no domínio.

Se o build falhar, o log costuma apontar lockfile: a Vercel usa o `bun.lock` e roda `bun install`. Caso dê conflito, remova o `bun.lock` do repo ou force `npm install` em Settings → Build & Development Settings.

## Etapa 5 · Domínio jonatanjamar.com.br

1. Registre em https://registro.br (CPF, ~R$ 40/ano).
2. Na Vercel: projeto → Settings → Domains → Add → `jonatanjamar.com.br`. Adicione também `www.jonatanjamar.com.br`.
3. A Vercel exibe os registros DNS. Tipicamente:

   | Tipo  | Nome | Valor                  |
   |-------|------|------------------------|
   | A     | @    | 76.76.21.21            |
   | CNAME | www  | cname.vercel-dns.com   |

   Use os valores que a Vercel mostrar na sua tela, não os desta tabela.
4. No Registro.br: painel do domínio → **Editar zona DNS** → inclua os registros acima.
5. Propagação: de minutos a algumas horas. O HTTPS é emitido pela Vercel automaticamente depois que o DNS resolve.

`site` no `astro.config.mjs` e o `public/robots.txt` já apontam para `https://jonatanjamar.com.br`. Nada a alterar.

## Etapa 6 · Validação pós-deploy

- [ ] Home, `/cases`, os 4 cases e `/sobre` abrem sem erro
- [ ] Filtro React (Todos / Enterprise / Builder) funciona em `/cases`
- [ ] Mobile: 360px de largura, sem overflow horizontal
- [ ] Navegação por teclado: Tab percorre links em ordem lógica, foco visível
- [ ] Links externos abrem certo: LinkedIn, GitHub, Exame, Valor, Feira Viva
- [ ] `Ctrl + Shift + R` para conferir sem cache
- [ ] `jonatanjamar.com.br/sitemap-index.xml` responde
- [ ] Preview de link no LinkedIn e no WhatsApp (Open Graph)

## Depois de publicar

Pendências que continuam abertas, na ordem em que valem mais:

1. Screenshots do Feira Viva (visão do cliente) → substituir os `<div class="placeholder">` em `src/content/cases/feira-viva.md`
2. Evidências visuais dos outros cases: gráfico NPS 16→47, diagrama do experimento de faturas, diagrama dos 7 canais, painel da triagem com dados fictícios
3. OG image dedicada 1200x630 (hoje usa a foto de perfil)
4. Revisões de texto: trade-off Java Portlet × Angular, narrativa do Card de Propostas, próximos passos da triagem jurídica
5. Atualizar o `CAREER_MASTER.md` com os fatos confirmados na conversa anterior

Para atualizar o site depois de qualquer edição: `git add -A`, `git commit -m "..."`, `git push`. A Vercel redeploya sozinha a cada push na `main`.
