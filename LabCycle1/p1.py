STYLE.CSS

body {
         font-family: 'Montserrat', sans-serif;
      }
      h2 {
         display: flex;
         justify-content: center;
         color: green;
         margin-left: 1px;
      }
      form {
         max-width: 500px;
         margin: 0 auto;
         padding: 20px;
         border: 2px solid #ccc;
         border-radius: 10px;
         background-color:  Whitesmoke;
      }
      label {
         display: block;
         font-weight: bold;
         margin-bottom: 10px;
      }
      input[type="text"],
      input[type="email"],
      input[type="tel"] {
         width: 100%;
         padding: 10px;
         margin-bottom: 20px;
         border: 1px solid grey;
         border-radius: 5px;
         box-sizing: border-box;
      }
      input[type="submit"] {
         background-color: forestgreen;
         color: white;
         padding: 10px 20px;
         border: none;
         border-radius: 5px;
         cursor: pointer;
      }
      input[type="submit"]:hover {
         background-color: darkgreen;
      }
      .submit-box {
         text-align: center;
         position: relative;
         display: flex;
         align-items: center;
         justify-content: center;
         margin-top: 20px;
      }
      div {
         position: relative;
         display: flex;
         font-size: small;
      }
      .error {
         border: 2px solid red;
      }
 
function validateForm() {
var Fname = document.forms["form"]["fname"].value;
var Lname = document.forms["form"]["lname"].value;
var email = document.forms["form"]["email"].value;
var phone = document.forms["form"]["phone"].value;
if (Fname == "") {
alert("Please enter your FIRST-NAME to proceed further...");
return false;
}
if (!isNaN(Fname)) {
alert("please enter valid name...");
return false;
}
if (email == "") {
alert("Please enter valid EMAIL to proceed further...");
return false;
}
if (phone == "") {
alert("Please enter your CONTACT number to proceed further...");
return false;
}
if (isNaN(phone)) {
alert("Invalid CONTACT number");
return false;
}
}
<html>
<head>
<title>Student details</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<h2>Student Details</h2>
<form id="form" onsubmit=" return validateForm()"  action="insert(student).php" method="post">
<label for="fname">First- Name:</label>
<input type="text" id="fname" name="fname">
<br>
<br>
<label for="lname">Last-Name:</label>
<input type="text" id="lname" name="lname">
<br>
<br>
<label for="email">Email:</label>
<input type="email" id="email" name="email" placeholder="abc@xyz.com">
<br>
<br>
<label for="phone">Phone:</label>
<input type="tel" id="phone" name="phone" placeholder="1234567890" pattern="[0-9]{10}">
<br>
<br>
<div class="submit-box">
<input type="submit" value="Submit">
</div></form>
<script src="script.js">
</script></body></html>
<?php
$servername="localhost";
$username="23mca008";
$password="2086";
$dbname="23mca008";
$conn=new mysqli($servername,$username,$password,
$dbname);
if($conn->connect_error){
die("connection failed:".$conn>connect_error);
}
$sql="INSERT INTO student1(fname,lname,email,phone)VALUES('$_POST[fname]','$_POST[lname]','$_POST[email]','$_POST[phone]')";
if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>




Date:
<html>
<head>
<title>Program 3</title>
<style>
h1{
    color:green;
    text-decoration:underline;
}
</style>
</head>
<body>
<br><br><br>
<center>
<h1>Current Date</h1>
<p id="date"> </p>
<script>
document.getElementById("date").innerHTML= Date();
</script>
</body>
</html>
 
Positive or negetive
<h1>Check if positive or negative</h1>
<label>
enter the  number</label>
<input type="text" id="x"></input><br><br><br>
<button type="button" onClick="myFunction()">Check</button><br><br><br>
<p id="eo"></p>
<script>

function myFunction(){
var x = document.getElementById("x").value;
if(parseInt(x)>0){
    document.getElementById("eo")
.innerHTML="The number is Positive"
    }
else if(parseInt(x)==0){
    document.getElementById("eo")
.innerHTML="The number is Zero"
    }
else{
  document.getElementById("eo")
.innerHTML="The number is Negative"
    }
}
</script>
text colour change:
<html>
<head>
<title>Change Text Color on Button Click</title>
</head>
<body>
<center><br><br><br>
<p id="textToChange">With great power comes great responsibility.</p>
<button onclick="changeTextColor()">CLICK
</button>
<script>
function changeTextColor() {
var textElement = document.getElementById("textToChange");
textElement.style.color = "blue";
}
</script>
</center>
</body>
</html>
 
Background-colour:
<html>
<head>
<title>program6</title>
</head>
<body >
<center><br><br>
<p>Click to change the background colour.</p><br>
<button type="button" onclick="myFunction()">Set background color</button>
<script>
function myFunction() {
  document.body.style.backgroundColor = "red";
}
</script>
</center>
</body>
</html>






 
para-colour change:
<html>
<head>
<title>program7</title>
<script>
function myFunction() {
  var setcolor=prompt("please enter the color ")
  var txtclr=document.getElementById("txt");
  txtclr.style.color=setcolor;
}
</script>
</head>
<body >
<center>
<h1>JavaScript</h1>
<p id="txt">JavaScript (JS) is a lightweight interpreted (or just-in-time compiled)
<br> programming language with first-class functions. While it is most well-
<br>known as the scripting language for Web pages, many non-browser 
<br><environments also use it, such as Node.js, Apache CouchDB and<br>Adobe Acrobat.
</p>
<button type="button" onclick="myFunction()">Set Paragraph color</button>
</center>
</body>
</html>

Age calculation:
<html>
<head>
<script>
function myFunction() {
var name = document.getElementById("string").value;
const yearob=parseInt(document.getElementById("date").value);
const cyear=new Date().getFullYear();
const age=cyear-yearob;
document.getElementById("age").innerHTML="hi "+ name+ " your age is "+age;
}
</script>
<style>
h2 {
font-size : 30px;
color : green;
font-weight : bold;
text-decoration : underline;
}
</style>
</head>
<body>
<center>
<h2>Calculate the age from date of birth</h2>
<br>
<br>
<label>Enter First name :
<input type="text" id="string" ></label><br><br>
<label>Enter Year of Birth :
<input type="date" id="date" ></label><br><br>
<button type="button" onclick="myFunction()">Calculate Age</button>
<h1 id="age" style="color:green;">
</center>
</body>
</html>
</html>










Random colour:
<html>
<head>
<title>Change Background Color</title>
</head>
<body><center>
<h1>Click the button to change the background color!</h1>
<button id="colorButton">Change Color</button>
</center>
  <script>
    document.getElementById("colorButton").addEventListener("click", function() {
      document.body.style.backgroundColor = getRandomColor();
    });
    function getRandomColor() {
      const letters = "0123456789ABCDEF";
      let color = "#";
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
  </script>
</body>
</html>
Adding 2 numbers:
<html>
<head>
<style>
p {
font-size : 30px;
color : green;
font-weight : bold;
text-decoration : underline;
}
</style>
<script>
function add()
{
  var numOne, numTwo, sum;
  numOne = document.getElementById("first").value;
  numTwo = document.getElementById("second").value;
  sum = parseInt(numOne) + parseInt(numTwo);
  document.getElementById("answer").value = sum;
}
</script>
</head>
<body>
<center>
<br><br>
<p>Enter the First Number: <input id="first"></p>
<p>Enter the Second Number: <input id="second"></p>
<button onclick="add()">Add</button>
<p> <input id="answer"></p>
</center>
</body>
</html>

Frame:
<!DOCTYPE html> 
<html lang="en"> 
  <head> 
    <meta charset="UTF-8" /> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
    <title>Frame</title> 
  </head> 
  <body> 
    <iframe src="" width="1500" height="80" 
frameborder="1"> 
      Physics.html 
    </iframe> 
    <iframe src="" width="1500" height="160" 
frameborder="1"> 
      not supported 
    </iframe> 
    <iframe src="" style="width:32%;" height="150" 
frameborder="1"> 
      not supported 
    </iframe> 
    <iframe src="" style="width:32%;" height="150" 
frameborder="1">
 not supported  
    </iframe> 
    <iframe src="" style="width:32%;" height="150" 
frameborder="1"> 
      not supported 
    </iframe> 
  </body> 
</html>

 
Calender:
<html> 
<head> 
  <title>Yearly Calendar</title> 
  <style> 
    table { 
      border-collapse: collapse; 
      width: 70%; 
      margin: 0 auto; 
    } 
    th, td { 
      border: 1px solid #000; 
      padding: 5px; 
      text-align: center; 
    } 
  </style> 
</head> 
<body> 
  <h1>Yearly Calendar</h1> 
  <label for="yearInput">Enter a year:</label> 
  <input type="text" id="yearInput"> 
  <button id="generateCalendar">Generate Calendar</button> 
  <div id="calendar"></div> 
  <script> 
    const generateCalendar = () => { 
      const year = parseInt(document.getElementById("yearInput").value); 
      const calendar = document.getElementById("calendar"); 
      calendar.innerHTML = ""; 
      for (let month = 1; month <= 12; month++) { 
        const monthName = new Date(year, month - 1, 1).toLocaleString("default", { 
month: "long" }); 
        const daysInMonth = new Date(year, month, 0).getDate(); 
        const table = document.createElement("table"); 
        const caption = table.createCaption(); 
        caption.innerHTML = monthName + " " + year; 
        const headerRow = table.insertRow(); 
        const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]; 
        for (const day of daysOfWeek) { 
          const th = document.createElement("th"); 
          th.textContent = day; 
          headerRow.appendChild(th); 
        }
let date = new Date(year, month - 1, 1); 
        let row = table.insertRow(); 
        let dayOfWeek = date.getDay(); 
        for (let i = 0; i < dayOfWeek; i++) { 
          row.insertCell(); 
        } 
        for (let day = 1; day <= daysInMonth; day++) { 
          if (dayOfWeek === 7) { 
            row = table.insertRow(); 
            dayOfWeek = 0; 
          } 
          const cell = row.insertCell(); 
          cell.textContent = day; 
          dayOfWeek++; 
        } 
        calendar.appendChild(table); 
      } 
    }; 
    document.getElementById("generateCalendar").addEventListener("click", 
generateCalendar); 
  </script> 
</body> 
</html>
 
quiz
<html>
<head>
<script type="text/javascript"> 
var i=0;
function exam()
{
if(document.f1.n1[1].checked) i=i+1; if(document.f1.n2[0].checked) i=i+1; if(document.f1.n3[0].checked) i=i+1; if(document.f1.n4[1].checked) i=i+1;
alert("your score is"+i+"/4");
}
</script>
</head>
<body>
<h2>Online Exam</h2>
<form name="f1">
<h3>spelling of 2</h3>
<input type="radio" id="2" name="n1" value="tow">tow
<input type="radio" id="2" name="n1" value="two">two
<h3>which is odd number</h3>
<input type="radio" id="1" name="n2" value="1">1
<input type="radio" id="1" name="n2" value="2">2
<h3>captain of mens indian cricket team</h3>
<input type="radio" id="1" name="n3" value="Rohit sharma">Rohit sharma
<input type="radio" id="1" name="n3" value="virat kohli">virat kohli
<h3>first cricketer to score 50 ODI centuries</h3>
<input type="radio" id="2" name="n4" value="Sachin Tendulkar">Sachin Tendulkar
<input type="radio" id="2" name="n4" value="virat kohli">virat kohli
<br>
<br>
<input type="submit" value="Submit" onclick="exam()">
</form>
</body>
</html>


