# Capstone---Blog
A user of my blog should be able to easily move around the app and read whatever blog posts are available.

The plan is for there to be two different "blogs". There will be one for software engineering/development and a blog section for woodworking. 

This project is meant to be a tool that I will use from now on both recreationally as well as professionally. I want it to be a reflection of my interests/passions as well as a documentation of my growth in both my craftsmanship in programming and woodworking. 

I hope that the content that I present in this app will give a better reflection of who I am currently and who I am growing in to as a new developer.

There will be multiple sections to the app including but not limited to, links to a portfolio(eventually) and an about me section. 

User comments will be welcome.




Models:
Post & User

Post = title,
       content,
       date_posted,
       author <--- this will be the foreign key relating to the User model
       
User = username,
       email,
       first_name,
       last_name
