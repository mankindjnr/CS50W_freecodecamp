# JAVASCRIPT
## ================================================================================
Javascript is written inside the script tags.
```javascript
<script>
    // Javascript code goes here
</script>
```

Javascript is especially good in event driven programming. For example, when a button is clicked, a function is called. The function can be defined in the script tag or in a separate file.

```javascript
<script>
    function myFunction() {
        // code to be executed
    }
</script>
```
### --------------------------------------------------------------------------------
### Functions
Functions are defined using the function keyword. The function can be called by using the function name followed by parenthesis. The function can also be called by using the function name followed by parenthesis and a semicolon.

```javascript
    <script>

        function hello(){
            alert("Hello World");
        }
    </script>
```

The function hello job is to display an alert box with the message "Hello World". 

We can link the functionality of hello to an event like a button click.
Inside the html body we create a button and call the hello function when the button is clicked.

```html
    <button onclick="hello()">Click Me</button>
```
### description
The onclick attribute can be used to call a function when a button is clicked.

## ================================================================================
### Variables
#### counter.html
```javascript
    <script>
        let counter = 0;
        function count(){
            counter++;
            alert(counter);
        }
    </script>
```
```html
    <button onclick="count()">Count</button>
```
### description
The let keyword is used to declare a variable. The variable counter is initialized to 0. The function count increments the counter by 1 and displays the counter value in an alert box.

### --------------------------------------------------------------------------------
This is fine, but we do not want to keep interacting with the user trough dialog boxes. We want to change the content of the page. We can do this by manipulating the DOM, all the elements in that webpage.

## ================================================================================
### DOM
In hello.html we have a function hello that when clicked, displays on a dialog box the string, hello world. In our body we have a h1 tag and a button:
    
    ```html
        <h1>Hello World</h1>
        <button onclick="hello()">Click Me</button>
    ```
The function hello is defined in the script tag and it displays hello world. But we want to instead change the content of the h1 tag. We can do this by using the DOM.

```javascript
    <script>
        function hello(){
            document.querySelector("h1").innerHTML = "mankindjnr";
        }
    </script>
```
```html
    <h1>Hello World</h1>
    <button onclick="hello()">Click Me</button>
```
### description
- The document object represents the html document.
- The querySelector method returns the first element that matches a specified element in the document.
** when the document.queryselector is called, it returns the first h1 tag it finds and now we can manipulate it.**
- The innerHTML property sets or returns the HTML content of the h1 tag(in this case __Hello World__). and now we will update it to __mankindjnr__. The value assigned to the innerHTML property replaces the content of the h1 tag.

Now onlick, the content of the h1 tag on the webpage is changed to __mankindjnr__.

### --------------------------------------------------------------------------------
### Toggle
Above we have the ability to only switch from _hello_ to _mankindjnr_ but we may want to toggle back and forth. To achieve this, we use conditions.

```javascript
    <script>
        function hello(){
            if(document.querySelector("h1").innerHTML === "Hello World"){
                document.querySelector("h1").innerHTML = "mankindjnr";
            }else{
                document.querySelector("h1").innerHTML = "Hello World";
            }
        }
    </script>
```
```html
    <h1>Hello World</h1>
    <button onclick="hello()">Click Me</button>
```
### description
the if condition are checking if the content of the h1 tag is _Hello World_ and if it is, it changes it to _mankindjnr_ and if it is not, it changes it to _Hello World_.
**The === is used to check if the content of the h1 tag is exactly _Hello World_**

### --------------------------------------------------------------------------------
Our code above has alot of repetition, during any single moment, only tow statements are going to be run. 
We are going to refactor our code to make it more efficient.

```javascript
    <script>
        function hello(){
            const h1 = document.querySelector("h1");
            if(h1.innerHTML === "Hello World"){
                h1.innerHTML = "mankindjnr";
            }else{
                h1.innerHTML = "Hello World";
            }
        }
    </script>
```
```html
    <h1>Hello World</h1>
    <button onclick="hello()">Click Me</button>
```

- we are using const since that will never change and javascript will enforce it.
## ================================================================================
### Function as a value
So far we have called our js function inside the html and this might get dirty especially we have alot of functions and larger code. i.e
    
    ```html
        <button onclick="count()">Count</button>
    ```
We can instead use the addEventListener method to add an event listener to the button. The addEventListener method takes two arguments, the event and the function to be called when the event occurs.
```javascript
document.querySelector("button").onClick = count;
```
```html
    <h1>0</h1>
    <button>Count</button>
```
### description
- The querySelector method returns the first element that matches a specified element in the document.
- The onClick property sets or returns the event handler for the click event.
- The count function increments the counter by 1 and displays the counter value in an alert box.
- **count is a function and we are assigning it to the onClick property.** passing it as a value.

### --------------------------------------------------------------------------------
### update of the above and error fix
```javascript
document.addEventListener("DOMContentLoaded", function(){
            document.querySelector("button").onclick = count;
        });
```
```html
    <h1>0</h1>
    <button>Count</button>
```
### description
- The DOMContentLoaded event fires when the initial HTML document has been completely loaded and parsed, without waiting for stylesheets, images, and subframes to finish loading.
- DOMContentLoaded is a great event to use to hookup UI functionality to complex web pages.

## ================================================================================
### Forms
```javascript
document.addEventListener('DOMContentLoaded', () => {
            document.querySelector('form').onsubmit = () => {
                const name = document.querySelector('#name').value;
                alert(`Hello, ${name}!`);
            };
        });
```
```html
    <form>
        <input type="text" id="name">
        <input type="submit" value="Submit">
    </form>
```
### description
- The querySelector method returns the first element that matches a specified element in the document.
- The onsubmit property sets or returns the event handler for the submit event.
- The .value property sets or returns the value of the value attribute of a text field.
- The alert() method displays an alert box with a specified message and an OK button.
- addEventListener() method attaches an event handler to the specified element.
- DOMContentLoaded tells js to wait until the DOM is fully loaded before running the js code.
- () => {} is an arrow function. It is a shorter way of writing a function. It is also called a lambda function.(anonymous function)
- #name is the id of the input field.

#### queryselector

**.class** is used to select elements with a specific class name.
**#id** is used to select an element with a specific id.
**'tag'** is used to select elements with a specific tag name.

## ================================================================================
## MANIPULATING CSS
```javascript
document.addEventListener("DOMContentLoaded", function() {

            // change color to red
            document.querySelector("#red").onclick = function() {
                document.querySelector("#hello").style.color = "red";
            };
```

### data attributes
They start with __data-__ followed by a name. They are used to store custom data private to the page or application.
Below, we want to store data about the __-color__ of the button. This way, we can access those attibutes in our js code.
```html
<h1 id="hello">Kikie!</h1>
    <button data-color="red">Red</button>
    <button data-color="green">Green</button>
    <button data-color="blue">Blue</button>
```

```javascript
document.querySelector
```
only returns a single element. If we want to return all the elements, we use __querySelectorAll__.
They return similar elements only that ALL returns an array of allllll the elements.

```javascript
document.addEventListener("DOMContentLoaded", function() {

            // change color to red
            document.querySelectorAll("button").forEach(function(button) {
                button.onclick = function() {
                    document.querySelector("#hello").style.color = button.dataset.color;
                };
            });
        });
```
### description
- document.querySelectorAll("button") - returns all the buttons in the document.
- forEach() method calls a function once for each element in the array returned above, in order.(in this case, the buttons) - _for each of the buttons, do something_
- button.onclick = function() - when a button is clicked, the function is called.
- the function that will be called will be affect the color of the element with the id hello.
- button.dataset.color - returns the value of the data-color attribute of the button.
### --------------------------------------------------------------------------------
### using a dropdown
```html
<h1 id="hello">Kikie!</h1>
    <select>
        <option value="black">Change Color</option>
        <option value="red">Red</option>
        <option value="green">Green</option>
        <option value="blue">Blue</option>
    </select>
```
```javascript
document.addEventListener("DOMContentLoaded", () => {
            document.querySelector("select").onchange = function() {
                document.querySelector("#hello").style.color = this.value;
            }
        });
```
### description
- document.querySelectorAll("select") - returns all the select elements in the document.
- onchange - when the value of the select element changes, the function is called.
- this.value - returns the value of the current select element.
- document.querySelectorAll("#hello").style.color - changes the color of the element with the id hello. - __where the changes will be reflected__

### --------------------------------------------------------------------------------
### other events include
- onmouseover - when the mouse pointer moves over an element.
- onmouseout - when the mouse pointer moves out of an element.
- onkeydown - when a user is pressing a key (keyboard event).
- onkeyup - when a user releases a key.
- onfocus - when an element gets focus.
- onblur - when an element loses focus.
- onloaded - when a page has finished loading.
- onload - when a page has finished loading.

## ================================================================================
## TASKS.HTML
```javascript
// when the DOM/webpage is fully loaded
         document.addEventListener("DOMContentLoaded", function() {
            //by default, submit button is disabled since its empty
            document.querySelector('#submit').disabled = true;
            document.querySelector('#task').onkeyup = () => {
                if (document.querySelector('#task').value.length > 0)
                    document.querySelector('#submit').disabled = false;
                else
                    document.querySelector('#submit').disabled = true;
            }

            document.querySelector('form').onsubmit = () => {
                const task = document.querySelector('#task').value;

                // clearing the input field in form after submitting
                document.querySelector('#task').value = '';

                // create new item for list
                const li = document.createElement('li');
                li.innerHTML = task;

                // add new item to task list using its id
                document.querySelector('#tasks').append(li);

                // disable submit button again after submitting
                document.querySelector('#submit').disabled = true;

                // prevent form from submitting
                return false;
            }
        });
```
```html
    <h1>Tasks</h1>
    <ul id="tasks">
    </ul>
    <form>
        <input type="text" id="task">
        <input type="submit" id="submit" value="Add">
    </form>
```
## ================================================================================
### INTERVALS
```javascript
let counter = 0;
        function count(){
            counter++;
            document.querySelector('h1').innerHTML = counter;
        }

        document.addEventListener("DOMContentLoaded", function(){
            document.querySelector("button").onclick = count;

            setInterval(count, 1000)
});
```
```html
    <h1>0</h1>
    <button>Count</button>
```
### description
- setInterval() method calls a function or evaluates an expression at specified intervals (in milliseconds).
- setInterval() method will continue calling the function until clearInterval() is called, or the window is closed.

But this state is not stored, so every time the page is loaded, it starts from zero. At times you want to store the state of the page. This is where local storage comes in.

## ================================================================================
### LOCAL STORAGE
Storing values inside the web browser.
Later when you visit the website, you can retrieve the state.

```javascript
localStorage.setItem('counter', counter);
localStorage.getItem('counter');
```

```javascript
if (!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0)
}
        function count(){
            let counter = localStorage.getItem('counter');
            counter++;
            document.querySelector('h1').innerHTML = counter;
            localStorage.setItem('counter', counter);
        }

        document.addEventListener("DOMContentLoaded", function(){
            document.querySelector('h1').innerHTML = localStorage.getItem('counter');
            document.querySelector("button").onclick = count;

            setInterval(count, 1000)
});
```
### description
- localStorage.setItem('counter', counter) - stores the value of counter in the browser.
- localStorage.getItem('counter') - retrieves the value of counter from the browser.
- if (!localStorage.getItem('counter')) - if the counter is not set, set it to 0.
- localStorage.setItem('counter', counter) - stores the value of counter in the browser.
- **document.querySelector('h1').innerHTML = localStorage.getItem('counter');** - this will ensure that even after our page refreshes, the value of the counter will be displayed as the last value it was before the page was refreshed.

## ================================================================================
## javascript object - import data type in js
its made of key value pairs.
```javascript
let person = {
    name: 'mankindjnr',
    age: 20,
    city: 'Nairobi'
};
```
#### this js object is very useful when it comes to exchange of data.(API's)

## ================================================================================
## JSON and API's and ## AJAX
Asynchronous JavaScript and XML.
- AJAX is a technique for accessing web servers from a web page.


We have been working with data that we provide ourselves, but what if we want to get data from somewhere else. We can use an API.

in a script tag we are going to interact with an API.
```javascript
document.addEventListener('DOMContentLoaded',()=>{

            fetch('https://api.exchangeratesapi.io/latest?base=USD')
            .then(response => response.json())
            .then(data => {
                const rate = data.rates.INR;
                document.querySelector('body').innerHTML = rate;
            });
        });
```
### description
Using fetch, we are querying the API and getting the data from the API. The data is returned in JSON format.
- **fetch** returns a promise.
- A promise is a commitment that a value will be available in the future.
- When the promise is fulfilled **then** you can do something with the value., in this case, we take the response from fetch and convert it to json.
- **response.json()** is a simplified version of **.then(response => return {response.json() })**
- **.then(data => {console.log(data.rates.CAD);})** - we are taking the data and logging it to the console. The data is an object and we are accessing the rates property and the CAD property of the data object.
- **.then(data => {const rate = data.rates.INR;})** - we are taking the data and storing it in a variable called rate. The data is an object and we are accessing the rates property and the INR property of the data object.
- **document.querySelector('body').innerHTML = rate;** - we are taking the rate and displaying it on the webpage inside the body element.

THIS IS DONE IN ASYNCHRONOUS WAY. i.e the webpage is not going to wait for the data to be fetched before it is displayed. It will display the webpage and then fetch the data.

### --------------------------------------------------------------------------------
```javascript
document.addEventListener('DOMContentLoaded',()=>{
        // only access the api when the form is submitted
            document.querySelector('form').onsubmit = () => {

            fetch('https://api.exchangeratesapi.io/latest?base=USD')
            .then(response => response.json())
            .then(data => {
                const currency = document.querySelector('#currency').value.toUpperCase(); //value of the input field
                const rate = data.rates[currency];

                if (rate !== undefined){
                    document.querySelector('#result').innerHTML = rate;
                }else{
                    document.querySelector('#result').innerHTML = 'Invalid currency';
                }
            });

            // prevent form from submitting and run everything on current webpage
            return false;
            }

        })
        .catch(error => {
            console.log('Error:', error);
        });
```

```html
<form>
    <input type="text" id="currency">
    <input type="submit" value="Convert">
</form>

<div id="result">

</div>
```

### description
the above code will now run on the data user enters in the form and the results will be displayed inside the div.

- .catch will catch the error if there is any, if the api is not available or if the user enters an invalid currency.
## ================================================================================

.