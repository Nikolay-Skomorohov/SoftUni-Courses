import { home } from './controllers/home.js';
import register from './controllers/register.js';
import login from './controllers/login.js';
import create from './controllers/create.js';
import cinema from './controllers/cinema.js';
import myMovies from './controllers/myMovies.js';

window.addEventListener('load', function() {
    const app = Sammy('#container', function() {
        this.use('Handlebars', 'hbs');

        this.userData = {
            username: "111",

        }

        this.get('/', home);
        this.get('#/home', home);
        this.get('index.html', home);
        this.get('#/register', register);
        this.get('#/login', login);
        this.get('#/create', create);
        this.get('#/cinema', cinema);
        this.get('#/myMovies', myMovies);

    })

    app.run();
})