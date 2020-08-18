function host(endpoint) {
    const appId = '400EA9C3-3466-CAB9-FFF6-E1A49B859600';
    const apiKey = '1E01CB70-04B3-4189-9EBE-BC531F5DADCD';
    return `https://api.backendless.com/${appId}/${apiKey}/${endpoint}`;
}

const dbName = "movies";

const ENDPOINTS = {
    REGISTER: 'users/register',
    LOGIN: 'users/login',
    LOGOUT: 'users/logout',
    CREATE: `data/${dbName}`,
    MOVIES: `data/${dbName}`,
    DETAILS: `data/${dbName}/`,
    UPDATE: `data/${dbName}/`,
    DELETE: `data/${dbName}/`
}

export async function register(username, password){
    return (await fetch(host(ENDPOINTS.REGISTER), {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "email": username,
            "password": password
        })
    })).json()
}

export async function login(username, password){
    return (await fetch(host(ENDPOINTS.LOGIN), {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "login": username,
            "password": password
        })
    })).json();
}

export async function logout(){
    const token = localStorage.getItem('token');
    await (await fetch(host(ENDPOINTS.LOGOUT), {
        method: "GET",
        headers: {
            "user-token": token
        }
    }))
    localStorage.setItem('username', "");
    localStorage.setItem('token', "");
    localStorage.setItem('userId', "");
    this.app.userData.username = "";
    this.app.userData.token = "";
    this.app.userData.userId = "";
    this.redirect('#login');
}

export async function create(movie){
    const token = localStorage.getItem('token');
    const result = (await fetch(host(ENDPOINTS.CREATE), {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "user-token": token
        },
        body: JSON.stringify(movie)
    })).json();
}

export async function movies(){
    const token = localStorage.getItem('token');
    return (await fetch(host(ENDPOINTS.MOVIES), {
        method: "GET",
        headers: {
            "user-token": token
        }
    })).json();
}

export async function details(movieId){
    const token = localStorage.getItem('token');
    return (await fetch(host(ENDPOINTS.DETAILS + movieId), {
        method: "GET",
        headers: {
            "user-token": token
        }
    })).json();
}

export async function update(movieId, newInfo){
    const token = localStorage.getItem('token');
    return (await fetch(host(ENDPOINTS.UPDATE + movieId), {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "user-token": token
        },
        body: JSON.stringify(newInfo)
    })).json();
}

export async function deleteMovie(movieId) {
    const token = localStorage.getItem('token');
    return (await fetch(host(ENDPOINTS.DELETE + movieId), {
        method: "DELETE",
        headers: {
            "user-token": token
        }
    }));
}

export async function like(movieId, userLiked) {
        const token = localStorage.getItem('token');
    return (await fetch(host(ENDPOINTS.UPDATE + movieId), {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "user-token": token
        },
        body: JSON.stringify({
            "movieLikes": userLiked
        })
    })).json();
}