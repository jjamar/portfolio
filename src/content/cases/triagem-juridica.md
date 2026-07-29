---
title: "Triagem de publicações jurídicas com IA e revisão humana"
tag: "IA responsável · Projeto pessoal"
natureza: builder
ordem: 4
resumo: >-
  Construí uma automação no-code, em operação, que faz a triagem de publicações de diário
  oficial: extrai dados estruturados com LLM (Claude Haiku via API Anthropic), cruza com uma base
  de processos que simula um CRM, identifica responsáveis, alimenta um painel de acompanhamento e
  envia e-mails marcados como [REVISAR]. A
  classificação de urgência é feita por regras determinísticas fora do modelo, e nenhuma ação
  final acontece sem revisão humana. O case não é sobre IA: é sobre desenhar um processo
  confiável em um domínio onde erro tem consequência.
destaques: "Human-in-the-loop · guardrails · em operação"
encontrar: >-
  desenho de processo com IA, guardrails, separação probabilístico × determinístico e
  human-in-the-loop.
meta:
  - label: "Papel"
    valor: "Concepção, desenho do processo e implementação"
  - label: "Stack"
    valor: "Make.com, API Anthropic (Claude Haiku), planilha como CRM simulado, Gmail"
  - label: "Status"
    valor: "Em operação, com dados fictícios de demonstração (caderno do DJERJ)"
seoTitle: "Automação de triagem jurídica com IA e human-in-the-loop · Jonatan Jamar"
seoDescription: "Automação que extrai publicações de diário oficial com LLM, cruza com a base de processos e cria alertas provisórios, mantendo o advogado como decisor final."
proximoSlug: "feira-viva"
proximoTitulo: "Feira Viva"
---

## Contexto

Escritórios de advocacia monitoram diários oficiais diariamente. Perder uma intimação pode significar perder um prazo, e perder um prazo pode significar perder um caso. A triagem manual é repetitiva, sujeita a fadiga e cara: exatamente o perfil de tarefa em que automação ajuda e em que automação mal desenhada é perigosa.

## O problema certo

A pergunta que define o projeto não foi "como automatizar a triagem?", e sim: **o que esta automação jamais pode fazer?**

Ela jamais pode: substituir a análise jurídica, calcular prazos oficialmente, agir sem supervisão ou esconder de onde tirou uma informação. A partir dessas restrições, desenhei o processo.

## Desenho da solução

<div role="img" aria-label="Fluxo da automação: PDF do diário oficial, extração com LLM, cruzamento com a base de processos, regras determinísticas de urgência, saídas em painel e e-mail de alerta, e revisão humana obrigatória no final." style="margin: 1.6em 0; font-family: var(--font-body);">
  <div style="border: 1px solid var(--line); border-radius: 10px; padding: 14px 18px; background: var(--cream-2);"><strong>1 · Entrada.</strong> Caderno do diário oficial em PDF (nas demonstrações, um caderno fictício do DJERJ).</div>
  <div aria-hidden="true" style="text-align: center; color: var(--sand); padding: 2px 0;">↓</div>
  <div style="border: 1px solid var(--line); border-radius: 10px; padding: 14px 18px; background: var(--cream-2);"><strong>2 · Extração com LLM.</strong> Claude Haiku extrai apenas informações expressamente mencionadas: processo, partes, teor. Tarefa probabilística: o lugar certo para o modelo.</div>
  <div aria-hidden="true" style="text-align: center; color: var(--sand); padding: 2px 0;">↓</div>
  <div style="border: 1px solid var(--line); border-radius: 10px; padding: 14px 18px; background: var(--cream-2);"><strong>3 · Cruzamento determinístico.</strong> Dados extraídos cruzados com a base de processos (planilha simulando um CRM) para identificar o responsável.</div>
  <div aria-hidden="true" style="text-align: center; color: var(--sand); padding: 2px 0;">↓</div>
  <div style="border: 1px solid var(--line); border-left: 4px solid var(--red); border-radius: 0 10px 10px 0; padding: 14px 18px; background: var(--cream-2);"><strong>4 · Urgência por regras, fora do LLM.</strong> Decisão de risco não é tarefa para modelo probabilístico. Regras determinísticas, auditáveis e editáveis.</div>
  <div aria-hidden="true" style="text-align: center; color: var(--sand); padding: 2px 0;">↓</div>
  <div style="border: 1px solid var(--line); border-radius: 10px; padding: 14px 18px; background: var(--cream-2);"><strong>5 · Saídas.</strong> Painel de acompanhamento e envio de e-mail alerta ao responsável, sempre marcado como <strong>[REVISAR]</strong>.</div>
  <div aria-hidden="true" style="text-align: center; color: var(--sand); padding: 2px 0;">↓</div>
  <div style="border: 1px solid var(--line); border-left: 4px solid var(--red); border-radius: 0 10px 10px 0; padding: 14px 18px; background: var(--cream-2);"><strong>6 · Revisão humana obrigatória.</strong> O advogado valida antes de qualquer ação valer. O sistema propõe; a pessoa decide.</div>
</div>

## Guardrails e confiabilidade

- **Separação probabilístico × determinístico:** LLM extrai, regras decidem. Essa fronteira é a decisão de arquitetura mais importante do projeto.
- **Guardrails contra prompt injection:** o conteúdo do diário é tratado como dado não confiável, nunca como instrução.
- **Log de auditoria:** cada item processado é rastreável da publicação de origem até o lembrete criado.
- **Convenção [REVISAR]:** todo evento criado se declara provisório. O sistema comunica a própria incerteza em vez de fingir precisão.
- **Falha segura:** na dúvida (dado ausente, cruzamento ambíguo), o item vai para revisão humana em vez de seguir o fluxo.

## Por que isso é um case de produto, não de tecnologia

Qualquer pessoa consegue pedir a um LLM que "leia um PDF e crie eventos na agenda". O trabalho de produto está em outro lugar: definir o que o sistema não pode fazer, decidir onde o modelo entra e onde regras determinísticas mandam, desenhar a revisão humana como parte do fluxo (não como remendo) e tornar cada saída rastreável. É a diferença entre demo de IA e processo em que alguém pode confiar.

## Resultados e estágio

- Automação em operação de ponta a ponta, demonstrável com dados fictícios.
- Evidência prática de IA aplicada com governança: extração por LLM, decisão determinística, human-in-the-loop, auditoria.

## Aprendizados

- O valor de uma automação com IA está menos no modelo e mais nas fronteiras que você desenha ao redor dele.
- Comunicar incerteza ([REVISAR]) gera mais confiança do que aparentar certeza.
- Em domínio regulado ou de risco, "human-in-the-loop" não é limitação do produto: é o produto.

## Outputs

Painel de acompanhamento com eventos de exemplo e e-mail com dados fictícios.

<div class="telas telas--largura">
  <figure>
    <img src="/fotos/triagem-juridica/01-painel.webp" alt="Painel de triagem em planilha, com colunas de número do processo, prazo em texto original, urgência final, resumo da publicação e status PENDENTE_DE_REVISAO em todas as linhas" width="1002" height="588" loading="lazy" decoding="async" />
    <figcaption>Painel de acompanhamento. Cada publicação processada vira uma linha com o prazo no texto original, a urgência definida por regras e o resumo extraído. Todas as linhas nascem em <strong>PENDENTE_DE_REVISAO</strong>: nenhum item é dado como tratado sem o advogado.</figcaption>
  </figure>
  <figure>
    <img src="/fotos/triagem-juridica/02-email.webp" alt="E-mail de alerta com assunto DEMO REVISAR prazo urgente, listando publicação, processo, tribunal, juízo, tipo de ato, prazo informado, trecho de evidência, urgência sugerida pelo modelo e urgência final aplicada pela regra" width="1177" height="622" loading="lazy" decoding="async" />
    <figcaption>E-mail de alerta. Traz o <strong>trecho de evidência</strong> literal da publicação e separa a urgência sugerida pelo modelo da urgência final aplicada pela regra. O rodapé declara que a data é provisória e não substitui controle oficial de prazos.</figcaption>
  </figure>
</div>

<p class="nota-telas">Demonstração técnica com dados fictícios em caderno simulado do DJERJ. Nenhum dado real de processo ou de cliente é exibido.</p>

## Competências demonstradas

Desenho de processo com IA · separação probabilístico × determinístico · human-in-the-loop · guardrails e segurança de prompt · auditabilidade · automação no-code multissistema · pensamento de risco em domínio sensível
