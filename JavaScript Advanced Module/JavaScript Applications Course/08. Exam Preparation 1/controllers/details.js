import {details} from '../scripts/data.js';

export async function getDetails() {
    this.app.userData.details = await details(this.params.id);
    this.app.userData.details.isOrganizer = details.eventOrganizer === this.app.userData.username;

    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };
    this.partial('./templates/details/details.hbs', this.app.userData);
}

