# cautious-octo-barnacle
A Real Estate Lead Program 

This project is a program developed to help process leads and information for a hypothetical Real Estate Company. 

Upon login, users will be presented with a screen that shows a list of address/property leads and their status. Clicking on any of these leads will display all related information. You will also be able to update notes or delete the lead from this screen. At the bottom of the home screen there is also the ability to add a new lead. You will be able to type and validate an address using the Google Maps API and manually enter information for property owners name, phone number, and email address.  



This program was developed to meet all the project requirements for the CodeLouisville Python Developer course in Fall of 2021.

The program meets the following course requirements: 

1. Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.  

2. Create a dictionary or list and populate it with several values, retrieve at least one value, and use it in your program. 

3. Connects to an external API



**To Install: 

A. Fork this repository.

B. Clone the repo to your local machine.

C. Navigate to the cloned folder via the terminal and create a virtual environment.

D. Activate your virtual environment, and then in the terminal type the following command to install all required programs:

pip3 install -r requirements.txt


**To Setup: 

1. Secret_Key Setup 

Prior to launching the program, you will need to generate and hide your own "special key" for the application. In order to do so, create a file called .env in the main folder and create a variable named “Secret_Key”.

  A. Next, open the terminal and type the following command: 

python -c "import secrets; print(secrets.token_urlsafe())”

  B. This will generate a secure key you will need to assign to the "Secret_Key" variable in the .env file. 

  C. Once you save the file, you will need to add the .env file to your gitignore file to prevent accidently listing your . 


2. Connection to API

  A. ????


3. Create SuperUser

  A. Navigate to the folder via the terminal and run the following command: 
  
  B. Follow the prompts via the terminal to enter a username, email, and password. 



4. Activate Local Host

  A. In the terminal, activate your virtual enviorment, and then type the following command: 

This will activate the Local Server and you can now enter the program by entering the following IP into the 




Developed by Sam Crabtree 2021. Please do not copy or redistribute without permission. 
