#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (const num of numbers) {
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num < firstMax) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}
