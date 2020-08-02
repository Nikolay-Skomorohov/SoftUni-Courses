export default async function myMovies() {
    this.partials = {
        header: await this.load('./templates/common/header.hbs'),
        footer: await this.load('./templates/common/footer.hbs'),
    }
    this.partial('./templates/myMovies/myMovies.hbs', this.app.userData)
}