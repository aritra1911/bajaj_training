"use strict";

/*
 * block scope
 * function scope
 * global scope
 */

/* Block Scope */
m = 4;
n = 2;
if ( m > n )
    var p = 4;
console.log(p); /* accessible */
if ( m > n )
    let g = 4;
console.log(g); /* not accessible */
if ( m > n )
    const h = 4;
console.log(h); /* not accessible */

/*
 * Function Scope
 */
function f1() { let v1 = 9; }
function f2() { var v2 = 10; }
function f3() { const v3 = 11; }
console.log(v1, v2, v3);    /* not accessible
                             * as v1, v2, v3 has
                             * function level scope */

/* global scope */
var v5 = 43;
let v6 = 5;
const v7 = 3;

function check() {
    v5 = 66; v7 = 77
}
console.log(v5, v6, v7);    /* accessible due to
                             * global scope */
