# JavaScript Functions

Functions are for code reuse and program structure. The make your code easier to read and allow for writing less redundant code. Functions can be called over and over. They can be recursive and there are multiple ways to both create and call them. (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions, https://www.w3schools.com/js/js_functions.asp, https://www.w3schools.com/js/js_function_definition.asp, https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99)

JS functions always return something. They either return the defined value or a value of '*undefined*'. Functions perform tasks, are invoked, and a JS function is an object as well as a function.  (https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99).

When a function is a property of an object it is referred to as a method. (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)


## JS Function syntax, invokation, and placement:
As shown above, JS has function declarations which can be defined before or after they are used, and function expressions which must be defined before they are used. Function expressions can be named, allows function to refer to iself inside the body and help identify it in debugging,  or anonymous. Function expressions also have a short form called *Arrow function Expressions* .(https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions,https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99)
The keyword *function* has to precede any function definition unless it is created using the *Function constructor*. (https://www.w3schools.com/js/js_function_definition.asp)

Functions created with the *Function constructor* are anymous. (https://www.tutorialspoint.com/javascript/javascript_function_constructors.htm)

Up to __255__ parameters can be passed in functions. (https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99)

```
// function declaration
function nameOfFunction(parameters){
  // body of function
  return;
}
// invoked

// function expressions - can be inline
// named
var variableName = function nameOfFunction(parameters){/*body of function*/};

// anonymous
var variableName = function(parameters){
  // body of function
};

// arrow functions
var functionName = (parameters) => {
  // body of function
}

// Function constructor
var variableName = new Function(arguments, separted, by, commas, the last argument; is the function body; with code separated by semi-colons;);


}
```


With _**if**_ statements, the 'condition' inside the parenthesis must evaluate to true for the 'statement' inside the curly braces to be evaluated.
Below you'll see examples of code syntax with each type _**if**_ statement, notice I separated the curly braces and their statements with new lines for easier reading. It is not required but is good style.
>NOTE: be diligent about using curly braces when else is involved to avoid the 'dangling else' problem. Otherwise you could get stuck with a 'nearest match' or 'furthest match' that you did not expect.
```

```



