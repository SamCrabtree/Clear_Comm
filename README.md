# cautious-octo-barnacle
A Real Estate Lead Program 

This project is a program developed to help process leads and information for a hypothetical Real Estate Company. 

Upon login, users will be presented with a screen that shows a list of address/property leads and their status. Clicking on any of these leads will display all related information. You will also be able to update notes or delete the lead from this screen. At the bottom of the home screen there is also the ability to add a new lead. You will be able to type and validate an address using the Google Maps API and manually enter information for property owners name, phone number, and email address.  



This program was developed to meet all the project requirements for the CodeLouisville Python Developer course in Fall of 2021.

The program meets the following course requirements: 

1. Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.  

This is taken care of by the use of Classes undeneath the file models.py. Both the Property and notes file have multiple variables containing user inputted data which is recorded and then displayed on both the admin side of DJANGO and the front facing web pages. 

2. Create a dictionary or list and populate it with several values, retrieve at least one value, and use it in your program. 

This requirement is met by using three list's (Type_Choices, Status_Choices, & Note_Choices) contatining tuple values in the models.py file. 

3. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 

These requirements are met 




**To Install: 

A. Fork this repository.

B. Clone the repo to your local machine.

C. Navigate to the cloned folder via the terminal and create a virtual environment.

D. Activate your virtual environment, and then in the terminal type the following command to install all required programs:

pip3 install -r clear_comm/requirements.txt


**To Setup: 

1. Secret_Key Setup 

Prior to launching the program, you will need to generate and hide your own "special key" for the application. In order to do so, create a file called .env in the main folder and create a variable named “Secret_Key”.

  A. Next, open the terminal and type the following command: 

python -c "import secrets; print(secrets.token_urlsafe())”

  B. This will generate a secure key you will need to assign to the "Secret_Key" variable in the .env file. 

  C. Once you save the file, you will need to add the .env file to your gitignore file to prevent accidently listing your . 


2. Create SuperUser

  A. Navigate to the folder via the terminal and run the following command: 
  
  B. Follow the prompts via the terminal to enter a username, email, and password. 



3. Activate Local Host

  A. In the terminal, activate your virtual enviorment, and then type the following command: 

This will activate the Local Server and you can now enter the program by entering the following IP into your web browser: 

127.0.0.1:8000

If you wish to view the admin side of things, you can login to the backend of the program by navigating to 

127.0.0.1:8000/admin







Developed by Sam Crabtree 2021. Please do not copy or redistribute without permission. 
