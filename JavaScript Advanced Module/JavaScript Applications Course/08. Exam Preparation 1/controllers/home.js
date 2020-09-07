import {events} from '../scripts/data.js';

export async function home() {
    try {
        this.app.userData.events = await events();
    } catch (e) {
        throw new Error(e.message);
    }

    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    }
    this.partial('./templates/home.hbs', this.app.userData);
}


