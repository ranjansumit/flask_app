Heroku_Setup

*$ touch Procfile*


Add the following line to your newly created file

*web: gunicorn app:app*

Make sure to add gunicorn to your requirments.txt file

*$ pip install gunicorn==19.4.5*
*$ pip freeze > requirements.txt*

One for production:

*$ heroku create wordcount-pro*

And one for staging:

*$ heroku create wordcount-stage*

These names are now taken, so you will have to make your Heroku app name unique.

*$ git remote add pro git@heroku.com:YOUR_APP_NAME.git*
*$ git remote add stage git@heroku.com:YOUR_APP_NAME.git*

Now we can push both of our apps live to Heroku.

For staging: *git push stage master*
For production: *git push pro master*