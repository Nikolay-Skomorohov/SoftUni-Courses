import {login} from '../scripts/data.js';

export async function getLogin() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };
    this.partial('./templates/login/login.hbs', this.app.userData);
}

export async function postLogin() {
    const username = this.params.username
    const password = this.params.password
    try {
        const result = await login(username, password);
        localStorage.setItem('username', username);
        localStorage.setItem('token', result['user-token']);
        localStorage.setItem('userId', result.objectId);
        this.app.userData.username = username;
        this.app.userData.token = result['user-token'];
        this.app.userData.userId = result.token;
    } catch (e) {
        throw new Error(e.message);
    }
    this.redirect('#/home');
}