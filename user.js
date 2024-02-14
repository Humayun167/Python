const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter your number: ', (a) => {
  rl.question('Enter number-2: ', (b) => {
    const sum = parseInt(a) + parseInt(b);
    console.log('Sum:', sum);
    rl.close();
  });
});
