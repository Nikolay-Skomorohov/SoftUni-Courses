class Company {
    constructor() {
        this.departments = [];
    }

    addEmployee(username, salary, position, department) {
        const funcArgs = [username, salary, position, department];
        funcArgs.forEach(element => function(){
            if (element === null || element === undefined || element === "") {
                throw Error("Invalid input!");
            }
            if (+salary < 0) {
                throw Error(" Invalid input!");
            }
        });
        if (!this.departments[department]) {
            let newDepartment = {};
            newDepartment[department] = [];
            this.departments.push(newDepartment);
            }
        class newEmployee {
            constructor() {
                this.username = username;
                this.salary = salary;
                this.position = position;
                this.department = department;
            }
        }
        this.departments[department].push(newEmployee);
    }

    bestDepartment() {
        let bestDepartment;
        let departSalaryList = [];
        for (let depart of this.departments) {
            let totalSalary = 0;
            for (let employee of depart) {
                totalSalary += +employee['salary'];
            }
            let departAverageSalary = totalSalary / Object.keys(depart).length;
            departSalaryList[depart['department'] = departAverageSalary];
        }
        departSalaryList.sort((a, b) => b.salary - a.salary);
        bestDepartment = departSalaryList[0];
        console.log(bestDepartment);
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());