import { register } from '../data.js';

export default async function() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs'),
        registerForm: await this.load('./templates/register/registerForm.hbs'),
    };
    this.partial('./templates/register/registerPage.hbs', this.app.userData);
}

export async function registerPost() {
    if (this.params.password !== this.params.repeatPassword) {
        alert('Passwords do not match.');
        return;
    }
    try {
        const result = await register(this.params.username, this.params.password);
        if (result.hasOwnProperty('errorData')) {
            throw new Error(result.code);
        }
        this.redirect('#/login');
    } catch (e) {
        if (e.message === '3040') {
            alert('Wrong email input.');
        }
    }
}