import { deleteMovie } from "../scripts/data.js";

export async function deleteFilm() {
    try {
        const result = await deleteMovie(this.params.id);
        this.redirect('#/home');
    } catch (e) {
        throw new Error(e.message);
    }

}
