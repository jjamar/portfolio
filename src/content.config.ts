import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Cada case é um arquivo .md em src/content/cases.
// O front-matter é validado por este schema: se faltar campo, o build falha (de propósito).
const cases = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/cases' }),
  schema: z.object({
    title: z.string(),
    tag: z.string(),
    natureza: z.enum(['enterprise', 'builder']),
    ordem: z.number(),
    resumo: z.string(),
    destaques: z.string(),
    encontrar: z.string(),
    meta: z.array(z.object({ label: z.string(), valor: z.string() })),
    seoTitle: z.string(),
    seoDescription: z.string(),
    linkVivo: z.string().optional(),
    proximoSlug: z.string(),
    proximoTitulo: z.string(),
  }),
});

export const collections = { cases };
