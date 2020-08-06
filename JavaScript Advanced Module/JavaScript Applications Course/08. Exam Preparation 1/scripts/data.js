function host(endpoint) {
    const appId = '2F9CF796-9B38-ECD1-FF1A-6F2D6480D300';
    const restKey = '9C0BA5BD-E71E-4DA9-BC2A-F3098C32E43C';
    return `https://api.backendless.com/${appId}/${restKey}/${endpoint}`;
}

const ENDPOINTS = {
    REGISTER: "users/register",
    LOGIN: "users/login",
    LOGOUT: "users/logout"
}

export async function registerFetch(username, password) {
    return (await (fetch(host(ENDPOINTS.REGISTER), {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "email": username,
            "password": password
        })
    }))).json();
}

export async function loginFetch(username, password) {
    return (await (fetch(host(ENDPOINTS.LOGIN), {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "login": username,
            "password": password
        })
    }))).json();
}

export async function logoutFetch(token) {
    return await (await fetch(host(ENDPOINTS.LOGIN), {
        method: "GET",
        headers: {
            "user-token": token
        }
    })).json();
}