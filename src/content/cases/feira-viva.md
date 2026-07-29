---
title: "Feira Viva"
tag: "Builder · Projeto pessoal"
natureza: builder
ordem: 3
resumo: >-
  Concebi, arquitetei e implementei sozinho o Feira Viva, uma plataforma web para descoberta de
  feiras livres e reserva de produtos para retirada presencial. Defini problema, escopo, modelo
  de dados e regras de autorização; usei IA (Lovable e Claude Code) como aceleradora de
  construção. O MVP está funcional e publicado. É um projeto de aprendizagem: o objetivo era
  provar, na prática, o ciclo completo de concepção a deploy.
cartao: >-
  Concebi, arquitetei e implementei sozinho uma plataforma web, do corte de escopo ao deploy, com
  IA como aceleradora. MVP funcional e publicado.
destaques: "MVP em produção · React · Supabase · RLS"
encontrar: >-
  corte de escopo de MVP, decisões de arquitetura (SSR, RLS), uso de IA como aceleradora e o que
  eu faria diferente.
meta:
  - label: "Estágio"
    valor: "MVP funcional em produção"
  - label: "Papel"
    valor: "Tudo, do discovery ao deploy"
  - label: "Stack"
    valor: "React, TypeScript, TanStack Start (SSR), Supabase, RLS, Vercel"
seoTitle: "Feira Viva, do problema ao deploy · Jonatan Jamar"
seoDescription: "Como concebi, arquitetei e implementei uma plataforma de descoberta de feiras livres com React, Supabase e IA como aceleradora."
linkVivo: "https://feira-local.vercel.app"
proximoSlug: "triagem-juridica"
proximoTitulo: "Triagem de publicações jurídicas com IA e revisão humana"
---

## Contexto

Feiras livres são uma instituição brasileira: acontecem toda semana, em dias fixos, em milhares de bairros. Mas a informação sobre elas é analógica. Quem muda de bairro não sabe onde nem quando tem feira; quem quer um produto específico não sabe qual banca vende; o feirante não tem canal digital próprio e depende de ponto e clientela habitual.

## Problema e oportunidade

Dois lados com problemas complementares:

- **Consumidor:** descobrir feiras por localização e dia, conhecer bancas e garantir produtos sem depender de sorte.
- **Feirante:** dar visibilidade à banca e receber pedidos antecipados, sem operar logística de entrega.

A hipótese central: uma camada fina de descoberta + reserva (sem pagamento on-line, sem entrega) resolve a dor dos dois lados com uma fração da complexidade de um delivery.

## Meu papel

Tudo. Definição de problema, proposta de valor, escopo, arquitetura, modelo de dados, regras de autorização, UX, implementação, deploy e iteração. Sem time, sem cliente, sem prazo externo: as restrições eram tempo pessoal e a decisão consciente de aprender construindo.

## Decisões de escopo (e o que ficou de fora)

O corte do MVP foi a decisão de produto mais importante:

| Entrou | Ficou de fora | Por quê |
|---|---|---|
| Descoberta por estado, cidade, bairro e dia da semana, com ordenação por proximidade | Mapa interativo | Distância calculada resolve "qual feira é perto de mim" sem o custo de renderizar, carregar e manter um mapa |
| Catálogo de bancas por feira | Pagamento on-line | Pagamento na retirada elimina PCI, split e disputas |
| Reserva para retirada no dia | Entrega e logística | Entrega transformaria o produto em delivery, outro negócio |
| Dois perfis (consumidor e feirante) | Avaliações e social | Sem massa crítica, avaliação é ruído |

Reserva para retirada é a aposta que define o produto: preserva o ritual da feira (a pessoa vai até lá) e dá previsibilidade ao feirante, sem criar operação logística.

## Arquitetura e decisões técnicas

- **TanStack Start com SSR:** descoberta local depende de busca; renderização no servidor garante páginas de feiras indexáveis por SEO.
- **Supabase (Postgres + Auth):** backend gerenciado para ir do modelo de dados à API sem construir servidor próprio.
- **Row Level Security:** autorização resolvida no banco, não na aplicação. Feirante só enxerga e edita a própria banca; consumidor só vê as próprias reservas. Defini as policies como parte do modelo de dados, não como remendo posterior.
- **Vercel com deploy contínuo:** cada push em produção em minutos, o que sustentou iteração rápida.

## Como usei IA (e onde ela não decidiu nada)

- **Lovable** acelerou a base de interface e a estrutura inicial.
- **Claude Code** acelerou implementação, refatoração e evolução do código.

O que a IA não fez: definir o problema, cortar o escopo, escolher reserva em vez de delivery, desenhar o modelo de dados, decidir que autorização viveria no banco via RLS. IA multiplicou minha velocidade de execução; a direção foi humana em todas as decisões que importam.

## O produto

A jornada completa do consumidor, do MVP em produção.

<div class="telas">
  <figure>
    <img src="/fotos/feira-viva/01-descoberta.webp" alt="Tela de descoberta do Feira Viva: lista de feiras em cards, com filtros de estado, cidade, bairro e dia, e ordenação por proximidade" width="1200" height="864" loading="lazy" decoding="async" />
    <figcaption>Descoberta. Filtros por localização e dia, com ordenação opcional por proximidade. A distância aparece em cada card; o mapa ficou de fora de propósito.</figcaption>
  </figure>
  <figure>
    <img src="/fotos/feira-viva/02-feira.webp" alt="Página de uma feira no Feira Viva, com endereço, dia e horário, e as bancas cadastradas" width="1200" height="534" loading="lazy" decoding="async" />
    <figcaption>Página da feira. Endereço, dia e horário no topo; abaixo, as bancas daquela feira. É a página pensada para ser indexável por busca, o que motivou o SSR.</figcaption>
  </figure>
  <figure>
    <img src="/fotos/feira-viva/03-reserva.webp" alt="Catálogo de uma banca com produtos e preços por quilo, e o painel lateral de reserva com total, data de retirada e observação" width="1200" height="720" loading="lazy" decoding="async" />
    <figcaption>Catálogo e reserva. Quantidade por item, total calculado e data de retirada. Sem pagamento on-line: o dinheiro continua acontecendo na banca.</figcaption>
  </figure>
  <figure>
    <img src="/fotos/feira-viva/04-minhas-reservas.webp" alt="Lista de reservas do consumidor com status pendente e cancelada, feira, data de retirada, itens e valor" width="1200" height="784" loading="lazy" decoding="async" />
    <figcaption>Minhas reservas. Estado explícito (pendente, cancelada) e cancelamento pelo consumidor. Cada usuário só enxerga as próprias reservas, regra garantida por RLS no banco.</figcaption>
  </figure>
</div>

<p class="nota-telas">Telas da visão do consumidor. A visão do feirante (gestão de banca, catálogo e pedidos recebidos) existe no produto e não está retratada aqui.</p>

## Resultados e estágio atual

- MVP funcional publicado, com jornada completa: encontrar feira → explorar bancas → reservar → retirar.
- Validação qualitativa com usuários próximos, com boa recepção. Sem lançamento comercial e sem claim de tração: o projeto cumpriu o objetivo de aprendizagem para o qual foi desenhado.

## O que eu faria diferente

- Ter definido as policies de RLS antes das primeiras telas, não durante: refazer autorização com o produto andando custa mais caro do que desenhá-la junto com o modelo de dados.

## Se o projeto saísse da aprendizagem para operação real

Levar o Feira Viva ao mercado foi uma possibilidade considerada e abandonada: o objetivo era aprender construindo. Mas o caminho de validação estaria mapeado:

- Onboarding assistido de feirantes reais de uma única feira piloto.
- Notificação de véspera de feira para reservas.
- Taxa de retirada das reservas como métrica central de confiança.

## Competências demonstradas

Definição de problema e proposta de valor · corte de escopo de MVP · arquitetura e modelo de dados · autorização por RLS · SSR e SEO · desenvolvimento assistido por IA · deploy contínuo · iteração sobre produto em produção
