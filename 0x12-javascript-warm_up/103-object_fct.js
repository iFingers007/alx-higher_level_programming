#!/usr/bin/node
const myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);
  /*
  YOUR CODE HERE
  */
 function increment () {
    this.value += 1;
  }
  myObject.incr = increment.bind(myObject);
  
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);