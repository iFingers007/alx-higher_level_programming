#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const numArray = args.map(str => parseInt(str));
  const sortedArray = numArray.sort((a, b) => b - a);
  console.log(sortedArray[3]);
}
