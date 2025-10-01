const BASE_URL = "http://localhost:8000";

// Crear un auto nuevo
export async function crearAuto(data) {
	const res = await fetch(`${BASE_URL}/autos`, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(data),
	});
	return res.json();
}

// Listar todos los autos
export async function listarAutos() {
	const res = await fetch(`${BASE_URL}/autos`);
	return res.json();
}

// Obtener auto por ID
export async function obtenerAuto(id) {
	const res = await fetch(`${BASE_URL}/autos/${id}`);
	return res.json();
}

// Actualizar auto
export async function actualizarAuto(id, data) {
	const res = await fetch(`${BASE_URL}/autos/${id}`, {
		method: "PUT",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(data),
	});
	return res.json();
}

// Eliminar auto
export async function eliminarAuto(id) {
	const res = await fetch(`${BASE_URL}/autos/${id}`, {
		method: "DELETE",
	});
	return res.json();
}

// Restaurar versión de auto
export async function restaurarAuto(id, version) {
	const res = await fetch(`${BASE_URL}/autos/${id}/restore/${version}`, {
		method: "POST",
	});
	return res.json();
}
