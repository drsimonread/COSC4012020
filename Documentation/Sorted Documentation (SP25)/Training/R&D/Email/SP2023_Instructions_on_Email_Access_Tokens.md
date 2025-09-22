# Overview

	The system we’re using is a third party django library, called Django Gmail Api Backend.  It can be found here [https://pypi.org/project/django-gmailapi-backend/](https://pypi.org/project/django-gmailapi-backend/) and installed via pip.  The core functionality of this is just what it sounds like: it adds the gmail api as a possible email backend in Django.

	Access to gmail is regulated through three kinds of tokens: A session ID, a client secret, and a refresh token.  At present, these three items are hardcoded into the settings.py file as strings.  Updating them therefore simply involves replacing these strings with new, valid information.

# Setting the Backend

	By default, the email background in the local environment is set to **console**.  This means that the email will be printed to the console, rather than sent to any actual address.  This is preferable for a development environment where we don’t have or need actual API keys, but is not representative of the production version.

	In order to test the Gmail API backend, make sure that the package is installed in your environment.  It must then be added as a third-party app in the Django config, and then finally set as the email backend. By configuring the three variables mentioned earlier, the program will begin to send emails through the authenticated account associated with those tokens automatically.

# Getting New Tokens

	The Gmail Backend package comes with a “helper script” that claims to be able to generate the relevant authentication tokens.  Unfortunately, this helper script uses Out of Band authentication: a deprecated method that, as of earlier this year, is completely disabled by Google.  Instead, we’re going to have to generate it ourselves.

	The Gmail API Python Quickstart contains code for querying an account to grab the labels associated with that mailbox.  To do this, it requires project credentials to identify itself to the Google servers.  These can be generated through the Google Developer Cloud API Console- Make sure they have the correct scope.

	Once you’ve acquired credentials.json from the API console, put that in the working directory of the example script.  Now, it should be able to grab the labels (provided that was included in the scope you gave your project.)  Django needs to be able to send mail, so you’ll need to change the “scopes” variable in the example script to point to [`https://www.googleapis.com/auth/gmail.send`](https://www.googleapis.com/auth/gmail.send)

	Note that the label grabbing will now fail, since the program is only asking for the ability to send messages.  This doesn’t stop it from generating the tokens we need, so go ahead and run the program.  If everything worked correctly, a browser will automatically launch and prompt you to sign into a google account.  Upon completion, the tokens will be distributed to the program and stored into tokens.json, located in the working directory of the program.

	Within tokens.json there are the three elements; the session ID, the client secret, and the refresh token that are necessary for the Django Backend to function.  These can just be copied and pasted into the settings.py file, and the program will now be able to send emails.  Emails will always originate from the email you signed into on your local computer, no matter what the “default sender” variable is in Django’s configuration.

