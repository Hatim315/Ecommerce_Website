# Ecommerce_Website
This is a e-commerce website made with Html,css,bootstrap,js and Django.This website is still under development and names of the directories can be confusing.
I will fix them in near future.

## How to start the server?
1. Start the virtual environment by using ```source bin/activate``` command.
2. Install all the requirements by entering ```pip install -r requirements.txt```.
3. Now, Change the directory to Mspp2 by using ```cd Mspp2``` command.
4. Here, migrations has been already done but you have to change **secret_token** in myapp/settings.py
5. You can generate this token running ```python secret_key_generator.py``` .
6. After all this you can start the server by using ```python manage.py runserver```.
#### Note: Admin page is on "adminJojoj/" url.

## For removing your confusion of dirs read below

**myapp/** - This dir contains common project files like settings.py
**jojo/** -This folder is an app which contain views of login,logout,about,home of the website.
**shop/** - This dir contains views of all shoppiing functions like checout, product page, cart, storing customer data.

## Conclusion

This website is made by me to test my Django and js skills
