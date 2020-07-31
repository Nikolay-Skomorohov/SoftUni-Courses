import { login } from "../data.js";

export default async function() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs'),
        loginForm: await this.load('./templates/login/loginForm.hbs'),
    };
    this.partial('./templates/login/loginPage.hbs', this.app.userData);
}

export async function loginPost() {
    try {
        const result = await login(this.params.username, this.params.password);
        if (result.hasOwnProperty('errorData')) {
            throw new Error(result.message);
        }
        this.app.userData.loggedIn = true;
        this.app.userData.username = this.params.username.split('@')[0];
        localStorage.setItem('userToken', result['user-token']);
        localStorage.setItem('userName', result.email);
        localStorage.setItem('userID', result.objectId);
        this.redirect('#/home');
    } catch (e) {
        alert(e.message);
    }
}