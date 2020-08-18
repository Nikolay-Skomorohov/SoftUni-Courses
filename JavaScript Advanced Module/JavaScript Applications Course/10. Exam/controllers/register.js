import { register } from '../scripts/data.js';

export async function getRegister() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };
    this.partial('./templates/register/register.hbs', this.app.userData);
}

export async function postRegister() {
    const username = this.params.email;
    const password = this.params.password;
    const rePassword = this.params.repeatPassword;

    if (username.length === 0) {
        throw new Error('Email field must not be empty!')
    }
    if (password.length < 6) {
        throw new Error('Password should be 6 or more characters')
    }
    if (password !== rePassword) {
        throw new Error("Passwords do not match!");
    }

    try {
        const result = await register(username, password);
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