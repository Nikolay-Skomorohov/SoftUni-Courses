function solve(name, age, weight, height) {
    class Person {
        constructor() {
            this.name = name;
            this.personalInfo = {'age': age, 'weight': weight, 'height': height};
            this.BMI = Math.round(weight / ((height / 100).toFixed(2) * (height / 100).toFixed(2)));
            this.status = undefined;
            };
            
        calculateBMI() {
            if (this.BMI < 18.5) {
                this.status = 'underweight';
            }
            else if (this.BMI < 25) {
                this.status = 'normal';
            }
            else if (this.BMI < 30) {
                this.status = 'overweight';
            }
            else {
                this.recommendation = 'admission required';
                this.status = 'obese';
            }
        };
    };
    let result = new Person(name, age, weight, height);
    result.calculateBMI();
    return result;
};

solve('Peter', 29, 75, 182);
solve("Honey Boo Boo", 9, 57, 137);