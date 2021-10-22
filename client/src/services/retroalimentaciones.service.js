import { API_URI, setHeaders } from './config';

export const registraRetroalimentacion = async ( id_usuario, data ) => {
    const resp = await fetch( `${API_URI}retroalimentaciones/${id_usuario}`, {
        method: 'POST',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const actualizarRetroalimentacion = async ( id_retroalimentacion, data ) => {
    const resp = await fetch( `${API_URI}retroalimentaciones/${id_retroalimentacion}`, {
        method: 'PUT',
        headers: setHeaders(),
        body: data,
    });
    return await resp.json();
}

export const eliminarRetroalimentacion = async ( id_retroalimentacion ) => {
    const resp = await fetch( `${API_URI}retroalimentaciones/${id_retroalimentacion}`, {
        method: 'DELETE',
        headers: setHeaders(),
    });
    return await resp.json();
}

export const obtenerRetroalimentaciones = async ( id_usuario = null ) => {
    const resp = await fetch( `${API_URI}retroalimentaciones/${ id_usuario ? id_usuario : ''}`, {
        headers: setHeaders(),
    });
    return await resp.json();
}

export const obtenerRetroalimentacion = async ( id_retroalimentacion ) => {
    const resp = await fetch( `${API_URI}retroalimentaciones/retroalimentacion/${id_retroalimentacion}`, {
        headers: setHeaders(),
    });
    return await resp.json();
}