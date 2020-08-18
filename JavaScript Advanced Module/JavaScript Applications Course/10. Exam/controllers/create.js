import {create} from "../scripts/data.js";

export async function getCreate() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };
    this.partial('./templates/create/create.hbs', this.app.userData);
}

export async function postCreate(){
    const movie = {
    movieName: this.params.title,
    movieDescription: this.params.description,
    movieCreator: localStorage.getItem('username'),
    movieImage: this.params.imageUrl
    };

    try {
        const result = await create(movie);
        this.redirect('#/home')
    } catch (e) {
        throw new Error(e.message);
    }
}