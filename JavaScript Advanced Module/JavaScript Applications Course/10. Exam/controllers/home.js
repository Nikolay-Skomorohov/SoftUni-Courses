import {movies} from "../scripts/data.js";

export async function home() {
    if (localStorage.getItem('username')) {
        try {
            this.app.userData.movies = await movies();
        } catch (e) {
            throw new Error(e.message);
        }
    }
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    }
    this.partial('./templates/home.hbs', this.app.userData);
}

