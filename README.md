<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="CollectiveCooks/static/images/image-logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Cooks Collective</h3>

  
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#project-resources">Project Resources</a>
          <ul>
            <li>
              <a href="#erd">ERD</a>
            </li>
            <li>
              <a href="#ui-ux">UI / UX</a>
            </li>
            <li>
              <a href="#gantt-chart">Gantt Chart</a>
            </li>
          </ul>
    </li>
    <li><a href="#functional-requirements">Functional Requirements</a></li>
    <li><a href="#additional-features">Additional Features</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributors</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## ABOUT THE PROJECT

[![Product Name Screen Shot][product-screenshot]](https://example.com)

[![Product Name Screen Shot][product-screenshot-1]](https://example.com)

Vehicle Rental System designed to streamline the rental process for both customers and administrators. Built with Django, this system allows users to browse available vehicles, book rentals, and manage profiles, while giving administrators control over vehicle inventory and rental records. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## FUNCTIONAL REQUIREMENTS
1. **User Registration**  

    The customer will input required data in the fields provided. If the information is verified, the system will create an account for the customer.

2. **User Log-In**  

    The customer will input their username and password. If the information is verified, the system will

3. **Vehicle Search/Availability**  

    The customer can search for specific vehicle or view all the listing of vehicles based on the date that they want to rent

4. **Booking Process**  

    The customer has chosen vehicles to rent, the system will summarize the rental dues/fees, the list of vehicles rented, the duration of the rental. A cancel button and pay button will display. When the user proceeds to pay then the booking is successful, otherwise, the booking is unsuccessful.

5. **Admin Dashboard/CRUD Operations for Vehicle**  

    The admin can Create, Read, Update, and Delete records of vehicles in the system

6. **Log Out**  

    When the user clicks the log out button, the log-session will be deleted in the system.


## ADDITIONAL FEATURES

7. **Vehicle Rating Functionality**  

    The user can leave a rating of the vehicle and add comment after the transaction has been completed

6. **User Profile / Email and License Verification**  

    The user can update their information and verify their email and license to make their account verify.


## Built With


[![HTML][HTML]][HTML-url]
[![CSS][CSS]][CSS-url]
[![Python][Python]][Python-url]
[![Django][Django]][Django-url]
[![SQLite][SQLite]][SQLite-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
##  **Getting Started**  

###  **Prerequisites**  

Before you start, ensure you have the following installed:

 [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### **Installation**  

1. **Clone the repository**  
   Open your terminal and run the following command:
   ```bash
   git clone https://github.com/valceven/collective-cooks.git
   cd vrs
   ```

2. **Create a virtual environment**  
   It’s recommended to create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   ```
   or

   ```bash
   py -m venv venv
   ```

   Activate the virtual environment:
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies**  
   Install all the required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**  
   Run the database migrations to set up the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**  
   Now, you can start the development server and view the project locally:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**  
   Open your browser and go to `http://127.0.0.1:8000/` or `http://localhost:8000/` to see the application running locally.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

### Top contributors:

<a href="https://github.com/valceven/collective-cooks/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=markyleangela/VehicleRentalSystem" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Val Mykel Ceven Bolante - [@valceven](https://www.facebook.com/valmykelceven.bolante) - VAL GMAIL

Dechie Sullano - [@dechie](https://facebook.com/username) - DECHIE GMAIL

Fiel Louis Omas-as - [@fiellouis](https://www.facebook.com/fiellouis.omasas) - fiellouisomasas@gmail.com

Project Link: [https://github.com/valceven/collective-cooks](https://github.com/valceven/collective-cooks)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/markyleangela/VehicleRentalSystem.svg?style=for-the-badge
[contributors-url]: https://github.com/markyleangela/VehicleRentalSystem/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/markyleangela/VehicleRentalSystem.svg?style=for-the-badge
[forks-url]: https://github.com/markyleangela/VehicleRentalSystem/network/members
[stars-shield]: https://img.shields.io/github/stars/markyleangela/VehicleRentalSystem.svg?style=for-the-badge
[stars-url]: https://github.com/markyleangela/VehicleRentalSystem/stargazers
[issues-shield]: https://img.shields.io/github/issues/markyleangela/VehicleRentalSystem.svg?style=for-the-badge
[issues-url]: https://github.com/markyleangela/VehicleRentalSystem/issues
[license-shield]: https://img.shields.io/github/license/markyleangela/VehicleRentalSystem.svg?style=for-the-badge
[license-url]: https://github.com/markyleangela/VehicleRentalSystem/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kyle-angela-mar-405aa3159/
[product-screenshot]: images/product-screenshot-2.png
[product-screenshot-1]: images/product-screenshot-3.png
[Django]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/

[SQLite]: https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/

[HTML]: https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://developer.mozilla.org/en-US/docs/Web/HTML


[CSS]: https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS

[Python]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

