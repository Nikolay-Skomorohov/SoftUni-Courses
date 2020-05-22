function fruit(type, weight, price) {
    let result;
    let kilos = weight / 1000
    result = kilos * price
    console.log(`I need $${result.toFixed(2)} to buy ${kilos.toFixed(2)} kilograms ${type}.`)
}

fruit('orange', 2500, 1.80)
fruit('apple', 1563, 2.35)
