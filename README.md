# cs345_project2
Dependencies:

    Python 3
    Pip install the following packages:
        flask
        flask-wtf
        flask-sqlalchemy
        newsapi-python


Running the news app:
    This must be run on a local computer, not on a remote server.

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
        a description for the article, if available. There are options
        to share the article to LinkedIn, Twitter, or Facebook at the bottom of
        each box. Finally, there's an option so save an article. Checking this
        box will save the relevant article to the Saved Articles page for you to
        look back at later. If the article is already saved, unchecking the box
        will remove the article from the saved articles page.

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

    Saved Articles
        This page stores your saved articles in the order in which you saved
        them. It operates essentially the same as the home page, but it will
        only update when the user adds or removes an article.

    Dark Theme:
        Use the check box to toggle dark theme. This setting is saved between
        sessions.

schedule_jobs.py
    This file runs in the background and grabs new articles for the active tags
    each hour as well as being responsible for fetching the initial batch of top
    stories when first opening the app.


Tutorials used:

    https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

News API:

    https://newsapi.org/
