"use strict";

const myObject = {
    x: 10,
    y: true,
    z: 'abc'
};

for ( let key in myObject )
    console.log(key, myObject[key]);

const myObject2 = [1, 2, 3, 4];
for ( let k of myObject2 )
    console.log(k)
