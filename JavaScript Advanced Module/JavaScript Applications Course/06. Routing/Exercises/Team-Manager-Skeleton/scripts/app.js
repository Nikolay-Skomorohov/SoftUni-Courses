import home from './controllers/home.js';
import register, { registerPost } from './controllers/register.js';
import login, { loginPost } from './controllers/login.js';
import about from './controllers/about.js';
import catalog from './controllers/catalog.js';
import details from './controllers/details.js';
import create, { createPost } from './controllers/create.js';
import edit from './controllers/edit.js';

window.addEventListener('load', function(){
    const app = Sammy('#main', function() {
        this.use('Handlebars', 'hbs');

        this.userData = {
            loggedIn: false,
            hasTeam: false,
        };

        this.get('index.html', home);
        this.get('#/home', home);
        this.get('/', home);
        this.get('#/register', register);
        this.get('#/login', login);
        this.get('#/about', about);
        this.get('#/cinema', catalog);
        this.get('#/cinema/:id', details);
        this.get('#/create', create);
        this.get('#/edit/:id', edit);

        this.post('/register', (context) => { registerPost.call(context); });
        this.post('/login', (context) => { loginPost.call(context); });
        this.post('/create', (context) => { createPost.call(context); });

    })
    app.run();
})