import { home } from '../controllers/home.js';
import { getLogin, postLogin } from '../controllers/login.js';
import { getRegister, postRegister } from '../controllers/register.js';
import { getProfile } from '../controllers/profile.js';
import { logout } from './data.js';
import { getCreate, postCreate } from '../controllers/create.js';
import { getDetails } from '../controllers/details.js';

window.addEventListener('load', function() {
    const app = Sammy('body', function() {
        this.use('Handlebars', 'hbs');

        this.userData = {
            username: "",
            token: "",
            userId: "",
            userEvents: [],
            allEvents: [],
            details: ""
        }

        this.get('#/home', home);
        this.get('/', home);
        this.get('index.html', home);

        this.get('#login', getLogin);
        this.post('#login', (context) => { postLogin.call(context) });
        this.get('#register', getRegister);
        this.post('#register', (context) => { postRegister.call(context) });
        this.get('#logout', logout);
        this.get('#profile', getProfile);
        this.get('#create', getCreate);
        this.post('#create', (context) => { postCreate.call(context) });
        this.get('#details/:id', getDetails);
    });

    app.run();
})