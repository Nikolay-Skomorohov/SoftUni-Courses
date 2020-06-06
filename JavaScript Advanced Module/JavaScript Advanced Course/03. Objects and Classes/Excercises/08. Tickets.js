function solve(inputList, param) {
    const result = [];
    const sortParam = param;

    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = Number(price);
            this.status = status;
        }
    }
    for (let item of inputList) {
        let ticketInfo = item.split("|");
        let newTicket = new Ticket(ticketInfo[0], ticketInfo[1], ticketInfo[2]);
        result.push(newTicket);
    }
    if (sortParam === 'destination') {
        result.sort(function(a, b) {
            if (a.destination < b.destination) {
                return -1;
            }
            else if (a.destination > b.destination) {
                return 1;
            }
        })
    }
    else if (sortParam === 'price') {
        result.sort(function(a, b) {
            if (a.price < b.price) {
                return -1;
            }
            else if (a.price > b.price) {
                return 1;
            }
        })
    }
    else if (sortParam === 'status') {
        result.sort(function(a, b) {
            if (a.status < b.status) {
                return -1;
            }
            else if (a.status > b.status) {
                return 1;
            }
        })
    }
    return result;
}

solve(['Philadelphia|94.20|available',
       'New York City|95.99|available',
       'New York City|95.99|sold',
       'Boston|126.20|departed'],
       'destination'
);

