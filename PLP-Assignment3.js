// Write a piece
// of code that creates variable of each of these common data types and follows the naming conventions:
// • int
var myAge = 41;
// • string
var helloWorld = "Hello World";
// • floating-point number
var floatingPoint = 1.2;
// • boolean
var yes = true;
// • array/list
var stringArray = ["Harry", "Hermione", "Ron"]
// • hash/dictionary
var  dictionary = {
    "key1": "Sulu",
    "key2": "Tasha",
    "key3": "Uhura",
    "key4": "Kira",
    "key5": "Dax",
};
/* can you add ints and floats? - Yes
If you do, is the resulting variable an int (narrowing conversion) or a float (widening conversion)? - the only
data type for a number is 'number' so I don't think it's actually widening like it appears to be since both numbers
are still just 'number'*/
console.log(myAge + floatingPoint);

// Can you put different data types in the same array or list? - yes
var intAndStringArray = [];
intAndStringArray.push(myAge);
intAndStringArray.push(helloWorld);
intAndStringArray.push(dictionary.key1.valueOf());
console.log(intAndStringArray);

// Can one data type be converted to another (int to float, string to int, etc)? - yes
console.log(yes.toString());
var name;
var intArray = [];
for (name in stringArray){
    intArray.push(parseInt(name,10));
}
console.log(stringArray);
console.log(intArray);
