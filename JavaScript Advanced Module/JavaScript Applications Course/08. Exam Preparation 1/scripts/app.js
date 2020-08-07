import { home } from '../controllers/home.js';
import { getLogin, postLogin } from '../controllers/login.js';
import { getRegister, postRegister } from '../controllers/register.js';
import { logout } from './data.js';

window.addEventListener('load', function() {
    const app = Sammy('body', function() {
        this.use('Handlebars', 'hbs');

        this.userData = {
            username: "",
            token: "",
            userId: ""
        }

        this.get('#/home', home);
        this.get('/', home);
        this.get('index.html', home);

        this.get('#login', getLogin);
        this.post('#login', (context) => { postLogin.call(context) });
        this.get('#register', getRegister);
        this.post('#register', (context) => { postRegister.call(context) });
        this.get('#logout', logout);
    });

    app.run();
})