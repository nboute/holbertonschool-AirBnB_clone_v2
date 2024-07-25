# AirBnB Clone - Web Frameworks

This project is part of the AirBnB clone series, aimed at building a web application similar to the AirBnB platform. In this phase, the focus is on developing the backend logic using Flask, a Python web framework, to manage data and serve HTML content. The tasks involve creating a web server, rendering HTML pages dynamically, and handling data persistence with a storage engine (either FileStorage or DBStorage).

All instructions mentionned here refer to the Holberton School project's tasks. They are already implemented in the project.
## Project Overview

The project involves building a web application using Flask that integrates with a database to fetch and display data about States, Cities, and Amenities. The application is designed to serve dynamic content, where various URLs are mapped to specific functions that process the data and render HTML pages. The project also emphasizes understanding routing, templates, and working with relational databases using SQLAlchemy in a Python environment.

![Project graph](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step3.png)
## Task Summaries

### 0. Hello Flask!

**Task:** Write a script that starts a Flask web application.

- The web application must listen on `0.0.0.0`, port `5000`.
- Route `/` should display “Hello HBNB!”.
- Use the option `strict_slashes=False` in your route definition.

**Summary:** This task sets up the basic Flask application with a single route that returns a simple text response.

### 1. HBNB

**Task:** Add a new route to the Flask application.

- Route `/hbnb` should display “HBNB”.
- Maintain the existing requirements from Task 0.

**Summary:** Extend the Flask application with an additional route that returns a specific message when accessed.

### 2. C is fun!

**Task:** Add a dynamic route to the Flask application.

- Route `/c/<text>` should display “C ” followed by the value of the `text` variable.
- Replace underscore `_` symbols in `<text>` with spaces.

**Summary:** Implement a dynamic route that accepts a variable, processes it, and displays it in a formatted string.

### 3. Python is cool!

**Task:** Add another dynamic route with a default value.

- Route `/python/(<text>)` should display “Python ” followed by the `text` variable.
- Replace underscore `_` symbols with spaces.
- The default value of `text` is “is cool”.

**Summary:** Add a new route similar to Task 2 but with a default value, demonstrating optional parameters in URLs.

### 4. Is it a number?

**Task:** Create a route that handles numeric variables.

- Route `/number/<n>` should display “n is a number” only if `n` is an integer.

**Summary:** Introduce integer-specific routing to verify and respond to integer inputs in the URL.

### 5. Number template

**Task:** Add a route that renders an HTML template.

- Route `/number_template/<n>` should display an HTML page only if `n` is an integer.
- The page should include an H1 tag: “Number: n”.

**Summary:** Implement a route that uses Jinja2 templates to render HTML content dynamically based on URL parameters.

### 6. Odd or even?

**Task:** Extend the number route to specify odd or even numbers.

- Route `/number_odd_or_even/<n>` should display an HTML page only if `n` is an integer.
- The page should include an H1 tag: “Number: n is even|odd”.

**Summary:** Add logic to determine if the given number is odd or even and display the result in the HTML content.

### 7. Improve engines

**Task:** Update the storage engine classes.

- Update `FileStorage` with a `close()` method to call `reload()`.
- Update `DBStorage` with a `close()` method to close the SQLAlchemy session.
- Update `State` to include a getter method `cities` for related City objects.

**Summary:** Enhance the storage engine with additional methods for better session management and data retrieval from the database.

### 8. List of states

**Task:** Create a Flask route to display all States.

- Route `/states_list` should display an HTML page with a list of all State objects.
- The list should be sorted by name (A->Z).
- Implement a method to remove the current SQLAlchemy session after each request.

**Summary:** Develop a route that queries the database for all States and renders them in a sorted list on an HTML page.

### 9. Cities by states

**Task:** Create a route to display Cities within each State.

- Route `/cities_by_states` should display an HTML page with States and their related Cities.
- The list of States and Cities should be sorted by name (A->Z).

**Summary:** Implement nested data retrieval and display, showing the relationship between States and their Cities.

### 10. States and State

**Task:** Add routes to display details for specific States.

- Route `/states` should display all State objects.
- Route `/states/<id>` should display Cities linked to a specific State.
- If a State object is not found, display “Not found!”.

**Summary:** Develop functionality to view all States and drill down into specific States to see their associated Cities.

### 11. HBNB filters

**Task:** Create a dynamic filter page.

- Route `/hbnb_filters` should display a page with filters for States, Cities, and Amenities.
- Load data from `DBStorage` and sort it by name (A->Z).

**Summary:** Implement filtering functionality to dynamically show data based on selected criteria.

### 12. HBNB is alive!

**Task:** Finalize the Flask application with complete functionality.

- Route `/hbnb` should display a page similar to the static website done previously.
- Copy and update static files as needed.
- Ensure all HTML tags from objects are correctly used.
- Load State, City, Amenity, and Place objects from `DBStorage`.

**Summary:** Integrate all components to create a fully functional web application that simulates the AirBnB platform with dynamic data loading and display.

