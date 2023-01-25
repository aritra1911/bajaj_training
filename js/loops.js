"use script";

let i = 1;
while ( i < 10 )
    console.log(i++);

for ( let i=1; i <= 10; i++ ) {
    if ( i == 6 )
        continue;
    console.log("Number " + i);
}

for ( let i = 1; i <= 10; i++ ) {
    if ( i == 4 )
        break;
    console.log("Number " + i);
}
