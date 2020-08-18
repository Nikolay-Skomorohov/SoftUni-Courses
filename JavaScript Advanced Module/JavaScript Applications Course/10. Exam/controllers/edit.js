import { details, update } from '../scripts/data.js';

export async function getEdit() {
    this.app.userData.editMovie = await details(this.params.id);
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };
    this.partial('./templates/edit/edit.hbs', this.app.userData);
}

export async function postEdit(){
    const newInfo = {
        "movieName": this.params.title,
        "movieDescription": this.params.description,
        "movieImage": this.params.imageUrl
    }
    console.log(newInfo);
    try {
        const result = await update(this.params.id, newInfo);
        this.redirect(`#details/${this.params.id}`);
    } catch (e) {
        throw new Error(e.message);
    }
}