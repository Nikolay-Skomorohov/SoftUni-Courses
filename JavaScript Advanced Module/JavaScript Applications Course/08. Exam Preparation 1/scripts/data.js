function host(endpoint) {
    const appId = '4DAB02D8-310E-567F-FF4D-6B5F2BE2B100';
    const apiKey = 'A1B1C47B-F3C6-417F-84F4-A6AC76132278';
    return `https://api.backendless.com/${appId}/${apiKey}/${endpoint}`;
}

const dbName = "events";

const ENDPOINTS = {
    REGISTER: 'users/register',
    LOGIN: 'users/login',
    LOGOUT: 'users/logout',
    CREATE: `data/${dbName}`,
    EVENTS: `data/${dbName}`,
    DETAILS: `data/${dbName}/`
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
    this.redirect('#/home');
}

export async function create(event){
    const token = localStorage.getItem('token');
    const result = (await fetch(host(ENDPOINTS.CREATE), {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "user-token": token
        },
        body: JSON.stringify(event)
    })).json();
}

export async function events(){
    const token = localStorage.getItem('token');
    return (await fetch(host(ENDPOINTS.EVENTS), {
        method: "GET",
        headers: {
            "user-token": token
        }
    })).json();
}

export async function details(eventId){
    const token = localStorage.getItem('token');
    return (await fetch(host(ENDPOINTS.DETAILS + eventId), {
        method: "GET",
        headers: {
            "user-token": token
        }
    })).json();
}
