import { create } from '../scripts/data.js';

export async function getCreate() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };
    this.partial('./templates/create/create.hbs', this.app.userData);
}

export async function postCreate() {
    const event = {
        eventName: this.params.name,
        eventDescription: this.params.description,
        eventDate: this.params.dateTime,
        eventOrganizer: localStorage.getItem(this.params.name),
        eventImage: this.params.imageURL
    };

    try {
        const result = await create(event);
        this.redirect('#/home')
    } catch (e) {
        throw new Error(e.message);
    }
}