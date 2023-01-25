"use strict";

/* function expression assigned to variable */

const myFunc = (a, b) => {
    let c;
    a += 1;
    c = a + b;
    return c;
};

console.log(myFunc(5, 4));

/* Function expression as argument in the function call */
setTimeout(() => console.log('Delayed noose'), 1000);
/*            ^
 *            |
 *            +--- callback function */

let i = 1;
const myInterval = setInterval(
    () => console.log('Here is the message variable ' + i++),
    2000
);
//console.log(myInterval);

setTimeout(() => clearInterval(myInterval), 10000);
