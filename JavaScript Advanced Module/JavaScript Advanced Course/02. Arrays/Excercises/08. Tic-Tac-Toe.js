function solve(aList) {
    const resultMatrix = [[false, false, false],
                          [false, false, false],
                          [false, false, false]];
    const player1 = 'X';
    const player2 = 'O';
    let gameWinner = null;
    let playerTurn = player1
    while ((resultMatrix[0].some(element => element === false) ||
           resultMatrix[1].some(element => element === false) ||
           resultMatrix[2].some(element => element === false)) &&
           aList.length > 0 && 
           gameWinner === null) {
        let nextMove = aList.shift();
        const moveRow = Number(nextMove[0]);
        const moveCol = Number(nextMove[2]);
        if (resultMatrix[moveRow][moveCol] == false) {
            resultMatrix[moveRow][moveCol] = playerTurn;
            playerTurn == player1 ? playerTurn = player2 : playerTurn = player1;
            }
        else {
            console.log('This place is already taken. Please choose another!');
        }
        let winCoords = [[resultMatrix[0][0], resultMatrix[0][1], resultMatrix[0][2]],
                         [resultMatrix[1][0], resultMatrix[1][1], resultMatrix[1][2]],
                         [resultMatrix[2][0], resultMatrix[2][1], resultMatrix[2][2]], 
                         [resultMatrix[0][0], resultMatrix[1][1], resultMatrix[2][2]],
                         [resultMatrix[0][2], resultMatrix[1][1], resultMatrix[2][0]],
                         [resultMatrix[0][0], resultMatrix[1][0], resultMatrix[2][0]],
                         [resultMatrix[0][1], resultMatrix[1][1], resultMatrix[2][1]],
                         [resultMatrix[0][2], resultMatrix[1][2], resultMatrix[2][2]]];
        for (let c = 0; c < winCoords.length; c++) {
            if (winCoords[c].every(elem => elem === "X")) {
                gameWinner = player1;
                break;
            }
            else if (winCoords[c].every(elem => elem === "O")) {
                gameWinner = player2;
                break;
            }
        }
        // console.log(resultMatrix[0].some(element => element === false));
        // console.log(resultMatrix[1].some(element => element === false));
        // console.log(resultMatrix[2].some(element => element === false));
        // console.log(aList.length != 0);
        // console.log(gameWinner === null);
    }
    if (gameWinner === null) {
        console.log('The game ended! Nobody wins :(');
    }
    else {
        console.log(`Player ${gameWinner} wins!`);
    }
    for (let row = 0; row < resultMatrix.length; row++) {
        console.log(`${resultMatrix[row][0]}\t${resultMatrix[row][1]}\t${resultMatrix[row][2]}`)
    }
}

solve(["0 1", "0 0", "0 2", "2 0", "1 0", "1 1", "1 2", "2 2", "2 1", "0 0"]);
solve(["0 0", "0 0", "1 1", "0 1", "1 2", "0 2", "2 2", "1 2", "2 2", "2 1"]);
solve(["0 1", "0 0", "0 2", "2 0", "1 0", "1 2", "1 1", "2 1", "2 2", "0 0"]);