import { useState } from 'react';
import './AutoCard.css';

export default function AutoCard({ auto, onEliminar, onEditar, onRestaurar }) {
  const [showActions, setShowActions] = useState(false);
  const [showRestore, setShowRestore] = useState(false);
  const [version, setVersion] = useState('');

  const handleEliminar = () => {
    if (window.confirm(`¿Eliminar ${auto.descripcion}?`)) {
      onEliminar(auto.id);
    }
  };

  const handleRestaurar = () => {
    if (version) {
      onRestaurar(auto.id, version);
      setShowRestore(false);
      setVersion('');
    }
  };

  return (
    <div 
      className="auto-card glass"
      onMouseEnter={() => setShowActions(true)}
      onMouseLeave={() => setShowActions(false)}
    >
      <div className="auto-card-header">
        <h3 className="auto-marca">{auto.marca}</h3>
        <span className="auto-precio">${auto.precio?.toFixed(2)}</span>
      </div>
      
      <div className="auto-card-body">
        <p className="auto-modelo">{auto.modelo}</p>
        <div className="auto-info">
          <span className="auto-color" style={{ backgroundColor: auto.color?.toLowerCase() }}>
            {auto.color}
          </span>
          <span className="auto-id">ID: {auto.id}</span>
        </div>
        <p className="auto-descripcion">{auto.descripcion}</p>
      </div>

      {showActions && (
        <div className="auto-actions">
          <button className="btn-edit" onClick={() => onEditar(auto)}>
            ✏️ Editar
          </button>
          <button className="btn-restore" onClick={() => setShowRestore(!showRestore)}>
            ⏮️ Restaurar
          </button>
          <button className="btn-delete" onClick={handleEliminar}>
            🗑️ Eliminar
          </button>
        </div>
      )}

      {showRestore && (
        <div className="restore-panel glass">
          <input
            type="number"
            placeholder="Versión"
            value={version}
            onChange={(e) => setVersion(e.target.value)}
            className="input-version"
          />
          <button onClick={handleRestaurar} className="btn-confirm">
            Confirmar
          </button>
        </div>
      )}
    </div>
  );
}
