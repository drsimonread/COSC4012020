

| Circular Dichroism Spectrometer  Software Test Results 401 Quality Assurance & Documentation Team |
| :---- |

---

 

**Test Number:** 01  
**Author:** QA Team  
**Date:** October 22, 2020  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the user registration and login menus.  
**Test Procedures:**

1) A user with public level access will be added to the database through the registration page.  
2) The team will attempt to log in using the newly created account’s credentials. Each account will be logged in multiple times to ensure that it persists in the database’s memory.  
3) More accounts of the same access level will be created and logged in with to ensure that the database is capable of properly registering multiple users.  
4) Steps 1 through 3 will then be repeated with student access level and administrator access level accounts.

**Measure of Success:**  
All accounts should be able to use it for login, taking the user to the home page once the login is completed.

**Results: Sign up resulted in internal server error on first try. Second try resulted in “User already registered under this email” error. Attempting to sign in using this account results in “The username and/or password you specified are not correct” error. Unable to login in at all.**

**Result 2: Only able to sign in through google school account using google link**

**Result 3: The website gave the option to sign in with google account. When attempting to sign in with the google account the website said to sign in first then link google account. After attempting to sign in there was another internal server error.**

**Test Number:** 02  
**Author:** QA Team  
**Date:** October 27, 2020  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the password reset function  
**Test Procedures:**

1) Open the application within a web browser.  
2) Click “login”  
3) Click “forgot password”  
4) Enter email address  
5) Click “enter/send” (submit email address)

**Measure of Success:**  
The user should receive a forgotten password email from the application and should now be able to reset their password. 

**Results: Attempting to reset password results in internal server error. Unable to reset password.**

**Results 2: When using google account to sign in, no option to reset password without signing out. After signing out, page redirects to Internal Server Error**

**Test Number:** 03  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 2.0  
**Test Purpose:** This test is intended to test the functionality of the application within several web browsers, including but not limited to: Google Chrome, Mozilla Firefox, Safari, and Microsoft Edge.  
**Test Procedures:**

1) Open a **Google Chrome** web browser  
2) Enter the link to the CD Spec application, hit enter  
3) Ensure that the application has opened and is displayed properly.  
4) Open a **Safari** web browser  
5) Enter the link to the CD Spec application, enter  
6) Ensure that the application has opened and is displayed properly.  
7) Open a **Firefox** browser  
8) Enter the link to the CD Spec application, enter  
9) Ensure that the application has opened and is displayed properly.  
10) Open a **Microsoft Edge** web browser  
11) Enter the link to the CD Spec application, enter  
12) Ensure that the application has opened and is displayed properly.

**Results:**   
**The application is functional on a google chrome browser, Safari browser, Firefox browser using Google to sign in otherwise setting up an account does not work.**

**Measure of Success:**  
The application should be opened successfully on various web browsers.

**Test Number:** 04  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the data upload function.  
**Test Procedures:**

1) Open the application with a web browser  
2) Login to account  
3) Select “upload”  
4) Select data file to upload  
5) Upload the file, confirm that the file has successfully been uploaded by the application 

**Measure of Success:** The data file has been successfully uploaded to the database and can be accessed.

**Results: Unable to login to a seemingly created account. After signing up, an error occurred, but would not allow signing with the same email address. Sign In page recognized when the password was incorrect, but when the correct password was entered it returned an Error page.**

**Test Number:** 05  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the search engine.  
**Test Procedures:**

1) Open the application with a web browser  
2) Login to account  
3) Select “search”  
4) Enter the desired file in the text field as well as any specifics (date, uploader, etc…)  
5) Click “enter” (confirm)

**Measure of Success:** The data file in the database that was searched for will be located and viewable by the user.

**Results: Search function works but only compares first part of text fields to the searchable term. For example if the name is “Buffer 3ds” if you search “buff” it will appear as a match but not “uff” despite it being included in the Molecule Name field.** 

**Test Number:** 06  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of an administrator account.  
**Test Procedures:**

1) Open the application with a web browser  
2) Login to administrator account  
3) Open the application in a web browser  
4) Login to student account  
5) Select “upload”, upload a data file to the database  
6) Go back to homepage  
7) Select “search”  
8) Enter a file’s information to search, locate a file  
9) Select “edit”, edit a file’s data within the database, confirm that the edit ability is functional  
10) Validate that admin abilities are fully functional and unique to the administrator account

**Measure of Success:** The administrator account has full access to all functions of the application, including editing, uploading, and searching files.

**Results: Unable to login to a seemingly created account. After signing up, an error occurred, but would not allow signing with the same email address. Sign In page recognized when the password was incorrect, but when the correct password was entered it returned an Error page. Safari and Chrome**

**Test Number:** 07  
**Author:** QA Team  
**Date:** October 27, 2020  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of a student account.  
**Test Procedures:**

1) Open the application in a web browser  
2) Login to student account  
3) Select “upload”, upload a data file to the database  
4) Go back to homepage  
5) Select “search”  
6) Enter a file’s information to search, locate a file  
7) Go back to homepage  
8) Confirm that the student account cannot edit anything within the database, only upload and search

**Measure of Success:** The student account does not have the ability to edit files within the database, but can upload files as well as search the database or existing files.

**Results: Unable to login to a seemingly created account. After signing up, an error occurred, but would not allow signing with the same email address. Sign In page recognized when the password was incorrect, but when the correct password was entered it returned an Error page, Safari and Chrome.**  
**Test Number:** 08  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of a public account.  
**Test Procedures:**

1) Open the application in a web browser  
2) Login to a public account  
3) Select “search”  
4) Enter a file’s information to search, locate a file  
5) Go back to homepage  
6) Confirm that the public account cannot upload to the database or edit any files within.

**Measure of Success:** The public account does not have the ability to upload or edit files, but can search for files already within the database.

**Results: Unable to login to a seemingly created account. After signing up, an error occurred, but would not allow signing with the same email address. Sign In page recognized when the password was incorrect, but when the correct password was entered it returned an Error page.**

**Test Number:** 09  
**Author:** QA Team  
**Date:** October 27, 2020  
**Revision:** 2.0  
**Test Purpose:** This test is intended to test the functionality of student account creation (by admin or in general).  
**Test Procedures:**

1) Open the application in a web browser  
2) Login to an administrator account  
3) Go through the steps to set up a new student account  
4) Logout of administrator account  
5) Login to new student account  
6) Confirm that the new student account has been created successfully 

**Measure of Success:**  
A CD Spec student account has successfully been created by a CD Spec administrator account and can be accessed.

**Result: Unable to create a new account unless signing in using a google account.**

**Test Number:** 10  
**Author:** QA Team  
**Date:** 2/17/21  
**Revision:** 2.0  
**Test Purpose:** The purpose of this test is to test the character limits within the file description.  
**Test Procedures:**

1) Open the application in a web browser (any browser specified in section 6 of this document)  
2) Login to any account type (admin, student, or public)  
3) Go through the steps to upload a data file  
4) Type a description for the file to be uploaded  
5) Verify that the character counter has displayed character count

**Measure of Success:**  
The correct character count is displayed within the description text box.

**Test Number:** 11  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 2.0  
**Test Purpose:** This test is intended to test the functionality of the color customizer on multi graphs  
**Test Procedures:** 

1) Open the application in a web browser  
2) Login to an administrator account  
3) Open any graph  
4) Select a new color for the graph information  
5) Confirm the color has changed

**Measure of Success:**   
Colors of multi graphs are able to be changed to whatever color(s) the user desires

Results: Unable to log in, otherwise the graph changed color with no issues.

**Test Number:** 12  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 3.0  
**Test Purpose:** This test is intended to test the functionality of graph image downloading  
**Test Procedures:**

1) Open the application in a web browser  
2) Login to an account  
3) Open any graph  
4) Press the download button  
5) Confirm graph has been successfully downloaded

**Measure of Success:**  
Graphs will be downloaded and saved onto a user’s hard drive

**Results: Unable to login, otherwise the graph displayed on the site properly and the download option also worked.**

**Test Number:** 13  
**Author:** QA Team  
**Date:** 2/17/21  
**Revision:** 2.0  
**Test Purpose:** The purpose of this test is to test the capabilities of the administrator level account.  
**Test Procedures:**Open the application with a web browser (any specified within section 6 of this document)

1) Login to an administrator account  
2) Select “upload”, upload a data file to the database  
3) Go back to homepage  
4) Select “search”  
5) Enter a file’s information to search, locate a file  
6) Select “delete”, delete a file from the database, confirm that the delete ability is functional  
7) Verify that admin abilities are fully functional and unique to the administrator account

**Measure of Success:**  
The uploaded file has been successfully deleted from the database by the administrator and is no longer visible by any account.

**Results: Unable to login to a seemingly created account. After signing up, an error occurred, but would not allow signing with the same email address. The sign In page recognized when the password was incorrect, but when the correct password was entered it returned an Error page.**

**Test Number:** 14  
**Author:** QA Team  
**Date:** 2/17/21  
**Revision:** 2.0  
**Test Purpose:** The purpose of this test is to test the constraints of the multi-graph function.  
**Test Procedures:**

1) Open the application with a web browser (any specified within section 6 of this document)  
2) Upload two or more data files to the database (if database does not have any files already)  
3) Select the graphing function, proceed to graph at least two data files  
4) Verify that the graph has taken the three specified constraints into consideration (an x, y, and z variable)

**Measure of Success:**  
The visible multigraph should have three variables graphed: an x, y, and z (temperature) variable.

**Results: Since the login is not working properly, it says permission was not given to upload.**

**Test Number:** 15  
**Author:** QA Team  
**Date:** 2/17/2021  
**Revision:** 2.0  
**Test Purpose:** This test is to test the functionality of account authentication and permissions  
**Test Procedures:** 

1) Open the application with a web browser (any specified within section 6 of this document)  
2) Follow the steps to creating a new user account  
3) Follow authentication procedures once login credentials are created  
4) Login using credentials after authentication

**Measure of Success:**  
Users will receive an email or code through the application’s account authentication feature and successfully create an account.

**Results: Unable to login to a seemingly created account. After signing up, an error occurred, but would not allow signing with the same email address. Sign In page recognized when the password was incorrect, but when the correct password was entered it returned an Error page.**

**Test Number:** 16  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 3.0  
**Test Purpose:** This test is to test the application’s handling of invalid file uploads.  
**Test Procedures:** 

1) Open the application with a web browser (specified within section 6 of this document)  
2) Login to any account with uploading permissions  
3) Select “upload”  
4) Go through the process of uploading a file to the database, choose an “invalid” file with deliberate errors  
5) Select “visible to students” and “visible to public”  
6) Upload the file  
7) Verify how the invalid file was handled (is it in the database? is it visible to all users?)

**Measure of Success:**  
The invalid file should not be uploaded to the database at all and an error message should have appeared indicating that the file is invalid. The file should not be visible anywhere by any account type.

**Results: Unable to login to a seemingly created account. After signing up, an error occurred, but would not allow signing with the same email address. Sign In page recognized when the password was incorrect, but when the correct password was entered it returned an Error page.**

**Test Number:** 17  
**Author:** QA Team  
**Date:** September 14, 2022  
**Revision:** 2.0  
**Test Purpose:** This test is to test the application’s About page.  
**Test Procedures:** 

1) Open the application with a web browser (any specified within section 6 of this document)  
2) Login to any account type  
3) Select “About” located at the top of the web page  
4) Verify that About page contents are visible/legible

**Measure of Success:**  
The CD Spec’s about page should be displayed properly, containing all information about the application for the viewer’s understanding.

Results: Unable to log in but the about page does load and is legible, not very visually pleasing though.