import { like, details } from '../scripts/data.js';

export async function likeMovie() {
    const getName = await details(this.params.id)
    const addName = getName.movieLikes + localStorage.getItem('username') + ",";
    const result = await like(this.params.id, addName);
    const getName2 = await details(this.params.id);
    const likesCount = getName2.movieLikes.split(',');
    this.app.userData.details.likes = likesCount.length;
    if (getName2.includes(localStorage.getItem('username'))){
        this.app.userData.details.aleadyLiked = true;
    } else {
        this.app.userData.details.aleadyLiked = false;
    }
}