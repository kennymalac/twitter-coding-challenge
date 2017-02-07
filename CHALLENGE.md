#Professional Services Engineer Coding Challenge
Coding challenge for candidates working on web services. Basic premise is to write a REST API that talks to Twitter and presents some information from tweets, and a front end app that interacts with API. Should be able to run locally on a laptop for testing and evaluation.

###Skills & Knowledge Being Assessed
 +  Software development
 +  Python web development
 +  REST APIs
 +  JavaScript
 +  Written communication

##Instructions
Timeframe: 7 days limit, can turn in early when done, can ask for extension.

This archive contains a skeleton Flask project which you will use to implement a basic REST API. The settings.py file in the project contains an Application Token and Secret for making authenticated requests against Twitter's API (see General expectations/notes below for 3rd party library usage).

When complete, send a link to a version of the updated project. The source code can be hosted online as an archive file or in a repository (e.g., GitHub).

###Notes About the Code Provided
The Flask application is already configured to read from the settings.py file.
No models, views, or url configurations have been defined.

##Deliverables
###REST API
Create a view that fulfills the following requirements:
####Backend
 + Accept a "twitter_account.id"
 + Use the Application Token and Secret to authenticate with Twitter's API.
 + Fetch the public timeline for the twitter_account.id from Twitter's API
 + Extract the Screen Name, Text, Tweet ID, Date, and Profile Image from each object
 + Transform the date into a Unix Timestamp
 + Render the result as a JSON response

####Front-End
Using the API written in Flask, you’ll create a JavaScript webapp that makes a request for a Twitter user’s timeline and displays the tweets returned. You can use a JavaScript framework (AngularJS, Ember.js, etc.) if you want. The tweets should be rendered in a list view and each message/tweet should display the following items:
 + Avatar image of author
 + Screen name of author
 + Tweet text
 + Reply icon (see below for details)
 + Relative timestamp (e.g. 5 minutes ago, 2 hours ago, 1 week ago)

#####Reply Icon
Each Tweet should contain a dummy reply action. When clicking on the Reply icon, the app should show a prompt that prints the Tweet text, Tweet ID, and the author’s user ID.

#####Markup/Styles
There are no strict requirements for how tweets are rendered.
###General Expectations & Notes

 + The URLs and views should be laid out in a RESTful fashion
 + Readable code (e.g., PEP 8)
 + Error handling matters
 + Clean markup and styles are important.
 + Use best practices/conventions
 + Feel free to use any 3rd party libraries (e.g. Python Twitter lib, Python OAuth lib, JavaScript time formatting lib, jQuery, etc)
