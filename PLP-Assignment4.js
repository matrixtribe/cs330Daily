// (for loop used to show the evaluation of both true and false, if and else)
var a = true;
var x = true;
for (let count = 0; count < 2; count++){
    // just if without else
    if (a) {
        console.log("This single line statement is True");
    }
    // one condition if/else statement
    if (a){
        console.log("This single condition statement is True");
    } else {
        console.log("This single condition statement is False");
    }
    // multi-condition if/else statement (i.e. "if x>0 && y< 10)
    if (a && x){
        console.log("This multi-condition statement is True");

    } else {
        console.log("This multi-condition statement is False");
    }
    // short form if
    if (a) console.log("This short if statement is True");else console.log("This short if statement is False");

    a = false;
}

for(let count = 0; count < 3; count ++){
    // if/else if/else
    if (a && x){
        console.log("a and x are True");
        a = false;
        x = false;
    } else if (x){
        console.log("x is True");
        a = true;
    } else {
        console.log("Both a and a and x are False");
    }
}

// break and continue statements
//standalone break
for(let i = 0; i<5; i++) {
    if (i === 3) break;
    console.log("break at 3: " + i);
}
// standalone continue
for(let i = 0; i<5; i++) {
    if (i === 3) continue;
    console.log("continue at 3: " + i);
}
//label break
break3:
for(let i = 0; i<5; i++) {
    if (i === 3) break break3;
    console.log("break label at 3: " + i);
}
// label continue
continue3:
for(let i = 0; i<5; i++) {
    if (i === 3) continue continue3;
    console.log("continue label at 3: " + i);
}
// a switch-case statement
var myFavorite = 'gray';
// uses default
switch (myFavorite){
    case 'red':
        console.log('Your favorite color is red!');
        break;
    case 'orange':
        console.log('Your favorite color is orange!');
        break;
    case 'black':
        console.log('Your favorite color is black!');
        break;
    default:
        console.log('You live in darkness.')
}
// stops at gray
switch (myFavorite){
    case 'red':
        console.log('Your favorite color is red!');
        break;
    case 'gray':
        console.log('Your favorite color is gray!');
        break;
    case 'black':
        console.log('Your favorite color is black!');
        break;
    default:
        console.log('You live in darkness.')
}
// evaluates and executes cases after the matched clause since no 'break' or 'return'
switch (myFavorite){
    case 'red':
        console.log('Your favorite color is red!');
    case 'gray':
        console.log('Your favorite color is gray!');
    case 'black':
        console.log('Your favorite color is black!');
    default:
        console.log('You live in darkness.')
}

// different kinds of loops: while, do/while, for, foreach
// for
for(let j = 0; j < 2; j++){
    console.log("for: " + j);
}
// for of
var itr = [1, 2, 3]
for (let e of itr) {
    console.log("for of: " + e)
}

// for in
var str = "enum";
for(let index in str){
    console.log("for in: " + str[index]);
}

// for await of -  asynchronous - code templated and  altered from (https://dev.to/nestedsoftware/
// the-iterators-are-coming-symboliterator-and-symbolasynciterator-in-javascript-hj)
const gettingSleepy = () => setInterval(()=>console.log('eyelids flutter'), 300);

class tired {
    constructor() {
        this.index = 0;
        this.steps = ['yawn', 'close eyes','snore']
    }

    next() {
        const value = this.steps[this.index];
        const done = !(this.index in this.steps);
        this.index += 1;
        return new Promise(
            resolve=>setTimeout(()=>resolve({ value, done }), 500))
    }

    [Symbol.asyncIterator]() {
        return {
            next: () => this.next()
        }
    }
}

const goingToBed = async () => {
    const interval = gettingSleepy();

    const bedTime = new tired();
    for await (const doze of bedTime) {
        console.log('sheep = ' + doze)
    }

    clearInterval(interval)
};

goingToBed();

// while - statement will execute 3 times
var num = 0;
while (num <= 2){
    console.log("while: " + num);
    num++;
}
num = 0;
// do while - even though num is 0 the statement will still execute once
do {
    console.log("do while: " + num);
} while (num > 0) ;

// short circuit - height is undefined so age is evaluated
// since age is successfully evaluated JS stops and doesn't even look at name
var height;
var age = 35;
var name = 'Alice';
console.log('short circuit:')
console.log(height || age || name);






