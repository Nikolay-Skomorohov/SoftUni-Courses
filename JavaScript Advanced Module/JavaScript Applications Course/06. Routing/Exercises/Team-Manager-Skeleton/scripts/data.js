function host(endpoint) {
    return `https://api.backendless.com/2F9CF796-9B38-ECD1-FF1A-6F2D6480D300/9C0BA5BD-E71E-4DA9-BC2A-F3098C32E43C/${endpoint}`;
}

const endpoints = {
    REGISTER: 'users/register',
    LOGIN: 'users/login',
    CREATE: 'data/Teams',
    UPDATE: 'users/'
}

export async function register(username, password) {
    return (await fetch(host(endpoints.REGISTER), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'email': username,
            'password': password
        })
    })).json();
}

export async function login(username, password) {
    return (await fetch(host(endpoints.LOGIN), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'login': username,
            'password': password
        })
    })).json();
}

export async function updateUserTeamID(userID, token, teamID) {
    if (token === null || token === undefined) {
        throw new Error('User is not logged in.');
    }

    return (await fetch(host(endpoints.UPDATE + userID), {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'user-token': token
        },
        body: JSON.stringify({
            'teamID': teamID
        })
    })).json();
}

export async function create(teamName, teamComment) {
    const token = localStorage.getItem('userToken');
    if (token === null) {
        throw new Error('User is not logged in.');
    }

    const result = await (await fetch(host(endpoints.CREATE), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'user-token': token
        },
        body: JSON.stringify({
            'teamName': teamName,
            'teamComment': teamComment
        })
    })).json();

    if (result.hasOwnProperty('errorData')) {
            throw new Error(result.message);
    }

    const userUpdateResult = await updateUserTeamID(result.ownerId, localStorage.getItem('userToken'), result.objectId)

    if (userUpdateResult.hasOwnProperty('errorData')) {
            throw new Error(result.message);
    }

    return result;
}

export async function getTeams() {
    return (await fetch(host(endpoints.CREATE))).json();
}

export async function getTeamsByID(id) {
    return (await fetch(host(endpoints.CREATE + '/' + id))).json();
}
