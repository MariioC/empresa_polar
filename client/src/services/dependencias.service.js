import { API_URI, setHeaders } from './config';

export const crearDependencia = async ( data ) => {
    const resp = await fetch( `${API_URI}dependencias/`, {
        method: 'POST',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const actualizarDependencia = async ( data ) => {
    const resp = await fetch( `${API_URI}dependencias/`, {
        method: 'PUT',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const eliminarDependencia = async ( id_dependencia ) => {
    const resp = await fetch( `${API_URI}dependencias/${id_dependencia}`, {
        method: 'DELETE',
        headers: setHeaders(),
    });
    return await resp.json();
}

export const eliminarCargo = async ( id_cargo ) => {
    const resp = await fetch( `${API_URI}dependencias/cargo/${id_cargo}`, {
        method: 'DELETE',
        headers: setHeaders(),
    });
    return await resp.json();
}

export const obtenerDependencias = async ( ) => {
    const resp = await fetch( `${API_URI}dependencias/`, {
        headers: setHeaders(),
    });
    return await resp.json();
}

export const obtenerDependencia = async (id_dependencia) => {
    const resp = await fetch( `${API_URI}dependencias/${id_dependencia}`, {
        headers: setHeaders(),
    });
    return await resp.json();
}

