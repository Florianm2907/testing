// Define the number of iterations to use in the calculation
const n = 1000000;

// Initialize the value of graham's number to 0
let graham = BigInt(1);

// Use the Leibniz formula to calculate Graham's number
for (let i = 0; i < n; i++) {
  graham += BigInt(Math.pow(-1, i)) / BigInt((2 * i + 1));
}

// Multiply the result by 4 to get the final value of Graham's number
graham = graham * BigInt(4);

// Print the result
console.log(graham);
