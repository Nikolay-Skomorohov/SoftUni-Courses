import { loginFetch, registerFetch, logoutFetch } from '../scripts/data.js'

export async function login() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    }
    this.partial('./templates/user/login.hbs', this.app.userData);
}

export async function loginPost() {
    const result = await loginFetch(this.params.username, this.params.password)
    this.app.userData.userId = result.objectId;
    this.app.userData.userToken = result['user-token'];
    this.app.userData.loggedUsername = this.params.username;
    this.app.userData.loggedIn = true;
    this.redirect('#/home');
}

export async function logout() {
    const result = await logoutFetch(this.app.userData.userToken);
    this.app.userData.loggedUsername = "";
    this.app.userData.userId = "";
    this.app.userData.loggedIn = false;
    this.app.userData.userToken = "";
    this.redirect('#/home');
    return result;
}

export async function register() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    }
    this.partial('./templates/user/register.hbs', this.app.userData);
}

export async function registerPost() {
    if (this.params.username.length < 3) {
        throw new Error("Username should be 3 or more symbols!")
    }
    if (this.params.password.length < 6 || this.params.rePassword.length < 6) {
        throw new Error("Password should be 6 or more symbols!")
    }
    if (this.params.password !== this.params.rePassword) {
        throw new Error("Passwords do not match!")
    }
    const result = await registerFetch(this.params.username, this.params.password);
    this.app.userData.userId = result.objectId;
    this.app.userData.userToken = result['user-token'];
    this.app.userData.loggedUsername = this.params.username;
    this.app.userData.loggedIn = true;
    this.redirect('#/home');
}

export async function profile() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    }
    this.partial('./templates/user/profile.hbs', this.app.userData);
}