function host(endpoint) {
    return `https://api.backendless.com/2F9CF796-9B38-ECD1-FF1A-6F2D6480D300/9C0BA5BD-E71E-4DA9-BC2A-F3098C32E43C/${endpoint}`;
}

const hostEndpoints = {
    REGISTER: 'users/register',
    LOGIN: 'users/login',
    LOGOUT: 'users/logout',
    CREATE: 'data/movies',
    UPDATE: 'data/movies/',
    DELETE: 'data/movies/',
    MOVIES: 'data/movies',
    MOVIE_BY_ID: 'data/movies?where=objectId%3D%27'
}

async function registerUser(username, password) {
    return (await fetch(host(hostEndpoints.REGISTER), {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "username": username,
            "password": password
        })
    })).json()
}

async function loginUser(username, password) {
    const result = await (await fetch(host(hostEndpoints.LOGIN), {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "login": username,
            "password": password
        })
    })).json();

    localStorage.setItem("userId", result.objectId);
    localStorage.setItem("userToken", result['user-token']);
    localStorage.setItem("userName", username);

    return result
}

async function userLogout() {
    if (!localStorage.getItem('userToken')) {
        throw new Error('User not logged in.')
    }

    const token = localStorage.getItem('userToken');

    const result = await (await fetch(host(hostEndpoints.LOGOUT),{
        method: "GET",
        headers: {
            "user-token": token
        }
    })).json();

    localStorage.setItem('userToken', "");
    localStorage.setItem("userId", "");
    localStorage.setItem("userName", "");

    return result;

}

async function createMovie(movie) {
    if (!localStorage.getItem('userToken')) {
        throw new Error('User not logged in.');
    }

    const token = localStorage.getItem('userToken')

    return (await fetch(host(hostEndpoints.CREATE), {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "user-token": token
        },
        body: JSON.stringify(movie)
    })).json();
}

async function getAllMovies() {
    if (!localStorage.getItem('userToken')) {
        throw new Error('User not logged in.');
    }

    const token = localStorage.getItem('userToken');

    return (await fetch(host(hostEndpoints.MOVIES), {
        method: "GET",
        headers: {
            "user-token": token
        }
    })).json()
}

async function getMovieById(movieId) {
    if (!localStorage.getItem('userToken')) {
        throw new Error('User not logged in.');
    }

    const token = localStorage.getItem('userToken');

    return (await fetch(host(hostEndpoints.MOVIE_BY_ID + movieId + '%27'), {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "user-token": token
        }
    })).json();
}

async function editMovie(movieId, newData) {
    if (!localStorage.getItem('userToken')) {
        throw new Error('User not logged in.');
    }

    const token = localStorage.getItem('userToken');

    return (await fetch(host(hostEndpoints.UPDATE + movieId), {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "user-token": token
        },
        body: JSON.stringify(newData)
    })).json();
}

async function deleteMovie(movieId) {
    if (!localStorage.getItem('userToken')) {
        throw new Error('User not logged in.');
    }

    const token = localStorage.getItem('userToken');

    return (await fetch(host(hostEndpoints.DELETE + movieId), {
        method: "DELETE",
        headers: {
            "user-token": token
        }
    })).json();
}

async function buyTicket(movieId) {
    if (!localStorage.getItem('userToken')) {
        throw new Error('User not logged in.');
    }

    const token = localStorage.getItem('userToken');

    const currentTickets = ((await getMovieById(movieId))[0].ticketsCount) - 1;
    if (currentTickets >= 0) {
        throw new Error("Tickets sold out.");
    }
    return await editMovie(movieId, { "ticketsCount": currentTickets });
}