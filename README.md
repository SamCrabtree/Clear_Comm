
# Clear_Comm

A Real Estate Lead Program

This project is a program developed to help process leads and information for a hypothetical Real Estate Company. 

Upon login (you will need to use the admin username and password you created in the setup steps below), users will be presented with a screen that contains a dashboard that shows it's organization's weekly goals, and a list of a few options such as "Add A Lead" which takes you to a form page that allows you to create a lead for a property, "Loops" which shows the team any open tasks they may need to complete, and "Call List" which takes you to a page that contains all of your current leads. In regards to the "Call List" page, you will see all lead entries in a list that shows its of address/property leads and their status. Clicking on the question mark next to any of these leads will display all related information. You will also be able to update the lead with updated information, add notes or delete the lead entirely from the list.



## Purpose

This program was developed to meet all the project requirements for the CodeLouisville Python Developer course in Fall of 2021.

The program meets the following course requirements 

1. Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.    


2. Create a dictionary or list and populate it with several values, retrieve at least one value, and use it in your program. 


3. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 

## Required Packages


asgiref==3.4.1  
Django==3.2.8  
django-ckeditor==6.1.0  
django-js-asset==1.2.2  
python-decouple==3.5  
pytz==2021.3  
sqlparse==0.4.2

**NOTE:** All of these Packages will be included in requirements.txt



## Download and Install

A. Fork this repository.

B. Clone the repo to your local machine.

C. Navigate to the cloned folder via the terminal and create a virtual environment by running the following command:

      python3 -m venv <name_of_virtualenv>

D. Activate your virtual environment by entering the following command:

        source venv/bin/activate

E. Once your virtual envioronment is active in the terminal type the following command to install all required programs:

    pip3 install -r requirements.txt

This will install the packages above and you are now ready to begin your setup. 





## Setup and Configuration

1. Secret Key Setup   

Prior to launching the program, you will need to generate and hide your own "special key" for the application.

  - Open the terminal and navigate to the root directory and type the following command: 

        python3 -c "import secrets; print('Secret_Key=' + secrets.token_urlsafe())" > .env

  This will generate a secure key and assign it to the "Secret_Key" variable in a .env file. 


2. Make Migrations
  You will now need to make dnago migrations to begin 
  - Navigate to the clear_comm folder in your directory using the following command:

          cd clear_comm

  - Enter the following commands to make your first migrations. 

        python3 manage.py makemigrations

and then 

    python3 manage.py migrate 



3. Create SuperUser 
 Creating a superuser creates your username and password for the entire program and is needed to access the programs functionality.   

  - Navigate to the folder via the terminal and run the following command: 

      python3 manage.py createsuperuser
  
  - Follow the prompts via the terminal to enter a username, email, and password. 



4. Activate Local Host
Activating a local server allows you to view the program via your web browser and interact with the program via a GUI. 

  - In the terminal, activate your virtual enviorment, and then type the following command: 

        python3 manage.py runserver 

This will activate the Local Server and you can now enter the program by entering the following IP into your web browser: 

    127.0.0.1:8000

If you wish to view the admin side of things, you can login to the backend of the program by navigating to 

    127.0.0.1:8000/admin
## Author

- [@SamCrabtree](https://github.com/SamCrabtree)

