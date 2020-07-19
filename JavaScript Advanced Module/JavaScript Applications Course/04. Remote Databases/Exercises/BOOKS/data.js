const appId = '41D4B624-B8DD-325A-FFB6-7BC21F74E200';
const apiKey = `CF8757C9-6592-4125-B4B6-F722F321F825`;
const host = function(endpoint) {
    return `https://api.backendless.com/${appId}/${apiKey}/data/${endpoint}`;
}

export async function getBooks() {
    const booksData = await fetch(host('books'));
    return booksData.json();
}

export async function createBook(bookInfo) {
    await fetch(host('books'), {
        method: 'POST',
        body: JSON.stringify(bookInfo),
        headers: {
            'Content-Type': 'application/json'
        }
    })
}

export async function updateBook(newInfo, bookId) {
    await fetch(host(`books/${bookId}`), {
        method: 'PUT',
        body: JSON.stringify(newInfo),
        headers: {
            'Content-Type': 'application/json'
        }
    })
}

export async function deleteBook(bookId) {
    await fetch(host(`books/${bookId}`), {
        method: 'DELETE',
    })
}
