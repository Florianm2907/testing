// calculator
const prompt = require('prompt-sync')({ sigint: true });
while (true) {
    let number1 = parseFloat(prompt("Enter first number: "));
    if(isNaN(number1)){
        console.log("Invalid number, please try again.");
        continue;
    }
    let operation = prompt("Enter operation (+, -, *, /) or 'exit' to quit: ");
    if (operation == 'exit') {
        break;
    }
    if (!['+', '-', '*', 'x', 'X', '/'].includes(operation)) {
        console.log("Invalid operation, please try again.");
        continue;
    }
    let number2 = parseFloat(prompt("Enter second number: "));
    if(isNaN(number2)){
        console.log("Invalid number, please try again.");
        continue;
    }
    switch (operation) {
        case '+':
            result = number1 + number2;
            break;
        case '-':
            result = number1 - number2;
            break;
        case '*' || 'x' || 'X':
            result = number1 * number2;
            break;
        case '/':
            if (number2 === 0) {
                console.log("Error: Division by zero");
                continue;
            }
            result = number1 / number2;
            break;
        default:
            console.log("Invalid operation");
            continue;
    }
    console.log(`Result: ${result}`);
}