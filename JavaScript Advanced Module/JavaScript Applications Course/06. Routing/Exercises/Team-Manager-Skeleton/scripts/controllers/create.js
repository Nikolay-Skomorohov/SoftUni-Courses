import {create} from "../data.js";

export default async function() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs'),
        createForm: await this.load('./templates/create/createForm.hbs')
    };
    this.partial('./templates/create/createPage.hbs');
}

export async function createPost() {
    try {
        const result = await create(this.params.name, this.params.comment);
        if (result.hasOwnProperty('errorData')) {
            throw new Error(result.message);
        }
        this.app.userData.hasTeam = true;
        this.app.userData.teamId = result.teamId;
        this.redirect(`#/catalog/${result.objectId}`);
    } catch (e) {
        alert(e.message);
    }
}