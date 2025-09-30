/*
  Simple example to demonstrate the basics of JavaScript
*/

/* 
  JavaScript has three specifiers for variables:
  * const - A variable is constant. By that we mean it cannot be
            reassigned.
  * let - A variable with block scope (within {} braces). This is how you would normally
            expect C/C++/Java variables to work.
  * var - A variable that has either function-level scope or global scope
            depending on where it is declared. This has fallen out of favor
            in modern JS, where let and const are primarily used.
*/
// This string is bound to the className variable
const className = "Introduction to JavaScript for React";

// We cannot do this as it would cause className to be bound
//  to the new string.
// className = "Changed"

// An array of student objects (Python Lingo: A list of dictionaries)
//  Making this list const does NOT mean you cannot add items to it or
//  modify the content in the list. It DOES mean, you cannot assign a
//  brand new list to the students variable.
const students = [
  { id: 1, name: "Alice", grade: 92, isPresent: true },
  { id: 2, name: "Bob", grade: 88, isPresent: false },
  { id: 3, name: "Charlie", grade: 95, isPresent: true },
];

/*
    Backtick (``) represents a template literal. This is like our f-strings
    in Python. Here we can add variable values into the string. Template
    literals also allow for the string to span multiple lines.

    Console.log() prints out messages to the terminal. When run on a webpage,
    these messages will appear in the web browser's developer tool console.
*/
console.log(`\n--- Welcome to the ${className} class! ---`);
console.log("Initial Roster:", students);


/*
  functions are created in JavaScript using the function keyword. From there,
  things are mostly the same as they are in Python. Functions can have zero or
  more parameters and return data when they are called.
*/
function findStudentById(id) {
  // For loops are written Java/C++ Style
  for (let i = 0; i < students.length; i++) {
    /* 
      We use the strict equality operator '===' because it requires the two
        things being compared to be the same type. 
        A good example is 1 == '1' is True. The string is "coerced" or converted to 5. 
        However, 1 === '1' is False because int and string are different types.
      
      Also of note is the .id portion. Remember these are objects, we do not use Python
      style ['id'] syntax to acess the key value pair.
    */
    if (students[i].id === id) {
      return students[i];
    }
  }
  return null; // Return null if no student is found
}

/* 
  Functions are first-class objects in JavaScript this means
  that you can treat them like variables.

  Why is this important? We can pass functions as arguments to 
  augment how other functions work. This is often referred to as
  a function callback.

  Let's look at a very simple example.


  This function formats student data into a neat format.
*/
function prettyStudentFormat(student) {
  return `${student["name"]}(ID#:${student["id"]}) ${student['grade']}%`
}

/*
  This function simply takes the student data and create a CSV or 
  comma separated list of the values.
*/
function commaSeparateFormat(student) {
  return `${student["id"]},${student["name"]},${student['grade']},${student['isPresent']}`
}

/*
  This function takes a student AND one of our above "Format" functions. Depending
  on which function it gets, will determine how the data will be formatted by the
  formattting function. This sending of a function with it's own functionality is 
  to suppoprt the formatting function is the callback.
*/
function formatting(student, callbackFunc) {
  return callbackFunc(student);
}

/*
  Arrow functions are a different way of writing functions in JavaScript (you'll
  see a fair bit of this). Parsing out this line of code for findStudentByIdArrow.

  This function can be called using the name findStudentByIdArrow. After the assignment
  operator are the parameters that will be given to the function. In this case, we have one
  paramter, id. The arrow indicates that what follows is the body of the function. This code
  will return the result of calling the find() array method on the students array.

  The find() method is interesting as it requires a function as the parameter so that it can
  decide what the find method should be looking for. This function needs to return True or False
  results to determine a "match" that is "found". These kind of JavaScript functions that require
  callbacks are a common use case for arrow functions.

  If you'll notice, this too is using an arrow function. The find function automatically iterates
  over our list of students. It then places each item in our list into the student variable (this
  is just a normal variable, it could be named anything. The arrrow function then takes the id of the
  student and compares it to the id value passed to findStudentByIdArrow)
*/
const findStudentByIdArrow = (id) => {
  return students.find((student) => student.id === id);
};

/* 
  This demonstrates using the findStudentByIdArrow arrow function.
  This specific usage will try to find a student with an id number 2.
*/
let student = findStudentByIdArrow(2);

// If statements work as expected and can be compared to C/C++/Java if statements.
if (student) {
  console.log(`\nFound student with ID 2: ${student.name}.`);
  
  /* 
    This is ternary condition. The ? is called the ternary operator and the the content before the ?
    is the condition. If it's true, you run the first statement after the ? and before the colon (:). If it's false, you get
    the statement after the colon.
  */
  const attendanceStatus = student.isPresent ? "is present." : "is absent.";

  console.log(`${student.name} ${attendanceStatus}`);
} else {
  console.log("\nStudent not found.");
}

/*
  The .map() method used to create a new list of data by performing an operation
  using a callback function on each item in the collection. The result is a list
  that is a transformation of the original data.

  This is a very important function for rendering lists with React.

  This code is essentially, making a list of just the students names
  from the list of student objects.
*/
const studentNames = students.map((student) => student.name);
console.log("\nStudent Names:", studentNames);


/* 
  Like map(), the filter() method uses a callback function for each item, but is
  intended to supply a subset of the original items in a new list based on the
  condition of the callback.

  In this example, we create a new list that is a subset of the students
  who were marked as present.
*/

const presentStudents = students.filter((student) => student.isPresent);
console.log("Present Students (filtered):", presentStudents);

/*
  In JavaScript, this is referred to as destructuring.
  We are essetially breaking down the data from the student object and
  placing (in this case part of it) into separate variables.

  Here we are asking to have the values from the name and grade fields 
  for the first student stored in the variables name and grade. Notice how
  the variable names match the attributes (keys) of the object.
*/
const { name, grade } = students[0];
console.log(`\nThe first student on the list is ${name} with a grade of ${grade}.`);

/*
  If you want to use different variable names, you can use key:value style syntax
  we've seen in Python.
*/
const { name:studentName, id:studentID } = students[0];
console.log(`\nThe first student on the list is ${studentName} with the ID #${studentID}.`);

/* 
  We can create a new student object. The syntax is similar to Python, but
  the quotes around the "keys" is not necessary. After all, these are JavaScript
  objects, so those are the attributes of the object! :)
*/ 
const newStudent = { id: 4, name: "Daniel", grade: 78, isPresent: true };
console.log("New student to add:", newStudent);

/* 
    Here, we are going to use the spread syntax (...) and create a new list
    with all our previous students from the students list and add our
    newStudent to the list.

    ...students take all the students

    This is how you should update state in React
*/
const updatedStudents = [...students, newStudent];
console.log("\nUpdated Roster (after adding Daniel):", updatedStudents);

// The original 'students' array remains unchanged
console.log("Original Roster (unmodified):", students);

/*
  Let's combine the destructuring syntax with the spread syntax
  to create a new list that removes the second student 
  
  First, we descructure updatedStudents array into to variables.
  firstStudent holds the first student while the empty,
  space in between the commas tells javascript to skip the
  second item. Last the ...rest is a spread operation that
  will hold the "rest" of the list. This is just a varible,
  but common convention is to call it rest.
*/
const [firstStudent, , ...rest] = updatedStudents;

/*
  No we will recombine our firstStudent with the rest of the
  array using the spread syntax (...rest).
*/
const removeSecondStudent = [firstStudent, ...rest];
for (let i = 0; i < removeSecondStudent.length; ++i) {
  console.log(removeSecondStudent[i].name);
}

/*
  Example of passing a function as a parameter (callback)
*/
for (let i = 0; i < students.length; ++i) {
  console.log(formatting(students[i], prettyStudentFormat))
}