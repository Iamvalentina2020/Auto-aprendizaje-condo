// Custom hook para manejar el estado y lógica de autos
import { useState, useEffect, useCallback } from 'react';
import * as api from '../apiAutos';

export function useAutos() {
  const [autos, setAutos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const cargarAutos = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await api.listarAutos();
      setAutos(data);
    } catch (err) {
      setError('Error al cargar los autos');
      console.error(err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    cargarAutos();
  }, [cargarAutos]);

  const crear = async (data) => {
    setLoading(true);
    setError(null);
    try {
      await api.crearAuto(data);
      await cargarAutos();
      return { success: true };
    } catch (err) {
      setError('Error al crear el auto');
      console.error(err);
      return { success: false, error: err.message };
    } finally {
      setLoading(false);
    }
  };

  const actualizar = async (id, data) => {
    setLoading(true);
    setError(null);
    try {
      await api.actualizarAuto(id, data);
      await cargarAutos();
      return { success: true };
    } catch (err) {
      setError('Error al actualizar el auto');
      console.error(err);
      return { success: false, error: err.message };
    } finally {
      setLoading(false);
    }
  };

  const eliminar = async (id) => {
    setLoading(true);
    setError(null);
    try {
      await api.eliminarAuto(id);
      await cargarAutos();
      return { success: true };
    } catch (err) {
      setError('Error al eliminar el auto');
      console.error(err);
      return { success: false, error: err.message };
    } finally {
      setLoading(false);
    }
  };

  const restaurar = async (id, version) => {
    setLoading(true);
    setError(null);
    try {
      await api.restaurarAuto(id, version);
      await cargarAutos();
      return { success: true };
    } catch (err) {
      setError('Error al restaurar el auto');
      console.error(err);
      return { success: false, error: err.message };
    } finally {
      setLoading(false);
    }
  };

  return {
    autos,
    loading,
    error,
    crear,
    actualizar,
    eliminar,
    restaurar,
    recargar: cargarAutos,
  };
}
