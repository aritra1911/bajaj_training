let day;

switch ( new Date().getDay() ) {
case 0:
    day = "Sunday";
    break;

case 2:
    day = "Tuesday";
    break;

case 6:
    day = "Saturday";
    break;

default:
    day = "No Match!!";
    break;
}

console.log(day);
