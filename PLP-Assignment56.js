// syntax for declaring a function
// function declaration
function functionOne(parameter){
    //body of function
    return "return statements are not necessary if no value to return is needed" + parameter;
}
console.log(functionOne(" and can have 0-255 parameters"));

// function expressions
// named
var variableName1 = function nameOfFE(parameter1, parameter2){return parameter1 + parameter2};

// invoked
console.log(variableName1("named ", "function expression"));

// anonymous
var variableName2 = function(parameter1, parameter2){
    // body of function
    return parameter1 + parameter2
};

// invoked
console.log(variableName2("anonymous ", "function expression"));

// arrow functions
var arrowName = (parameter) => {
    return parameter
};

// invoked
console.log(arrowName("arrow function expression"));

// Function constructor
var variableFCName = new Function('argument', 'return argument;');

// invoked
console.log(variableFCName("function constructor"));

// recursive function
function countdown(seconds) {
    if (seconds === 0) {
        return "Happy New Year!!";
    } else {
        console.log(seconds);
        return countdown(seconds - 1);
    }
}
// invoked
console.log(countdown(10));

// multiple value function
function shero(){
    return ['Xena ', 'Warrior ', 'Princess']
}

// invoked
var first, middle, last;
[first, middle, last] = shero();
console.log( first + middle + last + " is the BEST SHERO EVER!!");

// variable scope
// using var there is a duplicate variable because the x is global and there is no block scope with var
var a = 3;
var b = "Global b";
while(a > 0){
    var b = 'loop b';
    console.log(b);
    a--;
}
// Global b is overwritten in loop so only local b prints
console.log(b);

// using let makes the variable inside the loop block scoped so it will run 3 times since the original variable is no
// longer overwritten
var y = 3;
var z = "Global z";
while(y > 0){
    let z = 'loop z';
    console.log(z);
    y--;
}
console.log(z);

// functions inherently have their own scope
var c = "global c";

function functionScope(){
    var c;
    c = "function c";
    return c;
}

console.log(c);
console.log(functionScope());

// passed by value
var q = "initial value";
console.log("q before function " + q);
function changeValue(value){
    value = "new value";
    console.log("q passed to function " + value)
}
// invoke function
changeValue(q);
// print q - value stays the same
console.log("q after function " + q);

// passed by reference
var character = new Object();
character.name = "Gabrielle";
character.profession = "Bard";
console.log("Character name is : " + character.name);
console.log("Initial character profession is : " + character.profession);

function changeProfession(object, job){
    object.profession = job;
}

// object property is changed in function and shows outside function scope
changeProfession(character, "Warrior");
console.log("Character name is : " + character.name);
console.log("New character profession is : " + character.profession);

// Assignment handling
var r = ['c','a','t'];
console.log("first value or r: " + r);
var s = ['d','o','g'];
console.log("first value of s: " + s);
// r now refers to s
r=s;
console.log("value of r after 'r=s': " + r);
// the value of the element at index 1 in array s is overwritten by value 'u'
s[1] = 'u';
console.log("value of s after 's[1] = u': " + s);
// since r points to s now, they are the same even though the 'o' was changed to 'u' after r was assigned to s
console.log("final value of r: " + r);
console.log("final value of s: " + s);