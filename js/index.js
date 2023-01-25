"use strict";

const ages = [3, 10, 18, 20, 25]

function checkAge(age) {
    return age > 18;
}

function myFunc() {
    /*
     * The find() function returns value of the first element that
     * passes the test
     */
    console.log(ages.find(checkAge))
}

myFunc()