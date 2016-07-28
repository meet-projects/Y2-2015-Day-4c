MEET Friends Extra for Experts
------------------------------

**Important:** Welcome to Extra for Experts. This part is meant for people who have successfully completed and fully understand the previous labs for MEET Friends. We will prioritize helping students who have *not* yet finished the previous labs. Also, some of the exercises below *intentionally* go beyond the material that we have done lectures for: it is up to you to search on the internet for what you need to know to solve the exercise.

#### Exercise 1

Make the forms in your MEET Friends app use CSS and Bootstrap. Keep in mind ideas we had mentioned regarding user interface design.

#### Exercise 2

Add three columns to the Person table corresponding to:

* email address
* phone number
* date of birth

Modify your add friend and edit friend pages so that they can deal with the new columns added.

Also, add code that checks that the input provided by the user is valid (e.g., the name can't be an empty string, the email address is a valid email address, the date of birth is a valid date, etc).

#### Exercise 3

Add a page linked off the view my friends page that shows a birthday calendar with your friends' birthdays.

The birthday calendar should have 1 table per month and for a table cell corresponding to one (or more) of your friends' birthdays, those friends' names should be listed in that table cell.

Be sure to think about how to make this calendar easy for the user to use.

#### Exercise 4

It turns out that you want to keep track of what pets your friends own.

1. Design and code up a new table for pets. Be sure to add a foreign key in the Person table that refers to pet ID's. (You'll need to look up how to do foreign keys in SQLAlchemy.)
2. Storyboard what new pages you will have so that you can add a pet for a specific friend, and so that you can also list out all the pets.
3. Code up the new HTML pages needed.
4. Code up the new functions in the Flask app so that your storyboard becomes a full working web app!

#### Exercise 5

You have decided that you want more detailed information on hometowns.

1. Design and code up a new table for hometowns that, aside from the primary key, includes a town name, latitude, and longitude. Make changes to your Person table so that the hometown in the Person table is now a foreign key.
2. Modify the add friend page so that the hometown option shows a dropdown list of hometowns that already exist in the hometown table. Moreover, the dropdown list should also have an option for "add new hometown". (Recall that the dropdown list uses the HTML `select` tag.) Figure out a way so that only when this option is selected will a new hometown be added to the hometowns table.
3. Figure out how to add a page that edits hometowns.
4. Figure out how to use the Google Maps JavaScript API to display the locations of all the hometowns in a map in your web app. Note that you don't really need to know much of any JavaScript to do this since Google provides a snippet of code that you can just copy and paste, and you only need to change a list of latitude/longitude pairs that you want marked on a map.

#### Exercise 6

You have decided that the MEET Friends webapp should actually take login information so that anyone can log in and see information on their specific friends. Figure out how to do this.

#### Exercise 7

You have decided to keep track of what your friends' interests are (e.g., cooking, movies, hiking, etc).

1. Look up what many-to-many relationships are in a database. Why would people and interests constitute a many-to-many relationship?
2. Design and code up a new table for interests. Also code up an association table that associates people with interests.
3. Modify your edit friend page so that you can add interest(s) for a friend.
4. Add a page that lists all interests that have been added to the database and that allows the user to edit interests. Also for each interest, you should list all your friends that have that interest.
