# Elgini's Restaurant
(Developer: Daniel Richards)

![Mockup of Elgini's Restaurant](readme/mockup.png)

[View live site](https://elginis-restaurant.herokuapp.com/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Strategy](#strategy)
        + [Primary Goal](#primary-goal)
    2. [Structure](#structure)
        + [Website pages](#website-pages)
        + [Code Structure](#code-structure)
        + [Database](#database)
        - [Physical database model](#physical-database-model)
        - [Models](#models)
            * [User Model](#user-model)
            * [Meal Model](#meal-model)
            * [Category Model](#category-model)
            * [Allergen Model](#allergen-model)
            * [Drink Model](#drink-model)
            * [DrinkCategory Model](#drinkcategory-model)
            * [Comment Model](#comment-model)
            * [Booking Model](#booking-model)
            * [Contact Model](#contact-model)
            * [Reason Model](#reason-model)
            * [About Model](#about-model)
            * [Chef Model](#chef-model)
            * [Reasons Model](#reasons-model)
            * [Home Model](#home-model)
    <!-- 1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations) -->
    3. [Scope](#scope)
        +[User Stories](#user-stories)
    4. [Skeleton](#design)
        1. [Wireframes](#wireframes)
    5. [Surface](#surface)
        1. [Design Choices](#design-choices)
        2. [Colour](#colours)
        3. [Fonts](#fonts)


5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
6. [Features](#features)
7. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [JS Validation](#JS-validation)
    4. [Python Validation](#py-validation)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    7. [Device testing](#performing-tests-on-various-devices)
    8. [Browser compatibility](#browser-compatibility)
    9. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

# User Experience
## Strategy
### Primary Goal
The primary goal of the website from the site 
owners perspective is as follows:
- To attract customers to the business by showing an attractive and appealing variety of food.
- To allow a user to navigate the website and see food options easily
- To allow a user to make a reservation

The primary goal of the website from a site users perspective is as follows:
- To view the restaurants menu
- To view details about food dishes, including allergens, description and prices
- To be able to filter dishes by allergies
- To make a reservation
- To contact the restaurant
- To view opening hours
- To post a review or comment about their experience
- To view other customer’s reviews and comments

## Structure
### Code Structure
The project is organised into a variety of applications, as is constructed using the Django Framework.

App details as follows:
- Home - this app contains information about the restaurant home page with quick links to the menus on page and table booking via the nav bar.
- Meals - this app contains the menu structure, users can choose between the lunch drink and dinner menu.  Clicking individual items opens a sub  page where users can see detailed food information including allergens and calories.
- About - this app contains information relating to the business heritage the opportunity for users to view, add, edit, delete comments with authentication.
- Contact - this app is for users to be able to submit a message to the site owners and recieve acknowledgment.
- Booking - this app is for users to be able to submit a booking reqeuest with date validation so cannot be booked in past and also only within restaurant opening hours.

To complement the apps there are
- project: Project level files - settings.py for project level settings and urls.py to route the website URLS
- templates: Containing the base.html, allauth(django authentication)
- templates (app level): each app has it's own templates directory for HTML to consider portability and re-use.
- urls (app level): each app has it's own url.py file to consider portability and re-use.
- static: Base css and Javascript files
- manage.py: This file is used to start the site and perform funcions during development
- README.md: Readme documentation
- Procfile: To run the application on Heroku
- Requirements.txt: Containing the project dependencies
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings


Physical database model

This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database 
<br>![Database model](readme/misc/database_schema.png)

#### Models
- The following models were created to represent the database model structure for the website

##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined

##### Meal Model
- The Meal model contains information about meals available within each of the menus
- It contains Category as a foreign-key.
- It contains Allergen as a Many-toMany relationship.
- The model contains the following fields:  Name, Category, Description, Allergen, Lunch, Dinner, Calories, Price, Vegetarian, Vegan, Image, Slug.

##### Category Model
- The category model contains the available categories for a meal item
- The model contains the following fields: name

##### Allergen Model
- The Allergen model contains allergens that may be contained in the meals, this has a many to many relationship with meals model.
- It contains images so to be easily understood to non english speakers.
- The model contains the following fields: name, image.

##### Drink Model
- The Drink model contains a the drinks available at the restaurant
- It has DrinkCategory as a foreign-key.
- The model contains the following fields: name, description, category, image.

##### DrinkCategory Model
- The News model contains viable categories for the drinks.
- It acts as a foreign-key for Drinks model
- The model contains the following fields: name

##### Comment Model
- The News model contains a comment that renders on the about page.
- The model contains the following fields: user, comment_text, created_date

##### Booking Model
- The Booking model contains a collection of data submitted by the user when requesting a reservation.
- The model contains the following fields: name, email, phone, party_size, date, ,time

##### Contact Model
- The Contact model contains a collection of data submitted by the user when messaging the site owner.
- It contains Reasons as a foreign-key.
- The model contains the following fields: reason, email, phone, postcode, street_address, message.

#### Reason Model
- The Contact model contains a collection pre configured headers that the user can use to send the message.
- It acts as a foreign-key for Contact model.
- The model contains the following fields: reason

#### About Model
- The About model contains a collection of data and image to show the restaurant heritage..
- The model contains the following fields: title, body, image.

#### Reasons Model
- The Reasons model contains a collection reasons as to why the user should use the establishment.
- The model contains the following fields: reason, body.

#### Chefs Model
- The Chefs model contains the chef images, names and biography.
- The model contains the following fields: name, image, bio.

#### Home Model
- The Home model contains the items for the carousel on the home page.
- The model contains the following fields: Title, body, image.

## Scope
### User stories:

#### First time user
1.	As a first time user, I want to be able to view the type of food the restaurant provides
2.	As a first time user, I want to see professional and appealing images of the food
3.	As a first time user, I want to be able to navigate the website quickly and easily
4.	As a first time user, I want to be able to view the full menu
5.	As a first time user, I want to be able to view food allergies and calories
6.	As a first time user, I want to be able to view a description and price of the food
7.	As a first time user, I want to be able to leave a comment or review
8.	As a first time user, I want to be able to see other user’s comments and reviews
9.	As a first time user, I want to be able to edit and delete a comment I have made
10.	As a first time user, I want to be able contact the restaurant
11.	As a first time user, I want to be able to make a reservation
12.	As a first time user, I want to be able to view the restaurants location and opening hours
13.	As a first time user, I want to know about the business and it’s ethos
14.	As a first time user, I want to be able to see special offers and promotions.
15. As a first time user, I want to be able to to sign in to, or create an account
16. As a first time user, I want to be able to log out of an account
17. As a first time user, I want to be able to see separate menus for lunch, dinner and drinks
18. As a first time user, I want to be able to view the business’ social media

# Site Owner
19.	As a site owner, I want to attract customers to our restaurant
20.	As a site owner, I show appealing and professional images of our food
21.	As a site owner, I want users to be to view our full menu
22.	As a site owner, I want users to be able to view the food descriptions and prices
23.	As a site owner, I want users to be able to view allergies and calories
24.	As a site owner, I want users to be able to make a reservation
25.	As a site owner, I want users to be able to leave a comment or review
26.	As a site owner, I want users to be able to view other comments and reviews
27.	As a site owner, I want users to be able to edit and delete comments or reviews
28.	As a site owner, I want users to be able to contact the business
29.	As a site owner, I want users to be able to view the location and opening times
30.	As a site owner, I want users to be able to find out about our business ethos
31.	As a site owner, I want users to be able to have an idea of the restaurant’s welcoming atmosphere so they will make a reservation
32.	As a site owner, I want users to be able to navigate the site easily and quickly
33. As a site owner, I want to be able to promote special offers and events.
34. As a site owner, I want users to be able to sign in to, or create an account
35. As a site owner, I want users to be able to log out of their account
36. As a site owner, I want users to be able to see separate menus for lunch, dinner and drinks
37. As a site owner, I want users to be able to review and approve user comments
38. As a site owner, I want users to be able to view the business’ social media

## Surface
### Design choices

The overall design of the website was to keep it clean and simple, to allow the imagery of the food to shine through, and to choose colours that didn’t distract or take focus. The website also needs to act as a portfolio to attract users to book and visit the restaurant, so we chose a gallery image layout for the menu, and made sure to include photography of the staff and restaurant interior.

The site is straightforward to navigate, with a high contrasting navigation bar to enable ease of use for the user to find other main pages.

The background is neutral but bright, the images are the focal point of the home page so the user has an immediate view of the food. The rest of the colour scheme is reflecting the rustic Italian interior of the restaurant.

### Colours

The colour palette is fairly neutral and warm. The bold colours that are used in focal points such as buttons and titles, and the neutrals are used for backgrounds and body text.

- #212529 - Title text
- #4F4F4F - Body text
- #5A753A - Buttons
- #703D30 - Lines and subtitles
- #FBF4E1 - Background
- #FFFFFF  - Logo and header links

After choosing a colour scheme I tested a number of palette options to make sure the it met accessibility standards.

<br>![Database model](readme/misc/accessible-color.jpg)

### Typography
Maria Rose is the font uses for the logo, and is replicated in the main headings of the website. This font is licensed from Creative Market, with a standard license for personal use.

Josefin Sans is the font used across all of the body text, this font is from the Google Fonts Library.

## Features

The site contains 12 pages and
1. Home page
2. Full menu
3. Food description
4. lunch menu
5. dinner menu
6. drinks menu
7. about
8. contact
9. reserve
10. login
11. sign up
12. log out

### Page 1 - Home page
The home page consists of the following features:

Feature 1 - Header and navigation Bar, the header and navigation bar are shown across all pages.
The header shows the logo of the website, as well as a navigation bar with quick access to the main pages of the website. 
<br>![Navbar model](readme/features/navbar.png)

This feature covers the following user stories

*3.	As a first time user, I want to be able to navigate the website quickly and easily*

*10.	As a first time user, I want to be able contact the restaurant*

*11.	As a first time user, I want to be able to make a reservation*

*15. As a first time user, I want to be able to sign in to, or create an account*

*16. As a first time user, I want to be able to log out of an account*

*21.	As a site owner, I want users to be to view our full menu*

*24.	As a site owner, I want users to be able to make a reservation*

*28.	As a site owner, I want users to be able to contact the business*

*32.	As a site owner, I want users to be able to navigate the site easily and quickly*

*34. As a site owner, I want users to be able to sign in to, or create an account*

*35. As a site owner, I want users to be able to log out of their account*


### Feature 2 - Carousel

The carousel consists of 3 hero images, which play automatically upon landing on the page. It can be used by the site owner to promote any special offers and events.
<br>![Navbar model](readme/features/carousel.png)


This feature covers the following user stories

*1.	As a first time user, I want to be able to view the type of food the restaurant provides*
*2.	As a first time user, I want to see professional and appealing images of the food*
*14.	As a first time user, I want to be able to see special offers and promotions.*

*19.	As a site owner, I want to attract customers to our restaurant*
*20.	As a site owner, I show appealing and professional images of our food*
*33.  As a site owner, I want to be able to promote special offers and events.*

### Feature 3 - lunch, dinner and drinks images with buttons

The menu images show an image of the restaurant food with a clear button overlay which takes the user directly to the relevant menu page quickly and easily.
<br>![Navbar model](readme/features/ldd-images.png)


This feature covers the following user stories
*1.	As a first time user, I want to be able to view the type of food the restaurant provides*

*2.	As a first time user, I want to see professional and appealing images of the food*

*3.	As a first time user, I want to be able to navigate the website quickly and easily*

*4.	As a first time user, I want to be able to view the full menu*

*17. As a first time user, I want to be able to see separate menus for lunch, dinner and drinks*

*19.	As a site owner, I want to attract customers to our restaurant*

*20.	As a site owner, I show appealing and professional images of our food*

*21.	As a site owner, I want users to be to view our full menu*

*36. As a site owner, I want users to be able to see separate menus for lunch, dinner and drinks*

### Feature 4 - footer 
The footer features the business’ social media links, as well as links to the main pages the user would want to navigate.
<br>![Navbar model](readme/features/footer.png)

This feature covers the following user stories
*3.	As a first time user, I want to be able to navigate the website quickly and easily*

*18. As a first time user, I want to be able to view the business’ social media*

*32.	As a site owner, I want users to be able to navigate the site easily and quickly*

*38. As a site owner, I want users to be able to view the business’ social media*

### Page 2 - Full Menu
The full menu page has an internal navigation bar to guide the user through the menu sections. It also shows the restaurant’s full list of food dishes with images, descriptions, prices and dietary requirements. The images are professional quality and are shown in a clear grid layout, separated with header images.

It consists of the following features:

#### Feature 1 - internal navigation bar
The internal navigation bar helps the user to browse the menu without scrolling through the whole page.
<br>![Navbar model](readme/features/food-nav.png)

This feature covers the following user stories

*1.	As a first time user, I want to be able to view the type of food the restaurant provides*

*3.	As a first time user, I want to be able to navigate the website quickly and easily*

*6.	As a first time user, I want to be able to view a description and price of the food*

*20.	As a site owner, I show appealing and professional images of our food*

*22.	As a site owner, I want users to be able to view the food descriptions and prices*

*32.	As a site owner, I want users to be able to navigate the site easily and quickly*


#### Feature 2 - Full menu image gallery
The full menu image gallery shows a professional image of each individual dish, with the dish name and brief description, as well as the price and dietary requirements.
When the user selects on the image a new page opens for the item, which includes additional information including the allergy and nutritional values.
<br>![Navbar model](readme/features/full-menu.png)

This feature covers the following user stories
*1.	As a first time user, I want to be able to view the type of food the restaurant provides*

*2.	As a first time user, I want to see professional and appealing images of the food*

*4.	As a first time user, I want to be able to view the full menu*

*6.	As a first time user, I want to be able to view a description and price of the food*

*19.	As a site owner, I want to attract customers to our restaurant*

*20.	As a site owner, I show appealing and professional images of our food*

*21.	As a site owner, I want users to be to view our full menu*

*22.	As a site owner, I want users to be able to view the food descriptions and prices*

### Page 3 - Food description
The food description page is shown when a user clicks on the image of an individual item. The page enables users to find out a more detailed description of the item including the allergies and calorie content.
It consists of the following features:
<br>![Navbar model](readme/features/food-description.png)

Feature 1 - the additional nutritional information
The additional nutritional information includes: 
- Known allergies of the item, shown in text and a clear illustrated symbol.
- Calorie content

This feature covers the following user stories

*2.	As a first time user, I want to see professional and appealing images of the food*

*5.	As a first time user, I want to be able to view food allergies and calories*

*6.	As a first time user, I want to be able to view a description and price of the food*

*19.	As a site owner, I want to attract customers to our restaurant*

*20.	As a site owner, I show appealing and professional images of our food*

*22.	As a site owner, I want users to be able to view the food descriptions and prices*

*23.	As a site owner, I want users to be able to view allergies and calories*

### Page 4 - Lunch Menu
The lunch menu page shows items on the lunch menu only. It has an internal navigation bar to guide the user through the menu sections. It also shows the item’s image, descriptions, price and dietary requirements. The images are professional quality and are shown in a clear grid layout, separated with header images.
It consists of the following features:
#### Feature 1 - internal navigation bar
The internal navigation bar helps the user to browse the menu without scrolling through the whole page.
<br>![Navbar model](readme/features/lunch-nav.png)


This feature covers the following user stories
*1.	As a first time user, I want to be able to view the type of food the restaurant provides*

*3.	As a first time user, I want to be able to navigate the website quickly and easily*

*6.	As a first time user, I want to be able to view a description and price of the food*

*22. As a site owner, I want users to be able to view the food descriptions and prices*

*32. As a site owner, I want users to be able to navigate the site easily and quickly*

#### Feature 2 - Lunch menu image gallery
The full menu image gallery shows a professional image of each individual dish, with the dish name and brief description, as well as the price and dietary requirements.
When the user selects on the image a new page opens for the item, which includes additional information including the allergy and nutritional values.
<br>![Navbar model](readme/features/lunch-menu.png)

This feature covers the following user stories
*1.	As a first time user, I want to be able to view the type of food the restaurant provides*
*2.	As a first time user, I want to see professional and appealing images of the food*
*4.	As a first time user, I want to be able to view the full menu*
*6.	As a first time user, I want to be able to view a description and price of the food*
*17. As a first time user, I want to be able to see separate menus for lunch, dinner and drinks*

*19.	As a site owner, I want to attract customers to our restaurant*
*20.	As a site owner, I show appealing and professional images of our food*
*21.	As a site owner, I want users to be to view our full menu*
*22.	As a site owner, I want users to be able to view the food descriptions and prices*
*36. As a site owner, I want users to be able to see separate menus for lunch, dinner and drinks*

### Page 5 - Dinner Menu
The dinner menu page shows items on the lunch menu only. It has an internal navigation bar to guide the user through the menu sections. It also shows the item’s image, descriptions, price and dietary requirements. The images are professional quality and are shown in a clear grid layout, separated with header images.
It consists of the following features:

#### Feature 1 - internal navigation bar
The internal navigation bar helps the user to browse the menu without scrolling through the whole page.
<br>![Navbar model](readme/features/dinner-nav.png)

This feature covers the following user stories

*1.	As a first time user, I want to be able to view the type of food the restaurant provides*

*3.	As a first time user, I want to be able to navigate the website quickly and easily*

*6.	As a first time user, I want to be able to view a description and price of the food*

*20.	As a site owner, I show appealing and professional images of our food*

*22.	As a site owner, I want users to be able to view the food descriptions and prices*

*32.	As a site owner, I want users to be able to navigate the site easily and quickly*
￼
#### Feature 2 - Dinner image gallery
The full menu image gallery shows a professional image of each individual dish, with the dish name and brief description, as well as the price and dietary requirements.
When the user selects on the image a new page opens for the item, which includes additional information including the allergy and nutritional values.
<br>![Navbar model](readme/features/dinner-menu.png)

This feature covers the following user stories

*1.	As a first time user, I want to be able to view the type of food the restaurant provides*

*2.	As a first time user, I want to see professional and appealing images of the food*

*4.	As a first time user, I want to be able to view the full menu*

*6.	As a first time user, I want to be able to view a description and price of the food*

*17. As a first time user, I want to be able to see separate menus for lunch, dinner and drinks*

*19.	As a site owner, I want to attract customers to our restaurant*

*20.	As a site owner, I show appealing and professional images of our food*

*21.	As a site owner, I want users to be to view our full menu*

*22.	As a site owner, I want users to be able to view the food descriptions and prices*

*36. As a site owner, I want users to be able to see separate menus for lunch, dinner and drinks*



## Technologies Used

### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JS ES6](https://en.wikipedia.org/wiki/JavaScript)
- [Django](https://www.djangoproject.com/)
- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
#### Python Libraries

- astroid==2.8.4 - for pylinting
- cloudinary==1.29.0 - for media and static file remote storage and serving
- crispy-bootstrap5==0.6 - for form styling
- dj-database-url==0.5.0 - (Support for DATABASE_URL environment variable)
- dj3-cloudinary-storage==0.0.6 - for media and static file remote storage and serving
- django-allauth==0.49.0 - (Web framework authentication)
- django-crispy-forms==1.14.0 - for form rendering and handling
- flake8==4.0.1 - for linting
- gunicorn==20.1.0 - (Python WSGI Http server)
- Pillow==9.0.1 - (Imaging library)
- postgres==4.0 - (Postgres adapter)
- psycopg2==2.9.3 (Postgres adapter)
- psycopg2-binary==2.9.3 (Postgres adapter)
- psycopg2-pool==1.1 (Postgres adapter)
- python3-openid==3.2.0 (Support for the OpenID decentralized identity system)

### Frameworks & Tools
- [Bootstrap 5.0](https://getbootstrap.com/docs/5.0) - for general site layout, grid, flex, carousel.
- [Postgres](https://www.postgresql.org/) - the site is deployed on Heroku using a Postgress database.
- [SQLLite](https://www.sqlite.org/index.html) - this database was used in local development.
- [VSCode](https://code.visualstudio.com/) - my IDE of choice for this project.
- [Gitpod](https://gitpod.io/) - used occasionally for tutor support.
- [Github](https://github.com/) - used as the code repository.
- [Google Fonts](https://fonts.google.com/) - used for the main body font and some headings.
- [Balsamiq](https://balsamiq.com/) -  used to create the website wireframes.
- [Font Awesome](https://fontawesome.com/) - Font awesome was used to provide the relevant fonts/icons for the website social media icon links.
- [JQuery](https://jquery.com) - JQuery was used in some javascript files for DOM manipulation
<!-- - TinyPNG (https://tinypng.com/)
    - TinyPNG was used to compress images to improve performance and reduce space -->
- [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - for validation of the css in the project.
- [HTML Markup Validation Service](https://validator.w3.org/) - for validation the HTML in the project.
- [Firefox dev tools](https://firefox-source-docs.mozilla.org/devtools-user/index.html) - troubleshooting and debugging of the project code.
- [Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) - for performance, accessibility, progressive web apps, SEO analysis of the project code.
- [Responsive Design](http://ami.responsivedesign.is/) - for website mockup.
<!-- - GitHub Wiki TOC generator (https://ecotrust-canada.github.io/markdown-toc/)
    - Used for generating a table of contents for this README -->
<!-- - Gofullpage chrome plugin  (https://chrome.google.com/webstore/detail/gofullpage-full-page-scre)
    - This plugin was used to take full page screenshots for testing images -->
<!-- - Python online interpreter (https://www.programiz.com/python-programming/online-compiler/)
    - For testing python code snippets -->
<!-- - Unittest (https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
    - For Python unit testing -->
- [JSHint](https://jshint.com/) - for javascript validation.
- [PEP8](https://www.python.org/dev/peps/pep-0008/) - for python validation.
- [Quick Database diagrams](https://www.quickdatabasediagrams.com)- for the database schema diagram.



## Validation

### HTML Validation
The HTML of the each page of the site was validated using [W3C Markup Validation Service](https://validator.w3.org/).  All pages returned a pass with 0 errors and 0 warnings.

<details><summary>Home</summary>
<img src="readme/validation/html-validation/html-validation-home-index.png">
</details>
<details><summary>Full Menu</summary>
<img src="readme/validation/html-validation/html-validation-meals-full-menu.png">
</details>
<details><summary>Meal Information</summary>
<img src="readme/validation/html-validation/html-validation-meals-information.png">
</details>
<details><summary>Dinner Menu</summary>
<img src="readme/validation/html-validation/html-validation-meals-dinner-menu.png">
</details>
<details><summary>Lunch Menu</summary>
<img src="readme/validation/html-validation/html-validation-meals-lunch-menu.png">
</details>
<details><summary>Drinks Menu</summary>
<img src="readme/validation/html-validation/html-validation-meals-drinks-menu.png">
</details>
<details><summary>About</summary>
<img src="readme/validation/html-validation/html-validation-about.png">
</details>
<details><summary>Booking</summary>
<img src="readme/validation/html-validation/html-validation-booking.png">
</details>
<details><summary>Contact Us</summary>
<img src="readme/validation/html-validation/html-validation-contact.png">
</details>


### CSS Validation
The [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/validator) was used to validate the CSS of the website. 

The custom CSS file for the site passed with 0 errors.

<details><summary>Custom CSS file</summary>
<img src="readme/validation/css-validation/css-validation.png">
</details>


### JS Validation
The Javascript of the each page of the site was validated using [JSHint validation tool](https://jshint.com/).  All pages returned a pass with 0 errors and 0 warnings.

<details><summary>script.js</summary>
<img src="readme/validation/js-validation/js-validation-script.png">
</details>


### Py Validation
The Python of the each page of the site was validated using [Python validation tool](http://pep8online.com/).  All pages returned a pass with 0 errors and 0 warnings.

<details><summary>Details</summary>

#### Admin py-validation

<details><summary>about/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-about-admin.png">
</details>
<details><summary>bookings/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-bookings-admin.png">
</details>
<details><summary>contact/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-admin.png">
</details>
<details><summary>home/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-home-admin.png">
</details>
<details><summary>meals/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-meals-admin.png">
</details>

#### Forms py validation

<details><summary>about/forms.py</summary>
<img src="readme/validation/py-validation/py-validation-about-forms.png">
</details>
<details><summary>bookings/forms.py</summary>
<img src="readme/validation/py-validation/py-validation-bookings-forms.png">
</details>
<details><summary>contact/forms.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-forms.png">
</details>

#### Models py validation

<details><summary>about/models.py</summary>
<img src="readme/validation/py-validation/py-validation-about-models.png">
</details>
<details><summary>bookings/models.py</summary>
<img src="readme/validation/py-validation/py-validation-bookings-models.png">
</details>
<details><summary>contact/models.py</summary>
<img src="readme/validation/py-validation/py-validation-contract-models.png">
</details>
<details><summary>home/models.py</summary>
<img src="readme/validation/py-validation/py-validation-home-models.png">
</details>
<details><summary>meals/models.py</summary>
<img src="readme/validation/py-validation/py-validation-meals-models.png">
</details>

#### Urls py validation

<details><summary>about/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-about-urls.png">
</details>
<details><summary>bookings/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-bookings-urls.png">
</details>
<details><summary>contact/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-urls.png">
</details>
<details><summary>home/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-home-urls.png">
</details>
<details><summary>meals/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-meals-urls.png">
</details>

#### Views py validation

<details><summary>about/views.py</summary>
<img src="readme/validation/py-validation/py-validation-about-views.png">
</details>
<details><summary>bookings/views.py</summary>
<img src="readme/validation/py-validation/py-validation-bookings-views.png">
</details>
<details><summary>contact/views.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-views.png">
</details>
<details><summary>home/views.py</summary>
<img src="readme/validation/py-validation/py-validation-home-views.png">
</details>
<details><summary>meals/views.py</summary>
<img src="readme/validation/py-validation/py-validation-meals-views.png">
</details>

#### Urls py validation

<details><summary>project/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-urls.png">
</details>

</details>

### Accessibility
The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/ was used to ensure the website met high accessibility standards. All pages returned 0 errors.

<details><summary>Home</summary>
<img src="docs/validation/wave-validation/wave-validation-index.png">
</details>
<details><summary>About</summary>
<img src="docs/validation/wave-validation/wave-validation-about.png">
</details>
<details><summary>Quiz</summary>
<img src="docs/validation/wave-validation/wave-validation-quiz.png">
</details>
<details><summary>404</summary>
<img src="docs/validation/wave-validation/wave-validation-404.png">
</details>

### Performance 
[Google Lighthouse](https://developers.google.com/web/tools/lighthouse/) was used to measure the performance and speed of the website. Each page scored over 90 in all categories - performance, accessibility, best practice and SEO with results below:

<details><summary>Home</summary>
<img src="docs/validation/lighthouse-validation/lighthouse-validation-index.png">
</details>
<details><summary>About</summary>
<img src="docs/validation/lighthouse-validation/lighthouse-validation-about.png">
</details>
<details><summary>Quiz</summary>
<img src="docs/validation/lighthouse-validation/lighthouse-validation-quiz.png">
</details>
<details><summary>404</summary>
<img src="docs/validation/lighthouse-validation/lighthouse-validation-404.png">
</details>







## Deployment

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository 

By forking this GitHub repository you are making a copy of the original to view or make changes without affecting the original. You can do this by following these steps...

1. Log into your GitHub account and find the [repository](https://github.com/dannymagnus/CI_MS3_MitsurukiFMS).
2. Click 'Fork' (last button on the top right of the repository page).
3. You will then have a copy of the repository in your own GitHub account. 

### Making a Local Clone

1. Log into your GitHub account and find the [repository](https://github.com/dannymagnus/CI_MS4_Elginis_Restaurant).
2. Click on the 'Code' button (next to 'Add file'). 
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Then open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. In your IDE's terminal type 'git clone' followed by the URL you copied.
7. Press Enter. 
8. Your local clone will now be made.

## Credits

*All credit also included in the page files.*

<!-- ### Code

- **WebDev Simplified** - for [Flexbox](https://www.youtube.com/watch?v=fYq5PXgSsbE&t=363s) and [Grid](https://www.youtube.com/watch?v=9zBsdzdE4sM) learning about quiz concepts.
- **CSS Tricks** - for [Scaleable Divs](https://css-tricks.com/aspect-ratio-boxes/) for scaleable divs
- **W3C Schools** - for [jquery](https://jquery.com/) FadeIn and FadeOut methods.
- **Google Fonts** - for [Importing Fonts](https://fonts.google.com/)
- **Bootstrap** - for [Modals](https://getbootstrap.com/docs/5.0/getting-started/introduction/). Bootstrap was used for the responsive nav bar, some button styles and modals in the about page for planets.
- **Font Awesome** - for [Social Media Icons](https://fontawesome.com/)
- **Favicon** - for [Browser icon](www.favicon.io)
- **Solar System Scope** - for [iframe](https://www.solarsystemscope.com/)
- **Font Space** - for [Star-Trek Theme Font](https://www.fontspace.com/category/star-trek)
- **Transfonter** - for [Font conversion](https://transfonter.org/)

### Media

Media from the following artists was used throughout the site.

- [Adobe Stock Images](www.stock.adobe.com)
- [NASA](https://solarsystem.nasa.gov/planets/)
- [Solar System Scope](https://www.solarsystemscope.com/)
- [envatotutsplus](https://design.tutsplus.com/tutorials/create-a-star-trek-style-communicator-in-photoshop--psd-13545)


### Acknowledgements: 

- To my wife Rebecca Richards for her testing, support, feedback, permissions for content and images on this project. 
- To my mentor Mo Shami for his invaluable guidance and direction.
- To the Code Institute slack community of students.
- To the Code Institute Tutors -->








<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!


----------------------------------------------------------------------------------------------------------------------------

 -->
