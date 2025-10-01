import AutoCard from './AutoCard';
import './AutoList.css';

export default function AutoList({ autos, loading, error, onEliminar, onEditar, onRestaurar }) {
  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Cargando autos espaciales...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container glass">
        <p className="error-message">❌ {error}</p>
      </div>
    );
  }

  if (autos.length === 0) {
    return (
      <div className="empty-container glass">
        <div className="empty-icon">🚗</div>
        <p className="empty-message">No hay autos registrados</p>
        <p className="empty-hint">Crea tu primer auto espacial</p>
      </div>
    );
  }

  return (
    <div className="auto-list">
      <div className="auto-list-header">
        <h2 className="list-title">🚀 Flota Espacial</h2>
        <span className="auto-count">{autos.length} Autos</span>
      </div>
      <div className="auto-grid">
        {autos.map((auto) => (
          <AutoCard
            key={auto.id}
            auto={auto}
            onEliminar={onEliminar}
            onEditar={onEditar}
            onRestaurar={onRestaurar}
          />
        ))}
      </div>
    </div>
  );
}
