"use strict";

const fruits = ['Banana', 'Orange', 'Apple', 'Mango'];
console.log(fruits.toString());         /*  Creates a String from
                                         *  array elements */
console.log(fruits.join('<>'));         /* '<>' as delimiter */
console.log(fruits.pop());              /* Remove last element */
fruits.push('Kiwi');                    /* Add; at the end */
console.log(fruits);
console.log(fruits.shift());            /* Remove first element */
console.log(fruits.unshift('Grape'));   /* Adds at the begining */
fruits[fruits.length] = 'Raspberry';
console.log(fruits);
//delete fruits;                          /* deletes the array */

const flowers = ['Rose', 'Lily'];
const fruits1 = ['mango', 'apple', 'grape'];
const new_list = flowers.concat(fruits1);
console.log(new_list);

const fruits2 = ['Banana', 'Orange', 'Apple', 'Mango'];
fruits2.splice(2, 0, 'Lemon', 'Kiwi');
/*             ^  ^
 *             |  |
 *          index |
 *                |
 *                # of elements to delete
 */
console.log(fruits2);
fruits2.splice(2, 2, 'watermelon', 'maglemelon');
console.log(fruits2);
fruits2.splice(0, 1);
console.log(fruits2);
const new_arr = fruits2.slice(3);
console.log(new_arr);
const new_arr2 = fruits2.slice(1, 3);
console.log(new_arr2);
