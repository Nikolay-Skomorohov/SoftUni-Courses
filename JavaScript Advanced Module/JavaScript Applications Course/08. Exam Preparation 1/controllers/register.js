import { register } from '../scripts/data.js';

export async function getRegister() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };
    this.partial('./templates/register/register.hbs', this.app.userData);
}

export async function postRegister() {
    const username = this.params.username;
    const password = this.params.password;
    const rePassword = this.params.rePassword;

    if (username.length < 3) {
        throw new Error('Username should be 3 or more characters!')
    }
    if (password.length < 6) {
        throw new Error('Password should be 6 or more characters')
    }
    if (password !== rePassword) {
        throw new Error("Passwords do not match!");
    }

    try {
        const result = await register(username, password);
    } catch (e) {
        throw new Error(e.message);
    }
    this.redirect('#login');
}