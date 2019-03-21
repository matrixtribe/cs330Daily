# JavaScript Functions
>NOTE: Code examples can be found and run in this file: 

Functions are for code reuse and program structure. The make your code easier to read and allow for writing less redundant code. Functions can be called over and over. They can be recursive and there are multiple ways to both create and call them. (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions, https://www.w3schools.com/js/js_functions.asp, https://www.w3schools.com/js/js_function_definition.asp, https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99)

JS functions always return something. They either return the defined value or a value of '*undefined*'. Functions perform tasks, are invoked, and a JS function is an object as well as a function.  (https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99).

When a function is a property of an object it is referred to as a method. (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)


## JS Function syntax, invokation, placement, and parameters:
As shown above, JS has function declarations which can be defined before or after they are used, and function expressions which must be defined before they are used. Function expressions can be named, allows function to refer to iself inside the body and help identify it in debugging,  or anonymous. Function expressions also have a short form called *Arrow function Expressions* .(https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions,https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99)

### Placement
The keyword *function* has to precede any function definition unless it is created using the *Function constructor*. (https://www.w3schools.com/js/js_function_definition.asp)

Functions created with the *Function constructor* are anonymous and their arguments must be strings. (https://www.tutorialspoint.com/javascript/javascript_function_constructors.htm)

### Parameters
Up to __255__ non-typed parameters can be passed into functions. Tpassed arguments are not type or size checked and extra arguments are ignored. Missing arguments are set to undefined. (https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99, https://www.w3schools.com/js/js_function_parameters.asp)

```
// function declaration
function nameOfFunction(parameters){
  // body of function
  return;
}
// invoked
console.log(nameOfFunction(arguments));

// function expressions - can be inline
// named
var variableName = function nameOfFunction(parameters){/*body of function*/};

// invoked
console.log(variableName(arguments));

// anonymous
var variableName = function(parameters){
  // body of function
};

// invoked
console.log(variableName(arguments));

// arrow functions
var functionName = (parameters) => {
  // body of function
};

// invoked
console.log(functionName(arguments));

// Function constructor -- arguments MUST be strings
var variableName = new Function('arguments', 'the last argument; is the function body; with code separated by semi-colons;');

}

// invoked
console.log(variableName(arguments));

```
## Recursive functions
A recursive function calls itself. It's another way to write less code and cleaner code but can be inefficient.(https://eloquentjavascript.net/03_functions.html)
```
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
```
## Multiple return values
JS does not natively support multiple value returns. However some improvements have been made to work around that. IN JS6 (or ECMA Script 6) not only were paramater defaults and the Arrow function syntax introduced, but it also introduced an array-like return that allows values to be assigned to multiple variables. (http://qnimate.com/javascript-return-multiple-values/, https://www.w3schools.com/js/js_es6.asp)

```
// multiple value function
function shero(){
    return ['Xena ', 'Warrior ', 'Princess']
}

// invoked
var first, middle, last;
[first, middle, last] = shero()
console.log( first + middle + last + " is the BEST SHERO EVER!!")
```

## Variables
Variables are global if they are declared outside a function. A variable declared inside a function is local to that function (many functions can use the same variable names) as are the arguments passed to them, however a function can see variables outside of it. This only applies from the outside in. It is useful for nested functions. An exception to local variable scope in functions, is if a value is assigned to an undeclared variable. That variable will automatically become global.(https://www.w3schools.com/js/js_scope.asp)

