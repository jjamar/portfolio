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
  components/          ← Header, Footer, CaseCard, CaseFilter (React), Lightbox
  styles/global.css    ← design system (cores, tipografia, componentes)
public/
  fotos/               ← jonatan.jpg (retrato), og.png (card de compartilhamento 1200x630)
  fotos/feira-viva/    ← telas do produto usadas no case
  favicon.svg, robots.txt
```

## Como editar

**Um case:** edite o `.md` correspondente em `src/content/cases/`. O front-matter controla título, tag, resumo executivo, metadados e o case seguinte. O corpo é Markdown normal (aceita HTML para diagramas e placeholders).

**Adicionar um case:** duplique um arquivo existente, ajuste o front-matter (o campo `ordem` define a posição nas listagens; `natureza` deve ser `enterprise` ou `builder`) e ajuste a corrente de `proximoSlug` dos outros cases.

**Home e Sobre:** os textos estão em constantes no topo de `index.astro` e `sobre.astro`.

**Cores e fontes:** tudo em `src/styles/global.css`, nas variáveis de `:root`.

**Telas de produto:** ficam em `public/fotos/<case>/` no formato WebP, largura 1200px. No Markdown, envolva as figuras em `<div class="telas">` com `<figure>` + `<figcaption>`; a primeira ocupa a largura toda e as demais entram em grid de duas colunas (uma no mobile). Informe sempre `width` e `height` na tag `<img>` para não causar salto de layout. O lightbox (`src/components/Lightbox.astro`) se ativa sozinho em qualquer `.telas` dentro de um case, sem configuração.

**Placeholders de evidência:** os cases que ainda esperam material trazem `<div class="placeholder">…</div>`. Substitua o bloco pelo conteúdo real quando ele existir.

## Links externos que precisam de manutenção

Referências a coisas que vivem fora deste repositório e podem mudar. Ao alterar qualquer uma, rode `npm run build` e faça push.

| O que | Onde está | Quando revisar |
|---|---|---|
| URL do Feira Viva (`https://feira-local.vercel.app`) | `src/content/cases/feira-viva.md`, campo `linkVivo` no front-matter | **Se o Feira Viva ganhar domínio próprio**, troque a URL aqui. É o único lugar do portfólio que aponta para o produto: o botão "Ver o produto no ar" do case lê esse campo. Confira também se o texto do case cita a URL no corpo. |
| Matérias na imprensa (Exame, Valor) sobre o IDbra | `src/pages/index.astro`, card do IDbra | Se algum link quebrar. Links de veículo grande costumam sobreviver, mas vale conferir antes de mandar o portfólio para um processo seletivo. |
| LinkedIn e GitHub | `src/components/Footer.astro` | Se mudar de usuário em alguma das duas. |
| E-mail de contato | `src/components/Footer.astro` e `src/pages/index.astro` | Se trocar o endereço público. |
| Domínio do próprio portfólio | `astro.config.mjs` (campo `site`) e `public/robots.txt` | Só se o domínio do portfólio mudar. Afeta canonical, sitemap e Open Graph. |

## Publicação

Já no ar em **https://jonatanjamar.com.br**, hospedado na Vercel a partir de `jjamar/portfolio`.

Para publicar uma alteração:

```bash
npm run build      # confere que compila antes de subir
git add -A
git commit -m "descrição da mudança"
git push
```

A Vercel redeploya sozinha a cada push na `main`, em cerca de um minuto.

Configuração de DNS em vigor (Registro.br, servidores DNS do próprio Registro.br): registro `A` no apex apontando para o IP que a Vercel informa em Settings → Domains, e `www` redirecionando para o apex com 308. O apex é o domínio canônico, o mesmo declarado em `astro.config.mjs`. Certificado HTTPS emitido e renovado pela Vercel.

## Analytics

Preparado, não ativado. Em `src/layouts/Base.astro` há um bloco comentado para Plausible: descomente e ajuste o domínio (ou substitua pelo snippet de outra ferramenta).

## Acessibilidade e SEO já incluídos

HTML semântico, skip link, navegação por teclado com foco visível, `prefers-reduced-motion`, contraste AA na paleta, metadados por página, Open Graph com imagem dedicada 1200x630 e `summary_large_image`, canonical, sitemap automático (`/sitemap-index.xml`), robots.txt, favicon e página 404.

O lightbox das telas usa `<dialog>` nativo: abre por clique, Enter ou Espaço, navega pelas setas do teclado, fecha no Esc e devolve o foco para a imagem de origem. Sem JavaScript, as telas continuam visíveis, apenas não ampliam.
