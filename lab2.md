MEET Friends Lab 2: Building the Flask backend for viewing friends
------------------------------------------------------------------

**Important:** This lab relies on successfully completed code for [MEET Friends Lab 1](https://github.com/meet-projects/y2-meet-friends/blob/master/lab1.md). You should have a folder `y2-meet-friends`.

If you have not set up Python using the commands below, please do so now:

```
exec bash
wget http://tinyurl.com/MEETpythonY2
source MEETpythonY2
```

If you have already run the code above but you've opened a new terminal window, please run:

```
exec bash
source ~/y2-venv/bin/activate
```

#### Exercise 1

In `templates/view_my_friends.html`, notice that we've actually omitted something important: we need to have a for loop that goes through all the friends! Modify the file so that the table row (not the table header but the row that actually has columns that say `{{ friend.name }}`, `{{ friend.gender }}`, etc) is within a for loop. Remember that for how Flask templates work, the end of a for loop has to say `{% endfor %}`.

#### Exercise 2

In the same terminal that you have setup Python using the commands above, go to the folder `y2-meet-friends` and execute the command `python web_app.py`. This should run without error. Leave this continuously running (it's a server!).

Now open your browser and go to `http://127.0.0.1:5000/` (this is the default URL for where Flask runs your web app) and you should see the content that is in `view_my_friends.html` (but notice how `view_my_friends.html` doesn't appear anywhere in the URL!). Similarly, if you go to `http://127.0.0.1:5000/add` in your browser, you should see the content that is in `add_friend.html`.

#### Exercise 3

We've already imported the relevant portions of SQLAlchemy for you into the Python file `web_app.py`.

In the function `view_my_friends()`, change the first line so that it actually reads all the people from the database into the variable `friends`. After completing this exercise, when you go to `http://127.0.0.1:5000/` in your web browser, you should see a list of all the people you added to the database in [Database Lab 2](https://github.com/meet-projects/y2-db-lab2).
