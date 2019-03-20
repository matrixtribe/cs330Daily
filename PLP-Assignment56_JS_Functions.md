# JavaScript Functions

Functions are for code reuse and program structure. The make your code easier to read and allow for writing less redundant code. Functions can be called over and over. They can be recursive and there are multiple ways to both create and call them. (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions, https://www.w3schools.com/js/js_functions.asp, https://www.w3schools.com/js/js_function_definition.asp, https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99)

JS functions always return something. They either return the defined value or a value of '*undefined*'. Functions perform tasks, are invoked, and a JS function is an object as well as a function.  (https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99).

JS has function declarations, which can be defined before or after they are used, and function expressions, which must be defined before they are used and can be named or anonymous. (https://codeburst.io/javascript-functions-understanding-the-basics-207dbf42ed99)

## JS Function syntax:
The keyword *function* has to precede any function definition (https://www.w3schools.com/js/js_function_definition.asp).
```
// function declaration
function nameOfFunction(parameters){
  body of function
}

// function expressions
```


With _**if**_ statements, the 'condition' inside the parenthesis must evaluate to true for the 'statement' inside the curly braces to be evaluated.
Below you'll see examples of code syntax with each type _**if**_ statement, notice I separated the curly braces and their statements with new lines for easier reading. It is not required but is good style.
>NOTE: be diligent about using curly braces when else is involved to avoid the 'dangling else' problem. Otherwise you could get stuck with a 'nearest match' or 'furthest match' that you did not expect.
```

```
#### short form _if_
There's another, shorter syntax for the _**if**_ statement:

```

```

### break and continue
Before we move on to _**switch**_ statements we should go over the _**break**_ (sinece they are widely used in _**switch**_) and _**continue**_ operators.
These operators are similar in that they interrupt or change the flow of loops and other statements, and they can be used with lables or by themselves. They are different in that break completely exits a block and stop a statement, but continue simply skips a statement or single iteration of a loop. (https://www.w3schools.com/js/js_break.asp, http://exploringjs.com/impatient-js/ch_control-flow.html#controlling-loops-break-and-continue, https://www.tutorialspoint.com/javascript/javascript_loop_control.htm)

Here are examples of each option:
```

```

### switch
Switch statements are useful for simplifying multiple _**if else**_ options and other cases. They use the _**break**_ or _**return**_ statements to exit a clause. Without one of those statments the block continues to evaluate. They also allow for a default value in case no clause evaluate. (https://www.w3schools.com/js/js_switch.asp, http://exploringjs.com/impatient-js/ch_control-flow.html#if)
Main syntax (others shown in examples):
```

```
Here are some examples:
```

```

### loops
Loops run statements multiple times depending on conditions.(https://www.w3schools.com/js/js_loop_for.asp)
  #### _for_
  _**for**_ loops have a 3 parts to the declaration statement that are all optional, and are used to determine how the loop is executed. The first part is used for initializing one or more variables. If you omit this the variables must be declared outside the loop. The second part is the condition that, if true, runs the loops again. If you omit this is is best the have a _**break**_ statement in the loop to avoid it being infinite. The third part increments the variable that gets evaluated in the condition. Although it is optional, you could end up with an infinite loop without it unless you increment inside the loop.(https://www.w3schools.com/js/js_loop_for.asp, http://exploringjs.com/impatient-js/ch_control-flow.html#for, https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-javascript/iterate-with-javascript-for-loops)
Main syntax:
```

```
Example:
```

```
  
  #### _for of_
  Having the **Symbol.iterator** property is the most important part of something being iterated over in the _**for of**_ loop. It's a function that can iterate over any **iterable**. The header has two parts, a variable representing an element of the iterable, and the iterable itself.(http://exploringjs.com/impatient-js/ch_control-flow.html#for-of, https://bitsofco.de/for-in-vs-for-of/)
Main syntax:
```

```
Example:
```

```
  #### _for await of_
  Promises, promises, promises. This loop helps us iterate through asynchronous (promised) data. It is necessary because the _**for of**_ loop works through iterators consecutively, so a synchronous iterator would be completely evaluated, but an asynchronous iterator would stop before the end. The _**await**_ makes sure to pause a function or generator until the promise resolves. (https://www.codementor.io/tiagolopesferreira/asynchronous-iterators-in-javascript-jl1yg8la1, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of, http://exploringjs.com/impatient-js/ch_control-flow.html#for-await-of, https://medium.freecodecamp.org/promises-in-javascript-explained-277b98850de, https://dev.to/nestedsoftware/the-iterators-are-coming-symboliterator-and-symbolasynciterator-in-javascript-hj)
Main syntax (can only be called from within async function):
```

```
Example of code templated and altered from (https://dev.to/nestedsoftware/the-iterators-are-coming-symboliterator-and-symbolasynciterator-in-javascript-hj):
```


```
  #### _for in_
_**for in**_ is similar to _**for of**_ but its is used to iterate over anything with an **enumerable** property.(https://bitsofco.de/for-in-vs-for-of/, https://www.w3schools.com/js/js_loop_for.asp, http://exploringjs.com/impatient-js/ch_control-flow.html#for-in)
Main syntax:
```

```
Example:
```


```

  #### _while_
  A condition is evaluated at the beginning and then the statements are executed as long as it is true. (http://exploringjs.com/impatient-js/ch_control-flow.html#while, https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-javascript/iterate-with-javascript-while-loops)
  ```

  ```
  #### _do while_
  A statement is first executed, then the condition is evaluated, if True this process happens again. (http://exploringjs.com/impatient-js/ch_control-flow.html#do-while, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
  
  ```

```

### short circuit evaluation
javaScript short circuits - meaning, in a logical expression, it evaluates left to right and stops once it successfully evaluates without going on to further evaluate any other logical options. (https://codeburst.io/javascript-what-is-short-circuit-evaluation-ff22b2f5608c)
For example:
```

```




