// export const API_URI = 'http://mariioc97.pythonanywhere.com/api/';
export const API_URI = 'http://localhost:5000/api/';

export const setHeaders = () => {
    const headers = new Headers();
    const token = localStorage.getItem('token');
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');
    if( token ) headers.append('Authorization', token);
    return headers;
}