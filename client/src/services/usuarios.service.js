import { API_URI, setHeaders } from './config';

export const loginUsuario = async ( data ) => {
    const resp = await fetch( `${API_URI}usuarios/login`, {
        method: 'POST',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const comprobarSesion = async ( ) => {
    const resp = await fetch( `${API_URI}usuarios/sesion`, {
        headers: setHeaders(),
    });
    return await resp.json();
}

export const registrarUsuario = async ( data ) => {
    const resp = await fetch( `${API_URI}usuarios/registro`, {
        method: 'POST',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const actualizarUsuario = async ( id_usuario, data ) => {
    const resp = await fetch( `${API_URI}usuarios/${id_usuario ? id_usuario : ''}`, {
        method: 'PUT',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const actualizarPassword = async ( id_usuario, data ) => {
    const resp = await fetch( `${API_URI}usuarios/password/${id_usuario ? id_usuario : ''}`, {
        method: 'PUT',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const obtenerUsuarios = async ( ) => {
    const resp = await fetch( `${API_URI}usuarios/`, {
        headers: setHeaders(),
    });
    return await resp.json();
}

export const buscarUsuarios = async ( query ) => {
    const resp = await fetch( `${API_URI}usuarios/buscar/${query}`, {
        headers: setHeaders(),
    });
    return await resp.json();
}

export const eliminarUsuario = async ( id_usuario ) => {
    const resp = await fetch( `${API_URI}usuarios/${id_usuario}`, {
        method: 'DELETE',
        headers: setHeaders(),
    });
    return await resp.json();
}

export const enviarMensajeContacto = async ( data ) => {
    const resp = await fetch( `${API_URI}usuarios/contacto`, {
        method: 'POST',
        headers: setHeaders(),
        body: data
    });
    return await resp.json();
}

