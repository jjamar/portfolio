// Config do site. Decisões:
// - site: usado para sitemap, canonical e Open Graph. Troque se o domínio mudar.
// - output estático (padrão): SEO e performance sem servidor.
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://jonatanjamar.com.br',
  integrations: [react(), sitemap()],
});
