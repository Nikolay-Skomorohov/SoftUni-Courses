class Company {
    constructor() {
        this.departments = {};
    }

    addEmployee(username, salary, position, department) {
        this._validateParam(username);
        this._validateParam(salary);
        this._validateParam(position);
        this._validateParam(department);
        if (salary < 0) {
            throw new Error('Invalid input!');
        }
        if (!this.departments[department]) {
            this.departments[department] = [];
        }
        let newEmployee = {};
        newEmployee['name'] = username;
        newEmployee['wage'] = salary;
        newEmployee['post'] = position;
        newEmployee['depart'] = department;
        this.departments[department].push(newEmployee);
        return `New employee is hired. Name: ${newEmployee.name}. Position: ${newEmployee.post}`;
    }

    bestDepartment() {
        let resultDepart;
        let departSalaryList = [];
        for (let depart of Object.keys(this.departments)) {
            let totalSalary = 0;
            for (let employee = 0; employee < this.departments[depart].length; employee++) {
                let currentEmployee = this.departments[depart][employee]
                totalSalary += currentEmployee.wage;
            }
            let departAverageSalary = totalSalary / this.departments[depart].length;
            let newListObj = {};
            newListObj['name'] = depart;
            newListObj['salary'] = departAverageSalary;
            departSalaryList.push(newListObj);
        }
        departSalaryList.sort((a, b) => b.salary - a.salary);
        resultDepart = departSalaryList[0];
        let result = `Best Department is: ${resultDepart['name']}\nAverage salary: ${resultDepart['salary'].toFixed(2)}`;
        let resultList = this.departments[resultDepart['name']];
        resultList.sort(function(a, b) {
            if (a.wage > b.wage) {
                return -1;
            }
            else if (a.wage < b.wage) {
                return 1;
            }
            else if (a.wage === b.wage) {
                return a.name.localeCompare(b.name);
            }
        });
        resultList.forEach(element =>
            result += `\n${element['name']} ${element['wage']} ${element['post']}`);
        return result;
        
    }
    _validateParam(param) {
        if (param === null || param === undefined || param === '') {
            throw new Error('Invalid input!');
        }
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
c.addEmployee("Stanimir", 2000, "angel", "Construction");
console.log(c.bestDepartment());
