function solveClasses() {
    class Pet {
        constructor(owner, name) {
            this.owner = owner;
            this.name = name;
            this.comments = [];
        }

        addComment(comment) {
            for (let i = 0; i < this.comments.length; i++) {
                if (this.comments[i] === comment) {
                    throw new Error('This comment is already added!');
                };
            };
            this.comments.push(comment);
            return 'Comment is added.';
        };

        feed() {
            return `${this.name} is fed`;
        };

        toString() {
            let result = `Here is ${this.owner}'s pet ${this.name}.`;
            if (this.comments.length > 0) {
                result += '\nSpecial requirements: ';
                let textList = [];
                this.comments.forEach(element => textList.push(element));
                result += textList.join(', ');
            }
            return result;
        };
    };

    class Cat extends Pet {
        constructor(owner, name, insideHabits, scratching) {
            super(owner, name);
            this.insideHabits = insideHabits;
            this.scratching = scratching;
        };

        feed() {
            let result = super.feed();
            result += ', happy and purring.';
            return result;
        };

        toString() {
            let result = super.toString();
            let tempResult = [];
            tempResult.push('\nMain information:');
            tempResult.push(`${this.name} is a cat with ${this.insideHabits}`);
            result += tempResult.join('\n')
            if (this.scratching) {
                result += (', but beware of scratches.');
            };
            return result;
        };
    };

    class Dog extends Pet {
        constructor(owner, name, runningNeeds, trainability) {
            super(owner, name);
            this.runningNeeds = runningNeeds;
            this.trainability = trainability;
        };

        feed() {
            let result = super.feed();
            result += ', happy and wagging tail.';
            return result;
        };
        
        toString() {
            let result = super.toString();
            let tempResult = [];
            tempResult.push('\nMain information:');
            tempResult.push(`${this.name} is a dog with need of ${this.runningNeeds}km running every day and ${this.trainability} trainability.`);
            result += tempResult.join('\n')
            return result;
        };
    };
    return {
        Pet,
        Cat,
        Dog
    };
}