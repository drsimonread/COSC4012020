

| Circular Dichroism Spectrometer  Software Test Results 401 Quality Assurance & Documentation Team |
| :---- |

---

 

**Test Number:**  LEG \- 01  
**Author:** QA Team  
**Date:**November/30/2022  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the user registration and login menus.  
**Test Procedures:**

1) A user with public level access will be added to the database through the registration page.  
2) The team will attempt to log in using the newly created account’s credentials. Each account will be logged in multiple times to ensure that it persists in the database’s memory.  
3) More accounts of the same access level will be created and logged in with to ensure that the database is capable of properly registering multiple users.  
4) Steps 1 through 3 will then be repeated with student access level and administrator access level accounts.

**Measure of Success:**  
All accounts should be able to use it for login, taking the user to the home page once the login is completed.

**Results:**  Attempted to register an account using a gmail account. An account was created and a screen to verify your email address was displayed on docker site mimicking an email sent allowing verification.

**Test Number:** LEG-02  
**Author:** QA Team  
**Date:** November/30/2022  
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

**Results:**  Was able to reset Password.

**Test Number:** LEG-03  
**Author:** QA Team  
**Date:** November/30/2022  
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

**Measure of Success:**  
The application should be opened successfully on various web browsers.

**Results:** Google Chrome works,  Mozilla FireFox: Page Not Found, Microsoft Edge: Page Not Found,  

**Test Number:** LEG-04  
**Author:** QA Team  
**Date:** December 5, 2022  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the data upload function.  
**Test Procedures:**

1) Open the application with a web browser  
2) Login to account  
3) Select “upload”  
4) Select data file to upload  
5) Upload the file, confirm that the file has successfully been uploaded by the application 

**Measure of Success:** The data file has been successfully uploaded to the database and can be accessed.  
**Results:**  Unable to find the “Upload” button. Assuming it is located in the “Index” tab which is not accessible in the VM. \- Gavin

**Test Number:** LEG- 05  
**Author:** QA Team  
**Date:** December 5, 2022  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the search engine.  
**Test Procedures:**

1) Open the application with a web browser  
2) Login to account  
3) Select “search”  
4) Enter the desired file in the text field as well as any specifics (date, uploader, etc…)  
5) Click “enter” (confirm)

**Measure of Success:** The data file in the database that was searched for will be located and viewable by the user.  
**Results:**  Unable to find the “Search” button/bar. Assuming it is located in the “Index” tab which is not accessible in the VM. \- Gavin

**Test Number:** LEG-06  
**Author:** QA Team  
**Date:** December 5, 2022  
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
**Results:**  Admin Account does not currently exist, unable to test. \- Gavin

**Test Number:** LEG-07  
**Author:** QA Team  
**Date:** December 5, 2022  
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

**Results:**  Student account that did not post the data was unable to delete or change data in the database.

**Test Number:** LEG-08  
**Author:** QA Team  
**Date:** December 5, 2022  
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
**Results:**  Public account allowed the viewing of data but no uploading or editing files.

**Test Number:** LEG-09  
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
**Results:**  Unable to make a student account without manually adding student privileges to an account within the database. 

**Test Number:** LEG-10  
**Author:** QA Team  
**Date:** December 5th, 2022  
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

**Results:**  Unable to upload a data file as a student: “You do not have permission to upload”

**Results:** Uploaded as an Administrator, character counter did not prevent a description of size 2500, despite limit being stated as 2000\.

**Test Number:** LEG-11  
**Author:** QA Team  
**Date:** December 5th, 2022  
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

**Result:**  
Results: Multi graphs are able to be changed within a color selector, and project the correct color to the graph

**Test Number:** LEG-12  
**Author:** QA Team  
**Date:** December 5th, 2022  
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
**Results:** Downloaded “cdspecruns/Protein\_and\_ZnCl2\_Molar\_Ellipticity\_.csv” successfully on student account

\-

**Test Number:** LEG-13  
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

**Results**: The admin abilities are successful.

**Test Number:** LEG-14  
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

**Results:** Student account was successfully able to graph three variables.

**Test Number:** LEG-15  
**Author:** QA Team  
**Date:** 12/05/2022  
**Revision:** 2.0  
**Test Purpose:** This test is to test the functionality of account authentication and permissions  
**Test Procedures:** 

1) Open the application with a web browser (any specified within section 6 of this document)  
2) Follow the steps to creating a new user account  
3) Follow authentication procedures once login credentials are created  
4) Login using credentials after authentication

**Measure of Success:**  
Users will receive an email or code through the application’s account authentication feature and successfully create an account.

**Results:** Credential verification was successful

**Test Number:** LEG-16  
**Author:** QA Team  
**Date:** December 05, 2022  
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

**Results:** As a student user with upload permissions, I attempted to upload a .py file and was successfully denied. 

**Test Number:** LEG-17  
**Author:** QA Team  
**Date:** December 05, 2022  
**Revision:** 2.0  
**Test Purpose:** This test is to test the application’s About page.  
**Test Procedures:** 

1) Open the application with a web browser (any specified within section 6 of this document)  
2) Login to any account type  
3) Select “About” located at the top of the web page  
4) Verify that About page contents are visible/legible

**Measure of Success:**  
The CD Spec’s about page should be displayed properly, containing all information about the application for the viewer’s understanding.

**Results:** Once R\&D manually approved my account, able to navigate to correctly displayed about page with lowest level permissions..

**Test Number:** SYS-01  
**Author:** Eythan Jenkins  
**Date:** December 05, 2022  
**Revision:** 1.0  
**Test Purpose:** To test the login functionality via the Google log-in option as a Public User  
**Test Procedures:**

1) User will navigate to the SMCM CD Spectrometer website.  
2) The user will select the “Sign in” option at the banner on the top of the webpage.  
3) The user will arrive to the sign-in page, and select the blue hyperlink labeled “Google.”  
4) The user will arrive to Google’s ‘oauth’ log-in, and select a Google Account not associated with the school.  
5) The user should be denied access to logging in and not be able to proceed as a logged-in user.

**Measure of Success:**  
The user should not be able to access the CD Spec with a Google account not associated with the school.

**Results:** Successfully Denied Google login from outside account

**Test Number:** SYS-02  
**Author:** Eythan Jenkins, [Mathias Boddicker](mailto:mboddicker@smcm.edu)  
**Date:** December 05, 2022  
**Revision:** 1.0  
**Test Purpose:** To test the login functionality via the Google log-in option as a Student User  
**Test Procedures:**

1) User will navigate to the SMCM CD Spectrometer website.  
2) The user will select the “Sign in” option at the banner on the top of the webpage.  
3) The user will arrive to the sign-in page, and select the blue hyperlink labeled “Google.”  
4) The user will arrive to Google’s ‘oauth’ log-in, and select their Google Account associated with the school.  
5) The user should be able to log into the CD Spec as a student account

**Measure of Success:**  
The user will be able to log in to their student account.

**Results:** Successfully Denied Google login from outside account

**Test Number:** SYS-03  
**Author:** Eythan Jenkins, Mathias Boddicker  
**Date:** December 05, 2022  
**Revision:** 1.0  
**Test Purpose:** To test the login functionality via the Google log-in option as a Admin User  
**Test Procedures:**

1. User will navigate to the SMCM CD Spectrometer website.  
2. The user will select the “Sign in” option at the banner on the top of the webpage.  
3. The user will arrive to the sign-in page, and select the blue hyperlink labeled “Google.”  
4. The user will arrive to Google’s ‘oauth’ log-in, and select their Google Account associated with the school.  
5. The user should be able to log into the CD Spec as an administrator account  
   

**Measure of Success:**  
The user will be able to log in to their administrator account.

**Results:** Successfully Denied Google login from outside account  
