// Card de case. Usado na home (renderizado no servidor, sem JS)
// e na página /cases dentro do filtro interativo.
export interface CaseInfo {
  slug: string;
  title: string;
  tag: string;
  natureza: 'enterprise' | 'builder';
  resumoCard: string;
  destaques: string;
  encontrar?: string;
}

export default function CaseCard({ c, comEncontrar = false }: { c: CaseInfo; comEncontrar?: boolean }) {
  return (
    <a className="card" href={`/cases/${c.slug}`}>
      <span className="eyebrow eyebrow-red">{c.tag}</span>
      <span className="card-title">{c.title}</span>
      <p className="card-desc">{c.resumoCard}</p>
      {comEncontrar && c.encontrar ? (
        <p className="card-desc" style={{ fontSize: '0.88rem' }}>
          <strong style={{ fontWeight: 500 }}>O que você vai encontrar:</strong> {c.encontrar}
        </p>
      ) : null}
      <p className="card-foot">{c.destaques}</p>
    </a>
  );
}
