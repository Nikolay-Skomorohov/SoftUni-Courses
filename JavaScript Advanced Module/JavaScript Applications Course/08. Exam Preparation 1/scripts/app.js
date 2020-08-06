import { home } from "../controllers/home.js";
import { login, loginPost, logout, register, registerPost, profile } from "../controllers/user.js";

window.addEventListener('load', function() {
    const app = Sammy('body', function() {
        this.use('Handlebars', 'hbs');

        this.userData = {
            loggedUsername: "",
            userId: "",
            loggedIn: false,
            userToken: ""
        }

        this.get('#/home', home);
        this.get('index.html', home);
        this.get('/', home);

        this.get('#/login', login);
        this.post('#/login', (context) => { loginPost.call(context); });
        this.get('#/logout', logout)

        this.get('#/register', register);
        this.post('#/register', (context) => { registerPost.call(context); });

        this.get('#/create', profile);

    })

    app.run('#/home');
})