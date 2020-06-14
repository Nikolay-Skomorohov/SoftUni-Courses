class Company {
    constructor() {
        this.departments = [];
    }

    AddEmployee(username, salary, position, department) {
        arguments.forEach(element => {
            if (element === null || element === undefined || element === "") {
                throw Error("Invalid input!");
            }

            if (salary < 0) {
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
        return;
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