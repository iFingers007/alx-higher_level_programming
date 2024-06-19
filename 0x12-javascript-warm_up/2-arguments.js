#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('No Argument');    
} else {
    console.log('Arguments found'); 
}