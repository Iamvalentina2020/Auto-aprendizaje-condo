import { useState, useEffect } from 'react';
import './AutoForm.css';

const TIPOS = ['sedan', 'suv', 'coupe', 'hatchback', 'truck'];
const DECORADORES = ['sunroof', 'sport', 'leather', 'premium', 'electric'];

export default function AutoForm({ onSubmit, autoEdit, onCancel }) {
  const [formData, setFormData] = useState({
    marca: '',
    modelo: '',
    color: '',
    tipo: 'sedan',
    decoradores: []
  });

  useEffect(() => {
    if (autoEdit) {
      setFormData({
        marca: autoEdit.marca || '',
        modelo: autoEdit.modelo || '',
        color: autoEdit.color || '',
        tipo: autoEdit.tipo || 'sedan',
        decoradores: autoEdit.decoradores || []
      });
    }
  }, [autoEdit]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleDecoradorToggle = (decorador) => {
    setFormData(prev => ({
      ...prev,
      decoradores: prev.decoradores.includes(decorador)
        ? prev.decoradores.filter(d => d !== decorador)
        : [...prev.decoradores, decorador]
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
    if (!autoEdit) {
      setFormData({
        marca: '',
        modelo: '',
        color: '',
        tipo: 'sedan',
        decoradores: []
      });
    }
  };

  return (
    <form className="auto-form glass" onSubmit={handleSubmit}>
      <h2 className="form-title">
        {autoEdit ? '✏️ Editar Auto' : '🚗 Nuevo Auto'}
      </h2>

      <div className="form-grid">
        <div className="form-group">
          <label htmlFor="marca">Marca</label>
          <input
            type="text"
            id="marca"
            name="marca"
            value={formData.marca}
            onChange={handleChange}
            placeholder="Toyota, Honda, Ford..."
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="modelo">Modelo</label>
          <input
            type="text"
            id="modelo"
            name="modelo"
            value={formData.modelo}
            onChange={handleChange}
            placeholder="Corolla, Civic, Mustang..."
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="color">Color</label>
          <input
            type="text"
            id="color"
            name="color"
            value={formData.color}
            onChange={handleChange}
            placeholder="Rojo, Azul, Negro..."
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="tipo">Tipo</label>
          <select
            id="tipo"
            name="tipo"
            value={formData.tipo}
            onChange={handleChange}
            required
          >
            {TIPOS.map(tipo => (
              <option key={tipo} value={tipo}>
                {tipo.charAt(0).toUpperCase() + tipo.slice(1)}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="form-group">
        <label>Decoradores</label>
        <div className="decoradores-grid">
          {DECORADORES.map(dec => (
            <label key={dec} className="decorador-checkbox">
              <input
                type="checkbox"
                checked={formData.decoradores.includes(dec)}
                onChange={() => handleDecoradorToggle(dec)}
              />
              <span>{dec.charAt(0).toUpperCase() + dec.slice(1)}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="form-actions">
        <button type="submit" className="btn-submit">
          {autoEdit ? '💾 Guardar Cambios' : '➕ Crear Auto'}
        </button>
        {autoEdit && (
          <button type="button" className="btn-cancel" onClick={onCancel}>
            ❌ Cancelar
          </button>
        )}
      </div>
    </form>
  );
}
