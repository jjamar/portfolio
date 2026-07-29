// Limpa o cache do Astro antes de dev e build.
//
// Por que existe: o content layer do Astro guarda as entradas dos cases em um
// data store em disco. Quando o schema em src/content.config.ts muda (campo novo,
// campo obrigatorio), o store e invalidado mas nem sempre repopulado, e a colecao
// volta vazia: as paginas renderizam sem nenhum case, sem erro no terminal.
// Apagar o cache antes de subir resolve na origem.
//
// Nunca derruba o comando seguinte: se um arquivo estiver travado por outro
// processo (acontece no Windows), avisa e segue em frente.
//
// Uso: roda sozinho via "bun run dev" e "bun run build".
// Manual: bun run limpar

import { rmSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';

const alvos = ['.astro', 'node_modules/.astro', 'dist'];
const removidos = [];
const falhas = [];

for (const alvo of alvos) {
  const caminho = resolve(process.cwd(), alvo);
  if (!existsSync(caminho)) continue;
  try {
    rmSync(caminho, { recursive: true, force: true, maxRetries: 3, retryDelay: 120 });
    removidos.push(alvo);
  } catch (erro) {
    falhas.push(`${alvo} (${erro.code ?? erro.message})`);
  }
}

if (removidos.length) console.log(`cache limpo: ${removidos.join(', ')}`);
if (falhas.length) {
  console.warn(`aviso: nao consegui apagar ${falhas.join(', ')}.`);
  console.warn('feche o servidor de dev e o editor, e rode "bun run limpar" de novo.');
}
if (!removidos.length && !falhas.length) console.log('cache ja estava limpo');
