# cs345_project2
Dependencies:

    Python 3
    Pip install the following packages:
        flask
        flask-wtf
        flask-sqlalchemy
        newsapi-python


Running the news app:

    Navigate to the app folder and:

        On a Unix system:

            $nohup python schedule_jobs.py
            $python run_app.py

        On a Windows system:

            In two separate command lines, run:
            python schedule_jobs.py
            python run_app.py

    Open a web browser of your choice, and enter the following link: http://127.0.0.1:5000/
    If that link does not work, use the one provided in the command line.


Using the news app:

    Home:
        This is where your news feed is displayed. Articles with tags specified
        in the tag manager will appear here. Each article is displayed in its
        own box. The top left of the box displays the article's news provider,
        followed by the time and date published. The top right displays the
        estimated reading time for the article. The main body of the box
        includes a previews thumbnail for the article, the article's title, and
        a description for the article, if available. Finally, there are options
        to share the article to LinkedIn, Twitter, or Facebook at the bottom of
        each box.

    Tag Manager:
        Use this to specify your interests. Tags are essentially keywords, and
        can be made more complex using operators such as AND, OR, or NOT. The
        + operator can be used to specify that a term MUST appear within the
        article, and - can be used to specify that a term must NOT appear within
        the article. Each tag functions independently. Complete entering a tag
        via enter, entering a comma, or clicking anywhere on the page. When you
        have finished entering your interest tags, press the update button to
        update your tags and return to your home page. Tags are saved between
        sessions.

        You can use the "Top" tag to get generic top stories.

    Dark Theme:
        Use the check box to toggle dark theme. This setting is saved between
        sessions.
