export default async function login() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs'),
    };
    this.partial('./templates/login/login.hbs', this.app.userData);

}