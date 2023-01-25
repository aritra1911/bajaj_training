"use strict";

class Emp {
    static company = 'Bajaj Markets';

    constructor(eid, ename, esal) {
        this.eid = eid;
        this.ename = ename;
        this.esal = esal;
    }

    set id(eid) { this.eid = eid; }
    set name(ename) { this.ename = ename; }
    set sal(esal) { this.esal = esal; }

    get id() { return this.eid; }
    get name() { return this.ename; }
    get sal() { return this.esal; }

    disp() { console.log(this.eid, this.ename, this.esal); }
    static getCompany() { return Emp.company; }
}

let e1 = new Emp('E0001', 'Sandip', 56000);
e1.disp();
console.log(Emp.getCompany());
console.log(e1.id, e1.ename, e1.esal);

e1.id = 'E002';
e1.name = 'Kiran';
e1.sal = 35000;

console.log(e1.eid, e1.ename, e1.esal);
Emp.company = 'Bajaj Financial Markets';
console.log(Emp.company);
