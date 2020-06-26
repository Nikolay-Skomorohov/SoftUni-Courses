function pressHouse() {
    class Article {
        constructor(title, content) {
            this.title = title;
            this._content = content;
        }

        toString() {
            return `Title: ${this.title}\nContent: ${this._content}`;
        }
    };

    class ShortReports extends Article {
        constructor(title, content, originalResearch) {
            if (content.length >= 150) {
                throw new Error('Short reports content should be less then 150 symbols.');
            }
            super(title, content);
            this.originalResearches = originalResearch;
            this.comments = [];
        };

        set originalResearches(value) {
            if (!value.title || !value.author) {
                throw new Error('The original research should have author and title.');
            };
            this._originalResearches = value;
        };

        addComment(comment) {
            this.comments.push(comment);
            return 'The comment is added.';
        };

        toString() {
            let result = `Title: ${this.title}\nContent: ${this._content}\nOriginal Research: ${this._originalResearches.title} by ${this._originalResearches.author}`;
            if (this.comments.length > 0) {
                result += '\nComments:\n';
                result += this.comments.join('\n');
            };
            return result;
        };
    };

    class BookReview extends Article {
        constructor(title, content, book) {
            super(title, content);
            this.book = book;
            this.clients = [];
        };

        addClient(clientName, orderDescription) {
            for (let i = 0; i < this.clients.length; i++) {
                if (Object.values(this.clients[i])[0] === clientName && Object.values(this.clients[i])[1] === orderDescription) {
                        throw new Error('This client has already ordered this review.');
                };
            };
            this.clients.push({ clientName, orderDescription });
            return `${clientName} has ordered a review for ${this.book.name}`;
        };

        toString() {
            let result2 = `Title: ${this.title}\nContent: ${this._content}\nBook: ${this.book.name}`;
            if (this.clients.length > 0) {
                let tempRes = '\nOrders:';
                for (let i = 0; i < this.clients.length; i++) {
                    const orderInfo = Object.values(this.clients[i]);
                    tempRes += `\n${orderInfo[0]} - ${orderInfo[1]}`;
                }
                result2 += tempRes;
            };
            return result2;
        };
    };
    return {
        Article,
        ShortReports,
        BookReview
    };
};