"use strict";

/*
 * call() method
 * -------------
 *  An Object can use
 *  a method belonging to
 *  another object.
 */

const Emp = {
    //fullname: () => this.fname + ' ' + this.lname
    fullname: function () {
        return this.fname + ' ' + this.lname;
    }
};

const Emp1 = {
    fname: 'Ron',
    lname: 'Barry'
};

const Emp2 = {
    fname: 'John',
    lname: 'Doe'
};

console.log(Emp.fullname.call(Emp1));
console.log(Emp.fullname.apply(Emp2));
