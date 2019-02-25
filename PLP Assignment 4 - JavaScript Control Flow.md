# JavaScript Control Flow 
(http://exploringjs.com/impatient-js/ch_control-flow.html)

There are many ways you can control the flow of a program. Making things happen or not happen, repeat or not repeat, move forward or stop completely.
Please see this file " " for more complete examples of (and executable) code using the following control statements.
## JavaScript has a full compliment of conditionals:
Conditionals are things that happen given a certain condition or conditions exist or don't exist, depending on your logic perspective. The ways JavaScript deals wwith this is through _**if**_, _**if/else**_, and _**switch**_ statements.

### _if_, _if/else_, _if else-if else_
The main sytax is as follows (https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-javascript/use-conditional-logic-with-if-statements, http://exploringjs.com/impatient-js/ch_control-flow.html#if):
```
if (condition){statement}
if (condition){statement} else{statement}
if (condition){statement} else if (condition){statement} else{statement}
```
With _**if**_ statements, the 'condition' inside the parenthesis must evaluate to true for the 'statement' inside the curly braces to be evaluated.
Below you'll see examples of code syntax with each type _**if**_ statement, notice I separated the curly braces and their statements with new lines for easier reading. It is not required but is good style.
```
    // just if without else
    if (a) {
        console.log("This single condition statement is True")
    }
    // one condition if/else statement
    if (a){
        console.log("This single condition statement is True")
    } else {
        console.log("This single condition statement is False")
    }
    // multi-condition if/else statement (i.e. "if x>0 && y< 10)
    if (a && x){
        console.log("This multi-condition statement is True")
    } else {
        console.log("This multi-condition statement is False")
    }
    
    // if/else if/else
    if (a && x){
        console.log("a and x are True")
    } else if (x){
        console.log("x is True")
    } else {
        console.log("Both a and a and x are False")
    }
```
#### short form _if_
There's another, shorter syntax for the _**if**_ statement:

```
// short form if
    if (a) console.log("This short if statement is True");else console.log("This short if statement is False");
```

### break and continue
Before we move on to _**switch**_ statements we should go over the _**break**_ (sinece they are widely used in _**switch**_) and _**continue**_ operators.
These operators are similar in that they interrupt or change the flow of loops and other statements, and they can be used with lables or by themselves. They are different in that break completely exits a block and stop a statement, but continue simply skips a statement or single iteration of a loop. (https://www.w3schools.com/js/js_break.asp, http://exploringjs.com/impatient-js/ch_control-flow.html#controlling-loops-break-and-continue, https://www.tutorialspoint.com/javascript/javascript_loop_control.htm)

Here are examples of each option:
```
// break and continue statements
//standalone break
for(let i = 0; i<5; i++) {
    if (i === 3) break;
    console.log("break at 3: " + i)
}
// standalone continue
for(let i = 0; i<5; i++) {
    if (i === 3) continue;
    console.log("continue at 3: " + i)
}
//label break
break3:
for(let i = 0; i<5; i++) {
    if (i === 3) break break3;
    console.log("break label at 3: " + i)
}
// label continue
continue3:
for(let i = 0; i<5; i++) {
    if (i === 3) continue continue3;
    console.log("continue label at 3: " + i)
```

### switch
Switch statements are useful for simplifying multiple _**if else**_ options and other cases. They use the _**break**_ or _**return**_ statements to exit a clause. Without one of those statments the block continues to evaluate. They also allow for a default value in case no clause evaluate. (https://www.w3schools.com/js/js_switch.asp, http://exploringjs.com/impatient-js/ch_control-flow.html#if)
Here are some examples:


### loops
  #### various _for_ loops (for, for-of, for-await-of, for-in)
  for loops
  for-of loops
  for-await-of loops
  for-in loops
  
  #### various _while_ loops (while, do while)
  while loops
  do-while loops

### short circuit evaluation
javaScript short circuits - meaning, in a logical expression, it evaluates left to right and stops once it successfully evaluates without going on to further evaluate any other logical options. (https://codeburst.io/javascript-what-is-short-circuit-evaluation-ff22b2f5608c)
For example:
```
// short circuit - height is undefined so age is evaluated
// since age is successfully evaluated JS stops and doesn't even look at name 
var height;
var age = 35;
var name = 'Alice'
console.log(height || age || name);
```



