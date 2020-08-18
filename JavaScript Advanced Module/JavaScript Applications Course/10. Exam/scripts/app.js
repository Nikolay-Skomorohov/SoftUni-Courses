import { home } from '../controllers/home.js';
import { getLogin, postLogin } from '../controllers/login.js';
import { getRegister, postRegister } from '../controllers/register.js';
import { logout } from './data.js';
import { getCreate, postCreate} from '../controllers/create.js';
import { getDetails } from '../controllers/details.js';
import { getEdit, postEdit } from '../controllers/edit.js';
import { deleteFilm } from '../controllers/delete.js';
import { likeMovie } from '../controllers/like.js';

window.addEventListener('load', function() {
    const app = Sammy('#container', function() {
        this.use('Handlebars', 'hbs');

        this.userData = {
            username: "",
            token: "",
            userId: "",
            movies: [],
            details: "",
            editMovie: {}
        }

        this.get('#/home', home);
        this.get('/', home);
        this.get('indexExam.html', home);

        this.get('#login', getLogin);
        this.post('#login', (context) => { postLogin.call(context) });
        this.get('#register', getRegister);
        this.post('#register', (context) => { postRegister.call(context) });
        this.get('#logout', logout);
        this.get('#create', getCreate);
        this.post('#create', (context) => { postCreate.call(context) });
        this.get('#details/:id', getDetails);
        this.get('#edit/:id', getEdit);
        this.put('#edit/:id', (context) => { postEdit.call(context) });
        this.get('#delete/:id', deleteFilm);
        this.put('#like/:id', likeMovie);
    });

    app.run();
})