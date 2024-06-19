#!/usr/bin/node
const args = process.argv;
const argsNum = parseInt(args[2]);

if (isNaN(argsNum)) { console.log('Not a number'); } else { console.log('My Number: ' + `${argsNum}`); }
