# Instawork APP
## **Table of Contents**
1. Description
2. Technologies and Frameworks Used
3. Installation and Setup
4. Running the application
5. Test Cases
6. Test Data 
7. Contact


## **Description**
> Instawork app is a python Django application in which team members can be added. Already added team members data can be modified or deleted as well.

## **Technologies and Frameworks Used**
> * Django
> * Python
> * SQLite (Default database for Django)

## **Installation and Setup**
> Download or Clone the code from the github link provided.
> GitHub link: https://github.com/SreejaAtluri/Instawork

> Once it is successfully cloned, follow the below steps.
> Create a virtual environment for the cloned project.
> Install all the required packages from requirements.txt using the below command
> pip install -r requirements.txt
> After the successful installation of packages, run manage.py task.
> To make sure the database is up to date use the following commands.
> makemigrations Instaworkapp
> migrate Instaworkapp

## **Running the Application**
> After successful migrations, run the server using the command
runserver
> A url will be generated after running the server where we can access the project.

> ![image](https://user-images.githubusercontent.com/26114150/179570270-3c926779-dc23-43d9-ae46-6fd1c7ada358.png)

## **Test cases**
### List page

> This page lists the team members with subheading on number of team members. If the team member is an admin, it is listed next to their name. On click of the name of > the team member, it will redirect to edit page where the user can edit the details of that particular team member. On click of the add button, it will redirect to 
> add page where the user can add new team members.

> ![image](https://user-images.githubusercontent.com/26114150/179575264-dc60b041-20ab-4bc9-82f4-7c490e179b1c.png)

### Add page

> In this page, the user can add a new team member by entering their first name, last name, email and phone number. Also, the user needs to select the role of the team > member if he is an admin or regular member. By default, the role is set to regular. After entering the details, on click of save, the details are saved and is 
> redirected to the list page

> ![image](https://user-images.githubusercontent.com/26114150/179575898-82f45385-3fee-49e2-a830-7e983abe246e.png)

### Edit page

> In this page, the user can edit the details of that particular team member in which the user can also change the role. After changing the values on click of save 
> button, the details get updated and redirects to the list page. On click of delete button, it redirects to a new page “Delete page”.

> ![image](https://user-images.githubusercontent.com/26114150/179575999-13161b08-50ab-4a53-9eff-1d4c92f36a9e.png)

### Delete Page

> In this page, the user gets an option to either confirm the delete option or to cancel. On click of Submit, the team members details get deleted and is redirected to > the list page. On click of cancel, it redirects to the list page.

> ![image](https://user-images.githubusercontent.com/26114150/179576156-e5fc71aa-833a-4abb-99a5-59d7e16dc8dd.png)


## **Test Data**
> Sample data is considered to test all functional parts of the project.

## **Contact**
> Sreeja Atluri: atluri1@uwindsor.ca


