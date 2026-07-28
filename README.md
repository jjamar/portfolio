# Portfólio · Jonatan Jamar

Site estático construído com Astro 5 + React + TypeScript. Conteúdo separado dos componentes: os cases são arquivos Markdown, as demais páginas têm o texto no topo de cada arquivo `.astro`.

## Rodar localmente

Pré-requisito: Node 20 ou superior.

```bash
npm install
npm run dev        # abre em http://localhost:4321
npm run build      # gera o site em dist/
npm run preview    # serve o build local para conferência
```

## Estrutura

```
src/
  content/cases/       ← os 4 cases (Markdown com front-matter)
  content.config.ts    ← schema dos cases (valida o front-matter no build)
  pages/
    index.astro        ← home (textos nas constantes do topo do arquivo)
    sobre.astro        ← sobre + linha do tempo + formação
    cases/index.astro  ← índice de cases com filtro
    cases/[slug].astro ← template de case individual
    404.astro
  layouts/Base.astro   ← head, SEO, Open Graph, fontes
  components/          ← Header, Footer, CaseCard, CaseFilter (React)
  styles/global.css    ← design system (cores, tipografia, componentes)
public/
  fotos/               ← imagens (jonatan.jpg)
  favicon.svg, robots.txt
```

## Como editar

**Um case:** edite o `.md` correspondente em `src/content/cases/`. O front-matter controla título, tag, resumo executivo, metadados e o case seguinte. O corpo é Markdown normal (aceita HTML para diagramas e placeholders).

**Adicionar um case:** duplique um arquivo existente, ajuste o front-matter (o campo `ordem` define a posição nas listagens; `natureza` deve ser `enterprise` ou `builder`) e ajuste a corrente de `proximoSlug` dos outros cases.

**Home e Sobre:** os textos estão em constantes no topo de `index.astro` e `sobre.astro`.

**Cores e fontes:** tudo em `src/styles/global.css`, nas variáveis de `:root`.

**Screenshots do Feira Viva:** salve as imagens em `public/fotos/` e substitua o bloco `<div class="placeholder">…</div>` no case por tags `<img src="/fotos/arquivo.png" alt="descrição" loading="lazy" />`.

## Deploy na Vercel

1. Crie um repositório no GitHub (ex.: `jjamar/portfolio`) e faça o push:
   ```bash
   git init && git add -A && git commit -m "Portfólio v1"
   git remote add origin git@github.com:jjamar/portfolio.git
   git push -u origin main
   ```
2. Em vercel.com: Add New Project → importe o repositório. A Vercel detecta Astro sozinha. Deploy.
3. Cada push na branch `main` publica automaticamente.

## Domínio (jonatanjamar.com.br)

1. Na Vercel: Project → Settings → Domains → adicione `jonatanjamar.com.br` e `www.jonatanjamar.com.br`.
2. No Registro.br → DNS, crie os registros que a Vercel indicar (tipicamente `A @ 76.76.21.21` e `CNAME www cname.vercel-dns.com`). Use os valores exibidos pela Vercel, que são a fonte da verdade.
3. Propagação leva de minutos a 24h. O certificado HTTPS é automático.
4. Depois, confira se `astro.config.mjs` (campo `site`) e `public/robots.txt` apontam para o domínio final.

## Analytics

Preparado, não ativado. Em `src/layouts/Base.astro` há um bloco comentado para Plausible: descomente e ajuste o domínio (ou substitua pelo snippet de outra ferramenta).

## Acessibilidade e SEO já incluídos

HTML semântico, skip link, navegação por teclado com foco visível, `prefers-reduced-motion`, contraste AA na paleta, metadados por página, Open Graph, canonical, sitemap automático (`/sitemap-index.xml`), robots.txt, favicon e página 404.
