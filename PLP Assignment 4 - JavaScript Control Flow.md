# JavaScript Control Flow (http://exploringjs.com/impatient-js/ch_control-flow.html)
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
        console.log("This single condition statement is False");
    }
    // multi-condition if/else statement (i.e. "if x>0 && y< 10)
    if (a && x){
        console.log("This multi-condition statement is True")

    } else {
        console.log("This multi-condition statement is False");
    }
    
    // if/else if/else
    if (a && x){
        console.log("a and x are True")
    } else if (x){
        console.log("x is True")
    } else {
        console.log("Both a and a and x are False");
    }
```
### switch

### loops
  #### various _for_ loops (for, for-of, for-await-of, for-in)
  for loops
  for-of loops
  for-await-of loops
  for-in loops
  
  #### various _while_ loops (while, do while)
  while loops
  do-while loops


