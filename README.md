# CodeBytes: REST API Challenge
CodeBytes is a cool meetup group in Portland that sets up little 
projects in code that can be attempted in a short amount of time.
People are able to pair program on the problem. People work in 
various languages. It is a lot of fun and a great way to learn.

#### Original Challenge: [CodeByte Original Repo](https://github.com/CodeBytes-PDX/rest-api-challenge)

## Project Progress:
**Endpoints that Work:**
* GET `/` -- should return `"hello world"`
* GET `/books` -- should return a list of all books
* GET `/books/5` -- Get a specific book. Should return the JSON book 5 (or whichever)
* GET `/users` -- get all users as a JSON list

**Other Endpoints to Attempt Another Day**
* GET `/books/5/status` -- Get a specific book's status. Should return just the status for book 5 (or whichever).
* POST `/books/add` -- Add a book to the library
* POST `/users/5/books/5/checkout` -- checkout a book for a user
* POST `/books/5/return` -- return a book to the library
* GET `/users/5/books` -- get all books checked out by the given user



## Tools Used:

#### Vagrant
Because I like to be difficult, I am using vagrant for my setup on this 
project rather than the venv that the original CodeByte project suggested. 
Specifically, I used [Scotch Box]((https://box.scotch.io))
* Check out the official docs at: [box.scotch.io](https://box.scotch.io)
* [Read the getting started article](https://scotch.io/bar-talk/introducing-scotch-box-a-vagrant-lamp-stack-that-just-works)

## Run the Project:
1. Download or clone this repo.
1. ``` cd ``` into this project.
1. Run ``` vagrant up ``` to build the virutal machine environment.
1. Run ``` vagrant ssh ``` to get into the VM.
1. From inside the VM: ``` cd /var/www/ ```
1. Run ``` pip3 install -r requirements.txt ``` to install the requirements for this project.
1. Run ``` python3 app.py ``` to run the REST API program.
1. In your browser go to [http://192.168.33.10:5000/](http://192.168.33.10:5000/) (Or and of the end points listed under 'Endpoints that Work')

