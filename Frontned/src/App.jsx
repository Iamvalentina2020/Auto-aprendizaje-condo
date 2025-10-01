import { useState } from 'react';
import { useAutos } from './hooks/useAutos';
import AutoList from './components/AutoList';
import AutoForm from './components/AutoForm';
import Notification from './components/Notification';
import './App.css';

function App() {
  const { autos, loading, error, crear, actualizar, eliminar, restaurar } = useAutos();
  const [autoEdit, setAutoEdit] = useState(null);
  const [notification, setNotification] = useState({ message: '', type: '' });

  const showNotification = (message, type) => {
    setNotification({ message, type });
  };

  const handleCrear = async (data) => {
    const result = await crear(data);
    if (result.success) {
      showNotification('🚀 Auto creado exitosamente', 'success');
    } else {
      showNotification('Error al crear el auto', 'error');
    }
  };

  const handleEditar = (auto) => {
    setAutoEdit(auto);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleActualizar = async (data) => {
    if (autoEdit) {
      const result = await actualizar(autoEdit.id, data);
      if (result.success) {
        showNotification('✅ Auto actualizado exitosamente', 'success');
        setAutoEdit(null);
      } else {
        showNotification('Error al actualizar el auto', 'error');
      }
    }
  };

  const handleEliminar = async (id) => {
    const result = await eliminar(id);
    if (result.success) {
      showNotification('🗑️ Auto eliminado exitosamente', 'success');
    } else {
      showNotification('Error al eliminar el auto', 'error');
    }
  };

  const handleRestaurar = async (id, version) => {
    const result = await restaurar(id, version);
    if (result.success) {
      showNotification(`⏮️ Auto restaurado a versión ${version}`, 'success');
    } else {
      showNotification('Error al restaurar el auto', 'error');
    }
  };

  const handleCancelar = () => {
    setAutoEdit(null);
  };

  return (
    <div className="app">
      <div className="stars"></div>
      <div className="stars2"></div>
      <div className="stars3"></div>

      <header className="app-header">
        <h1 className="app-title">🌌 Autos Espaciales</h1>
        <p className="app-subtitle">Sistema de Gestión Intergaláctico</p>
      </header>

      <div className="app-container">
        <div className="form-section">
          <AutoForm
            onSubmit={autoEdit ? handleActualizar : handleCrear}
            autoEdit={autoEdit}
            onCancel={handleCancelar}
          />
        </div>

        <div className="list-section">
          <AutoList
            autos={autos}
            loading={loading}
            error={error}
            onEliminar={handleEliminar}
            onEditar={handleEditar}
            onRestaurar={handleRestaurar}
          />
        </div>
      </div>

      <Notification
        message={notification.message}
        type={notification.type}
        onClose={() => setNotification({ message: '', type: '' })}
      />
    </div>
  );
}

export default App;
