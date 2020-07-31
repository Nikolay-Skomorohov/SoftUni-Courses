import { getTeamsByID, getTeams } from "../data.js";

export default async function() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        teamControls: await this.load('./templates/catalog/teamControls.hbs'),
        teamMember: await this.load('./templates/catalog/teamMember.hbs'),
        footer: await this.load('./templates/common/footer.hbs')
    };

    const data = await getTeamsByID(this.params.id);
    //     teamId: '1',
    //     name: 'Test Team 1',
    //     comment: 'random comment',
    //     members: [
    //         { username: 'Goshko' },
    //         { username: 'Penka' },
    //         { username: 'Shishi' }
    //     ],
    //     isAuthor: true
    // }

    Object.assign(data, this.app.userData);

    this.partial('./templates/catalog/details.hbs', data);
}