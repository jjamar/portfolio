// Filtro da página /cases. Único componente hidratado no cliente.
import { useState } from 'react';
import CaseCard, { type CaseInfo } from './CaseCard';

type Filtro = 'todos' | 'enterprise' | 'builder';

const rotulos: Record<Filtro, string> = {
  todos: 'Todos',
  enterprise: 'Enterprise',
  builder: 'Builder',
};

export default function CaseFilter({ cases }: { cases: CaseInfo[] }) {
  const [filtro, setFiltro] = useState<Filtro>('todos');
  const visiveis = cases.filter((c) => filtro === 'todos' || c.natureza === filtro);

  return (
    <div>
      <div className="filter-bar" role="group" aria-label="Filtrar cases por natureza">
        {(Object.keys(rotulos) as Filtro[]).map((f) => (
          <button
            key={f}
            type="button"
            className="filter-btn"
            aria-pressed={filtro === f}
            onClick={() => setFiltro(f)}
          >
            {rotulos[f]}
          </button>
        ))}
      </div>
      <div className="grid-2">
        {visiveis.map((c) => (
          <CaseCard key={c.slug} c={c} comEncontrar />
        ))}
      </div>
    </div>
  );
}
