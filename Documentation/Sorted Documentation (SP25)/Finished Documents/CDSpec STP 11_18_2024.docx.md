

| Circular Dichroism Spectrometer Software Test Plan Version 1.3 11-18-24 402 Quality Assurance & Documentation Team    |
| ----- |

**Table of Contents**

[**1\. Introduction**](#1.-introduction)	**[1](#1.-introduction)**

[1.1 Purpose](#1.1-purpose)	[1](#1.1-purpose)

[1.2 Scope](#1.2-scope)	[1](#1.2-scope)

[1.3 Definitions, Acronyms, and Abbreviations](#1.3-definitions,-acronyms,-and-abbreviations)	[1](#1.3-definitions,-acronyms,-and-abbreviations)

[1.4 Document References](#1.4-document-references)	[1](#1.4-document-references)

[1.5 System Overview](#1.5-system-overview)	[1](#1.5-system-overview)

[**2\. Requirements to Be Tested**](#2.-requirements-to-be-tested)	**[2](#2.-requirements-to-be-tested)**

[**3\. Testing Approach**](#3.-testing-approach)	**[2](#3.-testing-approach)**

[3.1 White Box Testing](#3.1-white-box-testing)	[2](#3.1-white-box-testing)

[3.2 Black Box Testing](#3.2-black-box-testing)	[2](#3.2-black-box-testing)

[**4\. Test Process**](#4.-test-process)	**[3](#4.-test-process)**

[4.1 Unit Testing](#4.1-unit-testing)	[3](#4.1-unit-testing)

[4.2 System Testing](#4.2-system-testing)	[3](#4.2-system-testing)

[**5\. Reporting and Corrective Action**](#5.-reporting-and-corrective-action)	**[3](#5.-reporting-and-corrective-action)**

[**6\. Test Environment**](#6.-test-environment)	**[3](#6.-test-environment)**

[6.1 Unit Testing Environment](#6.1-unit-testing-environment)	[3](#6.1-unit-testing-environment)

[6.2 System Testing Environment](#6.2-system-testing-environment)	[3](#6.2-system-testing-environment)

[**7\. Test Procedures**](#7.-test-procedures)	**[3](#7.-test-procedures)**

[7.1 Tests](#heading=h.z337ya)	[8](#heading=h.1y810tw)

**Revision History**

| Date | Version | Description | Author(s) |
| :---: | :---: | :---: | :---: |
|  10/23/2022 | 1.0  | Created STP Template | Eythan Jenkins |
| 11/9/2022 | 1.1 | Added Legacy, Unit, and System Test Bases | Eythan Jenkins, CD Spec QA Team |
| 02/08/2023 | 1.2 | Updated document | CD Spec QA Team |
| 11/18/2024 | 1.3 | Updated Test Procedures | Michael Shively |

# **1\. Introduction** {#1.-introduction}

## **1.1 Purpose** {#1.1-purpose}

The purpose of this Software Test Plan (STP) is to define all testing procedures that shall be implemented in the testing of the Circular Dichroism Spectrometer (CD Spec) application.

## **1.2 Scope** {#1.2-scope}

The purpose of this STP document is to detail any and all test cases associated with the CD Spec application. All plans and specific steps that will be taken during the testing process shall be documented here. This document will be utilized by both the Research and Development (R\&D) and Quality Assurance (Q\&A) teams to test all possible cases within the scope of the CD Spec application.

## **1.3 Definitions, Acronyms, and Abbreviations** {#1.3-definitions,-acronyms,-and-abbreviations}

| CD Spec | Circular Dichroism Spectrometer |
| :---- | :---- |
| Q\&A | Quality Assurance |
| R\&D | Research and Development |
| SRS STP UM | Software Requirements Specification Software Test Plan User Management |
|  |  |
|  |  |

## **1.4 Document References** {#1.4-document-references}

## **1.5 System Overview** {#1.5-system-overview}

The Circular Dichroism Spectrometer (CD Spec Spec) software shall be a functional database housed within a constructed web application. This software shall be utilized by both instructors and students to monitor spectral changes in structure between protein-DNA interactions. Users of this web application shall be able to create three forms of user accounts. These accounts include a public user account, a student user account, and an administrator account, each of which have specific abilities assigned to them as well as some limitations imposed. A public user account may only view protein-DNA data submitted by account types with more permissions. Public accounts may not edit data in any way or submit data themselves. A student user account may view and submit protein-DNA data. Once submitted, the student account may not edit the data in any way. An administrator account has full permissions, meaning that this account type may perform all functions of the database, including: viewing the data within the database, uploading and submitting of user data, as well as editing of any data contained within the database. 

---

# **2\. Requirements to Be Tested** {#2.-requirements-to-be-tested}

Requirements to be tested are defined within the Software Requirements Specifications (SRS) document, currently at version 3.0. The SRS shall be updated in future to reflect any changes made by the client or the Research and Development team over the course of this project’s duration.

\-Login (SRS 2.1.1)  
\-User Creation (SRS 2.2)  
\-Password Recovery (SRS 2.3)  
\-Page Navigation  
\-Database Search Engine (SRS 2.5.2)  
\-Data Comparison (SRS 2.5.4)  
\-Data Upload (SRS 2.5.5)  
\-Data Editing (SRS 2.5.5.1)

---

# **3\. Testing Approach** {#3.-testing-approach}

## **3.1 White Box Testing** {#3.1-white-box-testing}

* Database functionality

## **3.2 Black Box Testing** {#3.2-black-box-testing}

Members of the CD Spec team shall test the functionality of the CD Spec application. The team will test all possible requirements that have been implemented into the application. Tests will include higher priority/core functions such as:

* Application Access (in various testing environments/browsers)  
* Account Creation  
* Data Search  
* Data Upload, valid and invalid files  
* Data Graphing


---

# **4\. Test Process** {#4.-test-process}

## **4.1 Unit Testing**   {#4.1-unit-testing}

Testers will test each function of the CD Spec application individually to ensure that they function correctly. Unit testing is the first stage of testing and will be done to ensure that the next stage of testing, the integration stage, can combine the pieces of the program together into a more finalized product. Unit testing will be done primarily to ensure that the application is able to at least run and display the implemented interfaces.

## **4.2 System Testing** {#4.2-system-testing}

The application at this stage will be tested within different testing environments by several different members of the team. The application must function in different web browsers as well as by different users.

---

# **5\. Reporting and Corrective Action** {#5.-reporting-and-corrective-action}

Errors found will be recorded on the error log document. The errors will then be directly reported to the development team as well as the project leader. From there the QA team will work on finding and reporting more errors while the development team resolves the errors that we have reported.

---

# **6\. Test Environment** {#6.-test-environment}

## **6.1 Unit Testing Environment** {#6.1-unit-testing-environment}

Unit Testing shall be performed using Docker container to ensure all dependencies needed for the software are present.

## **6.2 System Testing Environment** {#6.2-system-testing-environment}

System testing environment shall be performed in a browser or multiple browsers as specified by the tests that are being performed.  
---

# **7\. Test Procedures** {#7.-test-procedures}

Title: Login Screen  
Number: 2.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.1 in the CD Spec SRS.  
Procedures:

1. Open the application.

Measure of Success: The login page is displayed.  
Date:   
Result:   
Notes:  
Comments: 

Title: Account Creation  
Number: 2.1.1.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.1.1.1 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.

Measure of Success: There is an account creation option present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Enter Login  
Number: 2.1.1.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.1.1.2 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.

Measure of Success: There is an area to enter login information.  
Date:   
Result:   
Notes:  
Comments: 

Title: Login Retry  
Number: 2.1.1.3  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.1.1.3 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter an incorrect login.  
3. Enter login information again.

Measure of Success: The program allows the login information to be entered a second time.  
Date:   
Result:   
Notes:  
Comments: 

Title: Forgot Password Button  
Number: 2.1.1.4  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.1.1.4 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.

Measure of Success: There is a “forgot password” button present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Help Option  
Number: 2.1.1.5  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.1.1.5 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.

Measure of Success: There is a “help” option present.  
Date:   
Result:   
Notes:  
Comments: 

Title: User Creation Page  
Number: 2.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.2 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the account creation option.

Measure of Success: A user creation page is presented.  
Date:   
Result:   
Notes:  
Comments: 

Title: Login Credentials  
Number: 2.2.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.2.1 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the account creation option.

Measure of Success: A user interface for login credentials is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Creation Key  
Number: 2.2.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.2.2 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the account creation option.

Measure of Success: A key for student and admin account creation is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Password Confirmation  
Number: 2.2.3  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.2.3 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the account creation option.

Measure of Success: There is a password confirmation section present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Forgot Password Page  
Number: 2.3  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.3 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the “forgot password” button.

Measure of Success: A “forgot password” page is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Email Account Submission  
Number: 2.3.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.3.1 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the “forgot password” button.

Measure of Success: An email account submission block is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Forgot Password Email  
Number: 2.3.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.3.2 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the “forgot password” button.  
3. Enter email address.

Measure of Success: A screen showing that a forgot password email was sent is present below the email account submission block.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.4  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.4 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the “help” option.

Measure of Success: A “help” page is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Help Information  
Number: 2.4.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.4.1 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Select the “help” option.

Measure of Success: Information about how to use the CD Spec database is present.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct login.

Measure of Success: A “home” page is present.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.1 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title: Search Bar  
Number: 2.5.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.2 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct login.

Measure of Success: A search bar is present.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5.3  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.3 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct login.  
3. Select the “about” button.

Measure of Success: The “about” page is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Compare Contrast Button  
Number: 2.5.4  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.4 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct login.

Measure of Success: There is a “compare contrast” button present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Choosing Parameters  
Number: 2.5.4.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.4.1 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct login.

Measure of Success: A way to choose the parameters for comparison on graphical representations is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Graphical Representations  
Number: 2.5.4.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.4.2 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct login.  
3. Select the “compare contrast” button.

Measure of Success: The application shall create a proper graphical representation using practical numbers for the X & Y axis.  
Date:   
Result:   
Notes:  
Comments: 

Title: Z-Axis  
Number: 2.5.4.3  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.4.3 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct login.  
3. Select the “compare contrast” button.

Measure of Success: The application shall create a graphical representation of a third Z-axis, displaying temperature information.  
Date:   
Result:   
Notes:  
Comments: 

Title: Upload Button  
Number: 2.5.5  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.5 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct admin login.  
3. Select the “upload” button.

Measure of Success: An “upload” page is present.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5.5  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.5 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title: Edit/Create Data Button  
Number: 2.5.5.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.5.1 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct admin login.  
3. Select the “upload” button.

Measure of Success: There is a “edit/create data” button present.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5.5.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.5.1 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:   
Date:   
Result:   
Notes:  
Comments: 

Title: Description Box (1)  
Number: 2.5.5.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.5.2 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct admin login.  
3. Select the “upload” button.  
4. Select the “edit/create data” button.

Measure of Success: A description box is present.  
Date:   
Result:   
Notes:  
Comments: 

Title: Description Box (2)  
Number: 2.5.5.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.5.2 in the CD Spec SRS.  
Procedures:

5. Navigate to the login page.  
6. Enter a correct admin login.  
7. Select the “upload” button.  
8. Select the “edit/create data” button.  
9. Enter 2001 characters into the description box.

Measure of Success: A description box does not allow the two thousand and first character to be entered.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5.6.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.6.1 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5.6.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.6.2 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.5.6.3  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.5.6.3 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title: CSV Upload  
Number: 2.6.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.6.1 in the CD Spec SRS.  
Procedures:

1. Navigate to the login page.  
2. Enter a correct admin login.  
3. Select the “upload” button.  
4. Upload a CSV File

Measure of Success: The file uploaded successfully.  
Date:   
Result:   
Notes:  
Comments: 

Title: Text File Upload  
Number: 2.6.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.6.1 in the CD Spec SRS.  
Procedures:

5. Navigate to the login page.  
6. Enter a correct admin login.  
7. Select the “upload” button.  
8. Upload a Text File

Measure of Success: The file uploaded successfully.  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.6.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.6.2 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.7  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.7 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.7.1  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.7.1 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.7.2  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.7.2 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

Title:   
Number: 2.7.3  
Version: 1.0  
Classification: N/A  
Author: Michael Shively  
Purpose: To test requirement 2.7.3 in the CD Spec SRS.  
Procedures:

1. 

Measure of Success:  
Date:   
Result:   
Notes:  
Comments: 

---

# **8\. Miscellaneous**:  

