#!/usr/bin/node
const args = process.argv;
const argsCount = args.length;

if (argsCount <= 2) {
  console.log('No Argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
