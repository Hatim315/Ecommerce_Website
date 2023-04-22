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

## To-Do List
- [x] Start the project and add about and home page.
- [x] Add model for products as well as a product page.
- [ ] Add type of product in product table.
- [ ] Add filter of products in product page.
- [ ] Organising products in page numbers.
- [x] Add payment page on website.
- [ ] Fix errors related to payment of cart items.
- [x] Add search functionality.
- [x] Add Login,Logout and Sign ups.
- [ ] Add a User Profile page.
- [x] Add cart functionality
- [x] Add model of recording customer data of orders to database and show it on orders page. 
- [ ] Host this site on hosting service like aws or heroku.


## For removing your confusion of dirs read below

**myapp/** - This dir contains common project files like settings.py
**jojo/** -This folder is an app which contain views of login,logout,about,home of the website.
**shop/** - This dir contains views of all shoppiing functions like checout, product page, cart, storing customer data.

## Conclusion

This website is made by me to test my Django and js skills
