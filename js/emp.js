"use strict";

const Emp = {
    eid: "E001",
    fname: "John",
    lname: "Doe",
    fullname: function() {
        return this.fname + " " + this.lname;
    }
}

console.log(Emp.fullname())
