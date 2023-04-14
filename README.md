In this hand-in I completed the tasks from the previous hand-in (that i couldn't submit on time) 

I've built a flask backend application with three routes to different product types for e-commerce tea store. I've used jinja2 templates and dynamic routes to buy the products. I had no issues with this part of hand-in. It was pretty simple to follow the examples from Flask 2 tutorial.However, I had to spend a lot of time on static files (css and images) didn't work with jinja templates because i didn't locate the folders properly. due to often errors related to this and other issues, i've improved at working with terminal and figuring out errors, i do feel significantly better about it.

the second part of the hand-in, which is hand-in for 27.03.23 was the hardest hand-in so far.
as i was traveling last week, i've spent only 2h per day for learning the material and only started working on the actual hand-in on Sunday. That is why i did the bare minimum on html/css side of things and focused on working on creating models and database.

Tech stack: Flask as web framework, SQLAlchemy as an ORM, SQLite as a database, html,css. 

I have two models: Product and ProductType, where Product model represents a product on the e-commerce site and ProductType represents a type of a product, where each type can have many products, but a product can have only one type. with building such model i've learned about 'one to many' datamodel.
I had difficulty performing database migrations using flask-migrate. i need to spend more time reading and watching tutorials on this as i still feel not confident in this.

Also, i had lots of problems with styling issues not being applied as i expected. i m getting better at this with developer tools, but this is very frustrating part for me.

for some reason, when i try to run the app using chrome it doesn't always work, while in firefox it does work perfectly, i am not sure what's the issue at this point. 

___


in the current hand-in I applied the information from  CRUD tutorial to render data from database on multiple pages. the web app allows users to add, edit, delete products, (it should be behind authentication, but i didn't have time to implement it yet.)

the second part of the task, which is deployment , was the most difficult. 
initially i tried using render.com,  ( and still using the managed postgress database from there), however i had difficulties getting thw app to run , always had internal sevever error.

however, i managed to do it with digitalocean, because there i was able to see and debug errors better and understand how it works. to do so, i've used a step by step guide from https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04
for this assigment i was focused on making the logic of the app and generally learning about deployment and crud functionality so I did not focus on styling as much

the crud functionality is at 
/products/create where someone can create products 
/products/<id>/edit where someone can edit products
and /products/<id>/delete where someone can delete a product