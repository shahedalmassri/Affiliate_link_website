# Affiliate_link_website
A website that holds cards for products with an image, link and description for each item. Admins can add, edit and delete cards.

Hello, welcome to Shahed's affiliate link website.

OVERALL FILE STRUCTURE:
This website runs on a flask framework. The app.py file is where all the back-end code is located.
app.py is a python file utilizing the flask framework to manage the two routes (public, admin) that this website contains.
templates folder contains the front-end pages in HTML
  - layout.html is the overall layout and header for the site
  - public.html is the page for public access
  - admin.html is the page for admin access
website.db is a single-table SQLITE database that holds all data (links/images/text/dates). It is recommended to back-up this file periodically to avoid losing data. 

WEBSITE ROUTES (as seen in app.py):
The first route is "/" which is the PUBLIC access route. This is what everyone sees.
The second route is "/admin" which is restricted to authorized IP addresses.
This website uses Bulma library for style. Source: https://bulma.io/documentation/

WEBSITE USE INSTRUCTIONS:
RUNNING IT LOCALLY
Download python and flask on VSC
Go into the directory where the website is located
Enter the command python -m flask run
Click on the link that pops up

ADDING/UPDATING/DELETING AUTHORIZED IP ADDRESSES
Near the top of app.py, there is an array called "allowed_ips" e.g. allowed_ips = ["203.156.78.224.", "172.29.145.88."]
Add/update/delete authorized IP addresses into this array.

ACCESSING THE ADMIN page:
Manually type /admin to the end of the domain. This is the only way to accesss see the admin-only page.
If you get a 403 Forbidden request, you have to update the list of authorized IPs to include yours. See above.

ADDING A NEW CARD (ADMIN-ONLY):
On the add new card, click Add.
A form will pop-up. Fill in the information:
image_link is the link to the image to be used for that card. Use a direct link image ending in .jpg, .png, etc.
title is the link text e.g. LG Monitor 
product_link is the actual link to the product. Both the card image and the title will be lead to this link when clicked.
subtitle and body text are optional, used to give more information.
Click Submit to add new card.

EDITING A CARD (ADMIN-ONLY)
Find the card you want to edit. Click Edit.
Fill in edited information. If you don't update a field, it will keep it the same it was before.
Click Submit to finalize the edit.

DELETING A CARD(ADMIN-ONLY)
Find the card you want to delete. Click Delete.
It will ask "Are you sure you want to delete this card?" Press Yes to delete, Cancel to cancel.






