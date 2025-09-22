

| Circular Dichroism Spectrometer  Software Test Plan Version 2.0 02-15-21 402 Quality Assurance & Documentation Team |
| :---- |

---

**Table of Contents**

**Revision History**

| Date | Version | Description | Author(s) |
| ----- | ----- | ----- | ----- |
| 10/22/20  | 1.0 | Software Test Plan First Release  | Annette Orr, Braden Clough, Cameron Carpenter, Edward Park |
|  2/15/21 |  2.0 |  Software Test Plan Updated Release |  Annette Orr, Christopher Beatrez, Faith Meyer, Edward Park  |
|   |   |   |   |

---

**1\. Introduction**

**1.1 Purpose**

The purpose of this Software Test Plan (STP) is to define all testing procedures that shall be implemented in the testing of the Circular Dichroism Spectrometer (CD Spec) application.

**1.2 Scope**

The purpose of this STP document is to detail any and all test cases associated with the CD Spec application. All plans and specific steps that will be taken during the testing process shall be documented here. This document will be utilized by both the Research and Development (R\&D) and Quality Assurance (Q\&A) teams to test all possible cases within the scope of the CD Spec application.

**1.3 Definitions, Acronyms, and Abbreviations**

* CD Spec: Circular Dichroism Spectrometer  
* Q\&A: Quality Assurance  
* R\&D: Research and Development  
* SRS: Software Requirements Specifications  
* STP: Software Test Plan

**1.4 Document References**

* SRS, v1.0 released 9/17/20

**1.5 System Overview**

The Circular Dichroism Spectrometer (CD Spec Spec) software shall be a functional database housed within a constructed web application. This software shall be utilized by both instructors and students to monitor spectral changes in structure between protein-DNA interactions. Users of this web application shall be able to create three forms of user accounts. These accounts include a public user account, a student user account, and an administrator account, each of which have specific abilities assigned to them as well as some limitations imposed. A public user account may only view protein-DNA data submitted by account types with more permissions. Public accounts may not edit data in any way or submit data themselves. A student user account may view and submit protein-DNA data. Once submitted, the student account may not edit the data in any way. An administrator account has full permissions, meaning that this account type may perform all functions of the database, including: viewing the data within the database, upload and submitting of user data, as well as editing of any data contained within the database. 

This CD Spec software shall perform calculations within the backend in order to monitor changes and differences between the data within the database.

---

**2\. Requirements to Be Tested**

Requirements to be tested are defined within the Software Requirements Specifications (SRS) document, currently at version 1.0. The SRS shall be updated in future to reflect any changes made by the client or the Research and Development team over the course of this project’s duration.

* Account Login (SRS v1.0, 2.1.1)  
* User Creation (SRS v1.0,  2.2)  
* Password Recovery (SRS v1.0,  2.3)  
* Database Search Engine (SRS v1.0,  2.5.2)  
* Data Comparison (SRS v1.0,  2.5.4)  
* Data Upload (SRS v1.0,  2.5.5)  
* Data Editing (SRS v1.0,  2.5.5.1)

---

**3\. Testing Approach**

The CD Spec Q\&A team will individually be assigned testing procedures to test the functionality of the CD Spec application. Testing will be done in multiple environments and will be done according to the test process as defined in section 4 of this document. The core functions of the CD Spec application will be tested, including but not limited to the requirements as defined in the Software Requirements Specifications document, version 1.0 at present. 

* Uploading valid data to the database  
* Uploading invalid data to the database  
* Searching for data in the database  
* Creating a student account  
* Creating an administrator account  
* Creating a public account  
* Viewing data on all account types  
* Error handling

---

**4\. Test Process**

CD Spec Quality Assurance team is responsible for performing four types of tests: unit, integration, validation, and system.

Unit Testing: Members of the CD Spec Quality Assurance team will ensure that the application will function efficiently and correctly. Unit testing is the first phase of testing done to ensure that various pieces of the application function together into a finalized product. This phase is primarily done to ensure the application will execute, run, and display the implemented code and interfaces. 

Integration Testing:  Integration testing follows after the Unit Testing phase of the testing process. After the Quality Assurance team has verified the application is functional and running as expected then the interface is further polished and tested for a smoother navigation of the application. 

Validation Testing: Validation testing makes up a large part of the testing process. Most of section 6 are validation tests and conducted by the test team. Each of these will be correlated with an existing requirement as described in Section 2\. The goal of these are to ensure that all functional behavior of the software fills the requirements detailed in the SRS sufficiently.

System Testing: This phase of the testing process is to ensure that the application is compatible and capable of performing on various systems. The application will be run on various computing platforms as well as web browsers to ensure that a variety of users can utilize the application.   
---

**5\. Reporting and Corrective Action**

Any errors that have been found by the Quality Assurance team will be reported and recorded to an error log document. These errors will be communicated directly to the Research and Development team to fix any issues the application may be having or solving any unforeseen issues. The Quality Assurance team members will continuously monitor the application to ensure that the application runs into the least amount of errors as possible. Any errors found will be immediately reported to the Research & Development team and a solution will be made.

---

**6\. Test Environment**

Testing Environment 01:   
**Model:** Intel(R) Core(™) i5-9400F   
**Processing Unit:** i5-9400 6-Core processing unit  
**Graphics:** NVIDIA GeForce GTX 1660  
**RAM:** 24 GB DDR4  
**OS:** Windows 10  
**Kernel Version:** 10.0.19041  
**Storage:**  111 GB SSD/931 GB HDD

Testing Environment 02:  
**Processor:** Intel(R) Core(™) i7-9750H   
**Graphics Card:** RTX 2060 Mobile  
**RAM:** 16GB  
**OS:** Windows 10  
**Software:** Docker Desktop

Testing Environment 03:

**CPU**: Intel i7 8700k

**GPU**: Titan XP Star Wars Edition

**RAM**: 32 GB DDR4 

**OS**: Windows 10

**Software**: Docker Desktop

Testing Environment 04:

**Model**: Intel(R) Core(™) i5-6600K CPU

**Graphics**: NVIDIA GeForce 980 x2

**OS**: Windows 10

**RAM**: 16 GB

**Storage**: 1.80 TB

**Software**: Docker Desktop

Browser Environments

Testing Environment 05: Google Chrome

Testing Environment 06: Mozilla Firefox

Testing Environment 07: Microsoft Edge

Testing Environment 08: Safari (iOS)

Testing Environment 09: Internet Explorer

---

**7\. Test Procedures**

**Test Number:** 01  
**Author:** Q\&A Team  
**Date:** October 22, 2020  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the user registration and login menus.  
**Test Procedures:**

1) A user with public level access will be added to the database through the registration page.  
2) The team will attempt to log in using the newly created account’s credentials. Each account will be logged in multiple times to ensure that it persists in the database’s memory.  
3) More accounts of the same access level will be created and logged in with to ensure that the database is capable of properly registering multiple users.  
4) Steps 1 through 3 will then be repeated with student access level and administrator access level accounts.

**Measure of Success:**  
All accounts should be able to use for login, taking the user to the home page once the login is completed.

**Test Number:** 02  
**Author:** Q\&A Team  
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

**Test Number:** 03  
**Author:** Q\&A Team  
**Date:** October 27, 2020  
**Revision:** 1.0  
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

**Test Number:** 05  
**Author:** Q\&A Team  
**Date:** October 27, 2020  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the data upload function.  
**Test Procedures:**

1) Open the application with a web browser  
2) Login to account  
3) Select “upload”  
4) Select data file to upload  
5) Upload the file, confirm that the file has successfully been uploaded by the application 

**Measure of Success:** The data file has been successfully uploaded to the database and can be accessed.

**Test Number:** 06  
**Author:** Q\&A Team  
**Date:** October 27, 2020  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of the search engine.  
**Test Procedures:**

1) Open the application with a web browser  
2) Login to account  
3) Select “search”  
4) Enter the desired file in the text field as well as any specifics (date, uploader, etc…)  
5) Click “enter” (confirm)

**Measure of Success:** The data file in the database that was searched for will be located and viewable by the user.

**Test Number:** 07  
**Author:** Q\&A Team  
**Date:** October 27, 2020  
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

**Test Number:** 08  
**Author:** Q\&A Team  
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

**Test Number:** 09  
**Author:** Q\&A Team  
**Date:** October 27, 2020  
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

**Test Number:** 10  
**Author:** Q\&A Team  
**Date:** October 27, 2020  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test the functionality of student account creation (by admin).  
**Test Procedures:**

1) Open the application in a web browser  
2) Login to an administrator account  
3) Go through the steps to set up a new student account  
4) Logout of administrator account  
5) Login to new student account  
6) Confirm that the new student account has been created successfully 

**Measure of Success:**  
A CD Spec student account has successfully been created by a CD Spec administrator account and can be accessed.

**Test Number:** 11  
**Author:** Q\&A Team  
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

**Test Number:** 12  
**Author:** Q\&A Team  
**Date:** 2/17/2021  
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

**Test Number:** 13  
**Author:** Q\&A Team  
**Date:** 2/17/2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to test the functionality of graph image downloading  
**Test Procedures:**

1) Open the application in a web browser  
2) Login to an account  
3) Open any graph  
4) Press the download button  
5) Confirm graph has been successfully downloaded

**Measure of Success:**  
Graphs will be downloaded and saved onto a user’s hard drive

**Test Number:** 14  
**Author:** Q\&A Team  
**Date:** 2/17/21  
**Revision:** 2.0  
**Test Purpose:** The purpose of this test is to test the capabilities of the administrator level account.  
**Test Procedures:**

1) Open the application with a web browser (any specified within section 6 of this document)  
2) Login to an administrator account  
3) Select “upload”, upload a data file to the database  
4) Go back to homepage  
5) Select “search”  
6) Enter a file’s information to search, locate a file  
7) Select “delete”, delete a file from the database, confirm that the delete ability is functional  
8) Verify that admin abilities are fully functional and unique to the administrator account

**Measure of Success:**  
The uploaded file has been successfully deleted from the database by the administrator and is no longer visible by any account.

**Test Number:** 15  
**Author:** Q\&A Team  
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

**Test Number:** 16  
**Author:** Q\&A Team  
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

**Test Number:** 17  
**Author:** Q\&A Team  
**Date:** 2/17/2021  
**Revision:** 2.0  
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

**Test Number:** 18  
**Author:** Q\&A Team  
**Date:** 2/17/2021  
**Revision:** 2.0  
**Test Purpose:** This test is to test the application’s About page.  
**Test Procedures:** 

1) Open the application with a web browser (any specified within section 6 of this document)  
2) Login to any account type  
3) Select “About” located at the top of the web page  
4) Verify that About page contents are visible/legible

**Measure of Success:**  
The CD Spec’s about page should be displayed properly, containing all information about the application for the viewer’s understanding.

---

**8\. Miscellaneous**

None  
---

