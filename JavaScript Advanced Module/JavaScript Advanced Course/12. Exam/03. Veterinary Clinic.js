class VeterinaryClinic {
    constructor(clinicName, capacity) {
        this.clinicName = clinicName;
        this.capacity = capacity;
        this.clients = [];
        this.totalProfit = 0;
        this.currentWorkload = 0;
    };

    newCustomer(ownerName, petName, kind, procedures) { 
        if (this.capacity <= this.currentWorkload) {
            throw new Error('Sorry, we are not able to accept more patients!');
        };
        for (let index = 0; index < this.clients.length; index++) {
            if (this.clients[index].petList.petName === petName &&
                this.clients[index].petList.procedures.length > 0) {
                let result = [];
                this.clients[index].petList.procedures.forEach(element => result.push(element));
                throw new Error(`This pet is already registered under ${ownerName } name! ${petName} is on our lists, waiting for ${result.join(', ')}.`);
                }
        };
        let newClient = {};
        newClient['name'] = ownerName;
        newClient['petList'] = [];
        let newPet = {'petName': petName, 'kind': kind, 'procedures': procedures};
        newClient['petList'].push(newPet)
        this.clients.push(newClient);
        this.currentWorkload += 1;
        return `Welcome ${petName}!`; 
    };
    

    onLeaving(ownerName, petName) {
        for (let index = 0; index < this.clients.length; index++) {
            if (!this.clients[index].name === ownerName) {
                throw new Error(`Sorry, there is no such client!`);
            };
            for (let i = 0; i < this.clients[index].petList.length; i++) {
                if (this.clients[index].petList[i].petName === petName &&
                    this.clients[index].petList[i].procedures.length === 0) {
                    throw new Error(`Sorry, there are no procedures for ${petName}!`);
                }
            }
        };
        for (let index = 0; index < this.clients.length; index++) {
            for (let i = 0; i < this.clients[index].petList.length; i++) {
                if (this.clients[index].petList[i].petName === petName &&
                    this.clients[index].name === ownerName) {
                    const sumCurrent = this.clients[index].petList[i].procedures.length * 500;
                    this.totalProfit += sumCurrent;
                    this.clients[index].petList[i].procedures = [];

                }
            }
        };
        this.currentWorkload -= 1;
        return `Goodbye ${petName}. Stay safe!`;
    };
        
    toString() { 
        let procent = Math.floor((this.currentWorkload / this.capacity) * 100)
        let result = [`${this.clinicName } is ${procent}% busy today!`,
        `Total profit: ${this.totalProfit.toFixed(2)}$`];
        return result.join('\n');
    };
}


let clinic = new VeterinaryClinic('SoftCare', 10);
console.log(clinic.newCustomer('Jim Jones', 'Tom', 'Cat', ['A154B', '2C32B', '12CDB']));
console.log(clinic.newCustomer('Anna Morgan', 'Max', 'Dog', ['SK456', 'DFG45', 'KS456']));
console.log(clinic.newCustomer('Jim Jones', 'Tiny', 'Cat', ['A154B'])); 
console.log(clinic.onLeaving('Jim Jones', 'Tiny'));
console.log(clinic.toString());
clinic.newCustomer('Jim Jones', 'Sara', 'Dog', ['A154B']); 
console.log(clinic.toString());

