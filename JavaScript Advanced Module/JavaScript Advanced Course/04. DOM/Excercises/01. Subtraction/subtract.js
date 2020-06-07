function subtract() {
    const getFirstNumber = Number(document.getElementById("firstNumber").value);
    const getSecondNumber = Number(document.getElementById("secondNumber").value);
    const result = (getFirstNumber - getSecondNumber);
    const resultDiv = document.getElementById("result");
    resultDiv.innerText = result;
}