function solve(aList) {
    const resultMatrix = [[false, false, false],
                          [false, false, false],
                          [false, false, false]];
    const player1 = 'X';
    const player2 = 'O';

    while (resultMatrix.every(element => element == false)) {
        
        for (let i = 0; i < aList.length; i++) {
            playerTurn = i % 2 === 0 ? player1 : player2;
            const moveRow = Number(aList[i][0]);
            const moveCol = Number(aList[i][2]);
            if (resultMatrix[moveRow][moveCol] == false) {
                resultMatrix[moveRow][moveCol] = playerTurn;
            }
            else {
                consolve.log('This place is already taken. Please choose another!');
            }
        }
    }
    
}

solve(["0 1", "0 0", "0 2", "2 0", "1 0", "1 1", "1 2", "2 2", "2 1", "0 0"]);
// solve(["0 0", "0 0", "1 1", "0 1", "1 2", "0 2", "2 2", "1 2", "2 2", "2 1"]);
// solve(["0 1", "0 0", "0 2", "2 0", "1 0", "1 2", "1 1", "2 1", "2 2", "0 0"]);