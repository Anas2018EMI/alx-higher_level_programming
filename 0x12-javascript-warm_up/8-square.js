#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < size; i++) {
    row += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(row);
  }
}
