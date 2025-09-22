

|  Point of Sale System for Pizza Paradise Software Test Plan Version 2.3 11-22-2021  ![][image1]\[TEAM NAME\] \[Team Members\]   |
| ----- |

**Table of Contents**

[**1\. Introduction**](#1.-introduction)	**[1](#1.-introduction)**

[1.1 Purpose](#1.1-purpose)	[1](#1.1-purpose)

[1.2 Scope](#1.2-scope)	[1](#1.2-scope)

[1.3 Definitions, Acronyms, and Abbreviations](#1.3-definitions,-acronyms,-and-abbreviations)	[2](#1.3-definitions,-acronyms,-and-abbreviations)

[1.4 Document References](#1.4-document-references)	[3](#1.4-document-references)

[1.5 System Overview](#1.5-system-overview)	[4](#1.5-system-overview)

[**2\. Requirements to Be Tested**](#2.-requirements-to-be-tested)	**[4](#2.-requirements-to-be-tested)**

[**3\. Testing Approach**](#3.-testing-approach)	**[5](#3.-testing-approach)**

[3.1 White Box Testing](#3.1-white-box-testing)	[5](#3.1-white-box-testing)

[3.2 Black Box Testing](#3.2-black-box-testing)	[5](#3.2-black-box-testing)

[**4\. Test Process**](#4.-test-process)	**[5](#4.-test-process)**

[4.1 Unit Testing](#4.1-unit-testing)	[5](#4.1-unit-testing)

[4.2 Integration Testing](#4.2-integration-testing)	[5](#4.2-integration-testing)

[4.3 Validation Testing](#4.3-validation-testing)	[6](#4.3-validation-testing)

[4.4 System Testing](#4.4-system-testing)	[6](#4.4-system-testing)

[**5\. Reporting and Corrective Action**](#5.-reporting-and-corrective-action)	**[6](#5.-reporting-and-corrective-action)**

[**6\. Test Environment**](#6.-test-environment)	**[6](#6.-test-environment)**

[6.1 Unit Testing Environment](#6.1-unit-testing-environment)	[6](#6.1-unit-testing-environment)

[6.2 Integration Testing Environment](#6.2-integration-testing-environment)	[6](#6.2-integration-testing-environment)

[6.3 Validation Testing Environment](#6.3-validation-testing-environment)	[7](#6.3-validation-testing-environment)

[6.4 System Testing Environment](#6.4-system-testing-environment)	[7](#6.4-system-testing-environment)

[**7\. Test Procedures**](#7.-test-procedures)	**[7](#7.-test-procedures)**

[7.1 Functional Tests](#7.1-functional-tests)	[7](#7.1-functional-tests)

[7.1.1 User Management Tests](#7.1.1-user-management-tests)	[8](#7.1.1-user-management-tests)

[7.1.1.1 User Management Integration Tests](#7.1.1.1-user-management-integration-tests)	[15](#7.1.1.1-user-management-integration-tests)

[7.1.2 Placing Orders Tests](#7.1.2-placing-orders-tests)	[16](#7.1.2-placing-orders-tests)

[7.1.2.1 Placing Orders Integration Tests](#7.1.2.1-placing-orders-integration-tests)	[20](#7.1.2.1-placing-orders-integration-tests)

[7.1.3 Print Receipt Tests](#7.1.3-print-receipt-tests)	[24](#7.1.3-print-receipt-tests)

[7.1.4  Prices Test](#7.1.4-prices-test)	[28](#7.1.4-prices-test)

[7.1.5 Software Start Up Tests](#7.1.5-software-start-up-tests)	[39](#7.1.5-software-start-up-tests)

[7.2 Other Tests](#7.2-other-tests)	[40](#7.2-other-tests)

[8\. Miscellaneous](#8.-miscellaneous)	[41](#8.-miscellaneous)

**Revision History**

| Date | Version | Description | Author(s) |
| :---: | :---: | :---: | :---: |
|  10/29/2021 | 1.0  | Test procedures and preliminary sections have been initiated.   | xx |
| 10/30/2021  | 1.1  | A test procedure has been written. A traceability matrix has been created. | xx  |
| 11/1/2021  | 1.2  | A preliminary section (environments) has been written.  | xx |
| 11/3/2021 | 1.3 | A test procedure has been written. | xx |
| 11/7/2021 | 1.4 | Team members have been discussing test procedures; test procedures are being written. | xx |
| 11/8/2021 | 1.5 | Integration tests POI 1 through 4 written. POI acronym made. | xx |
| 11/9/2021 | 1.6 | Printing receipts (PR) tests have been written.  | xx |
| 11/10/2021 | 1.7 | Final edits before submission is made. | xx |
| 11/17/2021 | 2.0 | Uploaded STP with comments, and necessary edits. | xx |
| 11/20/2021 | 2.1 | Started some necessary edits: testing numbers no longer in table of contents (format correction). Edited UM-217. | xx |
| 11/21/2021 | 2.2 | Completed Document Procedure edits authored by xx. Advanced edits in sections prior to section 7\. Added DxDiag for xx’ Specifications | xx |
| 11/21/2021 | 2.2.1 | Section 2 edits completed. User persistence test created. All xx’s procedures edited, except one (need to consult about). | xx |
| 11/22/2021 | 2.3 | Finalized edits. | xx |

# **1\. Introduction** {#1.-introduction}

## **1.1 Purpose** {#1.1-purpose}

The purpose of this document is to formally state the procedures to be used for testing the software product and identify specific test cases. It can also be used to ensure all requirements are being met by matching each test case to the respective requirements in the SRS. Test cases are numbered with the section number they are from for this purpose. Furthermore, which sections of the software will not be explicitly tested will be stated, as well as procedures for non-software matters, such as performance will be accounted for.

There also exist ancillary purposes within this Software Test Plan (STP) document. It will contain an abstract of what will be included within our test procedures, as well as outline the approach for testing. The document will also highlight how unit, integration, validation, and system testing will proceed, as well as their respective environments.

Some minor purposes of this STP document include how reporting and corrective action will be carried out, in addition to other miscellaneous topics which may not be exclusive to this document (i.e. the Github repository).

## **1.2 Scope** {#1.2-scope}

This document contains specific test cases to be conducted by testers. Each procedure is a step by step guide with a pass or fail criteria. The results determined by the testers using this document will be later used for debugging purposes. The following are areas within this STP’s scope:

* Requirements to be tested: an abstract of what will be tested in this document.  
* Testing approach: Testing will be conducted via white box and black box procedures.  
* Test Process: Outlines how Unit, Integration, Validation, and System Testing will proceed with the software.  
* Reporting and Corrective Action: Outlines group communication for the aforementioned.  
* Test Environment: Outlines the Unit, Integration, Validation, and System Testing Environments.  
* Test Procedures: Contains and outlines step-by-step all of the test procedures which will be conducted on the software.  
* Miscellaneous: Licensing and Github repository for code.

## **1.3 Definitions, Acronyms, and Abbreviations** {#1.3-definitions,-acronyms,-and-abbreviations}

| CPU DES GUI IDE OS PIN PiOS PiPa PO POI POS PF PR PT | Central Processing Unit Design Graphical User Interface Integrated Development Environment Operating System Personal Identification Number Pioneers of Software Pizza Paradise Placing Orders Placing Orders Integration Point of Sale Performance Printing Receipts Pricing Test |
| :---- | :---- |
| SRS SSU STP UM | Software Requirements Specification System Startup Software Test Plan User Management |
|  |  |

## **1.4 Document References** {#1.4-document-references}

“SRS for PiPa POS Mark II” (Version 2.0.4, 10-25-2021, *Pioneers of Software*): This is our most recent edition of our software specifications. It should be used to decide which requirements will be tested, as well as how they will be tested. The “SRS for PiPa POS Mark II” can be retrieved within the group-shared ‘Software Engineering Project’ Google Drive, as a document entitled by the same name. The hyperlink: 

“Test to Requirements traceability matrix” (Version 1.0, 10-30-2021, Pioneers of Software): This is PiOS’s traceability matrix for matching test procedures as they are made to specific requirements. This check-as-we-go approach is meant to be a form of documentation testing, to make sure there are no oversights. The “Test to Requirements traceability matrix” documents can be retrieved within the group-shared ‘Software Engineering Project’ Google Drive, as a Google Sheets entitled by the same name. The hyperlink: 

	

“Change Requests” (Ongoing form, Pioneers of Software): This is a document used for explicitly defining things in the system that need to be changed. Now that requirements have been gathered, this document will be primarily for major errors, as outlined in Section 5 of this document. This document can be accessed in the top level of the Google Drive, as a Google Docs entitled “Change Requests”. The hyperlink:

“”SMCM Computer Lab DxDiag”(Version 1.0, 11/22/2021 \[author names\]): This is the DxDiag of the computer lab computers which will be identical to the testing environment in order to fulfill system testing. It contains the entirety of the hardware specifications (and some software i.e. Windows 10\) of the system testing environment. This document can be retrieved within the group-shared ‘Software Engineering Project’ Google Drive, under the ‘Computer Specifications’ folder, as a Google Doc by the name “SMCM Computer Lab DxDiag.txt” The hyperlink: 

[SMCM Computer Lab DxDiag.txt](https://drive.google.com/file/d/1V1IPSQrrHXifW2ygNxsANxtInr7TaNqr/view?usp=sharing)

## **1.5 System Overview** {#1.5-system-overview}

The PiPa software will be designed as a point of sale system for the client, Bob Tracy, according to his needs for his business. The main functionality of this software is to take orders using a GUI focused software that calculates price and displays a receipt. It will also have the ability to manage users and prices. The software will function using a Windows computer with a mouse and keyboard by several users with a log-in system.

---

# **2\. Requirements to Be Tested** {#2.-requirements-to-be-tested}

Most requirements should be tested, with a few exceptions. The following requirements will not be tested, either as they are implicitly tested, or not feasible to test:

2.1.4.1 Edit Limitations  
2.2.1.5 Pizza Default  
2.2.6 Display Order  
2.2.7 Default Screen  
2.1.6.1 Log-in  
5.3 User Reaction  
6\. Delivery

The general explanation for these is as follows: most requirements related to delivery of the software, as under section 6 of “SRS for PiPa POS Mark II” cannot be tested, as these are one time actions that may only be planned for. Documentation will not have test procedures generated for it, but will be subject to review by members of the team. Certain implicit requirements, which are not directly stated, such as disallowing the user to input negative values for prices, will be tested for as well. Certain requirements will not be tested explicitly as they are repeatedly tested implicitly.

---

# **3\. Testing Approach** {#3.-testing-approach}

## **3.1 White Box Testing** {#3.1-white-box-testing}

White box testing is largely concerned with the logic and internal functions of the software. It will largely be important for the boundaries and limitations of the software, such as character limits for user name lengths. Our white box testing will be most commonly used in relation to less strictly guided user input, such as input through text boxes.

## **3.2 Black Box Testing** {#3.2-black-box-testing}

Black box testing, as it is what is mainly concerned with what is visible (the output), will be what is most important to our customer. A POS system is a content based system in which receipts and orders are the content; as a result, it will be our first priority in testing.   
---

# **4\. Test Process** {#4.-test-process}

## **4.1 Unit Testing**   {#4.1-unit-testing}

Unit testing will occur intermittently as new, independently functional aspects of the software become complete. The importance of unit testing is assuring that these aspects work alone, and without consideration for other factors, so the testing will occur on a few various systems, such as team members’ personal computers.

## **4.2 Integration Testing**  {#4.2-integration-testing}

Integration testing occurs towards the end of most other tests. Once features are proven to work individually, they will be combined into larger, more expansive tests to assure the correct operation of the PoS in a more realistic fashion. Integration tests have been included as a part of our test procedures, and will be completely both implicitly and explicitly, as the software will contain plenty of separate frames which the user will navigate between (i.e. from a log-in screen to the ordering screen, etc.).

## **4.3 Validation Testing**  {#4.3-validation-testing}

Validation testing will be concerned with ensuring that the software meets the requirements requested by the user. As such, a test should exist for each requirement. Part of this process is already in process, through the use of our “Test to Requirements” traceability matrix.

## **4.4 System Testing** {#4.4-system-testing}

When the software is at the point where it is ready for system testing, it should be near completion. There should be a few preliminary tests while the software is early in development, alongside the unit tests, to ensure that the program’s functionality will not be disrupted by the final version it will appear on. This system will be PiPa’s POS system as it will be mirrored in Schaefer 161, the installation facilities.  
---

# **5\. Reporting and Corrective Action** {#5.-reporting-and-corrective-action}

The team members, if they find nonmajor issues with the program, may directly notify each other member in PiOS’s team group chat. This group chat is a static, mobile based platform, and may not be directly accessed over online platforms. For more serious issues, the team should document them with the “Change Requests” document found in the group Google Drive in addition to reporting to the group chat.

---

# **6\. Test Environment** {#6.-test-environment}

## **6.1 Unit Testing Environment** {#6.1-unit-testing-environment}

The unit tests will be performed on the coding hardware in the IDE software to maximize the efficiency of creating and implementing stubs and drivers. PiOS programmers xx and xx will swap modules for efficient testing.

## **6.2 Integration Testing Environment** {#6.2-integration-testing-environment}

The integration tests will be performed on the coding hardware in the IDE software to maximize the efficiency of creating and implementing stubs and drivers. Tests of high abstraction (defined by complete usability by an outside tester) will be tested outside of the IDE by non-developers. 

## **6.3 Validation Testing Environment** {#6.3-validation-testing-environment}

Most necessary for validation testing is the team’s copy of the SRS document to ensure all aspects of the software match the requirements. A deficiency list will need to be created to map where the software strays from specifications. This testing should be done on each team member’s work computer.   
xx’s platform will be a Windows 10 Acer Aspire E 15; 8 GB RAM, Intel Core i5-8250U CPU @ 1.60GHz  1.80 GHz, 64 bit OS and processor.   
\-xx’ platform will be a Windows 10 Dell G-5 Laptop. It has an intel core i7 10th gen processor, with 16GB RAM. The full specs can be found in the document references as “xx\_DxDiag”   
\-xx’s platform is an Acer Aspire Desktop, Intel Celeron J4125 Quad-Core Processor (Up to 2.7GHz), Intel UHD Graphics 600, 4GB DDR4, 256GB NVMe M.2 SSD, Windows 10 Home, XC-830-UW91. 

## **6.4 System Testing Environment** {#6.4-system-testing-environment}

System testing will be completed in PiPa’s provided testing location: Schaefer 161\. In the testing location, testing will be done on one of the available Windows 10 64-bit OS Intel Core i5-7500 CPU Dell desktops 8 GB RAM. Necessary will be access to this room, access to one of these desktops, ability to log-in to one of these desktops, access to a bundled mouse and keyboard, and for the software to have passed all previous subsections of testing. The full specs can be found in the document references as “SMCM Computer Lab DxDiag”  
---

# **7\. Test Procedures** {#7.-test-procedures}

Test numbers should have obvious correlations to the requirements they are testing as to make traceability easier; sections of this procedure then will be arranged by relation to test rather than relation to whether it is a white box or a black box test.

The testers should use an account specifically for testing to use in most logged in tests.

Certain unit tests should be completed before other tests may be completed; as for example, ‘add user’ should be tested as a unit before ‘user management’ is tested.

## 	**7.1 Functional Tests** {#7.1-functional-tests}

Tests lettered ‘UM’ are related to ‘User Management’. Tests lettered ‘PO’ are related to ‘Placing Orders’, ‘POI’ are tests that deal with placing order integration, ‘PR’ are tests related to printing receipts, ‘PT’ refers to ‘Price Tests’ and ‘SSU’ refers to ‘System Start UP’.

### **7.1.1 User Management Tests** {#7.1.1-user-management-tests}

Requirement edit permissions will not be tested for as it is a de facto requirement; it requires no extra coding to implement, and as such, should work well as long as nothing is attempted for it.  
**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-217  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to test adding a user when no other users exist \[IE under factory settings\].  
**Test Procedures:**

1. Start program normally  
2. If this test is the first test attempted, the program should sustain no ability to log in, and thus, be under factory reset state.  
3. If not, this state can be mimicked by deleting, or emptying relevant user identification info files.  
4. An ‘add user’ menu should appear  
5. For the name, enter “Tester”  
6. For the PIN, enter “9102”  
7. Click ‘Save’

   **Measure of Success:**

   The system should lead the user to the log-in screen once the first user has been created. There should be no log-out button here.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-2113  
**Author:** xx  
**Date:** November 21, 2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to check the functionality of the ‘delete user’ user interfacing.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the ‘user management’ button to go to the UM menu  
4. From the UM menu, click the ‘add user’ button to create a second user  
5. From this menu, enter “Tester1” into the user name text box  
6. Enter “9103” into the PIN text box  
7. Hit the ‘save’ button to save  
8. Hit the return button to return to the previous ‘user management’ screen  
9. Select the checkbox by the test user “Tester1”  
10. Click the ‘delete user’ button to delete this “Tester1”

    **Measure of Success:**

    The system responds, and should no longer display the user “Tester1”. All that should be seen is the current user “Tester”.

**\<\>...................................................................................................................................\<\>**

**Test Number:** UM-2114  
**Author:** xx  
**Date:** November 3, 2021  
**Revision:** 1.0  
**Test Purpose:** This test is intended to check the functionality of the ‘edit user’ user interfacing.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. From the UM menu, select the user “Tester”.  
5. Click the button to ‘edit user’.

   **Measure of Success:**

   The system responds and allows the ‘edit user’ process to begin. The user should see the ‘edit user’ screen, which will include an interactable textbox with the name “Tester” in it, as well as an interactable textbox with the PIN “9102” in it.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-2112  
**Author:** xx  
**Date:** October 30, 2021  
**Revision:** 1.0  
**Test Purpose:** This test is intended to check the functionality of adding a user as integrated into start up functions.  
**Test Procedures:**

1. Start the program normally.  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. From the UM menu, click the button to ‘add user’  
5. From the ‘add user’ menu, enter the feasible name “Tester2”  
6. Enter the feasible PIN “9103”  
7. Click the ‘save’ button  
8. Verify that the user “Tester2” exists and is listed on the UM menu  
9. Log out of “Tester” by clicking the ‘log-out’ button  
10. Log-in as with the PIN “9103”

    **Measure of Success:**

    The system can log in as “Tester2”. This is a multi-stage test to make sure there is full functionality once a user is added.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-212  
**Author:** xx  
**Date:** November 21, 2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to check the system’s boundaries for adding users, including maxes and minimums.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. From the UM menu, click the button to ‘add user’  
5. From the previous test UM-2112, there should already be two users: “Tester” and “Tester2”; continue this pattern and add users until there are testers numbered up to “Tester20”.  
6. Assigning PINs should function the same way; “9102” and “9103” should already exist; continuing assigning pins to new users through counting up to “9121”  
7. Attempt to add a 21st user

   **Measure of Success:**

   The system should produce an error message that states no more than 20 users are allowed.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-2121  
**Author:** xx  
**Date:** November 21, 2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to check the system’s boundaries for any single user’s PIN.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. From the UM menu, click the button to ‘add user’  
5. Enter the name “example” for the name  
6. Attempt to enter “01234” for the PIN in the PIN textbox  
7. Attempt to save by hitting the ‘save’ button  
8. Attempt to enter “012” for the PIN in the PIN textbox  
9. Attempt to save by hitting the ‘save’ button  
10. Attempt to enter “” for the PIN by deleting all previous text in the textbox  
11. Attempt to save by hitting the ‘save’ button  
12. Return to UM menu  
13. Use the ‘edit user’s function to edit “Tester”  
14. Repeat steps 6-11 for user “Tester”

    **Measure of Success:**

    The user should not be successfully created with an invalid PIN, nor should the user be able to save information with an invalid PIN.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-2122  
**Author:** xx  
**Date:** November 21, 2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to check the boundaries for the user’s username.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. Click the ‘add user’ button  
5. Type in the valid unused PIN “9123”  
6. Attempt to type in the 25 character name “abcdefghijklmnopqrstvwxy” in the interactable username textbox  
7. Attempt to save by hitting the ‘save’ button  
8. Attempt to type in the 0 character name “” in the interactable username textbox, by deleting all previous text in the box  
9. Attempt to save by hitting the ‘save’ button  
10. Attempt to type in the 24 character name “abcdefghijklmnopqrstuvwx” in the interactable username textbox  
11. Attempt to save by hitting the ‘save’ button

    **Measure of Success:**

    The user “abcdefghijklmnopqrstuvwx” should be created; at any other instance in this test, an error message stating that an invalid name has been entered should pop up, showing all other save attempts should have failed.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-2141  
**Author:** xx  
**Date:** November 21, 2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to check the boundaries for the user’s username from the edit user menu.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. Select user “abcdefghijklmnopqrstuvwx”, if testing after UM-2122, else create a user with the name “Tester2141” with “2141” as the PIN  
5. Click the edit user button  
6. Attempt to change the user’s name to “abcdefghijklmnopqrstvwxy” by typing in the interactable username textbox  
7. Attempt to save by hitting the ‘save’ button  
8. Attempt to change the user’s name to “”  by deleting all previous text in the interactable username textbox  
9. Attempt to save by hitting the ‘save’ button  
10. Attempt to change the user’s name to “bcdefghijklmnopqrstuvwxy”  by typing in the interactable username textbox  
11. Attempt to save by hitting the ‘save’ button

    **Measure of Success:**

    The user should have the name “bcdefghijklmnopqrstuvwxy”. All other save attempts should have failed.

    

**\<\>...................................................................................................................................\<\>**

**Test Number:** UM-2111  
**Author:** xx  
**Date:** October 30, 2021  
**Revision:** 1.0  
**Test Purpose:** This test is intended to check the system’s display of user details.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu

   **Measure of Success:**

   The system should display existing users.

**\<\>...................................................................................................................................\<\>**

**Test Number:** UM-211  
**Author:** xx  
**Date:** November 21, 2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to see the integration of UM features in the user interface.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. If test ‘UM-212’ was tested beforehand, be sure there are an acceptable amount of users for adding a new one.  
5. Click the button to add a user.  
6. From the add user screen, add a feasible user whose name is “Name1” and PIN in “0001”.  
7. Click the return button to leave this page without saving.  
8. Verify an error message stating, “Your edits will not be saved. Continue?” appears, and hit ‘cancel’ to return to the page.  
9. Click the ‘save’ button to leave this page  
10. Verify you have returned to the UM page.  
11. Select “Name1” and click the ‘edit user’ button.  
12. From the ‘edit user’ page feasibly edit the user’s name to “Name2”  
13. Attempt to return to the UM page without saving.  
14. Proceed without saving, by clicking ‘okay’ on the error message that states, ““Your edits will not be saved. Continue?” Do not hit the ‘cancel’ button  
15. Reselect “Name1”.  
16. Click the “delete user” button.

    **Measure of Success:**

    All other user management user interface test procedures (and thus, steps of this procedure) have succeeded. At the end, the user “Name1” should no longer be visible on the screen. 

**\<\>...................................................................................................................................\<\>**

**Test Number:** UM-213  
**Author:** xx  
**Date:** November 4, 2021  
**Revision:** 1.0  
**Test Purpose:** This test is intended to test deleting users and boundaries.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. User “Tester2” should exist; click the bubble beside their name  
5. Click the ‘delete user’ button  
6. If other non-”Tester” users exist, attempt to delete them in the same matter  
7. Select “Tester”  
8. Attempt to delete this user

   **Measure of Success:**

   All but the current (final) user have been deleted; some safeguard has been established to not delete themself.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-210  
**Author:** xx  
**Date:** November 21, 2021  
**Revision:** 1.0  
**Test Purpose:** This test is intended to see the persistence of users after editing, adding, or deleting them from the database between program use sessions.  
**Test Procedures:**

1. Start program normally, in windowed mode  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. Click the ‘add user’ button  
5. Once at the screen, in the user ID text box type “UM 210 Test”  
6. In the PIN text box, type the valid PIN “9999”  
7. Hit the ‘save’ button to save this user  
8. Exit the program by hitting the ‘x’ button at the upper right corner  
9. Restart the program normally, in windowed mode  
10. Enter PIN “9999” to log in as “UM 210 Test”  
11. Once at the order screen, click the button to go to the UM menu  
12. Select the user “UM 210 Test” by hitting the checkbox by their name, then hit the ‘edit user’ button to edit this user  
13. In the user ID text box, change the user’s name to “UM 210 Test Pt 2”  
14. Click the ‘save’ button to save  
15. Exit the program by hitting the ‘x’ button at the upper right corner  
16. Restart the program normally, in windowed mode  
17. Enter PIN “9102” to log in as “Tester”  
18. Once at the order screen, click the button to go to the UM menu  
19. Select the user “UM 210 Test Pt 2” by hitting the checkbox by their name, then hit the ‘delete user’ button to delete this user  
20. Exit the program by hitting the ‘x’ button at the upper right corner  
21. Restart the program normally, in windowed mode  
22. Attempt to use the PIN “9999” to log in as ““UM 210 Test Pt 2”

    **Measure of Success:**

    An error message on the login screen should pop up, stating that an invalid PIN has been entered and to try again. At every milestone step of this test, edits or created users should be retained in between sessions.

    

**\<\>...................................................................................................................................\<\>**

#### **7.1.1.1 User Management Integration Tests** {#7.1.1.1-user-management-integration-tests}

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-21  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 2.0  
**Test Purpose:** This test is intended to see the integration of UM features.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Add item ‘small pizza’ to the order  
4. Click the ‘display receipt’ button

   **Measure of Success:**

   On the receipt, the current user’s name “Tester” should be printed.

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-215  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test is intended to see how the UM menu works with the PO menu  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. Once at the order screen, click the button to go to the UM menu  
4. From the UM menu, hit the return button

   **Measure of Success:**

   You have returned to the PO menu. 

**\<\>...................................................................................................................................\<\>**  
**Test Number:** UM-2163  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to assure the function of logging out.  
**Test Procedures:**

1. Start program normally  
2. Enter PIN “9102” to log in as “Tester”  
3. From the order screen, click the logout button  
4. From login screen, enter PIN “9102” to log in as “Tester”  
5. From the order screen, go to the UM menu  
6. Hit the logout button  
7. From login screen, enter PIN “9102” to log in as “Tester”  
8. From the order screen, go to the price management screen  
9. Hit the logout button

   **Measure of Success:**

   You have logged out from each main menu screen.

**\<\>...................................................................................................................................\<\>**

### **7.1.2 Placing Orders Tests**  {#7.1.2-placing-orders-tests}

The alphabetical value of these tests will be ‘PO’ to represent ‘Placing Orders’. The requirement ‘Display Order’ will be tested intrinsically by many other tests in this section, and will not be tested itself. The requirement ‘Pizza Default’ will not be tested as it will be intrinsically tested by many other tests in this section. The requirement ‘Default Screen’ is tested implicitly by most unit tests, and thus, will also not have a test explicitly written for it.  
**\<\>...................................................................................................................................\<\>**  
	**Test Number:** PO-2211  
**Author:** xx  
**Date:** November 4, 2021  
**Revision:** 1.0  
**Test Purpose:** This tests intends to test adding a ‘small pizza’  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to add a ‘small pizza’

   **Measure of Success:**

   A small pizza with default values (no toppings, quantity of one) should be printed in the display order box.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PO-2212  
**Author:** xx  
**Date:** November 4, 2021  
**Revision:** 1.0  
**Test Purpose:** This tests intends to test adding a ‘medium pizza’  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to add a ‘medium pizza’

   **Measure of Success:**

   A medium pizza with default values (no toppings, quantity of one) should be printed in the display order box.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PO-2213  
**Author:** xx  
**Date:** November 4, 2021  
**Revision:** 1.0  
**Test Purpose:** This tests intends to test adding a ‘large pizza’  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to add a ‘large pizza’

   **Measure of Success:**

   A large pizza with default values (no toppings, quantity of one) should be printed in the display order box.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PO-222  
**Author:** xx  
**Date:** November 4, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to test adding toppings to pizza, and the boundaries of it.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to add a ‘medium pizza’  
4. From the now available toppings menu, add topping ‘Bacon’  
5. Attempt to add the topping ‘Pepperoni’

   **Measure of Success:**

   A medium pizza with only ‘Pepperoni” should be printed in the display order box.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PO-2222  
**Author:** xx  
**Date:** November 7, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to test the boundaries of the toppings list.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to add a ‘small pizza’.  
4. Add the topping ‘bacon’ to the small pizza.  
5. Add a new ‘large pizza’.  
6. Add the topping ‘onions’.  
7. Add a new ‘medium pizza’  
8. Add the topping ‘no toppings’

**Measure of Success:**  
	The boundary toppings of the enumerated list will have been shown to be able to be added to pizzas functionally; the three pizzas will display on the order preview as set.

**\<\>...................................................................................................................................\<\>**  
	**Test Number:** PO-223  
**Author:** xx  
**Date:** November 4, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to test adding a soda  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to add a ‘soda’

	**Measure of Success:**  
	A soda with the default value \[quantity: 1\] should be printed in the display order box.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PO-224  
**Author:** xx  
**Date:** November 7, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to test changing the quantity of an ordered item, and the boundaries of the quantity function.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the button to add a ‘soda’  
4. Click the quantity textbox to type in a quantity of 100  
5. Click the button to add a ‘small pizza’   
6. Click the quantity textbox to type in a quantity of 99  
7. Click the button to add a ‘medium pizza’  
8. Click the quantity textbox to attempt to type in a quantity of 0

	**Measure of Success:**  
	The order preview should display the order: 100 sodas and 99 small pizzas \[default value: ‘no toppings’\]. It should also display a single medium pizza, as a quantity of 0 should not be possible.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PO-225  
**Author:** xx  
**Date:** November 7, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to test clearing an order.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the placing orders screen, click the button to add a ‘soda’  
4. Click the button to add a ‘large pizza’  
5. Click the button to add ‘extra cheese’ to the pizza  
6. Click the quantity textbox of the pizza item to type in a quantity of 99  
7. These two items should be visible at the order preview  
8. At the bottom of the order preview, click the ‘clear order’ button

   

   

	**Measure of Success:**  
	There should be no items of the order visible or recorded in the order preview.

**\<\>...................................................................................................................................\<\>**

#### **7.1.2.1 Placing Orders Integration Tests** {#7.1.2.1-placing-orders-integration-tests}

	This subsection exists for checking the integration of tests. Integration tests begin with POI (placing orders integration) followed by a number starting at 1 in the order they were created.  
**\<\>...................................................................................................................................\<\>**  
**Test Number:** POI-1  
**Author:** xx  
**Date:** November 7, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to add several pizzas with the correct total displaying on the sidebar.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Ensure the prices have already been set as follows

| Small pizza with topping | $6 |
| :---- | :---- |
| Medium pizza with topping | $7 |
|  Large pizza with topping | $8 |
| Small pizza without topping | $5.25 |
| Medium pizza without topping | $6.25 |
| Large pizza without topping | $7.25 |

4. Add a small pizza with bacon to the order  
5. Add a medium pizza with sausage to the order  
6. Add a large pizza with extra cheese  
7. Add a small pizza with no toppings to the order  
8. Add a medium pizza with no toppings to the order  
9. Add a large pizza with no toppings to the order

   **Measure of Success:**  
   The sidebar must list every item added from the test with the correct price next to it as indicated by the table from step 3\. The subtotal must display $39.75, the correct subtotal from the given prices.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** POI-2  
**Author:** xx  
**Date:** November 8, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to add pizzas with the correct quantities displaying on the sidebar.  
**Test Procedures:** 

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the placing orders screen, select soda  
4. Click the quantity box to enter 3 for the quantity   
5. Select medium pizza with onions  
6. Input the quantity as 1  
7. Select small pizza with no toppings  
8. Enter 0 for the quantity  
9. Select medium pizza with sausage  
10. Set the quantity to 100  
11. Select large pizza with no toppings  
12. Set the quantity to 101

    **Measure of success:** 

    The sidebar must list the following items:

* 3 soda  
* 1 medium pizza with onions  
* 1 small pizza with no toppings (as the minimum quantity is 1 even though 0 was entered)  
* 100 medium pizza with sausage  
* 100 large pizza with no toppings (as the maximum quantity is 100 even though 101 was entered)

  The sidebar should list items in order of placement.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** POI-3  
**Author:** xx  
**Date:** November 8, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to print a receipt with the correct items, prices, subtotal, and total displayed.  
**Test Procedures:** 

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Ensure the prices have already been set as follows

| Small pizza with topping | $6 |
| :---- | :---- |
| Medium pizza with topping | $7 |
|  Large pizza with topping | $8 |
| Small pizza without topping | $5.25 |
| Medium pizza without topping | $6.25 |
| Large pizza without topping | $7.25 |
| Tax | .06 |

4. Add a small pizza with extra cheese to the order  
5. Set the quantity to 2  
6. Add a medium pizza with onion to the order  
7. Set the quantity to 4  
8. Add a large pizza with pineapple to the order  
9. Add a small pizza with no toppings to the order  
10. Add a medium pizza with no toppings to the order  
11. Set the quantity to 3  
12. Add a large pizza with no toppings to the order  
13.  Hit the print button

    **Measure of success:** 

    The receipt must appear on screen and display the following information:

    2 small pizza extra cheese: $12.00

    4 medium pizza onion: $28.00

    1 large pizza pineapple: $8.00

    1 small pizza no toppings: $5.25

    3 medium pizza no toppings: $18.75

    1 large pizza no toppings: $7.25

    Subtotal: $79.25

    Total: $84.01

    Formatting of the receipt should not completely match the above, but all values must be explicitly represented on the receipt.

**\<\>...................................................................................................................................\<\>**  
	**Test Number:** POI-DES1  
**Author:** xx  
**Date:** November 7, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will see if the button to go to the Price Management, from the ‘Placing Orders’ Screen, functions correctly.   
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the Order Screen, click the ‘Price Management’ Button

   **Measure of Success:**

   Following the pressing of the ‘Price Management’ button, the system should take the user to ‘Price Management,’ from the ‘Placing Orders’ screen.

**\<\>...................................................................................................................................\<\>**

### **7.1.3 Print Receipt Tests** {#7.1.3-print-receipt-tests}

The following tests relate to how receipts are printed.  
**\<\>...................................................................................................................................\<\>**

**Test Number:** PR-231  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test assures that a receipt contains a complete list of items listed as entered.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, add a medium pizza by hitting the ‘medium pizza’ button with pepperoni topping by clicking the ‘pepperoni’ topping checkbox.  
4. Set the quantity of the item to 4 by typing 4 into the quantity textbox  
5. Add a medium pizza by clicking the ‘medium pizza’ button with pepperoni topping clicking the ‘pepperoni’ topping checkbox.  
6. Set the quantity to 2 by typing 2 into the quantity textbox.  
7. Select the “print” button  
   **Measure of Success:**  
   The receipt should appear on the screen. The items listed must be...  
* 4 Medium pizza with pepperoni  
* 2 Medium pizza with pepperoni  
  ...in that order.


**\<\>...................................................................................................................................\<\>**

**Test Number:** PR-232  
**Author:** xx \[Edits by xx\]  
**Date:** November 21, 2021  
**Revision:** 2.0  
**Test Purpose:** This test assures that a receipt displays a total and subtotal calculated correctly based on the current prices and tax.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. From the order screen, hit the ‘prices menu’ button to go to the prices menu  
4. From the menu, assure that the price of a soda is set to $2.20, and tax is set to 7% (or $.07).  
5. Return to the order screen by hitting the ‘return’ button.  
6. At the order screen, add a soda to the order by hitting the ‘soda’ button.  
7. Select the “print button”  
   **Measure of Success:**  
   The receipt must display the subtotal as “$2.20”, the tax as “$0.15”, and the total as “$2.35”  
   

**\<\>...................................................................................................................................\<\>**

**Test Number:** PR-2332  
**Author:** xx \[edits by xx\]  
**Date:** November 22, 2021  
**Revision:** 2.0  
**Test Purpose:** This test assures that a receipt displays all items on individual lines with the names of items not exceeding 20 characters  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, add a medium pizza with extra cheese to the order by clicking the ‘medium pizza button’ and selecting the ‘extra cheese’ checkbox  
4. Add a large pizza with extra cheese to the order by clicking the ‘large pizza button’ and selecting the ‘extra cheese’ checkbox  
5. Add a small pizza with extra cheese to the order by clicking the ‘small pizza button’ and selecting the ‘extra cheese’ checkbox  
6. Add a medium pizza with pepperoni by clicking the ‘medium pizza button’ and selecting the ‘pepperoni’ checkbox  
7. Add a medium pizza with pineapple by clicking the ‘medium pizza button’ and selecting the ‘pineapple’ checkbox  
8. Add a medium pizza with mushrooms by clicking the ‘medium pizza button’ and selecting the ‘mushrooms’ checkbox  
9. Add a small pizza with no toppings by clicking the ‘small pizza button’   
10. Add a medium pizza with no toppings by clicking the ‘medium pizza button’   
11. Add a large pizza with no toppings by clicking the ‘large pizza button’   
12. Select the print button  
    **Measure of Success:**  
    The receipt must appear with all items listed not exceeding 20 characters each. Any item that would normally be over 20 characters must be displayed using an abbreviation or cutoff. Item quantity and price does not add to the number of characters.  
    Truncated versions should appear as:  
    MED X-cheese  
    LAR X-cheese  
    SMA X-cheese  
    MED pepperoni  
    MED pineapple  
    MED mushrooms  
    SMA plain  
    MED plain  
    LAR plain  
    

**\<\>...................................................................................................................................\<\>**

**Test Number:** PR-2333  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test assures that a receipt displays all prices to the second decimal place  
**Test Procedure:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Assure that the price of a soda is set to $2.20, the price of a medium pizza with toppings is $6, and tax is set to 7%.  
4. If applicable, navigate to the order screen.  
5. Add a medium pizza with onions to the order.  
6. Add a soda to the order.  
7. Select the “print” button  
   **Measure of Success:**  
   The receipt must appear with the following information:  
* The price of the medium pizza with toppings displayed as “6.00”  
* The price of the soda displayed as “2.20”  
* The subtotal displayed as “8.20”  
* The tax displayed as “0.57”  
* The total displayed as “8.77”  
  The inclusion of a currency unit does not affect if the test succeeds or fails.


**\<\>...................................................................................................................................\<\>**

**Test Number:** PR-2341  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test assures that a receipt displays the date and time when the order was placed.  
**Test Procedure:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, add a soda to the order  
4. Select the print button, making note of the system time at that moment  
   **Measure of Success:**  
   The receipt must appear on the screen. Included on the receipt must be the noted date and time from step 4\.  
   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PR-2342  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test assures that a receipt displays the name of the user who placed the order  
**Test Procedure:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, add a small pizza with no toppings to the order  
4. Select the “print” button  
   **Measure of Success:**  
   The receipt must appear on the screen and include that “Tester” was the one who placed the order.  
   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PR-2343  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test assures that a receipt displays the PiPa logo  
**Test Procedure:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, add a large pizza with no toppings to the order  
4. Select the “print” button  
   **Measure of Success:**  
   The receipt must appear on the screen and include a designated PiPa logo.  
   

**\<\>...................................................................................................................................\<\>**

### **7.1.4  Prices Test** {#7.1.4-prices-test}

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2411  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test is the initial test, it will ensure that the program is pre-loaded with prices and values within the Price Menu  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button

   **Measure of Success:**

   Following the pressing of the ‘Price Management,’ the user should be able to view the initially set prices within the .csv file:

* Small Pizza: $1.00  
* Medium Pizza: $2.00  
* Large Pizza: $ 3.00  
* Small Topping: $4.00  
* Medium Topping: $5.00  
* Large Topping: $6.00  
* Soda: $7.00  
* Tax Rate: .08


**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2421  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will see if the soda field within the Price Menu is manipulable with whole numbers.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will click and into the Soda Price text box, deleting the previous information and entering: 2, for a price of $2.00  
5. The user will click out of the Soda Price text box  
6. The user will delete the old information, and enter into the Soda Price text box: 4, for a price of $4.00 

   **Measure of Success:**

   The Soda Price should be changed to $2.00, then changed to $4.00; this will be represented by the text box being filled first with 2, then with 4\. 

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2422  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will see if the soda field within the Price Menu is modifiable via float/double style inputs.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will click and into the Soda Price text box, deleting the previous information and entering: 3.00, for a price of $3.00  
5. The user will click out of the Soda Price text box  
6. The user will delete the old information, and enter into the Soda Price text box: 4.701, for a price of $4.70 

   **Measure of Success:**

   The Soda Price should be changed to $3.00, then changed to $4.70; this will be represented by the text box being filled first with 3.00, then with 4.701, which will be rounded by the software to 2 decimal places. 

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2423  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:**   
This test will ensure that the soda field within the Price Menu only accepts numerical and decimal inputs, and won’t accept extraneous symbol or string inputs into the field.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will click and into the Soda Price text box, deleting the previous information and entering: \-8, for a price of \-$8.00  
5. The user will click out of the Soda Price text box  
6. The user will delete the previous data, then enter into the Soda Price text box: soda5 

   **Measure of Success:**

   The Soda Price text field should not allow the user to go forward with changes such as these; the text field will not be changed with the extraneous symbols or strings, leaving the field with a value of 5 by the end.

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2431  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:**   
Now that procedure was “in the small” by only testing soda, we will move to “in the large” by testing the other text fields within one test, since the logic is identical for the remaining fields. This test will ensure that the small, medium, and large pizza fields, as well as small, medium, and large topping fields, within the Price Menu are modifiable with whole numbers.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will click and enter into the following text fields to change their values after deleting the previous data:  
* Small Pizza: 4  
* Medium Pizza: 5  
* Large Pizza: 6  
* Small Topping: 1  
* Medium Topping: 2  
* Large Topping: 3  
5. The user will perform the operation again, deleting the information previously in the field, and entering into the following text fields to change their values:   
* Small Pizza: 5  
* Medium Pizza: 6  
* Large Pizza: 7  
* Small Topping: 2  
* Medium Topping: 3  
* Large Topping: 4  
6. The user will click out of whichever text box they currently have selected.

   **Measure of Success:**

   The UI should accept and display to the user the Price Management screen with the newly set prices in step 5:

* Small Pizza: $5.00  
* Medium Pizza: $6.00  
* Large Pizza: $7.00  
* Small Topping: $2.00  
* Medium Topping: $3.00  
* Large Topping: $4.00


**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2432  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:**   
This test will ensure that the small, medium, and large pizza fields, as well as small, medium, and large topping fields, within the Price Menu are modifiable via float/double inputs.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will click and enter into the following text fields to change their values after deleting the previous data:  
* Small Pizza: 2.0  
* Medium Pizza: 3.00  
* Large Pizza: 4.0  
* Small Topping: 1.000  
* Medium Topping: 2.000  
* Large Topping: 3.00000  
5. The user will the perform the operation again, deleting the information previously in the field, then clicking and entering into the following text fields to change their values:   
* Small Pizza: 2.2  
* Medium Pizza: 3.55  
* Large Pizza: 4.99  
* Small Topping: .705  
* Medium Topping: 1.2000  
* Large Topping: 2.05400  
6. The user will click out of whichever text box they currently have selected.

   **Measure of Success:**

   The UI should accept and display to the user the Price Management screen with the newly set prices in step 5, and doubles with more than 2 decimal places will be rounded to 2:

* Small Pizza: $2.20  
* Medium Pizza: $3.55  
* Large Pizza: $4.99  
* Small Topping: $.71  
* Medium Topping: $1.20  
* Large Topping: $2.05


**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2433  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:**   
This test will ensure that the small, medium, and large pizza fields, as well as small, medium, and large topping fields, within the Price Menu only accepts numeric and decimal inputs, and won’t accept extraneous symbol or string inputs into the field.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will click and enter into the following text fields to change their values after deleting the previous data:  
* Small Pizza: \-1  
* Medium Pizza: \-2.2  
* Large Pizza: \-3.0  
* Small Topping: \-1  
* Medium Topping: \-1  
* Large Topping: \-1  
5. The user will the perform the operation again, deleting the information previously in the field, then clicking and entering into the following text fields to change their values:   
* Small Pizza: @3  
* Medium Pizza: \#9.9  
* Large Pizza: ….  
* Small Topping: .105\!  
* Medium Topping: 1.2.2  
* Large Topping: 9+10=21  
6. The user will click out of whichever text box they currently have selected.

   **Measure of Success:**

   The Small Pizza text field should not allow the user to go forward with changes such as these; the text field will not be changed with the extraneous symbols or strings. Only the numeric values from step 5, and their first decimal, should be left behind in the text field, resulting in:

* Small Pizza: $3.00  
* Medium Pizza: $9.90  
* Large Pizza: $.00  
* Small Topping: $.11\!  
* Medium Topping: $1.22  
* Large Topping: $91021.00


**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2451  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will ensure that the system will be able to change the tax rate which is set in the program.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will click and enter into the tax text box: 20, for a tax rate of 20%  
5. The user will click out of the tax rate text box  
6. The user will click and enter into the tax text box: 80, for a tax rate of 80%

   **Measure of Success:**

   The tax rate should be changed to 20%, then changed to 80%; this will be represented by the text box being filled first with 20, then with 80\. 

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2452  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will ensure that the system will be not be able to change the tax rate to an invalid value, like a negative or letter value.  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will try to click and enter into the tax text box: \-3, for a tax rate of \-3%  
5. The text box should only display 3%, since it doesn’t accept negatives. The user will click out of the tax rate text box displaying ‘3%’.  
6. The user will delete the prior entry, and click and enter into the tax text box: ui

   **Measure of Success:**

   The tax rate text box should not be fillable with these parameters; instead, it will not allow the user to enter the negative(symbol) or the letters. Therefore, success hinges on the tax rate text box yielding 3% after step 4, and being left blank after performing step 6\.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2453  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will ensure that the system can enter single digit tax rates, such as .03 (entered as 03\)  
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. The user will try to click and enter into the tax text box: 03, for a tax rate of 3%  
5. The user will delete the tax rate text box contents, and click out of the text box.  
6. The user will try to click and enter into the tax text box: 00, for a tax rate of 0%

   **Measure of Success:**

   The tax rate should be changed to 3%, then changed to 0%; this will be represented by the text box being filled first with 03, then with 00\. 

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2461  
**Author:** xx  
**Date:** November 7, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will see if the button to return from the Price Management, to the ‘Placing Orders’ Screen, functions correctly.   
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. Once at the Price Management Screen, click the ‘Return’ button

   **Measure of Success:**

   Following the pressing of the ‘Return’ button, the system should take the user from the ‘Price Management’ screen, to the ‘Placing Orders’ screen.

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2462  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will see if the button to log out of the instance, functions correctly.   
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. Once at the Price Management Screen, click the ‘Log out’ button

   **Measure of Success:**

   Following the pressing of the ‘Log Out,’ the user should be taken back to the log-in screen with the PIN text field, as seen in Steps 1 and 2\.

   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2471  
**Author:** xx  
**Date:** November 7, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will ensure that the system will be able to display previously set prices without modifying them.   
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button

   **Measure of Success:**

   Once at the Price Management screen, the system should display to the user the Price Management screen with the currently set prices. 

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2472  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will ensure that the system will be able to display newly set prices which have been modified in the session.   
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. Once at Price Management, change the values of the following:  
* Small Pizza: 24.00  
* Medium Pizza: 25.00  
* Large Pizza: 26.00  
* Small Topping: 1.10  
* Medium Topping: 2.20  
* Large Topping: 3.25  
* Soda: 4.44  
* Tax Rate: 09  
5. Click the “Save” button  
6. Click the “Return” button to return to the Order Screen  
7. Once at the order screen, click the ‘Price Management’ Button

   **Measure of Success:**

   Once back at the Price Management screen, the system should display to the user the Price Management screen with the newly set prices in step 4:

* Small Pizza: $24.00  
* Medium Pizza: $25.00  
* Large Pizza: $26.00  
* Small Topping: $1.10  
* Medium Topping: $2.20  
* Large Topping: $3.25  
* Soda: $4.44  
* Tax Rate: 9%

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2473  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will ensure that the system will be able to display newly set prices which have been modified in a different session.   
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. Once at Price Management, change the values of the following:  
* Small Pizza:  12.33  
* Medium Pizza: 23.44  
* Large Pizza: 33.33  
* Small Topping: 1.11  
* Medium Topping: 2.22  
* Large Topping: 3.33  
* Soda: 6.66  
* Tax Rate: 02  
5. Click the “Save” button  
6. Click the “Log out” button  
7. At the start-up screen, press the “Exit” button, and wait 5 seconds after it closes.  
8. Start up the program normally  
9. Enter PIN “9102” to login as “Tester”  
10.  Once at the order screen, click the ‘Price Management’ Button

    **Measure of Success:**

    Once back at the Price Management screen, the system should display to the user the Price Management screen with the newly set prices as defined in step 4:

* Small Pizza:  $12.33  
* Medium Pizza: $23.44  
* Large Pizza: $33.33  
* Small Topping: $1.11  
* Medium Topping: $2.22  
* Large Topping: $3.33  
* Soda: $6.66  
* Tax Rate: 2% 

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PT-2474  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test will ensure that the system will be able to display newly set prices which have been modified in a different session by a different user.   
**Test Procedures:**

1. Start up the program normally  
2. Enter PIN “9102” to login as “Tester”  
3. Once at the order screen, click the ‘Price Management’ Button  
4. Once at Price Management, change the values of the following:  
* Small Pizza: 11.11  
* Medium Pizza: 11.22  
* Large Pizza: 11.33  
* Small Topping: 1.44  
* Medium Topping: 2.44  
* Large Topping: 3.44  
* Soda: 1.11  
* Tax Rate: 25  
5. Click the “Save” button  
6. Click the “Log out” button  
7. At the start-up screen, press the “Exit” button, and wait 5 seconds after it closes.  
8. Start up the program normally  
9. Enter PIN “9122” to login as “TesterTwo”  
10.  Once at the order screen, click the ‘Price Management’ Button

    **Measure of Success:**

    Once back at the Price Management screen, the system should display to the user the Price Management screen with the newly set prices as defined in step 4, by the other test user:

* Small Pizza: $11.11  
* Medium Pizza: $11.22  
* Large Pizza: $11.33  
* Small Topping: $1.44  
* Medium Topping: $2.44  
* Large Topping: $3.44  
* Soda: $1.11  
* Tax Rate: 25% 

**\<\>...................................................................................................................................\<\>**

### **7.1.5 Software Start Up Tests**  {#7.1.5-software-start-up-tests}

Successful log-in is a prerequisite action of many tests, and thus, is not specifically tested for.  
**\<\>...................................................................................................................................\<\>**  
**Test Number:** SSU-252  
**Author:** xx  
**Date:** November 3, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to check the ability to quit the program by hitting the ‘quit’ button .  
**Test Procedures:**

1. Start up the program normally  
2. Hit the ‘quit’ button   
   **Measure of Success:**  
   The window is no longer seen, and the icon is no longer visible on the Windows taskbar.

**\<\>...................................................................................................................................\<\>**  
**Test Number:** SSU-2534  
**Author:** xx  
**Date:** November 3, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to test an incorrect PIN logic path.  
**Test Procedures:**

1. Start up the system normally  
2. Attempt to input the unused PIN “0000”

   **Measure of Success:**

   The system does not log in.

**\<\>...................................................................................................................................\<\>**

## **7.2 Other Tests** {#7.2-other-tests}

The following section is for testing of non functional aspects of the program, to ensure correctness without necessarily following the procedure format. PF is shorthand that will be used for performance tests.  
**\<\>...................................................................................................................................\<\>**  
**Test Number:** PF-25411  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to time performance.  
**Test Procedures:**

1. Start up the system normally on PiPa’s Dell  
   **Measure of Success:**  
   This process does not take longer than 10 seconds.  
   

**\<\>...................................................................................................................................\<\>**  
**Test Number:** PF-25412  
**Author:** xx  
**Date:** November 9, 2021  
**Revision:** 1.0  
**Test Purpose:** This test intends to time performance.  
**Test Procedures:**

1. Start up the system normally on PiPa’s Dell  
2. Enter the PIN “9102” to login as “Tester”  
3. From the PO screen, add a ‘small pizza’ to the order.  
4. Add a soda to the order  
5. Click the button to display the order.

   **Measure of Success:**

   The individual loading processes associated with each act (adding an item to the order, logging in, and displaying) do not take longer than 10 seconds.

   

   

   

---

## **8\. Miscellaneous** {#8.-miscellaneous}

The program should not be limited to one download. There are no set number of licenses provided to the client.

Our Github is open to collaborators by request, but is currently private. All team members should have access. It is not referenced in this document. If one has collaborator access, it is available under this hyperlink:  

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkwAAAGhCAYAAACTVusCAACAAElEQVR4Xuydd9glRbWv739mAbkgDlFgAEFykDSAgCMcogKSYTwiCgKSBEUByZkhowySkRxmyFFAQJAsQZIiOUl0ABmUvvctz2+f9a2ve+/eOa33eerp7urq3t3Vtbt+vWpV1f/JgiAIgiAIgqr8Hx8RBEEQBEEQjCQEUxAEQRAEQQ1CMAVBEARBENQgBFMQBEEQBEENQjAFQRAEQRDUIARTEARBEARBDUIwBUEQBEEQ1CAEUxAEQRAEQQ1CMAVBEARBENQgBFMQBEEQBEENQjAFQRAEQRDUIARTEARBEARBDUIwBUEQBEEQ1CAEUxAEQRAEQQ1CMAVBEARBENQgBFMQBEEQBEENQjAFQRAEQRDUIARTEASFfPjhh9lTTz3loyt85jOfyb7whS9kyy+/fLbJJptk22yzTbbjjjtmRx11VPbkk0/65EEQBH1LCKYgCEZx5JFHZvPNN1/2iU98Ijv//PNT3LRp01I49dRTU5gwYUK2zDLLJMH06U9/OoVPfepTKWh9+umnd2cOgiDoT0IwBUGQPfzww9kSSyyRLEaEz33uc9nYsWOT5WjFFVccEZ5++unsvffey6ZOnVo1kGaeeeZJxyCuJLRsCIIg6BdCMAXBkHL11Vdns8wyS8UqNOecc2abbrppRRjNP//8Kdj1oji/7eMeeOCB7JFHHqmcGwFVFI4//vhspZVWyj7++GN/yUEQBF0jBFMQDBGPPvpo9qUvfSkJpM9+9rPZQgstNEqwSNBY4aNtiSClqyaSbDotffC/Tdhqq62ymWaaKV3jdNNNl+21115hjQqCoOuEYAqCAQex8ZWvfKXiZyRh44OaybwIKhJO8mPSut0PEkBs27Qsld5ue+FEQNDJAva1r30thFMQBF0jBFMQDChTpkxJDtk4bmNVWmGFFUaJJWsVknjx+xTvhY5Pb4WOF0BeGPljFC9B5M+xyiqrJN+qT37yk9miiy6a4oIgCDpJCKYgGDC23HLLJC6wykj4FAW7v4ygscGKHB2TZ0my6W0algp22/6Gv4711luvIpwWX3zxisAKgiBoNyGYgmBAWGqppZKYmGGGGZJoqiaWrBCxgskGK35A8XZdgsUKIRvvz2Xj/VKCSdu6Rh/Y9+1vfzvdK02M2267bQinIAjaTgimIOhjGFhy7rnnThaX2WabLYkJL46sQLLBWpgkbKy4kQjylh8bB3a/XWrdprHrPi7vXHZbQddM2GWXXZIljWEQjjvuuHSOIAiCdhCCKQj6kEsvvTQNCYBQssLHiyQtrZDywkhiReJGEM+xWlc6sELInqMofd56nrDyeNFkrUx2ucgiiyRr0xxzzOFPEQRB0BJCMAVBH3HPPfckYYBQmn322XOFkrccaWkFFHgBYkWP3VZajgUrhoi34skutd+KHr/PLsHut+dT4BpYco1aWuFEcyT5c+ihh1bOEwRB0ApCMAVBH/Duu++mcZMQSuuuu+4ogWSFksSNFUhWuFjBxLYXNV4s2XW/7fflUSZ9XryP0/WBhJoEk+6RcOyxx1bGcJo8efKIcwRBEDRKCKYg6GGYu01Nb1YcSAwpSCxYIWHFj+K0H6xAgiKh5IVLEWXT1cIKo7zr8dsShcoT3eO8886bHMPJvyAIgmYJwRQEPQZCgGlBxo8fn4TSXHPNNUosSRxoHSQUvIiywsiKEft71YRJJ/HXkSec7D5/XxKFyhfimGYFi9Ptt98+4hxBEAT1EIIpCHoILEoETYBrK38JIK2Dtr2AsHFKC4r32DS9ir9ue2/aZ/NFQorlQQcdlPJ03LhxleODIAjqIQRTEPQQyyyzTLIqLbzwwqOEkg1WDNk4sJYWK6Tsfis+vBDpRfw1+nuw+Lyw+cTI5winIAiCegnBFAQ9ggad9M1KNijeiiHIEwmevLh+pcy9SCgpP7SNGCWv77vvPn9IEARBISGYgqDLXHDBBcmqtOqqq44QRApeLHkBYMWDFU126df7mSJBWITPL8Imm2xSmYg4CIKgDCGYgqCLXHLJJckhuUgg2ThV+KAlEM9+rdv44H+xwkkBS9PYsWN90iAIglGEYAqCLkGFveGGG1asRFYgSRDliaRaosgKgqAY5Q/DDjDGVRAEQTVCMAVBF5AQ8kLJCiRZlaz1yIopxWkZAql+yLP//u//TqOmY+kLgiAoIgRTEHQQK3okhmxzm+LBW5SsICpaD8ojsaTAQJf4NQVBEOQRgikIOoQVRQp5Pd6UTuta2jRB60E0felLX8o+//nP+11BEAQhmIKgE/zjH/+oCB4rkPKsSzYdWNEUtA4EUt72Jz7xiVH7giAIQjAFQZthyIDdd989rVezLlkLkhdHfjtoLRJILL/yla9ks846a4imIAhGEIIpCNoI1oqNNtqo0LJUy5IUQqlzeNFECIIgECGYgqBNIJY233zzqs1uQe8goaQllsGwMgVBIEIwBUGLmTRpUqpst9pqqzSS9JgxY9IS4cTSWpZkXYIQUN1HliWEEs8wLE1BEIgQTEHQQhA9WJbmm2++ikCyI3cH/QEiacYZZ0yDWkpABUEw3IRgCoIWYcWSde4GNcvVokyaoH1oTCZE0v/9v/83PU+WIZiCIAjBFAQtAGFE5brCCiskq5IsS77ZLehtJIxkVWKuubAwBUEAIZiCoEmwCuHvwqCH1sHbWpXCctQ/2N5yBAayDMEUBEEIpiBoAoQQc5AttthiFYFkhwwI+g9vZcJyGFamIAhCMAVBE+AUvMYaa1SGC6BHnB06IOhvEEnjx48PwRQEQQimIGiUDTbYIDXDSRjhtxT+SoODbZqbfvrpY3iBIBhyQjAFQQMcd9xxyW9JYklDBwSDhURTNMsFQRCCKQgagAoUrGCKJrjBBJH0hS98IQaxDIIhJwRTENQJlqVTTjmlsi2fpWCwUC85+O53v5utuuqqIZiCYIgJwRQEdfD8888nfxY5dRPCb2kwQSzZZrhPf/rTIZiCYIgJwRQEdUBTnBVLtjdcWJkGG569RFQQBMNHCKYgKAkWho8++ihXLAWDiRVH+DGFYAqC4SUEUxCUYNKkSdlyyy2X1tUMF4JpOLDDC4wbNy7mlguCISUEUxDUgEpSveLACqZg8LF+TDEZbxAMLyGYgqAGVJKIJgKEWBoubDOcBBMhCILhIgRTEFSBIQRAzTFeLIVwGnxsb7kFFligMh5TWJmCYLgIwRQEBbz00kvZbLPNlipG3wwXQmk4oSyMHTs2BFMQDCEhmIKgAOu3JOtSMJwgjhQ0HlMIpiAYLkIwBUEOiKNNNtkkCSVvXQqGD4kl0LxyMbxAEAwXIZiCIAcNUiixFASASLIDWIaVKQiGhxBMQeCYZZZZ0tJXhmFhChBJM800Uzh+B8EQEoIpCBwxZ1hQhCxLEkshmIJgeAjBFASGT33qUyOaW6JCDITKAsuTTjppRFwQBINPCKYgMHz+859Py6gIA48ENAErZAjqIBguQjAFwf8w3XTTJcsSozhHL6igGnL8DsEUBMNDCKYg+B/kuxQOvUEtNEZXlJMgGB5CMAXB/+erX/1qxbIkH6YgKCKGFgiC4SMEUxBkoydVjUowKAKRNPPMM4clMgiGjBBMwdBz+eWXV8QSIXxTgmpQNlZbbbVKOQlrZBAMByGYgqFH1iVb+YVgCqrx0UcfjfB3C4Jg8AnBFAw9s846axJMn/3sZ8O6FFTFlg8JpRBMQTAchGAKhpoZZ5yx0hQXgikoi7UuhWAKguEgBFMw1PjmuBBLQS1UTkIwBcFwEYIpGFqo9GRZCrEUlEEWSJUd6/cWBMFgE4IpGFqYN06VHqIJQjQF1ZCwlmDS2F1BEAw+IZiCoUWjNYeVIGgE2ywXBMHgE4IpGEoOOOCAbMKECRVLQT81yU2bNi2bPHlydvzxx2cTJ07MrrrqqhQXdAZrZVJzbhAEg08IpmAowbpknXd7jZtvvjk76qijsuOOOy675557/O6gS0goUWYklnqx/ARB0HpCMAVDyaabbjpiGpROW5eefPLJ7IQTTkii6K677goLUR+gMmKb4uQDFwTB4BOCKRg69txzzxHWpU5UeFdeeWV28cUX++igj5CwVrkJp+8gGC5CMAVDh5rjOjVQ5dSpU31UTV566aVkfSrLv//9bx8VtAFrXVJod/kJgqA3CMEUDB2f/OQnK2KpFyo8/JUOPvjg7NJLL80+/vhjv3sUTzzxRHb44Ydnv/71r7P333/f7w7aiBXYsjKFhSkIhoMQTMFQQWWnphRVfN0WTNV45JFHUo++G264we8KusgMM8xQKUshmIJgOAjBFAwNVHAzzzxzpZKT03cvgKXosssuyw466KAkkoLewopryo2adUMwBcHwEIIpGBqo7DR3XDf9T2h2Ywylc845x+8KehyVGQkmhSAIBp8QTMHQ4Cu6bjTJXXPNNT6qFO+880520UUXZfvvv382ZcqU7JVXXvFJgjbhy4cV3mFhCoLhIQRTMDRQsY0dO7Ynm+TgjTfeyG666abkAD5p0qQ0VlPQOyCUJLa9pTIIgsEnBFMwNEgkWadvbz3oJFdffXVy6GaakxdffNHvLgWDXuL3hPUp6BxjxowJC1MQDBkhmIKhgZ5Naorrtliqh9dffz07++yzs8MOOyymSekBVHZCMAXBcBGCKRgabDMK9JpgYoDLM888Mzv66KOjp1yPYf3d1l133WiOC4IhJARTMBTkOep2SzDdcsstSRQxsW74KfUP8mGKHnJBMJyEYAqGAgkmzTBvLQZBUAuJJSu8FRcEwXAQgikYCuRzYgVTiKWgXigztqdlCKYgGB5CMAVDARUdYklzyCkuRFNQBl9mFEIwBcHwEIIpGAo+85nPjBhOoJs+TEF/4MsHZWammWYa4b8UgikIhocQTMFQ4HvICV8pBoHw1iTKD+VI6yGYgmC4CMEUDAVy+P7kJz85QiSFYArKgkhi8mZEkrVWBkEwHIRgCgYeKjVZmFhKNEWzXFAWysnaa69dKTMhmIJg+AjBFAw8VGqIJAkmjaOjppYgyENlQ2VFzXES25SnIAiGhxBMwcBDBadpUaj0PvWpT4VQCqpixbQE0qc//emK75LigiAYHkIwBQOPtQj4Jrmo9IJqSDStt956Ixy9o+wEwfARgikYeGQtkGDC2qS4sDQFRdgyYqdDyettGQTB4BOCKRh4VOnNNddcFQuTKrwQTEE1VHZUZiS8QzAFwfARgikYCqjoGLzSOn0HQRHW+shUKNa6RHyUnyAYPkIwBUOBmlXyBFNYmYIiKCcakoJxvKzTdxAEw0UIpmAo8IIpKr6gCFmXKB8LLLBANs8884xy+A6CYPgIwRQMBRJM+KJMN910lTF0Bq3ye+ONN7Kzzjor23///bMLL7zQ7w5KImFknb0VQmQHwXASgikYCiSY6CHHOEz9XvHdfPPN2cSJE7NJkyZlb7/9tt8dNInEEc1wBJWXfi4zQRA0RwimYCiYf/75k2D6/Oc/n6a4oMcc9HoF+MEHHyRRdPLJJ2evvPKK312Kxx9/3EcFJWCgSsqHbb7t9fISBEH7CMEUDAXTTz99qgDlv+Qdv3uBl156KTvmmGNSU9qHH37od5eG43/729/66KAEEkRqjrOO3v1ulQyCoDlCMAVDwbLLLpv913/91wjBpC7i3eL888/PTjjhhOzjjz/2u+ri3HPPzc4++2wfHdSJLEgEhhKgfNgQgikIhpsQTEFP8/LLL2e33357sprQLHXYYYclh+a9997bJ63JMsssU7Esfe5zn0txsjK1uyKcOnVqduSRR2a33Xab31UXb731VnbooYdmDz74oN9Vk7vuuivl33nnnZe99957fneQ/a9oopzY5rgQS0EQhGAKugaV/znnnJNtt9122eqrr54qpS9+8YupFxu92ai0cNBm3QfisRitscYa2fjx49N6LTSkgB2IsF0V4RNPPJHttdde2VNPPeV31cVjjz2W/fSnP63bD+mqq65Kwqre44YdCaZXX321YlmylqcgCIaXEExB28Gyse+++2ZrrbVWttBCCyVRhPM1Vh6Nvo0Awl+EOPYhmqxYktgpE0iPvxLj52DZETZNO5pY6LX26KOP+ui6uOaaa7Kjjz46++c//+l3FfL73/8+O/jgg7O//OUvfldQB7Y8eEHdynISBEF/EoIpaAn44WDV2GWXXbKvf/3r2ZxzzplEC6JHwscLm2aDtTblWaDsOk7fM844Y+VYazmAblSI9Ho7/PDDs6uvvtrvKuR3v/tdalZ79tln/a66QdwdcMABPnrosGWAsssSoRS944IgsIRgCuoGYfSjH/0oW3HFFVP3fFmDvKCRqNE+BBQWJNJjRcKiJGGjfRJYBLb9+RoNVkyxjWXL+qe0mwceeCA76KCDsilTpvhdhSCosBxdf/31fldDvP/++9lRRx2VriX4X6xVibJhrUudKBtBEPQHIZiCQlZdddVswQUXzL70pS9V/Iq88FCQwFFTm4QQoog4xatrvxdPrPtz1gpWXHkrlrVuIY68oON3vXWpVVaEK6+8su6mOZywTz/99OxXv/pVXc1x1cB/Cgf5RhzEhxHKD2XAD1YZBEEAIZiCBFNqUEHMPPPMIwSPhIkXK14MsS5rkoSTtSIRlB6xYv2XrMiRtUpCyv+uD7VEFvv5LX7b7/N+Kp1i2rRp2amnnpoGpGxVbzX8l/B9YqiCoDx67ldccUX25S9/eZR1qZPlIgiC3iYE05By6aWXZmPGjKlYdqzYkRXIBgkoiSErqGQt8o7cNr6aeCI92xJMrONztNhii40SP6QhvY5V4JwcQ7BxVvT5+/KO341UjggeeqP94Q9/8LsSCFEGo2ScJOuA3ihYizQlyr333ut3l+Lf//63jxpa9MytgPblIgiCAEIwDQnvvvtuNvfccyehIXFkhZK31EiYsG4tSUrHPiuSdBzxpPHiSekRMgg1xNAGG2yQfHTuvvvuyuCNLLfeeuv0mzPNNFO6Dv0+xxPoZcdUJ0svvXTyoyIsscQSqVfcF77whYq4ssLM3puCtSLUUzmeccYZqdmtGk8//bSPKg0+RieeeGKyGN15551+d2kQceRvWJ3y0bNXWUAoUV5CMAVBkEcIpgGG6TXorSYRQ8VghZIXSVY4SfTkxUm8sE/HSjwpHb9JEwcWH+KwaNWa7gMHco5jbCXgGPynEFA33XSTS10dutpvttlm6Xh+3zfJce1MxNuqnlBMRXLKKaf46FyYH+7yyy9PPdQYRLIVPd4uuuii1OPur3/9q98V5KBnTRlAlEswhVgKgqCIEEwDyFJLLTVC6Mi/yFqCrNCRJUZprSDyzW22SY30CCIGgsR6RbwsIliROJZeWWVAKNHMZGHwx1Zwxx13JOuTmv247gUWWCAtfQVZVjgx4OZpp53mo3M58MADmx7hW+CrhDC67LLLsueff97vHsUll1yShiFoVU+7QYLmUsosz9uWA5ZBEASeEEwDwgorrJDEi7caSSzZOFmXrLVJYsg3wxGv5jlEB9YfBqHkt2QxQqAhmuBvf/tbOo9vBlp77bVHbHcD5m3jXrAq0NwnwaTKstfAXwkr1HXXXed3jYKedViruMfXX3/d7w4ctinO+i6VEctBEAwnIZj6DKYAsdOA2MEYqwVZhVgihNTV3ooibdNTDh8jmsKwUNDchKiyaJv52dZZZ520jjWJc1hwMCbteuutNyK+W/z9739PzVfKF5oB67UuFVHk+F0GBq9krrk//vGPftcoHn744eyQQw5JFrl33nnH7w6qoGfMs58wYUJa539h/dmCIAjyCMHUB0gkKeCXg6jxoqgoyJIkx2vi5ECNpQgHaioPpuXwLLnkkum3LLPOOmv2r3/9K3vuueeSsILjjjtuVDoqc35XDt29BHkgnys1w9Try8SkwMcee2z20Ucf+V1V2XTTTdPAnzQJ1YLfQIjefPPNfldQJ3rOfGTQ09A7efeilTEIgt4hBFOPY4USIJZ893iCmtZ8vHqZ2f30VFtkkUWynXbaKTWhFYElw1uWgHPYpV+3cS+//LKP7gmoNCUebUVZq9LE+ZyeZ+10rj7zzDOzk046KXvttdf8rqBJEO88czW/hVgKgqAsIZh6FG9RyvNFKgpKZ0US4mD22WfPVl55Zf9TuWBB8s1rsOiii1bW6V4PeaIKP6FervDxv1J++eaYTlWeWJiOP/74JJDeeustv7tvoNmWsaYeeeQRv6snsFZDnrfiQiwFQVAPIZh6jDyhVFYseaHEcfReW3PNNf3P1EQVi4dmLKDLPtAD64YbbrBJEuuvv/6Ibfygeg0JSfLKCqYyTXIMBYDPEcMD1ANNn/3Or3/96zQydj9gnynPG2Hqm2CDIAjKEIKpR8jzU2JZRihZwYSfEl/Oq622mv+J0tDj6h//+IePToNDevKEVZ7FKc9a1W2WX375St5ZS0ORHxM91loxZlI/QRMW89sVCUOadM8991wf3VPwf6BMcp0SSWFZCoKgXkIwdZk8oYRlSN37vSDycTZgLbHnahR+Ow8vjhAceXAdljwB1SvIGkdvOZBYyhNM1UBYXHvttcni1s8glHEy91ZDLEr77bdfUz0BuwGiiGZkLJ4SSfJfqvcZB0Ew3IRg6iKII1mStK6RqYuCbXZT3GyzzTZKeDVDkTXIW62sgLr//vvNnpH0ypACedi8tc00eRUqPkeMPr733nunueEef/zxEfvLwnH0Kjz55JPTMAfdhPvgWl599dVKHOM50fuvH4cs0DPTc9xmm21ST1CJpGiKC4KgUUIwdQFZkSRsJHJqWZBsYOBFfJMYSLJZgeS57777ssmTJ/voqljxNG3atMo6zVi9zDPPPJMEItc/xxxzjLI+sLzrrrvcUeVgdG8sTjQFMZdfr0HzImLp1FNP7cnrawT73DSQq0SSxlsKsRQEQSOEYOog1opkm99qWZUUePlTCXzzm99suUiqFzl/i1deeaWyzojgwgqpXsXmsZpsyoKFCId2hOGtt97qd5eCueUYsJK56H75y18mn6Hf/e53Scy1EprUHnvsMR89UEgM8SyZiJlt2xsuxFIQBI0SgqlDWHGE8JFwyhtTyQoku45VqRtCCb8VP2+ZF0IMQyC4T+HT9SL77LNPJY/pVWjhvpjIl3njEEX49jTSVMUQC1iaDj300Oyqq67qycE8+xlrWcK3jkFUbTNcTHsSBEGzhGBqMwgcDQvghwhQU1CtMO+887bEN6lR5IBu8dvjxo0bsS28A3ivYvNbTXL1VrBPPfVU9pvf/CY1w+EkzbQw9cIxnOPEE0/s67GZOo2eF3Ma8hGiZ4dQkoUpCIKgGUIwtRHbBCexJEuGF0U+kIbRqLslkixcD5aRs846qxLnHcO9gBLW2tTLfPvb3055TlMjS7CiaYsttkhChnxgwE5GQW8Wmt1ktaoFQz2cfvrp2dFHH5098MADfvfQgyD64he/mMQSIJI0f2KIpSAIWkEIpjZg/ZNkWbJCyIsjH3jRN+po3A7oSYUjtxVFtgkOlltuuRHbokhI9SLKf/zEaNbJszL57Vow397555+f7bvvvmk+uDJWp8suuyw78MAD+64LfzeR0EUo8X8Ly1IQBK0mBFOL8c7cZQQSQek23HBDf8qeQBYlWV/y8FYn6CfBxNx69nnZpjkvlHD2fuihh5IYwupEMxxThNQzsCUWpr322iu77rrrwqfp/8NHwkEHHZSdc845pefq47kw3AWWJQkkCSb/zIIgCJohBFOLsGMgqdKtRyzxwl999dX9aXsGxnoCrB9FfklUUEzsa9l1111HbPc6/tmo0m2m8r3llluSECDvQhj9B8azonmxkfkGeRbq8UaPUZ6ThFKIpSAI2kUIphbgm+CsEPIVsA+kYfyfXvBVqoX8QxjUsGg08DyqWaV6jdtvvz1dLxYjns+YMWOqWpoETW+TJk1K88vRq64IBoXEobuacPLNnf0OvQrJF8alygMHefyz6oHnwFAMEkthWQqCoN2EYGoS9YKzfkp23QaarKiM1TsOJ9Xx48f7U/YsG2ywQcWCxBxiJ5xwgkuRTzUB0YsgDGX14znZcaUkmtZee+2aFfPLL7+cHXHEEdmdd97pd1V44oknsoMPPjhZXOyAn/0MDvE4sz/99NN+V+LKK69MY07Vg3yRJI4efPDBEWJJPktBEATtIgRTg9ieb/ValQiau6zfwIoy6GD94Tkq8Ly+/vWvj7Aw+SXcdNNN2eGHH56Ekuejjz5KQoGmuWrTyPQbDKWAOMKhvQgG9KT5rVHLmfJYzXAbbbRRRSzJyTucu4MgaDchmOpEzW8KXgj54AemZPThqVOn+tMOFEzgWjZojCfyyQYq12rNVu3mJz/5yahnucACC1QsGlTciJ8bb7xxxHE4fdO8hGWpmoiw0BuOJkCOG6SxlxrxTyqC/CbfN9100/Qs2La94WpZ+4IgCJolBFMdyKnb9n7jpe1FUV5AGNxxxx3+lH2P7g/fHH/PtQLNe3bdBuLoKm4DzuaIrE4JKXutama1gslanIpAHGNRYgwnhhYgn5588kmfLMjB5y8fGzyD+eabryKgQiwFQdApQjCVREKp3l5wpFl88cX96foSxAr3BP4+WxXk38USIYrQJKj5k4BwIlgx1Q4RtdBCC426PoIVTWoKevzxx7MJEyZUjqXpkiY4D2KJyW6rwTQ0DI55yCGHpG38xTgXzX3tmMz47rvvziZOnJgm4u2F8b9sc6fymNHuyfv555+/LsEaBEHQKkIw1SBvuIAyTXEKTMzar0ggdSpYi5ONI3hLk4IVUFZE5cH9lIVz+Wuxoaji3nLLLdOSMZr233//7Oqrr8713XnvvfeSKNp2222zbbbZJttjjz3S+EOM4s2o3q2GyZFp8jvqqKN6ekBM74vENhY68twKqBBLQRB0mhBMVbBiyTt31wpYSPphqIA8sDj4++lksM7WsjTlWZu8cCKwX1YqzsG2tz6x7eMsM8wwQzp+6aWXLrQyERgRXNYmhTfffDOd4y9/+Ut20UUXZTvuuGPydSoz/UkRiCia9MpAV3scrLFwvf766353BXylGHDzgw8+8Lvajhc7XvhYCx5DbpDXrKv5zR8fBEHQCUIwFSChBBJLclCuFRZccMG+FEtYQvy9tDrI2VtO3WUD6REDRdYmG2etUuzTMAE8x2pCSXCdO++8c1rnOX7ve99LcUWCGWdwWT7KWj9oXsMCtd9++2XHH398duGFF6bhB1588UWfdBQ0mzGuEY7iZf3iOC/CDTHcq9i8Y11WPtatWAqCIOgGIZhysFYl9Ybjhe0rSh+oUNdcc01/up5HvdWs87qsNGUC2O08MVQvtY5jTjamxGCMJISRrE8a64rr4H6smJLglcjKO7/10wKmqtF90dzm712BiZJVmUs4QaOVPM1mjM+Epeixxx7zu6vy6quvZieddFKaLJnhDHoV5YsVSQp6hjyzsiI0CIKgnYRgMkgoSSTV0wyHU2q/gTiwIol7VdOXvTfm9fL3S8Ba0e3u/4J7weLCeEmzzDJLxcLEvei+JJ7UxKd10sjPiDgm3vVgnbnvvvuyt99+e1Q+KCDWtthii0rlL1ThVwNfp0ZgUFCGMJg8ebLf1TXy7lX5Ya1wdluBZk4rlkIoBUHQK4Rg+h/s2Er1iCXS4AfS601wVtQgDhAKssbIOuOFkg1qSusX3njjjWz77bfP5p577krTnPyh2NbzJV73rqEDiCvinnvuyWaaaabs4osvHpVHCvyOtZjYSr/Ryp/BHxGEjQqrTuJFjre22aA8wlK43HLLVfKQD5CVV1654fwKgiBoNUMvmKxFSb3fqgkHG3BI7XXojSUklFSpSyjI4sJULaeddpo5ejD48MMPs+9+97vJ8iS/GDmNs64lARFF3rCfZZH1jHRYQxBfvlwoqDnJWpu8mPDb/Yi/Py8UCXZEbta1HDt2bGV8JQJNmyGUgiDoRYZaMHmxVMaiRCDdN77xDX+6ngIfH4FQovJXkBM098L27LPPniadHQamTJmSLbroohWRqOfpn7EPXjgxYewOO+yQ9nE+n94GLCdeRFiR0Q9UEzC6Hyv+5KRtxZHygJCXZwj29ddf3509CIKgNxhawZTXBOdf4HkBa4Sa32xPul5FIolrl1CSdWnZZZftaadgD/fQKuhWv+qqq456vrWChBPlBesSk8iqWbOW8GK4AgmHfiHPGmYFkpaa+Nb2ZtO0JbIukV95ebTWWmslP6wgCIJeZigFk0SSxI7G3akVaNLpdYEkcMiWNYlrl1hiSVMiPj7thN+shU1TtF4tDoriy+Cfb9lA3jIukrbpGUm+jh8/vmZZ4hkwH5rEhrfMSExVs+jUS5lz+d/1S2GvFXT9YAWSRHqeQFI8vfjozRcEQdAPDJ1gqtepW0HWpH4QTLb5jWvXOvd87rnn+uSl4VxlsWl9XnrsPsYXYnT0d9991ydL+PMWxZXFXtO6665bKRNlygblCLA6MZ7SUkstleLff//9St4XBc7PaOHWImPFh136ILyYKSLvnHZpsb+hpbWIWYFHsE1us802W818w18JLr300mzatGmV8wZBEPQ6QyWYvM+Sf5nnBZparDWql6EXm8SR9VHC+rHKKqv45HXBufJQPtltu7TxjYbNN9+8sm7PZ5eWvLhq+PMSrCN4rSBrHc1zTGti9+VN9+IDjs+ID+vjA3nixcfZbYuP89uK88fbOIIXSH5fmaZs0jC9CdDLr0gMB0EQ9DJDKZjKWpdIY8VSL4umvHnfEEs0ETF5a7vgd+x6O4OsNrvuumta5v2mJy8uD38Olkya7M9fLYjNNtssm2uuuUb0/iJUK3N6VhJLXjhp6ZvwrNgRPs5aiKzY0bYVanZb59E2vkY05+bdhx0/iYBIP/DAAyu/e9NNN7VljrwgCIJOMTSCSc1pZb6ICRJKWvZqc5yEkrUsEVhv1fX6vMmL60So1oVfwVNtv9/Owx9fKwgG+8Sp3u7juSBCEBf+OBs22WSTEU11VihZIWVFT17IE1c+6HxqWlM8go8xrKo1Ldr/EvfGlEA33nhjJQ9ELw2qGQRB0ChDIZisWMr7OrYvfVUE3jG8F0Es2fuRUKIZkVGpm4Vz2nXCxIkTR+VbrwdPUXwR/ny1gh3g85vf/GaaN4546xCeVw7z4r785S8nAWN7oXmLkBU/YOOE9tu0nItrmnnmmUt/SNjA/+Pyyy+v/EYQBMEgM/CCKU8syQpjX/4MmKc0Ekv2+F5CU5LoPuy9zDnnnD55XXAOLQc52Hstgz++TAB8oRgTS8+rmsWmnqApXSi3Cy+8cDovU7qMGTMmW3HFFdOSMszYRoxMjrWojD9VtUAvUSZADoIgGEYGWjBJ7Fi/JQLrqri0zVLCitBrIklwnWqG8wLw+9//vk9eGs6jZbVQqzmpX4PPhzz8MUXBWms0aCiT6ercK6ywQmry4plh4SkSUV7U1wpqlpWY4ng7SGk9Qf+LRRZZJFkVgyAIhp2BFUzWsuTFku0hJzGltNa61EtgpUAoYV1ShabAdr1f/hxj14c91Is/vkwQGuX6+uuvLxRL7Q6UG0QV1iccuSdMmJCdcMIJ2YsvvmjuMgiCIBADLZioFCSIqCQknlRpPPLIIxVLkhVYvYgmv1VlpyWh3lGSOVbLbgf8acrElQ32HhsNZck7zsf5/QLfH5q4ZBFiPwKGONbzrEISV/CnP/0pu+qqq7JJkyZlhx56aPaLX/wi23PPPbPdd98922233bI99tgjhQMOOCA79thjs/PPPz9ZuV599dUR1xEEQRCUYyAFk8SSrXSsWOKreqGFFhrRZCdhpeN7CZp1dB/2vqhAn3nmGZ+8Krby9hVyPwWcln1cs8Hnibar4c9hgyY29vGC/fPMM0/yL3r55Zdz0371q1/NvvWtb6VBIeklGARBEHSHgRRMtvmNSsdamYi3IgmscOo1aGqzzW8SS9wPQqostrL2lXKE6kF5VoRP74MXQhbE0k477ZTE02GHHZaWPFumWXn00UeTRYhjVlpppRHHBUEQBJ1loASTmtSsWNK2Kiv5K0kw9apQAuvfYsUS3cAbwVfkgx7oNq/1PItUPXlSBn+MHK4Jdk4/9ZzzxxF/8803V+Ll6xRO10EQBN1nYASThI8VFr7yUrOcbZ6z9JJw8lYJhfnmm88nrYo/vteDFTmtDq04t8/bPPwxBPVgo2xq/bXXXqukZ7wmYFT2eeedN8Wtuuqq9rRBEARBF+l7waTmNFmXJIRssE10Ske8fJV6zWepaB4zxtcpgz1GlW+E1gXlcS38cbI4WeF0++23p6EFnnvuuVQuidt66639qYIgCIIu09eCyYslO1yADVROsj5JLK2++uojhNINN9xgztw9vBVE1rKNNtrIJ63KFltsMSofhjHU6rbv87ueUAaltU1yfsmkvc8+++yIZrogCIKgt+hLwWSFkprirGCyViaJJQkmJkRdYoklRliXGAH5xBNPdL/SeZgGw1fKhB/84Ac+aS6kpUnHHx8hP9Qrlhhw0seVhRG3rWVJfk1aMiRAEARB0Lv0nWCyQgms87avzAjah4iiYqIXkj3PkksumQbt6zarrLLKqGsnMKZONXz6bgY7Kaydu8wuEQh2njMtfVrt07b/rVYFK5rqFVA26FlUA/8zjbskPyYrosoK4yAIgqDz9K1g0rr8lqyjN5WPrEyyMCmNPcc3vvGNbJ111rGn7wp77733qAqYUEssgT+mFUETs/p4BQkeL4Z8vIIVSDwDxfFM8o4D1nmOLO3EsxzD0gZ/fd0KZWB4ANL6qUvUdNgL4j0IgiAYTV8JJiuUQGLJiiNVXrI8KRBnrVMMXKnKuZs88MADoypewnbbbeeT5uKPazbkCRAJKCt8rMhRkLDJsxJpnfN5gaS0oN9hqd/Vsf4YK8h0rL/2bgTQMg9EEfsRTSzlzySLU4imIAiC3qOvBJNFPkt5Yol1L6ZsE94LL7yQ/Ja6zbRp00ZVtoSNN97YJx3FBx98MOq4VgYvdKxQsdtKkyeSvKghcG5h0/vzSjhZ/HXo3DxjH98q8VTLabxaqMZ+++03ysKk5jmO/dGPfuQPCYIgCLpIXwomCaUisWQFE07exCOYOA603e3Rk30FSxg3bpxPNgKfvlXBW2vAChSJEPBprdjRtkfHqEnOxkPR8fp9YUWRvTa/zbUiQFrZbFfveTw+7qKLLhrVJGfFE3PEBUEQBL1B3wkmhI4VRKqcJJpYytGbnkmLLLJIRSwpPZx++umpsuoWzAvmK9ixY8f6ZCPw6csERISPI1irjG0Gk1iRAPHBCiWfBrS0+y277rprWvrjhH7Dbtvf83F56zbIn0336fOhE8Hitx977LFRTXI2MElvEARB0H36SjBJ+FgnbiqaPLGkSsj6LUloHXjggcny1C0YgNJXqrLeeO6+++609OkbDRIOWko4Saj4dZEnTLRehBU+YM+tbRsv/G/nUbRfx1pBaIMsTz5f2h0sfvvNN9+s9Jyz1lIC2wxqGQRBEHSXvhJM1ombClGiSNYmCSLEkeLVDDdmzJjsrLPOSvNzFYmTTnD99dePqkxrWbp8+jIBcWC3rSiRJalWEFqvN75o+7777huxnUct0ZS3T3H2WCuctFQzHds+3zoR8vjwww8r5VnNyvZDIAa1DIIg6C59I5hkXdLSV0KqYLRPoor0zMmFYLrnnnuy6aef3p+6YxQNH1DEP/7xj1Fp6w0SMzaARIO19tgggWHFpT3ex/l47ctDY2E1i85vf8datXQfViQpjd1nm3Y7EUBLy0cffZTyxjbJSTQxXU4QBEHQPfpCMJVpipN1ST4rYK1NTG7Kvm4xderUURUn4b333vNJUzPcv/71r1FpawVrVZIgkEjIE0PCiyat5y09Pt5v58H1NUvR7+j+tC4UJ8uSBJREI2WDdZ+n7QpF0HNSTYbe0jTbbLP55EEQBEGH6HnBZMUS69Ya4JvhZplllrQtnyWllWjqJr7CJNxxxx0+Wfbxxx8nweTT1hOsOLICyQoi8NuKs+t+fxFKV+YYrvGVV17J7r///tREecEFF2S/+c1vsuOPP35EunvvvXfEdjXs73uIk1DStpZal7iU1cnnabtCHu+//35FJBG8cCo6LgiCIGgffSWY8qxL8lNSU5zEE0uaN+iF1O0KZtZZZx1VUTI5rgex1EwznKwoWveWJLBiodp+T1F8Hg899FC2++67p6k+LrvssmRds3B9r7/++oi4Il566aVsww039NGlyLtmiSQrlLRtfZsUfB5XC9Wa9mafffZRcQSeN7BueeONN0Y0yVmxpBAEQRB0jp4WTF4sqUKySyoSL5bYRqQwmS0V4FtvvZXiu8FNN900qqJjuIM8aIZr1Lqkin+GGWbIttpqqxEVv8Vu2/1+WRaaFBlkEYf6snC99f6O2GabbXxUVfz9QlETJEH5KGtTJ5rpeO55IDytYArRFARB0D16VjBZsSTBZCsOiSXf9AYrr7xyEiXLLrtsttlmm7kzdxZfwRVVcmXFkm8uspU897rYYoul81lxYIVBK7j22muzQw45xEeXhutu1p9MTXnVyLtn5UWeUNK2hFIz1iYbNHhqtYB1MY9JkyaNSkuwQyMEQRAE7advBJNvmpBoknUJJKDYPvbYY7temfjBKWkiLLIm1NsUx73byp2lFSFeGJShVtqy89vVYq655mrps6H3YbPY/LL5JsFpRZR/Fq0KoCY6y6abbpr2+/+APzYIgiBoHz0pmLxYstYlLb1wIoAqj2YtGM3CCM1lK7V6xRJ4q4iN175aAqgsP/nJT3xUUzzxxBNV86NR9t9/fx9VE+WRzStEEVixpDQSqv6ZtCJQDqyliTix4IILpu08sWTTBUEQBO2h5wSTF0uyIFFRyNJU1BSHY+3yyy9fqUC65bcEvkLD+TyPeoYPkHXDWkGozDXwZZ5lROuNsM8++/iolqFn1GpefPHF1PuuEaxo8k10IAsT2wT/fGqFMiOMF1kgAf+0sDIFQdBPUA83Epql1eeDnhZMrPtKQYJJzXFy9GacJfbPM8882cwzz9yyDGqEmWaaacQ1r7DCCj5JBX9/RSHPp4bABK1MnaHK3lbwFisGegHuqZ3stNNOPqomNo/ynOYlQpXHjTTPlRFN3p+JOCCedSuWvHAKgmD4YJgWBmaeMmVKGqKFeuGnP/1pcqOgR/a3vvWtVEfi34tv75JLLpn8Xeeff/4UmMd0jjnmSAHDA0HbdKBiDDiWDACNa4mCb+2x2zbO1te1go7JS++NKX6fXYeBFkxWLCnjfGWih2AzSMIKWjWKdKO88MILo64VvOVAlV+ZYCtoWTdUcePcnle518vJJ5/so9qKnle7+eMf/+ij6saKJC1t8M+rFaGI559/vvB/UevYIAjaDxZufGgfeeQRv6sQhk+59dZbszPPPDPNdUrP44033jhbbbXVkriZb775klihAwmj/vPhZYVLrUArRF7IEzkKeXHVQl56DSSdJ2pUj2vdblvRo21/biusdF67JAyFYCrKIAWbjqXiWNpzdQN/rcwBZq8LEE9l/Za4Rypp2xykCtyft6xgyhNXFLw999xzRFw74dpbIWbKsPnmm/uomvj8EXmiyT+zVoU8iD/iiCMqafJeUkEQtBeGUznnnHOy73//+8kNBOsL4gARQmcfpuA64YQTsqOPPjqNR0d9hGUH4cMAy+y3/19NhWRDNTHTrYD48nEKedeqvMi7H63POOOMI86hdW+N13beOWTt8sf462mWnhFMtaxLVpFascQDGTduXLbccsulQRK7JZRg/fXXH3HNcpb2TSxl/ZYkGvMsHMQLW7lrvajCB2ulElyrPWe74bf4cuoUkydP9lFV8fnnRaaeA8+o06IJKO8+bZnjgiAoD01dEydOTIPnShhR50g4IJCw+PjmKRtIYy09Rel6LViB4veVDUUih/jppptuxLmVhjzCkqa8Yomo0hLDAfFf+9rX0vrtt9+eNACtLd/4xjfS9FKyLlluuOGGNEbh3HPPPSK+HnpWMPmMt0FpcIJlmWdd2mGHHczZ24+/Rh5oHmXFkipognptycJE+/SWW25ZShx5fHMSFS/mYNhoo42ypZZayh3RHhhUtCiP2snLL7/so0qRJ5gEz8V/2bQqVOPHP/5x1ZdZEATl4B144oknpiE8FllkkVS3IHAQRwSJIv5XNr5WXTWIodo7xwsg2zyWF6wBRBpAx2ufzqPANvHUVfPOO282fvz4ZMXCd1i/ryZLNV/yrBjOZt11180uvPBC//hL0xOCqUxTnOKVFgc2Vbg4plnUa6yT+Ov1ViUo2wznm31sZc0Sld0o9ryyjtjKH9X/6quvmiPaAxYf7rUbHHbYYT6qbuzzsILWP8tmQ964TMTbdYJeFDYuCIKRMCUTc1biH4TTM81jVKrUGfxneCdakaTmMcVba5L/rw5qsPfqmwuL0mqpOl0CyRpG7LYVTPYY3qnqROV/j7oKJ3aaRWn+xOnd+wq3mp4STFZd2oxXsBnPPo4jYK2wLL300iO2240vNFtvvbVPkvDp8oIVS+AtG6Sp17Jk0+vc9IKwflEWfoOed+1ETu/dAsHdDF7MWv8y/0ybDXni2+LT2xAEwwgTWJ999tnZhAkTsiWWWCJ9ZHqLkSp+K5JkwSBUEwbDECSOyBc1oWmbgMjEEqe8Je/IV/aRln3CNo+p3qaJzKJ4PQN+C2MIPfg+/PDDEem6RU8IplrWJYIvuBwDrNsM5IF1En+dCp6y055YAWOtP+QNwyXkiaV6hBMBx0OJJQV7DhzVyd92O2Xn5VMn2W+//XxUKfwzsMJJ69XKciOhFjZdvccGQT9z9dVXJxeMFVdcMVWwVNh5zWfWYiR/Ioki/5/p5yCxIREjIUNAyBAkbKzVTIFtiR2JGJEnVhTn0+aB/5AseghZ4BjqNtXxO+64Y13n7CRdF0xkhgSTf/B6+PoK0JIKnuPYVnOIwHLSSfz15jWhgE9H8PdshYu3MLGN6bERdE6+tuz5JNDyrEw40K2zzjotH+Xbwj13m7vuustHNYTylaDn2MomulrYZtR6jw2CfuD3v/999rOf/SxbffXVsznnnLNSuavi9yKJ9+sgCiIC97Twwgtna665ZnJIp1Xjhz/8YbbrrrumPGLWA3rTHnfccWk+Snr04buDK8SNN96Y3XHHHdmf/vSnNAwO1rhmKSNquG6GTfBI3HEvViD1mliCrgumPOtSUQEnrUQTEGehAHUSf30M7pWHT+eDhEuexcKeoxk22GCDEefNE05eNJHPZ5xxRrbooouOiG8Vzd5TK/noo498VENYC5PEqH/ejYZ6aObYIOgWf//731MFz8fdqquumpx61blH1iHWbbMQ5Vsf1kV1Rz8E3RsfqzRDLbDAAtniiy+eOubgq4NzM07LdM5hMMqpU6f67OtZeI4e+fSutNJKaduLpV6kZwSTLzwEL6KUocTzhYGDl81g0nQSf7151OoVJ0sE95QnlEDNj8Lvr0WeFUUCqZpguvjii9Of+Mknnyy8v2bgnLwge4VmmiBt3uk5rrLKKmndP/NGQy1fJiCdlj4EQS+AP8oVV1yRxn3DqoCLQF6vNLUq8A7q5+Yzrpl7Y0gCROAvfvGL7Pzzz88efvjhln2o9TrkgwWxZ+v0XhdKoquCSeJHwqjan0GZS1qW/HkstGN3En99dEnVerV0PsgSYS0+dh2s81y9MNEtSGTp/IqTYLPiyWLviT99K+G8jTYztguGbGiEPBHL/cnC1CrhVBalbeTYIGiWBx54IL0T+X8zWjXWEvxUeN/JKqQxjIjj3cI73Zf3fgnUT9wLoogmQ6xk+IL2CoxPJItcNyCPLDJuWMFkhVOv0lXBlNcc5wP71DOOIEsS3UFBGewfSLvx16k4S63pTyRWvEACVcDeulQvt912W2XdV+oST1YsecFEF1wGBuNlhqlY+d4KOCcvmF6D6UeaQc8TM7rNY//8Gwll8MfUe3wQlIVJxWm232WXXdJ8ZfRQptcyXcFxLpa1SCJJzWr9ai1S4NoZ+4e5SzfZZJPs9NNPz/75z3/67Ok6TKAuMbf22mt3ZMiYPPbaa6/UzCjeeOONvhFJlq4LJg0R4AOZyFJiSsJK8WAzWh73ncBf6x577OGTJHw6ez8EVaay8MjnxQobnPga5ayzzvJRI86tit2GvKY5rpWBMlnSFt2qpk++xPQse41LL73UR5VG+SeRJFrxBV3UqcBCOr/UehCUAevIH/7wh+Q0vO2226bmZSo8rERysFaQhYjQq01nXI8C16uu79ZZ3Kclni7zWMfoAMNEtjgtU9n3Ojh+cw/t8j9thM022yzlvaD+9saQvNBLdE0wkRHeumT/ZIqXoFJaTIs+I73lpN34P6PiLGWsS7Lo2CYx3QtLpWuE3Xff3UdVyDunfps89qKN9uYXX3yx8nzoZdGK5rk///nPo/Jt0GA0WitIyedqFtUyoR6aOTboDxA3/Jcuv/zyNIAfX/PbbLNN6ujBRwlOw1SczErPaMdYdTVpN8391hLUbNnsVlBPK9tNnngEnPWNIjDtBt3bsQDThf28885L802ecsop2YMPPljKV7BXefrpp1NeNGNA+PrXv+6jWoIXQlYoVRNMvr7vJl0TTNWcvRXYry8CZRrxPgOJ6yT+OhVXLY0NvKjUI0KCCaxlhz9wo909t99+ex9VFYk1iaU8K5OsSvaeWyGafL4NEhKd5J1temW9VtmvZo0qM5qt8tUfG/QfNIn/8pe/TN3HmT8LKy+CxzpIy7pje43pmbMux2lrFVLQGD0Kvsz0SrBWIu6Ba7VWIlm3WEcI0jGIsZn4zyGGNAXUoIK7BPlRL7Y+/epXv5p6KLYSL3q0LpGkOCuaFAd0DKCpl+ZPyj3XeMABB/zn5B2ma4JJf1b9EexS67IusU7m8QeRKrUwlkSn8H9ixYGc/PKsS7aC9MLEWh/s7zTCaaed5qMK0W9qqWvKaxqEY445JplV7b3zTO6///4R6eqh0fvsF8hDXtw2n/WcfRnJKytFweK3PdWODXoDOmcwyesaa6yRpuygYkAAUBYkCqw4sgKIOO3XwIR5wVpZrECy4qmaUO9EkCCyvk7ES+T5PMBXiq73iMmDDjoou/fee33WDjxY/MkzxlpqBIkURDnlr1XkiR8trVhCEGER4/nyrqSsSviqPPDc+U/gH3fSSSd1rVm0K4KJjCJzrEDyfxotZYliSQb6h0DGdhJ/rYqz4sKnscG+nHxTjSxNzfjP1IsqcFuZywLirUzqYaF70aCWOBMyC3QjKA8HGfKWP7uP09KXEUKtiqss/rh6jg1aCx9Sl1xySRpUkHeXRtz370FZTiRmJI4koKzoYZsl+yQ0dB5t51mWrGCyQqpWuWtVsNem+9I+4nWNOFYzGPGSSy6ZnMr33Xff7He/+11P9UDrFjhwkz/+3VIPqksZ3oDn3wpUR/vAwJlYwfCDs4KYsoCfGH6yyyyzTOWa7Lm03m26Ipj0p/V/IBsnZUkcGeXFkuikYPJ/esVZqo27ZC1KVpx4C5M/Z1kw3deL/W1rZSLf86xMfIG8/fbbo/KBiQ8b+eM2eq/9Bl/Cwj7rIsFUJliK/C78MXnHBq0Hnz8meebrma9mKjaJHJb+edgg0SLRIOsQ29a6ZIWPtSIVWZaUVuLK/26rg/8NroVrtr9PvpA/VJQMyEivrilTpvTVoIzdAJ80niWjnzeKFTM8i2ax56OTgDoISBzTpPa9730vjT/lm+OKqLavG3RVMHmBZP9c7JNokmASysROf2X4F4JCmTRUkNyLRInEoOeaa67xUaVgELhGkGCy6xJ2Wlo0DAD3ZL9GQWKxHkh/3XXX+eiB5Lvf/e6IbZ/feeLJ5rH/+i8SSR6cf/15g9bBNBM77bRT8pfh/0El4S1CrPtnUBQkeiQuiJN1yFqEWJflyJcTvTv9uQnEc4y1LOk3fdq8oHNb65WuS8KQc+FHZK9JgojpOd555x2fjUEJHn300ZTnjfrwkP9C4ubHP/5xZTLyRgUKH9L0KOQ5y/KJY73wxo4yYqkX6Zpg0h8vb2kFFRnKlCfeIQxI2yn8S0NxHp9OgUqRwiQhAt6ypOO7ga6DPJeVScFbmZgC5oMPPhjxzOx15wnBIjgub9j8XuSiiy7yUXXBvSovZdGzQWlsUEXIkmfh95fFH1fPscF/wGpEN/vvfOc72YILLlix+lgLEPkqMVKPSPKB522FjM7nrU+K9+KIbeKVRtYlCTjEDOUJKwDvVoQelh6JKTX10KtukUUWSRYDrGXrr79+tummmybxz4S3fKgxifXRRx+dnXzyydlvf/vb7LLLLkt+NYycTwX/7LPPds3nZJDgefFcmoHyI1SXUl4aFS4LLbRQpbypqdkG4c9v9/t9vUzHBZOEkP8CIs46eRMUx7ocvW1G22aOduNfaIqz+JeWDbIkSJCokpRQYfn666+PEidl2HnnnX1UXegaFCSU9Ky8lYnuuMB90fbMC1j3LuwfsxqIJZ+PgwoWUQa5A2vVs2WhWhnKC2Xxx9Vz7LBxyy23ZHvvvXcae4ceOQgHWXPIN2ud0btM1pZ6n19e8OfWu1DbSidRxPUx5caPfvSjZHlgrCAEC1Ma8WET9DeM/8Rzvvnmm/2uukB4C9WjWPcbESwIY8ogwruWOBokuiKYZKrWH18vAvWAI04WJURRnhpttMt9I/gXmuLgL3/5S2E6AoKClylB4sNacmRlsufsBroOCbs8gWfRdC3LLrts5V6XX375EffAeCfMiF0NmiC7ed/1cuutt/qouuBe7TO3+S7RZP8bCkUVsR9ioKiZzh/XT3neSsgfenX+6le/SsNvMK4b/1HKuJqWZNGx/j5WJBEvIVP0XJoJej+qqU1NbPiA0JPJP/NgMNGYSrxj6+XNN99MS1t3Un6E4ilv9QocNbv5Otmu13vOfqErgsm+HHgRkLnqDad4L548xHcC/zKzAeRHpZmXbVDlJ+FhrTiqIEGV53PPPfefH60D9VRrFltxW+FEUHOQZeONN05L7pPJNB966KGKnxlx+HUAbeO1xvXo1LNsFcwU3ij4uYAVTXZblgQ1vZQJZWn0uH4BMUTHh6OOOirlJXOYMX4LTU3yr+C+ZZkhn22TlwQSadScJV+iep5HM4HfpdmFcsLk18HwQY81yl2jzW+UIyFhxPhdFgka5s4sK26Y+oX/DoOhWiEm/PYg0lHBpMpALyv7dWYFk8QSga8/8KLJb7cL/0JT8BBnX6rcm8SG7psgoWQtNqoobQXaSVRZqzkOrHVJgslfHwKJ6RPwWeCe55hjjkpTHNuMNgxUYtWaT/Pyc5DBbwSsaJKIts+BpS93ecGTZ4HwxxQd2y8w7Q9CnIpgzJgxqYJRs1meMLKWI+tzpLRKJz+hVluOiqxR/Baijg+OXgMXgXPPPTfNE8fQIYyVg08T/2VrbfN+Uspb5TkVP9tBbSjLlIm//e1vflcp6G3I/H7CWpK0raXvwl8NdejJE0rDRMcFk38ZSTgRtK4/1y9+8Yu0tA+ZgEWjU/gXnOI8Pp1EhrUqgbfUAJVkI18TDOvfSlRpy7JkhR7345vldtttt7RUfjA9g56hjRcSUx6frh+46qqrfFRpqEiEBJPEks17tvMqWR/KzC8HeQOq9gt83TL+zhFHHJHG/CoSIAq2Oz15iZDSMZRDhWrnaDQUXRtxiOW11lorOUN3i2eeeSYN8khzpIY8IFhLG/lFszs9nVZYYYVs6623zg455JDUhP7aa6/5Uw4NuILIkt5KyGfE+tVXX+131YX/MFWdybPWtpaUSUs1IURancueQ1Q7dpDouGDSi0MvEdvsJrEkwaSHBPaB+AfdLvwLT7/r/UTuvvvuEWm4flkJFKz1wDbFWStDL+CvWWKpyMpkvxy5d5oRqMCvuOKK1KtI1hRh0wuOa6Q5sttccMEFPqo0OBbnofIh0eTLX1HwFMX50E348GHuLvLx4IMPzn74wx9m6667bpr7jM4AdoA7KinyQxW6vw8fJFqKxEurggRY3m/I72ncuHHJSbZTIGgQRDTr4RDOtdkmSCpV/GKYVPfKK6/0hwc5MEcfecezLvuBUgaEEudk9OpmYcRzD/UmliQfZwWTFUF5UI5tPSz/4mGkY4JJTW72xaJ1/3JTcxzm9jwVS8HtBP4FqOCx+/gqk+iTxYAKkG1rcbIUWV66gbWI2WDvyYqmPfbYo7JOpSf0Fca9Pf/88yOEEs/PO8tTqQwTthzZ/LTCWuXFl7+84PGiXvixdpqF36H54IYbbsgmTZqUfCIY14Wu5/ivUTHTBR9LBpW3mmd805cVRWrW4VoViNNx/t47ESSMCH4fgXiumXVG8KZnU7ssMVhymWB3pZVWSk04sgjp/UlnCyZ9ZmyoBx54wB8e1AET0ZK3PFMsc60AKxX/BcrzGWec4Xc3DGXPQ51JmfBxBD5MakE6rlPHKAyraOqoYGJYdC+YCDwQWZr0MKyPUrcejH8pKlh8M4dtUrECSXF5gslbYbqFF0Ncp628dU/eyuT/kEJfTeQLI7yK2267Lfv2t79d+fLhvD5f+4Xdd9/dR5Xi17/+tY8akf8qJ4rzZdAHrJy18McoeBg3BwshTTA8N8beQfjgT8gYXFgobPONxDRiRr3KdG6EBHHqgZYnhuy5JEr8e8JfczuCRJHeS/5elEbCjm2uneeEPxXjDrUC/LNoAuO8fIApv5RHVLb8d/Atuu+++/zhQZMwxpSc/rF6tgo6I+j/0sz8m0UwgnYelFMvePKCx++34fzzz++pD/1O0VHBxIPTi8aKJatgJZ4U9CC15MWR93DbgX+hgneo9b3jEBQUJC+WtM0SvOjoFVRBSyjZ61dlpopcFPlSKc+YsJcJRXlJ2Lx89913U+XDl47ihgnbzVco75XnVkD58uhDWfxxOOtbESQRw3+R5yNrkNJb0UDgGAUvhGxFr8rCOmYTrHXJX1srg8SPxJCunaUXRja9mtYIOD3jD8JAjc00zXAsE8YiiCQmuQ6sQ5QLxus65ZRTsvfee88fGrQYuu/jeM/z5jnQC6xVYEnHUMAzZjqTIstvszDuVh7UlZRhu21DEdrPe1vbWlI+e+Ujv9N0XDBJKBHkt2SFk8STLExa6oHZh99O/MuzCJvGW5K8UMoTSZpqpNew1g37bBTYb+FFUw0qG56zLCE2T1V59iv4gjQC+eGxViYrnAi+TPpQFn8cQcKIdf0fJXTkEGwFlbUuWVFlRYkVQta65IWV4lolmPSbuh6Wuh+WeeKINLoftkk7//zzJ+vaMcccUxnXphnw2dI1EBiaAz+/oLNgHWFAUpVLPhYOPPBAn6xhXn755SSsOTeCuNmx28pAmc1DgskbHmqJJu1j2Bx84WS8oPzSPKk0w0bHBBOZqya5IrGkhyLB5B8y4A/TCezLVNt52HTWqiQLjbXUgBdNReftBaxgkhBU5eOtTPhsVEOVktY1US/+LYor06Y+SEybNq1wJGabt1Z82/LmQ1msdUfBTg5LQMjIEmSbprRtRZC3KHkhlCes9Lv+fP66agW9Q2zQ7+QJIwK/qWvDooPjLaPXM6ZZkTN+K+CaerVzw3nnnZfeuXzAYXEkT8aOHZuEBc1/+Bjik4ZvGh8IP//5z9NUKIwU3av3xHXhx6XZCCSGsZBgIWwlWHhorpYwZ7T1TsJ95SHBpHWB5ais4OF4ygb199lnn136uEGkI4JJYkkiSQJJIkkFWULKCib7cBqdcLAR7AtWWD8RTKsam4JgLUlgLUoSHtZ6IBjHqFfRPcjSYYWTRJNFo3/noecL+GfceeedqZJW/rLEd4Pz4tTab/iJdcuiPBG2nEhoK69rCaayTURKbydHRWSwlB8S2xI93sJkLUJKb0UQ96RzSAjpmGqiStdgg0SQhBVpJOS03x9jj5OAwjmacYSYAPawww5LvfOC/4W53vhP3nTTTdmUKVNSrz6aBBnGgdHFmX6J/y0TOdNkRRMWFrjZZ589DQqqZ6OyIOuefSbspx5g/jEEKs2OP/3pT5PwotNArbGHKN+MMcSQHscee2yaCmb8+PHpOrgGzm/LGh9lOG2fdtpp/lRNw4cOY1PxO9wnIrOZqUuo52x+kX8Iu1133dUnzYVj8rCCSdtAnlmDRDURpP2adWOY6Zhg4qF5waQXmgSSFUu2KU4PqahQtAP7R89Dzt5UZFpaixJ4oeTFUq+j67X3RqVtrUxWNDG+TBEcy7NmFFvQy0EzWtt8xidKwnPQ4asUfNlQvkoo2TJky6YPZfDHEKhorCiRGGKfxAlLCZZqIsgLIf3fsebwv+aZ84XLSNxYLHCcp4MAFY6Or2UlIlhhxrm//OUvp4oYCwiVPb2a2uUzEtQP/lg844kTJ6b/OHP1MZ0SVmYsW5RzxLmslr5ssZ/yowmBmT+PTgknnnhiTbHVDJQhRCMdHyTWuc4tt9zSJ22IvHJttynjTGxbDdLl4QWTYGwtK5iqwX7uuVa6YaCrgonCJ3FEvKxN3sok+CN1Al+A8wqc7x1nLQJCIqNILHGv9cCXcafRfbHUc5NgkmiySOjmQT7xNam84MV37bXXVibg5etW8GXLl2g/QS+YRrAj84ItM7Lo2W1fNhX4D9XCH+OPV/D7itLJmmAtU1yvtUT54MWVDfY3dF5ZC/jipnlo8803z/bbb7/UDCIBHgStgBHXEfG8x/RRwHLJJZesDKTcSvL+Wz6O/xTxDNhaBO/QPKg/uQet2/p0zTXXHBWXh+rvMmkHnY4IJgqfvhYlioCHIEuT4hXyBFOnsIW1Gkqz3nrrjRAWYJdWOFlqnd9z+OGH+6i2o+uXD43WZXJXnPAix+aDDRxjm/C80FK54GXRL9DbphGKyoHyThYm5XXeS7VMeQWfXtYj8p8vfRw8GfIB3w+GPsCn56233vKnaQtTp05N1gcCA6A+8cQTPklHYERxLApYQGi6CAaLyZMnp+ZFnq2a1PgPUEfxP8DRn+bJduP/i3n/a1l1a/23i2a/oP6kWVL1qK1PVc/m7bMQTw+/oIOCyQsitlVIJI4U8pQsJthO4QttXmG1/ku2+cSKBwmDIhiPqNexgoklz85W3LIyWTFIs4iO1dIGjtN6Nei6SpNVvwmnesGx1mLzxea/tqtZmco0Qfljisr4IIMfDMMD0LQiiykWLrbxR8FHhy96/OraDRNVI9AY5ZyygJ+PPkhUiQaNgd+pLJtq5sXvirzGt8kPE9MpeEfa/16eWCJQLpt5/qpHcXz3dSrnzatrPeynCS/ogmCSNUmCiYdhLUz+4emBNlNo6sVXIix9RaTpUPCbUKVmRQHUEgS9jq7f+tDwjNQMoz8zSwv+JDYvJCRxFqUywIdFlT5WhWpQLigf0Mky0Cj1+jXge4GD7QsvvOB3JWweSiwpP/3LlVDG8Zt0eaJrELn33nuz73znO0l4U2mqzFJpfv/73y/M91aAIzWDf2rONjm2y6qnDwEc0mlqRKAdeeSR2T333JO6cweDi/5zdGSijGyxxRYV1wQFlZVmhjyw9aevWxn+AN8xH5+3rWa9YaftgonM5qFbwSTLBJWnRJIsT9rnH1reIH/tokxFon2Ydb1IskLJbwv8d+qBWcO7gRU+aoqzook8YOmtTDhz6njgy451vlT4kpf5m2OLYOwbKhOcLSWatOxV7GjPTEuB8/EOO+yQHOLxg+C5q0ePzb+8fFDe2byVeCoSTEXl1eOPKXtcL/LUU08lJ2JZPclb+UpRIdDEeNddd/nDWgKTAu+7776pB55G5ZYwY3vhhRfOfvCDH6ReYEEAtf5zOLKrHBelqQfVr3Zb8N7hQ9bXtx6uQ+ILaqUfVDoimMhs2yTHuvbZOAoJX4J6MPYBdQoVZHV5LyrYisfUqUrMigsb8sg7ZzW+9a1v+ai24ytsiSYJJpmRWcoKJYjnOHseRAP5SkWCaLB5gPCkcuErCzGF5Y6vcglojtEz8X5Sneb1119Pzuo44WOlWGONNZIY4nrtiNmqOG0+cW/EqUJXulpCkLzkOIklPQtbRvUbZcCC4Y/tVV599dWU13QhJ4+VryqD5Dl+GvSWamcTC5ZAfLzshx1lkjkvsRIUjakVBKLsfw5/yFa5IagetUMJWGgerCWE+N+VdRIfZNoumFRZSBBZXyXfVMcSXyX/UJiFmW0JrXZSpkDb6VAohLYSs5YAv22pd4TvVsxmncc111yTrCKIAN/jyF4z6zwfltwrlZXEk76GEDkMbnf66acnx138MS655JLKeegGvM8++6RnLItK0QSlCGeet3pOCSaubHTMI6BSe+mll7I//elPyaH5oosuSj33MI0z1gxNagg7LGTcJ003VMiaNFY9Z9SrywojdWzg3iSM1HuMeAVbvpS+lgVE5Yul8h1Y+jLrm4+LIK31xesGOJQziCD/b6zIylObv9wvwxDw5d3MWDdloYxtv/32yRqo50v5ptJgsukiB9sgqIX/r3YC1af8XpHY8XUu2KEa/PE+7bDQMcFUVFHwwpeYsoIK7IPuFGUKs/yXEEtUOFYw5QmnVkB3126ie1KFzbqakvQsra8TkEfMpYTYwEeDCpC8s4KnWm8UfD84xyqrrDIiXk1ZcuJkqSYuu02QaGFp4yR+7PhDtYLu1ZZl3bsXRD6dTW8D16EBJPPwZUk+TGoeVV4ocL5agkm/5a+tHfz1r39NgxNihZFVUc/DiiF6LV1wwQWjRHu74WMBCyFllOfBtfE8GCOKCYiDoFX4oWja9Z/zqB7lf/b444/73YX462NoDw20nCewhoGOCSYbVFnYisZWvLYiBo7h5Upcu/HX6guNTcNLnsq/SBQVxTdCq5sa6DJOEwbjHR166KHJD2OvvfZKX9C77bZb9rOf/Sxt45ux1FJLJRF7/PHHJx8krGNULOQBFY21oKi5DasM4kTPP2/aE46zKC3xOMwCpmmaQWiWEbI6kU6ixwsfX9aqBf+884Itq7pfe982reI4hjwgv3CEJy+xnNHsKCGkQL4XoXIkoSSBjujIa5Yr4/gN/rhGeOedd5J1bqWVVko+iba5jHNyfVjrmEoD8dxtGEuHa1KZoVzTrNqpoROC4YV3mv/Ptfq9XkQZK5MH/0uLPb7sOQaNjggmW6HYbTLd7uPlJVHEi5f9Ek95yFzeSnQtWDWKKhLFI5jkw2QtAVRmgwb3xn3R7EaXazuthg0SEla4UDFdeuml/pTJogCM/8NozzoHkzsyFo6g7dxCGlXIshTZStqWMStetF4r2PuQf5GO12/rN3FKZ84tfJhovmNdeaUAXiDZ8iJqWYasYNLx+g3/HGrh05c5hv8jQlj/OwJCkHtnHrZWjLZ84YUXpnFwWglNwTwvnh+WrkceecQnCYK2w7hi/j9X9uOmWSRycG/xw5hUw/tR8S7mukMwtQFVNqpoCIgilnxta13xjLvDUi9jCag8YeS3W4Uv0HmVCRWVLeyq+MoKJvx8egnECtYk5i2i+YTAnFE0o+G3gThCHEhE+LzJC6RVkxnbWFYQl5YJEyakJU7c/InpTSYLhUeT9AJp9BssrYVJ5U1Cm3WJKVWaXBPXhomZc+n+sJBgDWKb38PqxjYDGCKErFCRWLEoLk8M+TLi9wM+VNWwv02wzXPkgxVO1dB+/8xqwQjIrWoafvTRR1Ozl+9Zht9QvUMz5IEfkiyAKmdB0E3wm/T/uU5aXSVyyvzXBe9I77NH5wv+V140+e1BpK2CyVZgtoJTsPESTzwgWZaIB7btV2078QU6D+2rVjFWo9oktZ2Gru+M/YJAoqlIliMqGw3qp+ck8UrFVks4ydqDCGYdywSCBNECjOQsYYSfi/zWuBZEih9GgnylMuWa8Dnh3IgaxnFCbGncGi9atA1W4Nh9Pm2eVShvW+QJJ3xjdC5/vF8XWKvKYv3FlNc21ELpyMOyxzQDvg/0gpSvGc+bOd/effddn7RpaMalfPoXfRB0E8ql/5/eeuutPlnbkJWJd6W3HFVD9bCFdzDx8kEdBrEEXRNM3vdCFgzWlflUzlSQQmLJiya/3Qz2mrSNo3JeGvAVoK0Ei74edGynuf7669MM31j3EDLqiYSI0dc4z0F+SVwnS56j9tv8yQtKQ+XIcPpYrng+zP1F5YwQYhJOD019jLuEYKbLvuA6Qb/Ptey5557ZuHHj0u+Q36eeemr28MMPV44BPQsrZqwQ0jJPTOVhn2uZ9UZGpi9bjq0fk22is/+pMvhn12qwFPHcKFOI4OOOO84naQvtuJcgaBZ6Ivv/HP6jnUSiiVYOfA8VV40HH3ww993EcdwDI+PrvINO2wUTGWqbR2xh4SHYZjkFNcXpeFkf2AZrbcp7kM3gr4VQJJiopPBjAi+WqsGx9fLiiy/6qEIYTA8RQRMK1hecsMl7+eQQ+MLQfWifzXMrdBWsaNFzsb3O1PQl4aU8wbKEvxI+PqCvG8QRFenzzz9fmTwSUaVxdQAnXcagYlgFzsufU3nPb+k3EH4WK4aKRI3FP7+idBZ/jAVhWi95TZEW/VaeUCLoGZA/tfyh9Izt822kXFoYnoHmVcoJIpyv0E45tQZBr0Mzsf+/MQp9J7HCht+nWbwMuG3ktYxwLo1Qzn/+8ssv90kGio4IpjwLk4/3/kwEKVgh/ybRarEE9vpEkWCyFFWcefhjy8CEkXkwjtIuu+ySepKRP1SYXhTJQmQtfnbdPhe7n3NgJUKk4Aciq4a1blihpG3WFU++6EXBFw0TFbMfvyCZc/FvwvJEWq6TihYQiWuvvXblfF5cSzABy0bytV0wT1W9eNGXhxd1yhsJKOVNGaFi8zKvTJcBK5JEM79Pz8sgCEZjxzxTwAm700g0EXjX0ymijHUIH9O8jzqdi57XvKN5h+e1IgwCbRdMvnKmkGgpQeWDHoD2t8OSVIS/FoW8NCArQ7sFE3MN0axF4Wb8JypX5ama1CSKOD/xViTZOCuQJHSwQmHtQRhxL8xrxTq/Rdhkk03SFBO0udNkR5MYU5ZwDixFnFPdyvkNVaLKGypSLF+kY6wd/b79akGccQ1UvPgrcT7+gFwLTXP2unEg988AZI3sNn/+8599VE1wsK+FLW8SrfJnYlsWprKCSR8ltkzXgnIhXySOj3nPgqAc9r9GqHcA41bhRdPBBx/sk+TCwLH874d1qp+2CyZVylYcUcErniWVnK0M8yxMrHvR5LdbgS/QChYqc8XXK5bAny8PxuxAZGCRoZs9IgSRRIUooaR8tUKJ4IWR0itQ2eEzhJOx5sITWrf3ZStorVNJgypsVdaydmhdoonfQRzhpC2xd9ttt43KX8bzIa3uj2dsxZisZvLXQehZrM9bv1HmK8/ixZOeD/lSTTDZcv3jH/94xHY1zjnnnMrz2HDDDf3uIAhqYP9rhDJW5XYhwfTss8+ma2HWgzIwGTDvdaYKGjY6IphUUauQaJtKXdv6MibwUpYYAIklL5C07eObwRfoPLSvEbEE3K/lscceS87RiAXuhXPLMuQFkRc/Pk9tvPIVwXX22WdXRlG2widvG6GGYzjNfDgHUjnKV0tphW2e4xolnLQtwaTJeBGbWFJ03TS5+Ty3wYttgkQB4ohxgFi3+PwdVLxYUhzrvhk5D5/XPh8FI64jVBlaYdq0aX53S8CPjbG3CK+88orfHQQDgf+/qY7zMJAqfkP4B+kjhfRa4ojdLNbKpBYdPkBr+T8KPoAxfvz973/3uwaWrggmiQFtWwsTgyJaU6H96q4mkPLiGsEXaIW8NBIO9Yom7gufJISMxhCyfwgvfPLyTGnVFId4wGJEsxb+Qao47RLytu2yGv4cdl2iyTYRyRom0cRS1kWeF015Ejy1gixLHM8fVdtYnlh68kYWHzRsvtvnUK9g8usCAU8+t3ocI75oKfv+GSuonPOcy5TLIOgXfFnXfw6rDc1zfl9eqGfgyTJY0cSHMu9Y3s1lBtVkqATS8z5nnKlBp+2CqajyV8VJsIKJfbZXnN0uQ7PCyRdOxVk/Dawtdn+9cJx6EtUSSEon8cn9MaAkvZHoeaapWWwAK2hspVOrAqq136OKmqWsSrIs2eevSl09KpQHNA36UcP9ts5Lev0OS/bJfwoOOuigynUxUWu1Zql+pNqz0TNQKFM2lcbmNSC2yFNZFVsBTqBlxLHKud3mGcfUJcEg4Mt7I6EdWNEEtEjIpaIMCCfNx0gHHvxVB5G2CiZZibwYULy27X6JJzXLgZrj8ixMzQqkPHzBzCukSuMFSRk4Ts2REo/cswQG22rWmnvuuVOe4PRNvum37O/aitJaj4qotb8IRgA//PDDk+WBnmwbbbRRaqKRVUNihnVrXZJ40u8ikqg89ZxtOdC6jScoP6wVBei+Lz8mCSeR99x6lVZ0L9bzJ/i8yEOO8zZAK/9TEydOHPUbRcE+fwU11fOfCIJ+wpflVoR2YgWTaGTwVzonYZnm/8y0SR988IFP0rd0RTDZilIWJO1nKYdvYD/rXiy18qXu8QWUpbdWNFOAJZBkZWNJcxrzceHT40WY1iUShN/2NCqMyuCvT1Yf7/DNtv48hM022ywdw1AIPFscvLl/0tETTkvlr/3Csfmi5WuvvZatu+66aV3P49577/3PAdl/8rofKCNwqmHFMkH3Xe1lZct5M+U5Dzor+HNXC3liSeVG26uvvrr/mSDoSXxZbkXoR7bbbrv0LsJAwPh6v/zlL32SvqJjgokHriXxMr3LqqIvSSugCJj5vOr1FqdWowJKD4aiwtpsQaat+PTTT0/rquRU6fk4gZXJCga7L09MdAJ7nfpdniH3oaY0LfWcLViHmC3enoNpRcBa4fy92XvUoJ5U0mCfCeIJc3Gv02g5Eso7iSYNDlqtLOg3mynHHt/rrlaw7wcfLz81G4KgF7Fl05fZegLiAssvHW0YtBc3gyOOOKJtnS06CTM44H+lGSYQUBtvvHFdgzJ3m7YLJlWUFAaJJGs9QvSwrUEJSav91golvEjy263AF+I8qu0rgxUBFlvx9QL0WmLCVaYeYcncc/TQYJ0RuJlZniY2As+NHnCIXIKeJ38OxA/Pim3unS+NvffeO/0G6WjmE+pqSzzH5Y0wWw2sVhYv0noRPzFxvajMSDCRz1Bteh6V32bLMiy11FKj/jc28MzpbXfHHXdUemsKeuX8/ve/T9ZViWR9QPkwqAPiBf2L/e+oE0o9QdM/DRtMwE2docnPFei4hKsFvcd7jY4IJgklb2mSYNK4S9rHOvGMAE0BFO0QR3n4Aq1goQeBj6uHvHvJE1CenXbayUd1FQk8i/dj0jZLWQ4QVMwtxnAK5OPOO++c7bjjjul4CSTmozv++OOzzTffPG1feeWVld8o4oUXXkhL/0XWzLPqB6x1iVDrfn3ZrpW+CHwc/HkUeM433XSTP6QmGt3dn4/AwHlBb2A/ZIcV+7+ZMmXKqPJq/wsM/MvYRX6fPm6C/3w8HXLIIWlQZDvfaV5oZytTER0RTLIUecHEFyf7rYVJFilZIrbffvt0vNJBuzPJF2gFT1F8WRoZIfmll17yUR2FwSZfffVVH12pqK2FTILJfj3ICoJ4IoDykF5/NFUWQbpaA1NKbPmXEGP7XHzxxSPiBol6BRPUKt+1KOr11opBLelQoPPpfUFQM3bQPfAbbKS8tJo//OEP2XnnneejOwZ5gJuEwGLOR6AdZ06Bdx8ffrzz/b5eyMtaaIiRYacjgklfi97SpIJCvPdh4li2mYRVAkmK0m7nURRfD2UKdLV9ZRi0LzRV1nRHx9KDeOFZa6woO0QCge7icnyfNGlSOgf+RqSzXHrppWkQN748JLLk51TE+PHjfVTl2F6j2eY48IK1TLksU8aL8MfyPL1Vr1nUhGt/ZxhHF+4l9PHLcCbdgt66XIM+qrtB0X/m9ttvH/Xf0DRCcg3w+wmN9EbrBAhS8vmHP/yh39U2qPtrhW7RUcHkX34ECSDtU/OcjtE57FhMnfiT+OvMo9q+MtQzvpRFTVe9hvyurKWDl4SsSdbKpDgCecio4hYrmlQ2gPGnEEsqT3DuuedW0tbCW57awd/+9jcfVZVmypCF/BZlzlmmjOdhj2lnfjKxr79GfOiC7lBUVvBL6xT2GhAi3fgI4rdnn312H53w5ZW6Sn55yre8epCPwl6DDjm4xbQbL4asKCqK6xZtF0wqNCzzCgpYwSQ/F33JQDtfykX4a8yjWT8muOWWW3xUXyOhpHUrjnjBYXViCAWeKRYmRrdlnWArfCC9hnN44okn0pI/MHlOExuOwqBmujIWDpyGDz30UB/dUhgyoR5wmG81Zcpl3n+xGuSvP+awww7zyVoG8yn63+vVL/FBp6ic+O12Yq9BIqTT8JtFU4f4skrwPT3BDpuisPLKK488WZfhfVzGZ3SfffbJ5phjDh9dEy+ErCDSfrvU+pprrpmm6yIwJctf//rXjn5EdV0wSRzZNMCAVypgYJvZOG8rmt2qYa9Rznwe/jh58fXQ6PEnnHCCj+oK999/f/ab3/wm9WrAgRs/pA022CCJH0SSRBNBZmlZmySk9PJjnZHAGVeJL65TTz01vXD4DZBFjoHRQC8jrFO2PNUCH4NBp1Y++P9hmXKodHvssUdlvd1NM/VeY9Bazj///ML899tl0HudgHB45JFHfJJcfDlo5LebpexvMhcnnZV4r/k6D+z7SqEblrIiuB4+VqrBgMq8w5l1oqwvrhVG+C9TJ/DRLF9X5Rf1hDSBHLxZ58NYrh28+wnkMx/gnaJtgkkZQ+bLWuQLj/aRGXafXVclaX2XtN1u/LUSPEXxZTnzzDN9VF9DL6ZjjjkmfXksssgi6aWIIze9Hs4666xUyHEWVtMcSwkfXhoSV9baRO8SviwslBG+MqZOnZqa6CgPjFuCBeu6667Lvva1r41I76klKBoFh9h62HTTTX1USygzr1Otsm2xaXiu2takyu2inmsMasO7tqyVjspM+c7wIpZjjz12xHYtttpqq1HPksB/v9VltR008pt59R3wfvTxjZy/HdBho5p/KOKEd3bZzhcIKupwnrPygyXvaZr8EF7UGRgfiqxMeeRZpTpB2wST0J+CpaxINkgwSVQRJLRw+Ab5LOVlTjuFU5nC3IpmOQbwGlTURCf/Ju/HxLqclBVvg4QTplc7avfll1+elozZwR8Qp0S+NuSkyNQtBxxwQCW9h6Y+BllsNbbXTBmaLTt5lBVt/r9YBPvU+5BemvaYsWPHutStxf5WJ3wXB5W11lor5SEfGWWoVS4Yl60svpzZ1gTqBo27VgRpNXo/PV1rWT9aTVEe1IKPNnvfen+9+eabo/KEUNZS006KesIxvAvP66qrrvK7KlAXrrDCCun5KlA/zzXXXNmqq66a0liRk1ef9zodEUwKVhQpoDKJVy85ggSTMtSKKm9paif+WhU8xL3zzjs+ujRYXAYdiabVVlstO+OMM9KXCgKHr1i9QHmuOFPyByNPZHGy1ib1NBF8oQAVN+eQtRLBlPesLIsttpiP6jjt8GErYz3zZboorxDzzAcn/DHtLrv2t9rpLzXI1HrGHqUtarqudR7GTwOsyr682I9mNcVUO5/S6kOkjJ9iK+G3jzzySB9dioMPPnjEvdvWBJ8vBCzj3aTIssRAwNWcvxm9m+dIwKWC5jZrASojjMqk6QU6LpisMFKAX/3qV2md7uC2AvVCSZWnFU3tElD+Ou315qVrhl133dVHDRTW0mSXBJWJddZZp/LMNf+Q9YPSs2efHU6fPxuDHfLlKd8u0vAlx7l4cRf1SCwjLsrCGCz1wEjp7aBWWfTluaj8MsSDr6D8MX4IiFZT7fqC6vDxUW/+Ke2zzz7rdyVqnYf9ReNz6WNG5cb3HvP44/kPb7vtttnbb7/tk7YFvZfef/99v6sUWMPs9VuscFTotuN33rsQ0Vfkp8hwKBzDu7lIIPntfqfjginPyoQZUIWTzOXLXwXMW5VswWuXULL4a1WwvPzyy6Pi6qXM8Zhs6R1Gt/WnnnoqNVMhHN59912ftKfg5cuXBybbCRMmVIQSf7i33nor+fFw/wyFT1mYZ5550hxDrFsHcTXTAW3tRb0zeBnR+w7nc87LMAxYMvnCy6vgNXlvs5RtChNlnnkjlDmv0hSV6SL8/yDvJdsqnnvuubqvL/gP/jnV4rLLLquZtto+8L+p8LOf/SyNT8TkyWyrKU7iKc+nSscqjQ8SHDgCY/1YfPHFs+9973t1NRXWQr9Fb6xG0HhRChb19rWh3imgWo2/xqI4oGcv7+88caS4QRJKoqOCia/+PMGkfSzt/jwrkuI7IZbAXychD+1jtFemg8C6UQ/41NAbD1GEiKCyYK6du+++O7vxxhuzyZMnZyeddFLqss4oyPh3LbfccqnHBS8irBV8ffU6EksKgrzTNkv1oJNYku+T4oVvooN99903LVWZc269YBGXvpIv69dRjeuvv95HdQW+ahHw1fDluVq59vhjyh7XCIhi/Yb8GYPq0Jxtnw3lXtxwww0m5f9S61nSsaJon8A64stFXjn8+c9/nsSStbB48oaTsEHHSkxpSTwfRFi46hmbLQ/7e436OvKRWHSPm222WWWfmrP8e6nT5P2+v3YJInxHtW3jLX57EOiIYLKm1yLBZJvhfCGTOMI6YV8AnnaIKH+dvgAJCkfRPsE8cKeddlr2zDPP+F2JWscX0YuDnpVFIol7ZzwNNb9JGHnxJMdwK7aIyxtbSZY3zs3QB2oSYEBEX1YazXvBhMT10OzvFVHmvL48VyvXHn3Y1HtcI1jrQlAb/1ys5aYoD2s9R6w2Rfss9jx5VlwL4rfaby699NJpX551yYskK5YI6mBUdO4y0KvX/p6dz7Qe7HV7eNf5eyN0c3JpejH7ibFpjlOnJC+OvCDy24NIRwSTDVRUVkD5wBeS9ntLEnFWBfv97cBfX7XmN6VpFKxM9UxWSvrXX389DerIHG+MmYIPz4EHHpj95Cc/SdYozMKMW0Q8+/nKpMfJn//859S0x/0QNGltJ5HoQQCRb7xI6X5MEx3NZDS5URbwXeClxQsRJ3HWsazxB0VEA5a4amUBUYXVT1YLzMnf+c53RqRRc1+9NOKsycupHZQpfxo/zIcy8PJs5LhG6MRvDALeurPKKquM2F+Uf+oogVNvHvqIrYV/nzMafzUYkoB0RaNl0ynEnk/BCygvljQ+j/avt956/tSlyDu/9Zksi85ThL8/Aha4buKvl3csz0sO61YUWQE1LHRFMPk4H5RGgkgVIXFqgrGVY7WKshXYa7NO6x7+rI1cC451O++8c3byySen8yJe/GiyKH/a0vFdojcDlTRd6DnmoIMOSi+9bbbZJvvBD36Q7bnnnumciCQKOs001157bRJV99xzT2rn5zz4Fj3//PNJOCGgGDm7W3N18ZLlBUX3Z66XXnSaIgf/BF4kCCXylwqBHjw0TfqmPfYXTcjJfHRLLbVU+h3OS1prGdptt91M6vLgHF0PtSYQbhS+Trm/aqjsMq6V/9+VwTsSlz2uXuwkpd0Q8/1CrWeRFyd0jH/X2H15/kUefG/sNdRqwiq6VgvvLT6KfPObghUz+j/7DkX4LTaC/x2EGB/y+GCWBcf0Wveoe7MB/81ugvihTvFxfnsYxRJ0RTD5wu+DnD3Bjr2j44XWraiy5MU1wkMPPTTqGkFLwVeIj+Nl//jjjycTLOdhZFvECkIFXyULAubOO+9MFTtOmPVSNLQBvTzIU0bMxoJ14YUXpl6JTGaLEEGsMY4Ro3Vvt912KXANWKc6xRVXXJHyzoofNc9JFLHOC4UxPRgQk8AYLjgg0u1Yx+LzVevZ60XLb7KOwARrwSyDf7mUgbFK2kGZa/fl2JbnMuSNUpxX4TaLnfE9GM0ll1wy4hn4AVDlcFzUO7Tas6/3ufryQGeUauT9ZjX++c9/phkEeC+NGzcu+Qbx37f/YetErsD+RtDxEmKyXNXTNMfxtT6MeJf5vGv0mlsJ943g801vw25dgq4IJgpfni+ELTRKq6XW88gTUa3GXp96e+RBvJ1IdocddkgWH5rJ8KNh4K8nn3zSHDEanXv77bdPo1czDggCB+sPwuLWW29N4gvRZb96yk4z0GtwH+QL900TG1YSBCMvXvWMkz+ThJOC9XGi0iDvmboDKGP0tvNQRihjOGrrmSIkNcR+rRddM7Rj3jhRVCY9ume/XgY6F9j/AqGMFaJedO5Jkyb5XUOPz39PtX1g99sPUluB14N/l1ej1v56wRLJ/942xSk0Kj44VmKJICd1dTqp9Z7VtdSCj1JdK78nwdcLcB3qDFMkjvz2MNBRwUSh+3/tnfvzf1VV//+LfmhqphK6qJnpUEMMqCUxTZqOIMNFNMMLaBFhpdOFm5cCA0khrKGMhMQREMYPWOKgmEiOJYmQIqglpJaTltU4zTTz7vs4fp/v1vv53vucfc7rvG7v93rMrHmd17nss885++y9ztprry3lRwpQn9AFpQIUFSZXkEpKUmndInjetM5hCG1p/ViIRzUFLEWbSs0CJvy+SUGS5QifBELtMzUHVqbTTjttj/IUFSuBda00kg6llfOhqMlpnK5Juhdwov/nf/5nP2QfWOTGQpC3ZUDD0RpE0suy3/c+Lr744n3H4kc3J/jmjc3XYeBb3/rWnvvOh1uE7uWWZ8qHgfYhTIl3ZY3FLTs1+rYtCqOTYx4QQotMAfcGWa/cLwrhP/5f+Ijy4crULnwUR8WxBXoYoqIk6YumvUrIF/5xNSvTYWTpCpPmI5KmjiKj8AItShMS95UiVPtdFvgQeaHmtwTrr7jiCl9dpRSCYJlWjk2Ebkvum3ywCKNQi3+imEzR2hTjNKH0UFky9BUzPmC1Kn1xUingZMo2ui8YWUf08NK+izLVp6KFoZFJAsXQ369aOS7xnve8Z9+x+L/NidK97777fNPWgN8d9Rz3aw4oO33PK24rfSBE/Pn1pdtCSxqsr3UPzoXnY6xvocCCz/Fqs2Ka0eLk5+u7/hp+LDI0D+aqQDmifiRmVIvSVFt/kFi6wsQwegoBFboUHylOrjC5pi2RMhSXYdlKkuP5kjh8obD+8ssv72IClYa818CygVM2jt2tjaCzjOk2VkHpXoKsTIxsw8rEFzKjtahYUI6kLKlrLgrrIzRiTOYbodxpGgPKFPceR/o+pWnKaBac8pdF7d45XnZrZbgGZdOPpYGZk7F52iSwIMZ7M8bvpQRBV2N6fIBGYsBJ5I/+6I/2bC/hzw+ZWtdATKdk5dS2KXik+T7iZMFTzyeY3oV2SiMA46+WS+3VWFwRRmI36SbAxzt1YVSaIqV1B5WlK0xxCLP6hfmNCpO66rzgSKLCtE48X335YVv8QsZPh+4Mhvu/+c1v7hyTh3w/2H9qXA7vmuNcRNLmi5dJaRnJQvrMOs1M5OsaiUTXGKPaLrzwwu6eoVwy5J7RfLXKMlqXYredW55Qpqh85JskcCLFWTxaRiiDjCokD1SIzIdEV1Oc/0m0zK7u9JWVRaGrprWSJR8+iGEMpaCC73znO323yehjY1N54hOf6Kt28fuiLh1Gp04lpsdzrm1rvWcvf/nLJx3XR0zLpweacg7KmCw4Y8A/UOejXluUqIDJquQhFBa9j5rzUqIuuk2DgSrki3sSLU0uB52lK0zgBQuJChO/FEZ3HowFUaZRffXr+FUT86X8lkArn1rw6dtGuSHyN+njaMswcEa+XHnllZ3lCrnqqqs6p1iUoLvvvrtryKM/SYsfzibBtRL+oAVGGmK95IueueKYS07TrkRfpthVF32bQMEsBcvcRz1fKseShWDsFChYZXxE5Jy0ljN/r+L71QqKtx+PAj4XU/K0KshXbRodvyeI6ixGp06h9ow0lZCkzxLqxOOm1p8xP3zUxDTjyDr+a3LsFlyZGwt17tRjaxBGQ8rSXN1wEUZFc7z7MtWCG68bRieST8IslBQn4et8+7ayMQqTCp07ICI4JhKdOR4LU1/4RfC8RQtaRA6aFHyUGobFEjDy85//fK/zM8P/sT794R/+YedATiOPVo8vztipT/rOs4nwIvIFj9LHaEAcORlJwhDqWuC4qARF5UgKE10E0dfJlSZg7kLKEg0beUAh4tlRUaoSE7WJKPtoVWim4mWvxtOf/vR95bf1WFEKekm30RzQ5dqSH57LqlG95MEWY7yoKNH3ZUz8HqFjPS6anwffvzHEYz2qcwscF6ELMKYp+IDh/5Avpz5a/LoEDTSWI7rfCTrLR+Odd965z+8TNwQ/di7wqeTDyfNId9ocdaynizAP5ibDh2q0OLmA/x4EVqowydyOuMKkPnStc2EeNS1fd911doZh5lKuPF+SElwThYpGlvAAhAYgBhJRqcdYf+hPn8oqYymN4W1ve1vXPUmDIOduHLNr97IEX7dELkexwqeIYbA0uhCVJhhSmoBGUQoSXZQs00AyVcJUpWfZjTsNTkuoAi+vQ2W3Dz/eYwBNpSUvLfuMgTLIB1kflFFdqz/PeB9qU3qMpXQsI0Pj+inl8a//+q+LabdSUoyJxl9KU/+pA7H88G7/1E/9VDcQg4+YeIyLpyGJ99XvsR+7TbhjOaLpSDYdfEplHaOdarEy+T7bxEoUppJjmytMPnKu9kJIIm5xUjrLwvNSyhN8+ctf7tYzXN3BvwklCgvKDTfc0ClRNNI1v6ZS+q38xm/8hq/aSJjR3K8THy78iLC24WNUUzTl3B2VoqgkMQyYKOL4M/FVxJcrgTup8HHyxhKI7wRfjOSB58LXMV+/dPlRgXHMGGiIMbkvE79ffXh5HXNsxNPA32tRSGdICZiaX8F7FodsE4eL5ztmVFnMo9bhEycUo23qPfbuNvD0sFJPwSNyj4VuGCemp48V/ZfPT8mCVBNN2Mtyi4IUZVvBwu3Xsm3XQ8y8qDxTV8ZJzV1Jqlmf+v77tnWwEoWJKTe8METliApLViaZvnHK9WOiPPe5z92jGCnNVeB5QWqo77sVuuQYdYTjM07ZDLNnyg4cxTELU8mjXBFzZYzz8VQ/ilWAPxLXqDmmxoCSieWOhuaEE07olCTKG0TrUlSeXEoWJ76KKYt0rVJZ8xXIXHz4I7Uy5rlPQd2+LTDqz8ts67GOp0FsrEUZygvb3aF4DCV/Q/7LP4WyV8KvVQoTyyjSJfyYMfixUabUb1FB9PTGUNs/pqfYZpIxyhLKnAZ5+DEtyhLtwbaC+4WuM15ra6T1TeQlL3lJV151TYSU4GPCFaWSEjRkkfJ1q2QlChN4AZdFSf+1rJclbusTty758jLwPCBxWwTLBes0Uua8887ruhcZqYT/QwuMGMO6whcew99RqBh1dxDhXhELKfK3f/u33Sg6lEa+rt/ylrd01p/aKDoRlaGawqTwAyWliajhVPoo75RLXnwq9ha8HCwDztHqJO/l1cvtGDyNvpFjLQzlg+1D1qc+1AhF+B/j6dTm8PJrleIVrUqO7z8GP59kqKyXYGBIxNOsxTlz2LdGTC/+b1WWNHm2cJ8oSZ/ShGVjm/EYf5JtDQ/jUJ8zcEllAuHdwwBAF60rT/6r5agoHRqFKcawcIUpvhT+vyZKQ+dwBWpZypPnQ1JCfdQ1mEOObiemQsE/q08Z6ktn2/nP//zP7vqI4q1uB7rLsLKhNE6BbgK+PpleBkdFuuGIok4DSWVdGkXHSLkIz499+WXbkOWI8/kQ8LmRGb8VL6d95XUIT6PFh6pGSx5q+xAccgh1Q0X4T90Sh4jXnmkcedV6z+K+Yyt2PxfPeS48beZfHKLvelHWY3o4R/PLve1Tlggqy7tegvcQa4Q+UpSep4Hw/GrpbBula/R4cQcJDAkYAKIVSsJz50ODbj3mlKRM4Ef6Ez/xE13kcSZfx+DAdFYPP/ywJ71UVq4w1YQbF7vh+F8aMefCF4lbl0pKUmndIng+ojiM6GC9ZvGeMrIC8yzKgwKBTnXmrvlIbQpcW+uz4mXBiR4fLe4t3Zi1LjN1y7mlydcfe+yxRWsT3X1YnBStuBSgD/BbOvvss3317HCfTj31VF9dxMtnrZy24ul4nKtWeF5D1PJZWx8pXafmSys1xiV8glTewT40S70Ev7xWmKMsHlvLUwt+LOXS0259z2rwseH5xFrCCC/8BPnAoOFDQeKdYJqiqVD/UXch29xVVSNOVyMhwvZhhBA6jOglJAX1LT7Q6AaUJXQCyhXC/VkkxtkUVqYwoRV6gXCB+B+HX9+nJHrxlcayrUuCRtTzojw4OA2zjVEFNPBMxks3G+EGqIRbzePAMGU070WYMqR4mRBEkgCIuod0vxGHii8JH0I8BBY7LEH4NjEK6klPetJukE4CxfEiEqaAbhUpTaxzRcrB8qfny4ijUsBGH0W1DGjENaq0BS+ffeW0BU9nyoge4okN5YFKssTQcaC88Z45PFu2+Vd9qSGmLIy5Z9dee+2e/cdYGgk/Eo9tOV+J0nH4O8Z0URgpQz4fndC8dH0sksdkL2eccca+Z7+KuiQZx8oUJs0VNiS14JWxEPk6Xn7NSi8L07KVJfB8IDXoUmL70Igch0YdS8rNN9/c+SSgAGBd4ppvu+22Xl+KPuaa42puhu4jX6koUViWLrnkku7LlejgTBHx0EMPVX09ojVJ/7WObrr4v09pwsFZo4G8G2fss50K94cGrRUvo0P3eAhPp9WvK9Jyfo9BBC3HQd9+fHD4NSAl5YYPkzH3zD8MS0pYjdLExmOpHePWq6gsyvItNN3KEOzj70AyDep3f/YtzyBZLStTmMALg4sUHV+P0BgxTP+oo47at00SzxN/xdxKlJ8fYfi7n1fIH4KGmMYAKwjWpXvvvXfn1ltv7b66qbzwZaIRx4LBPiib7ggNtfOMgYjim4S6SuhqpZJfBJRJvqwJfEngO5QgnMcx5eJnpIbCu+p82YlTkdDwiNIzmht8qcY8dy+fkkXwtMa8V1hSp56f41pCO7SkX+ruL01D5B9wQ3i6YyAwreepz5/R6Tuf3AIQOd6yTPktfYQOoQCmyTzUHL9XDb0mSZ2NUpj6pE+ZiqLziGV3z/n5Yz4cXgo5ms7FHGnNMe/SXPQpBNw/wiMQTwdLGwoPIw4JI9A6XQmmb3yRQMqQFKYoQ91zIJN5SyM+F9wbPhxa8XLZVz5bcYfeVssa92nquVvzzT4tVh2C7Pk9KR0Xt7c4mXua//M//+O7VMEJ249vbcDYF5+iPthHXXFKP44UlNClPcRUH8qkjj97ZJWs+nzbyEoVJo8KO0b0UuPX4L4HUZxld89xTs8PEW21zVF3wJRujBJ8gXJ+rFOvfvWrO6fTqRCyYN0wLQr3BwvcmK/rPrA0EaWYqNj4tPziL/5i51SI0zFTOGC1BLcuuZQgr1isSHPZ4AAZLVpDKL6Ly6K4RWLInyrON1Zzyu+jNd/6oGqBBr/lvsTtcZ7GGp5mKWhtDcqeH4/0dbtjie7Lf4RyrtkH2L809L/mN5YsH7dOjnnXF4XzHX/88b56Y4hhBQ5FHCbwESRTJFaKvg2JjnLLVJQinocoJYg4zbYzzzzTN3WOzkxmSgOMTwONPMEq8dshCm7JWZtRd3NdK9Gu8QlaJ9ybUveIoOGS0zVdbPgx4d/FvSMIpqBxbvkSLlmX4m9UoiLE0aK84TBOEEO6VpcFjSb3pTV2F3hZ7CuTY/Buqr6KPX5M0DU6Fh3b8oEx5trcp6d27NB2x9M8//zzfZcqfqyEaycsRoQPgLF5I7Ckh1KIaZQmmk5WB8Psxz7TRcHvc5XnawWFiAE6KHFMq8PAHQa70EPAh6Nma+CX/8w1uwpWqjBBLBAl8W43t96wndFlLMeXPwrWCVmWSopEad0i+Pklfehrggl5BY0hJnyUBReWcAIAAEQrSURBVBQXGn+m1sC5G8WJkWMXXXRRpwQQ84SpVVBurrnmmi4K8twOmGMn+50KI9auuuqqnZe97GXdL/eFrrkpw5DxCfuVX/kVX93dz7/8y7/slFCFICj5SEk50nJJcVIXXXzGdGty/znPMuBcCmnQAmXHy+NQmWylFIVfUHZL04NMiZdC9HcdPzQq1PMxBMPTY/5K3VlMAF26xholP5SWoeF8CLEvAWn5jXWefIy8HhyTrwhzOJKWK0tT45wl08GvjFHTlBF/p1ZBtBQvG9wIcKMglhLzc+LPyzVLaJPlWydhH/JInDfCuKAcEX6BuoCPVBQohA9mYvWtgpUrTH0vfkk++MEP7i6jIEWFiuVY0JS2+unF3ApSCc830udXQ4VNfpEhPwcUB6Jd0yhjfUJhQphwFgVAsWGYz2dsZOEWsOjQ3XfBBRd0o+uweC0T7smQXwz3DGf4G2+8sXsJid3B/cC/iXvV141RI1qQomLk1idGyfF8HTXCtZF6U9GQ41a8HMZ1cxDj77TIVGIaHhE6MvVc8bhSAMQ491qLsso8h37t1EN9IxoVbgQo014/8h64chNlKkTKx4qNi0Cyevw5RmF6rGUzRxnqg/ZJMZNofynnxx13XLfeY5mVutpq6yLr6JpbucIUZ/6eIlKYXCOXqMJBixXrUpiQPlCA2Aclh1FyxGFpcbgsgWWDEW90S81taarBFzhTvdDt8K53vas4LLsFFEuOx+mVbkq+KLgvd911V6cEyhkXCxFfE8yLNsVXi3uDgvnbv/3bXfwrNZIohEyGjAN5VI4koGW+bMhbVKgcts/VEGm+OPyRWtFINJe5QHnwtGsyFVccau/F1PO5NahE3N7SneguB9E6hK9RBKVe+0VlLX4Qcmz0OYpyzDHHhNSSbYJpQvx5Sob8ARflKU95yp7zzQ2Bf7kGXBSGrO1SeLBIUyfz4fv93//9+xQh/79OVq4wgRcSF++WmyL6Ih1Sloa2j8HzgFx66aW+2x6YBoQK0f0HCC3AhKAoDYSRH8uqlKZlgPmWezcGrHA0agQFJT7TkSNHutD5+Db9+q//eqdkoeCNVbRkVUKoCDCfx665mtLEM53DaZ37MLYS9TIomQv3tSjJ85//fD9sFJ5eDd8PRbgFFOQxabei/Xn+UdkpKT2I+8VRX2j/0gg2ZIr1dBG4VwSBTRZHvog1WRZx4AVSmzh6UTTgqQZhcuheUxcc5ZxlrNZHH310N22VW5ZE33/ftiw2UmHqE1U8mL+VFnhoeeLsSBnid07FqIbnVTIEjTDXpdFaY2EkDtYT+oijcygV9hQ/oE0g3je6AYmgzMvIi/5zP/dznZ8Sfl04WssRnmulm+7OO+/suhywfP3qr/5qZ7mj0h/64ilBg4Yyy72kK07KU1SkakoTw9AXadywkraUn4gmey7JXKhLsiRzRSd2BaME047EfaiAW7rOQGEFCElRgkEWfeeuwf5Slnw0oQszupc4/fTTi8pSX7fkMuHcuAIki+NlQDL2o2gMXo6m9gRMhY9VelF4L/jVZN2rUnLmZC0KEy+fF5gpIkuUYFmVlbZr/SoUJvA8IqrEY14dBbWkMOGYiQIkpXAR8MOoVcybTOlerWMePMoTozWiciRlCbR+bvSOENF8DF72JHPCDOOePsrrnHj6JRgZo+36WuXdbxke3ZcuTFFWAYfUFmWpZbQjvh73339/074O9QlhXPiIWgTllzksk8XQvdSE3ygMhINZFijeXu5WCe8n7yUWJXxMSwrSOqxEi7AWhQn8QU4RWY70VRu78mRy1/rS77IgqrTntaXhQ/umgDEz85xcdtllXWOyTXDPSiEUpsLoLaZ8wDKFY/gQ+Mih6EbrkfszRetSzco0hccff7y7fvylxkAD6+VOMicoJMtMH1rSP+WUU7ptskbx7mj0Kc+PBgPrJP5kRGFnZGSsI/pgO4MIxoIvYt+oNkb6LBs/J8rTkGtAiZjGMkNmHAbGzBU6FSaphZKVGb+pZRN7SDind6+VRGyDsgRbrTAhVIDMhi0lSDFiQErCshWkEp5P5Um/JXBulumSbg9iZDDkeC7LCo0JoQi2Ae4Tw8offfTRzhfp+uuv78Iq0IgRFuCcc87pYtHgs8R6tuOjhNKAwjEVLHLerVRSkKJlSdvnUJqwJnDtY33QvKx5uZsTKrdlnyOmXeuuYPqcuJ8H/kNqissQLfvUYCCEnw8pjcSbGz8nIudxGtTbb7/dDynisbb6Rvwm6+e0006bXNYXQYoP7g4EA9YUPFjlW5Si0rpNZm0KE197/mCniL4Y5TzGcoxWizlwHeBL5HktxXpxGFpM5YYo9gwxlxR7ibnq+EVxYOQNpnLit7R23xHpmsqwNA3EJsH9Gqs0TIUAmNzvlpAMbnGaU1kCVXpjoRx4eZPMTewKW8Y5fHLcZz3rWb5LB++K9tE74/kqyapAkadrdVV+hOeee253fbHh5B2K3YMsE7NtCL9nc4fKSObD3xeJJqTvg0EwU+cTjZYivVf8RmXJrUnbpiA5a1OYID7c1srOJZrY1UUH+nVrwSqtTaVrkq9SHygzmgJG/k/vf//7u0YRJQmFCWH5pptu6ixRYytl0vV7s0kQ2XXoPs0FFqxWooVpLiVJKO7PV7/6Vd/Ui5exKMsAZ/plnsc/pvogCjDvScm6VJKDjK4xOvnKusQy90nK0xCH6b5tO/6sWp8X+9Wst0NExQcFSZx00klFyxLv57YrS7BWhcnNviVxD/+SSFHSMkTFiNgO6wAzZcynvvxUwFjuQ0HtaEhxBGeIPBYiuqMYts0UK8gLXvCCzl+DGEV0UzEyjK4qhtMPQdo8B47bJDR1xSayDGWJkZJcL8rCWPx9iLIMCNvg55nimFyDL+Mx16B7NyQHGb9WxJ3PFQSTeoiu/j48rWQx8KFkCqu58efU4isV29SpRKVIPQFMal6yKNG+4M90EFirwsSXtD/wKfLhD3+4+6VCoHsFZYkI4RoyvE5fJvp1Pb8S0G8NhRzg2mrB++aA+8X9wbK1Kd113JvWYeJDoLx6rKspTJniYwiFxCCi91i8THn5WgaEafBzLRI+wcF5dOw18NFQGplGeZ4SToKPkjET564Tv2YaKX6j87ksTfxv6er2NA8qDAZYFlhb/D5y73/sx37Md52Epz3kIzf2Q6QPKUW4ivBLPc11ucIE+OMeBOsSrFVhAn/oUyWmB8RhYllKAHFXYpfdKqk548V890H3FC8aFd6f/umfdiEH+MonOiqO0QwdRuTjhGM3o2Lwn8CXigjWY6Cbg/uEk+hcEaunwP3hOU4FS56smGMmQR0DSiyOtNxjuki571j3eDaauoZngCJPENLoPIuSoYj1UyM3e3kaW7amQPewnwtnz7lYNP9zKPyc//Of/7yv3kj8WRBDCjTJt7riZFlowdM8iKBIc0/mKC8R4sT5/UOinx0hHxbhpS996b70a5R8nBZFShFpSRnCysyk6AIlSsaKg8LaFSYNDa5J9FHqk2hFIsCh1mtOMpbXBcEUPb9RWuCapDTxsqwKno8mSERxm3Oo/xDcG6bSaQVLoxQQosauMq9j4ctMzx8r5BhimfGyNKZMTSVO6yH5zGc+47tNYkyjvix0TZ/73Od800bizyJOo4OiHv2YWonpHbRGD7BI6p5wj+bCn4WkNChhkY+MUjd0Cd8HIbbXokhhOuGEE/ZYj0hf3fOuUB0E1q4wgT9QSUlZ6vNpkvXI9wEaUuYoEyVfp2XCxIOeX4TumFaYLFOjXmSRIPovw5ixNBFjiAlysTZhZcLCRMRrrB9zBRY89dRTu/OjiCLM//ONb3zDd5sFumb6zMxYa7h/3BOe45wVXw2ulefAPWa0Eda+T3/60735jGAZlG8a+W7xM3OYX0/l3ctTLPPLohTnhXn+FoWGftl5HyJe08c//nHfvJH4s/CYO694xStG3VcNDZdQXjeZsbGtYtctyiDzq01FAzSoF/w5SFRnq6dBvz4J7Rg00XeUCPfEt8/l3gAoQSeeeOK+7jd6QC688MLdfThnKkwzo5FjfaLuNF8fJX4JxfUnn3xyt640ImCV3XR9I3lEXC5x8803776AFEaGVt944407t912WxeYEWGZQJk4EK+iWwGHcTmPS5gPblHcVI5TO9fN8+Icy+pmGwJTPo71Y31jVEYph5T5MfcIh38cR8HLjsuy8QYVaRmqPgTdFOuME+bXRNDLbcDzXQp4ivW1FfmESobmB1snfICM8QlyKw9Sahda4diST59EdXXpvIs4gf/FX/zFvvTgCU94wr712jYnKEEoZUPKEH6jQ/tsExuhMJX6WCVSaCSKhu37SeiKAV9P9wzH01CtC+bw0dDxPhmCBov7wEuIEvaRj3ykW4/PDF+TWJ1e+cpXdtYLonyjOH3gAx+wVFbHy172sp0XvehFO9ddd92+eFE4XWKdwPcKfyVeeClf+irjeTOjtRSGbYNr11clzwyH4rE88sgjnfUQq4eXlzFlZw58Ik+Ecrft+DUtOq3IqvB8t8QT64NyFtN717ve5btsDOQPi2sr7F/yKZ2Cp4FQ98qRnI/Zq6++uuvZ8P2mnlOUfJhKMvajrhWUIO6jW5gc8hD36dt3G9gIhQn8QbuiFIURXb5/FJn2o1CJcKyCR67SshTBauJ5izIGAltyDArFuibmHAOKEc7Q5JWwCIzawFLDDPMHMZIw1ynFDyEi/SJflcSLwqHcy8yUsrMIpTLMiKBtx69J/o+bjud7UZ8juqhiegQ33ESUv1bY95prrtl3v5Cx3a9+/GOPPea77IGBNH7MIjAJuacXZWp7MOYjgXZHylBNIWpRqraJjVGYsJL4Q3dFKSo5/Pr+Eh4SEb59vXxdWHZcefL/c0Lfdekrx6WF5z3ved11kd73fM/3dI0ZlhjicWDN4QuDL51kNeDwiKUsPl98QO68807fdRCeHSMf5evAspeRseVlLvzcP/qjP+q7bB1+TQgN3abjeabsLRKZ2+vOTWRs/uJ+pfv1zGc+M+zdj3evtcwTSp0cj1m0Tia2oF8HwofZVG655RZf1YsmEAZXiGTZwrcTC5vv5/tvCxujMIE/fAqmK0sufsyQ4KRHEK0YTycqR8tUlCIEPvS8IXGUkNYNQZebrBjk/znPeU7XDYZvEc7gWHEkmNtxEn/5y1/ebZtrnrrDDv5IOOLrGVJ28THDn2wKn/jEJ7o589SNSbp91qWWcjInfu45HUrXhV+TBAWY6SMWUUKWiecXufbaa323ZvxjbtPQoInW/Pk+8iXlOnWtcTqtPkpTEDFSrIUxeR7C84As4nOHknzmmWf66kF4FtHKJInXyLJvjwrTNilPG6UwveUtb9lXCFxBAl/nx0j8xUdozCA+0HXx5Cc/eV/+ooyBmD6Ke8Gxz3jGM7rRCm9605t2rrrqql0/pgceeKDr/pozMvNhhglg6WqTcyeVMZY+uo3H4hOjMnwfpRYF2MuGy6rx869rzsY58Wty2VRKg0l+5Ed+xHdrxtNaBI6f2j1UI+ZtyF+LfXw0Wq07q4WnPvWp+44jXl0LY87Th59fMnX2gUXyFY+L1iM+HvHdBPyHqRu3WVESG6UwgRcCxBUkV57il8KQsB+e+7xocQ4cpbVqSsM/Jccff3z3Owa66GRt4kWWQ3gyH1jlCK+gsidF6WlPe9rOo48+6rs3g+8dCm6MH/WqV72qq6T9qzrKOvA8LDLSaBPgQ8KvKQr1xRzxa5YBkZQ9v4t0zcR0KN81iL1FkMba/JhMlaF05iTmj4/OGhog4RB+xO8X14lVdwjFeXMZAgt0y35DMBE17ZefH6GLbAzUVa35r4ELCPcuKkP65SNSXY8vfOELu/asZGHaJjZOYWJYsRcE+R71iR8Tj/V1CN1ysTKoKUu19XNSewklIi73cffdd+9GuKbirM32noyDES/EhkI5ouyoy5jgnlMsdjfccMO+RpjpfOiKu/fee3de8pKXdM+wr3ysC8/HOvMyF349En2ALKKELJPSZMiLPI+YhuLE3XPPPZ1iVvswZRSno335nSNOFzDJeDwv3dQ12F4K3cG7quPjxzYK3hD4hvq1I0O07NMKafGx73kY01bF57goivxfUppiG4tx4MUvfvGefbZNcdo4hQm8IKgwDEntZfb1ekn4mo/K2DopmdVdxoJGr6H5KFBM05GM48orr9x1sOQZcT9ZZoQiCtQifOhDH+rCP7zvfe/zTd3XIgEyNc9cSdZJ6UNk2yldE6JnjpRiHK2bf/qnf9qXZ95574pqgdAnntaQlBzj5Rite/rEJz7Rd5nEG9/4xj3njlNxRLS9hgbKxLSGuveEXz/SN/p1KC9jIB2eEf6pnoeonNRAcY3HzAW+wSWFCbeC2LbSdf/jP/7jeyxN26Q0baTCREPkhQFxBQni/3PPPXffMS7xi4JfhkMTeKzEKpUoumFqFTaVDy/zgw8+2O3LulbuuOOOLpSCrCKE1Cc6dVIH50k5cHPfFO8KobyMiW3CcyU9orDj70Rl1wejafCBIlpzzbK0CUQlYky+CKy6qcP1S/fbR0SR95/5mZ/xQ9eO8hfrN/wYW0DhotHCulm6B0PiKA+xPmtpzFvwmEYlRUVTY330ox/1Tbv4SEDdsxZLsStaSGkmBUKo1O7RFEhH7w5TRnkeECJtlyjFTpubmgKED1ucO495XSkbpX03nY1UmMAfrsSVpqg4gRfm0pcEEpWmUuGJytKqFCcKdZ+liUaK4JRQynMfp59++q7SxC8VD2b25Nswmo1pXrg/6s6UkoT5+6abbvJDqnzta1/zVbugbF1//fW+uoMuOMoaypU/+yibQMmP4r777tt56KGHdvchyjxd31xT3G8V0eenwIcF+WNEHL9SlJVvyoYstm9729v88LWiMhulb+QXfjylY8aKgzLJPZKyFOveMSNy6foq4R+VJfq24Yjs1xCFCbSHYHCNH+fKKe95Xz7G4mnJJyoK9wZ/sjhNE1ZG32+ZwZtrChDdnQyOEfIX6yujm8jGKkzcUH/QCC+gFKVS2AHw/fWS+RdPVJqi06orYatESlNN0YsC+m2BkXRMIyAnZdKni4EQBIcR5tjDkiQlSb/ce8zGU2In8bVOXBb8kN7whjd03W5DkwDL4odlCVN7TWleNHbLnJDXmDeV1e/+7u/el+8omxyvifcCRYh88ktZiBYmlvWf690kjj322H33Gom0WOBbBIUB60kNQpawn9dfLcoIsG/tnfG8OLJ8lojHMfmu54//WOCHQCnwfPABEanlbwqltDx4rNq5Wt0h+dKXvrQnnVXCbA3M4hDhPdumASMbqzBBbY45mSVZdisT4mblqBjF9a5I8bL1KUlxW99+cyCF0PPsMgVmYcdHJlpSOB/xRKgIlzWZ7rqhPx3zMNY1KY08eylJjEZ7xzve4YftgZFsTDmDFYhQDZ/97Gd9lw661vC3oBuuz8xP5GHg60vPtDTtgc+rt25+8id/cl8eW2STUWMjGNmjfFM+ZF3SurGjkoZg1NlUmL7E7zV5Pe200/atHyN8YPEBMMY6BPE+sYwwYGIIPuA4ho+7Ep4/p7QOSsf5B3QtTYcudk8vKtCt6bTQl5bn3cunyybAAAVXkLDGkXdmMth0Nlph4ivDH7qEBj4uu/gLW1pGZMnRenUXDClEQ9vngC+5IaVJX3PIWOg+wcIihUEKFOfj+nB2/tmf/dnOOX4bpy659dZbu+lX6D/nemRFomFUdwsNAqPVFgXTN4FB+/wmBPf4rLPO6paxZPkzdZnCXKOSSvCl6HlskU2nlEf8LVgfu5mivO51r/NDJkE3Sun8Y+D4WJeNFT+O650KIU08zahUlIhzita65DzPvq1E7Rhfr7ziZ9dHzTEelI6Ulx/4gR/o6qGxxHAzNb7jO75jN8+yfvozRPhQ3CQ++clPdvn64he/uGc992zuj5C52WiFCUrDJ13UwEfxfdyaVBJtI8DjKhSiFpjXqVZZR1k0zsdFF120p29eLyDnVjcEeUD5YBoBJsvFZ2UTYLJLfDKwHhELiYok+mvxLHU9WHKYx27s3FGRT33qU51ypElJcTwlAjBBJumC6yP6vtAVGp8h4R/8uY6FypzntKz4W56/FnEz/CZCPvFdKkHjX2uMeD/msP6R1iLgN+d5axEsOnHofdyGsjgVBi2U7lcfcT9Co5SopYd1gu5sJ+7Lx0lpvUtLo+3HSFTPqM6U8A7QJToE9Uo8rg+6/bVfybrESN5NhrrZfb+Iqs+1MMH8JrLxChN4oSwJjUSfwoTEAuUKCP/jOrpTSij9VXLyySd3hSgqLy7kncLGMuh3LMQFwuqC/w3WJSpULDO88HR10k2KsIxo2xOe8ISdpz/96Z1vABUXXU1Eu/7KV77ipxgF5lqc0xnJSFcYASOJ1IsPDefnnpAHPRc1bFKU8Knhvoxx2gbOi+n97LPP7ixQdL3RzcaUEyiLpVAALfBcYkC/mkxphHkGXP+yfJ0oF57PkuAH8vrXv35wROCmQJ77YpWhXJfeOzWMlPtFIK2plJTsmuDUjkJPF1upm9gt+lMsI4K4TH5+pPaR5fthOXfoFvT9+tA+//iP/7hnPS4Jng4S24chXDnR8aqjfTv/VV74MMVKiwJFnUb3Nsd5ei1Q38q1QMe1+GFtCrw73JPos0Z3LNdx9NFHhz03g61QmB5//PF9hakkVNJqOL3ASljvylIUVYwUYBQViAqSlletNKGAkG/yV3q5SuvmhAoQKxQvOl8uur/q3pJCp3uo+xzzjHDfGNJL5GosQThLYn6mMkcRYx+O4XhJTEPKUVTY9MyoiI477rjO0qMQDGNBMbriiiu6gHg333xz1fl0CL//l112Wae8yU+mVj79uBb0PBaZP2wIdRm58Ox+7/d+b5KCtwkQqZryM8Q555yz79rVACJTR/7VnjnKAR8eJeUXZb2v/Li0+iQeOXJkz3Fj/ZYczwfCR5ijuRKjlCJ447Ac96FeqMF2XApKuMN0SYbKM3WXH0N+Yj0YJdaHvs2llu8aWNcuueSSnX/4h3/wTVsBz5960X3csMBz37CkbQpboTAB2qYXrJLIIVyNaEmGCq0qIwo+y9FytU6werhDe5/wJanlZUClwlcoE/oS7ZqvBRyqUYbcEiWJ9zJK3F46hl+UKpQD5sli+PKv/dqvdf4Gi1gyLr300uLXdg0UKqxvKI9D06Bw3/l6pCwOjV5BSo1jDbqqpUgyQe+yUR45J46bY+7ZJjPm3Yh1kBo/CRbPsSitUuMcPxQI+qh9xoQC0AdHq6WIsBrx+EXB8hzzwbKPJgO6tD3vpaHviijdtw+wbUiB9fO5DOH3CuEa9cFX2tai5H7hC1/wUx0aCNTLvaMLnF4BwbtFucftYt1sjcJEY+KFqyY0sDFomIsqI/369rgfvxqyC+tWmj72sY91eah9yUShQqEQrhpCQuDTg5WG2EIMw6UbiiHl+AfwJcFLgOkYwS8KRYsGiS9LFC9G7PH1j2meCOUEasNqVGpclsW//du/daPcMJszMTRfQi3oC9aD4/VJ63VxL+SfhTVtFSiPmxZ7aFG4pjG8/e1v37Uoqf6Iik3rMxS6r47WxwZWk+l6uYnCe+PrkNZZ6L28Looc5qNwrxx8EH0/rp1pUCI+OXut66kl7/E8fu6W41/96lfvO8Y/imQVV3npa2sQPt4OO4RloW3wdpY2BKWJoKTrZGsUJqjNmVQSbrhGRfm2WHj1W9oPUQWJ1YQw/P4g1wVKB3muWdLUVablTTJrrhMUb+ZpQwF761vf2vkjodhdddVVnTKKFQ+LDesuv/zynb/5m7/xJKrE+09FKcXGn02U1kaWAJCkyTQUrcfMAfdrledbFdz7KWBZiA2glCXSw7+uFT1/ujQjKMSsj42rzudlB6Feig6y1E++TwwY2IcftyhvfvOb96VZSveLX/zivn0QD/DKPGRxO+4BDutbnJ376v0WaAv8ONobYMJsrGtqOyS+/9hzJjs7J554YlcP4q85xiI/F1ulMIFr8TXhRaDyiBVNfDlYjj43XqD9RdL2PsYoU1NM+M5rX/vaqgkY0b2KZnwqncMOw5cJWsn9o7tiqp8ScE+xnvEMWhQkyVglpDT1QjIN7v8iyGrgigzPvhUd47DOrRElSzIDEkpQFmX5UllszVdMv9bdNQa6ymNelB+fWogBHX59CIMMIm5B85hpWt9CHLYfxfNWwx3kS+d+97vf3VnV5drh++JiQKDiZDx80KpNplzccsstvstS2DqFCbzg9QnKQs3/SYXYK6jaOvlHRZg8dSyPPfZYl96YL9IajNzi+nykRMyzr+OeMLqGL1OtA/0eVOb4ItH9KkX7bZFkvcyhCGCtdWUJ4X9LOIf4cRZRGnG7v79DMBrUy1zLcRD3J+DlHHg+EAbnRGqxyLy+9SlJfOi51vd9jJR8j6K4xS/iZcePxbJUAwULp2wfsZcsDkGEFWvv4Ycf9s2zspUKU2l27j758Ic/vLtc0vRL6xAqrmg10JdatCSxHofkMeALofTmshww7QD58ArWxSt5pC9+iZYPM36/Sl/8fbJIzKdVQvBNulHwOzv++OM7szdfwVIO+N12cJafAx98ofcKB+0+CCKoY3zOQWIPyZmf7dxvtyAPOdvXfD3xE+rDR0HWItiPxf2iEJ8ep6/O6tsvonXUqXTJMdiC8CM0pGPfV/bHakHQW9IonS+es7Y9OXhspcIEpekj+sRftpqo+0qVVLQ0ERRRo7pAfe9jFSYc16ISNjSiYwwEjKv5bpUkdtfxpacot/w/yOj64nXG5dLs3mNlDovWIjAsnNnLmXCUBuA7v/M7u7LKM0dklVR3CV/XT3rSk7qh34xAJDDnOueemhueyVzEQSWqH/TO9RHLRx9EiHZlaegY4eUQcX8gB6vP2PO0ULLoDFlqJNzP+DHn2wXTFWmdu1aMlVjfRykR687kcLC1ChPQAHjB7pOWl0nm4eg8Gb/45NjH9t///d/fc2yrDxP7RYUJWTTmSYS0GEFF+mOGIZe+xISv8//bQi2/uhbCFWiZexcVZ783JenrDlgWxGFBCccaRNmKoRiI6cIQXaa3YUqCw0rtuS9CrXH10V0R7dMyerX07rZAOfDjhkYXMeJs7HlaYLSs58XT923xYy9+jMZ9orXTjxv6WFScI7r4eH6xXSgdW4ORvX3bk+WDawSCZZYBMfgGE5aAcoNBY262WmGCUiPfJ6UKztfLiiSlCedDzqO5jqQYeVruPKz92BbRV308N+nPDfO/MRyZirdFWRwjUPqN2+O2qbQeXzun58mvQ1JqnMbIKmEKGMqWKnu6IGiAWx1WDxvLej5EWY5lQB8/tW722I3XQmni3BaYusiPQznowxWFuShF547pexBJV3oo4wRGhbgfXYjCj62JQjMIlLmherGvOx3FNJmXBx54oAvA+4pXvKKL2UWXrizhfcJzZFYKjqFb3Nviudh6hYk+/aEXxaVlfylLKB38YvYFrefXu/n4H61MrCvxgz/4g3vywS8PfVlzbhE/iFhSNcfwPhmjSIB+tRzX+z6+zo8tLTul89fOo9nnS34V3Bd/nkOySmsSw2k5J8+Dr6lFgnUeJrhnyyKOlIp1CgpLCW3HB7OF0nD7FuiG9eP6Psg0FcXY87TiaSMqv3GEXFSS9Cs/Uk9HaABNX51OqIYazGUW943p0J14kJF1ZqrUYCASVu8rr7yyi9bNACPaPJR2tZtq81zYRv2M4oO1iFhe9JZQ5/n5XaAvX3Ow9QoT4GfR98KMEb2sUowQJmvVOvBjorQ4laprT1+kHKflZX61UJDJH+cZqxy0iuaO8/WldVqvbU7fcaXjiaPE7+mnn75vv7lk1X5JfG1RVn7hF37BNyUD8LyWDZW71z2lgIoEQGUbH2CtuB9daX61ErznXm777gUxyeJ+fSPFplCy4tx1113dtlgP0ajGe8lxCOv6rHP0AMgnj/qTRpb5H1thpDMNtBQ0QjNsC640LCLEesMlBT9GlBUUHLq3sGB7t6Wek54RCrmUIbVvHEsadF3yTLivuDz4eUuia4vX6b+l7b48NwdCYQJeeq+4FhX5ggCFQN10wveXUFjivr7MPljG+JWmHY+fu8IqQeWLRUt59WtYRMZ2k0r+7u/+rvstBYVDyLOvcyndzykihZYKwC1Jc/qbJcuBZ7gKSsq5OzWDtmHNacUtP2PwPPUdz2CWuF9pvrcpEPSV9GhwPS9YHkD//+zP/myf4qZ4Vy3XcBhxJcMF6xm+i8yYQJlEgfE2UsoPgvLPfJeMYkTR4bkxMwMxjrASkSbrET+XlBRfp/V920rLpeM2gQOjMIHmovGXc0i8EEVxRUfLCA1p1LZj4WNbVK50jBzFKQDE5GDZzZIIkzuuAsz3dPdIOVyW5WkRmVuhiyKlSA7eWnYI23BQYGg700ww0pTGkcqQLltGWBIQDnP6NoNvyqr46le/uq9MxfceYtedD6nvw7vkxlCq02r4B86ic3Z9+tOf3nNOypXnBSsGeN6iguT5wgKSlKE90cev7iG/jI7F55FQNrzncX9HiklJIYqKkitN8diW/76ub3sfQ9uXwYFSmCAO2Z9TQA13/O1rzLVdFSjrPK6H/A1kGUGUf6Y9WCVXXHFF5zCnPI/xX9pU4TpU8crHTNYjmZE1fNstSXOGe1glWC+ZIBgnV5UnmckRKrunPvWpXQN01llndUO3cbLEWoK/AFNpcF/4KtUvw9zZbygO0CbAHICrxMucW4h9+9CINcEchjpmLJr4NkoN329oUukaz3ve84rni5OAS8gfFg/PF2UsfoCW0ku+TVQYXPFYBFdaXIb2i/g+cX3Et/n2Ei37zM2BU5jA+8L7xL9iSqLGBqREgBSh0mzbCHnQPto/WnDkr3T22WfvO07KE5Yfb8hXAXOscR85fxTyN6QoSlr2WVR4NlKEZCXjGekrS0pRvPfav9Tdto3ceOON3Re7FCLKDZYMFOC5RovgS8WwXe6nrKgEt9y07kme76rxMhn9zeT/6NIylUOsm8ZCV4qfs4bvF0egDcEcjKW6ltFOwoNiIuoJKEG3kO+fLM6QguHKT1xf2lZaLp2jb9u2cSAVJlCMDX/xFhWgMSYKshQCrfN9EfIQ8e30MYMsY7Fbju2ky/pvfOMbe9JZJYwQpD8cixeVOIpGtNZIIVmGP5TOFc8TFTgpPrr/6laLedL9ZJlo1tusJFEO+JLn2mU5QrG9+uqrfddR3HfffTuXXXZZZ2liODvWJmZkZ869WvBKIoKTD/KwCY6yPP914JbYqER6eY7yyCOPhFT2o/2m4CEP+tLx/frmN2N6j2glLwm+MI7vgxBJuwYKH+9syR8sWQ0lpcmVpNKvLx8kDqzCBKW+80VFFgsaK74ehe8Xv7rOO++83f3iaA+JlCFGe8QuOSlL+v3ABz6wmw6M+RKcExQoGm3iXkihIY9SpvRLQxIVLG9YJNE65CKridKN94dl1kmZigoUo9mQbehCGoKRK1wz10k3xhlnnNHbqPXxwQ9+sOt2415JmeReMkqIbjr82SjXOIqiJNMVR6MlpZPnzEgX5+STT961iDDX2qrhvOvCu78EI7W8rKvsqiz/1m/9Vkjp/2DY/SLXROwiP3eJ0iSyKluM7Hvyk5886iPoyJEjdoZv4/shyebjio//P2wcaIUJ6DYomYz7pGV/VSLnn3/+7rmkDOn4mA5dXEAUYE8LEVRQUSGIVifWMdGgOOqoo7oGbt3g+Ipp/pRTTukaXSKwS9mJipCUn6gERWVIy1G0r9IgPaxEUoiQaDFieZstSCU+9KEP+aomaHSxAtGgy8LGyBd8Yxa5RziKUy7vuOMO39SBxQvFCivVKsDnZh1KmogKBQptxCeMlaIUu9s4nu5O4oSdcMIJu+//IlBmanVMJDpoS1rqP5djjjnGk96Duz4k02CCX94vYn3hf3juued2H+QMeMK5mzqYefQoT0Q0J8SFIl+r/mwRyiiWQgYfUYbxayQtukv55T/1PNv42OKX9bRJuAcQw4oPL9rH6667budTn/qUX8pWcuAVJmCkgBSORUVdP64MqUHnC96P0Zc5AqXAidGMLSUpno9frWM7qPKlUONHtYl87nOf27ntttu60YG/+Zu/2Tl18mLT7UO3AS8VU3cgLGOpOPXUU7vGHuuQW4j8f/JtiO/DUG0qNJVFFM7nPOc5zYESx6JyWAM/KvLw2te+1jfNCu/EOonvsXPPPffsqQdkcdW6mnKi6NZTKU1QXoLggr7fGLnooos8ySI0qjommQ7vOd3k55xzTldnPvvZz+6MAoyAI8Ye9SoKFJNo42zPiNipgyCI50UXLOFeiHFHWWYi+4985CM79957b/fhiiL00EMP7dx///2dkk5oCOr617zmNV09Tlc9Vmqev+olDSaRcsYH3dFHH90NQqGNUIyuTeRQKEyg6NpzigLU6b++NF0580oxfpHGfShUgtgo6orTPur2In0cxrUsZYwJQZODDZUUiiZlRV/tNMCUh5NOOmkjQwIwYzx5/OY3v+mbFobrXzd6P/nqLoHSqudUqg9Ksijc65Y06d71/YaErvixkebVbZkkDh/BhLLAGk67p7qNtm1dbic1Do3CBLzo/vIPiSs/fetZByxTKcaKkW0S/jN8349HotKEaVXWJlma9JWqxjL+Zx/MoYt0tySbB1946q5kyDpfkXSlbBNf//rXuzIau7AX4fHHH+/Kf+sQ/WWid7cPIh23KEpD6bTiI9OI3FwCC4CfvyT4vS1ixX7jG9/oq5L/xwUXXNBZaIi5ta1gADgsHCqFCaYoTUMSK0IUFlmQShYnac5+fFSoMFnKjBq75KLFqVT5Kh0a1+uvv96uPEnWj/v4TIGyLn/BdUOXVGs+hvwp8V+cC+qPmHYNH/FG/UQdiU/M1772Nd89mRnqdD6SGYFMvY+oq0pdWO5f1Cd+TO34eB6dF8ESiIsH/kl072MdZkQ4ZYLyiYKNb+Lll1/epCgxQAhHcT5sGHX70Y9+1HfZKg6dwgSlOB8l6avcSsKoPClDQIGSwoOoS03WIaItx+N1rKxGWBRI45JLLtmzPqbpxyt9ljFvJslBIpb3TWBsPu6+++5uOD2NpPwS8d+YG3fmrkFe2P6Zz3zGN02i1IiW1kFtfbI4LfdWypWWAQUKaxcf3ZSLO++8s2uHiPX21re+dbfMYhjA71btVBygo0E8HI8rDD6rhCvhgwFFzPdryeumcCgVJliGpUnC9BL8Qm1UHMoYBYWIzHF97HpjWfFtcCZvVeDYj2NViHEATA43ON/ffPPNa/VxihXjlEoylnFG+q0bGgy62jaRSy+9dPde9cEcbiWmPJ8S3iCrkS411qXl1nwMpdsK01VRJ+N3hlIgZ2VZYugSp3uT0cBYTnBufu973+vJNDHm+mpwPM+4dP3a7vg+WgcqL/rVvvEcvi2m5/8PGodWYQLMja5szCW8SCgtTKCJeVwaNyKlCChYDBHlv7rkpMWri42X9XWve12n/LDcojjFfVCc+Ir913/9V7sDyWGBxp3yTgNA2VD5wPzOaBYmPF4lYytUvkxj+V43m5APnt2ZZ55ZfK9b8ueNnK9flL50+ra14o1za5pMCswoM8WYim4PdI0xJP/FL35xFymfkV+MOOQeo0wxWgwl88ILL+wc5hk+jwIVu7gkvGtsx0+J98vz5/8jQ9fk2/nV8473JK7z90frZO1h0FCt9wJRunHZ5aBzqBUm+N7v/d5BBSQqO1OE4wkG5+tjIdO8X6xX15qO1XoJL6eWKei+vSbsyzDUJBHvf//7u+HIxFGhLEa/BgYmMHLFA6a20leB1ipYrYu/qqSjTB0qvSgMs1Ye1gkNmz6syEupDiP4aOkeQ2k9x9Sei4jb+vZzavv6c/b94jr/7YN96AqSJZ8yzS/KAWWdYfjXXHPNbFMHlWBIPx/O+IlhmeL+qjtKz0gfMlisGORDHCXCg+j5ygWD+Ht0a7FMHDR9UJeee608jBV9oLfc78PCoVeYYMzcc1OEQk4QMQoeXzZaD7FCqOUh+j256Jja9pKwL19HOn+SlMBnAQUbS4bKGkIIAxqjRekre3Fb6b0oRRtfNvH860B1hT6iSvellkdXNvzeK21fL0rrh9bVlv0/efXt4MfX8k53M/dDH5KqC1Es+EgsEdPy9CJ+H6Fv/z50nfqVyJdHCjCCK4beN4T/sQdCypQ/c5epeU3KpML0/8EXoc8cOZdQ4PnyYLRQqQLgK4P9Yl5qLwZfALxMUaFqtTYhsjjdfvvtu+eHfMmSPih3TJuir0+stDRaJfrKUm2br/eh72pEVgXvajz/OiFqsr/HJYHYKOs/2+JvpLR/idr6ErW0dB7lNf7Ge+zHv/3tb++mkFL+ERR6FPh4jngPSvh1xv18/V/91V/t3HTTTV19SUDR17/+9V19e/HFF3fLzMHIf7ZrP7r96MpTWv58dO3xHiSbTypMAaYlGKNw6IXy9UNCZa8pTpRGfGFLiltpHRKVqVL3XatgGsYUzFQjpcoj2V5oYJiPTtPzzIXKLZYohiOjSOG3QWOh7fE30lLGtD6W6WhVWfYo0NK7PUTtWsYS753OXcpPSWJ9UlqO4vuArtPXD+H7+zl8XbymUp5cUUYRwe8If84Y0NDzWLoHvr1UV/IB4PcSUZnzX8lTnvKU7pdehHiMK9olUT5ZTjafVJgMvlRqyomLCvoiwrlEfHliP3dN2DcO4ZxLeNlbpzxI/o9NDRiKgyqNDFOVUN54voTWuPrqq33XKt7oROI2RuLFcqRYPt6Axf9OXM+yyndsqGRZZdqFOTn77LP3vQ86Xx+la4nXO4TfmwjnZ5038C7k0e+tLwtfr3OAlktp6H/E/wvPi+PnBf4D9Z+mnBKen1K6cRtC/egKjqS1nndRvofE8+Li+ySbTypMBfhiHqOExBdgisQuBn+R+irJ+MKrYphaCbiQFmkyD9+b3vQmu0NJhCjGGmmyLdC1wchJlTNGB+FwypxQYylV9qwjfpjmjWLS39r9qTUYWl+a5oO0tMy7ijXi7//+7z2JQR588MFu+LinH4V5s5xSfkvoHcb5lzyXIjrHtHTNWhf/x3Xki+C0zO0lx2XWaTvlMabLtlI6fesi8X/tOMe3aX/d11I6cX1cjscL349rrtWX6j729SWJabskh5tUmCp89rOf7V7AuRSQIdFXkEZRCF7SL3zhC52PlR+DqBKQRapWYUwV0qVBivmp0bftoHHfffd1Sgb3iBEum4yeS9/zeeCBB7qygz8IDbuEa6SrGt+ZiKfl/yNsI+IvZVwj8F70ohf1WuS8oYrlWg6yLOsjQc6w6gpBCSK6MOtRBBkJSLcklrXWjyGV+3j//DpL64Dj4ctf/nI3wIKpRcibHOil0CD81+hEnTsux1Gxishc2k9C2hqV5fdR+yiP8dr039fHZf9FmVWdpTLDfSMOFFZNOSjHepSpfeLz1DK/EsqcuuS4b1hH+WXk5lFHHVW1GkVRuvH5xOthXkbKYK0c1tYnh5dUmHpgUkCGfJb6u128wkHwC/L9xgiNFXFA9JJTOVLxqMLXb/zanlO4ZiomV+BKvxGtI2jnQYI5n7CU8AyIC0RclnXzpS99aefIkSPdDOEEc3zpS1+688IXvrCLOs8vYQGYAZzAp1B6XqK0jWfPcGamR1DZlr9biVIaDmkwuEFKPsdQ1ijrjsr+ueee2+0ry6fKqN4HKUux/Mpy6+W6RXj3+8p4hP0jftzQ8ZHavjGtuI/OHfOg56T9dE2+LV4v3V963//gD/5gj4LDOiYWdp8ct3DHbaVzlEQKn/8OiRRlXx/lP/7jP1LpSWYlFaYGNNv4GFHFdtZZZ+3bNlaoyPiqVHRj0qWx0dfqskSVIOevoeuMlbiWCatPPgmuF9dvC3/8x3/chZzQfeCr/X3ve5/vNjvcp3vuuadTVLAscg9pIFAMyIvuN40LeWKUGo6nfJFjSXnBC17QPTMUppNOOqmLA/Nd3/Vde4LrcT18tfMbz6tn5M/Vl7GYcCzLOJX79vjbgpc9hAYxxltCWfXtWnbFaIqyxD377//+73359nsQrzWuj/+BNOM6/19bLv3n2FI+IKarayHum6zD3CeeF12wpWv2dSVRHiQqQ1ov5VfvSvyoi1amPiVH1iVfXxM9XxSjJFkFqTA1QvRXf2H7JFZqyNjKW6KKSKIK5Zhjjumiz9KoT027RThfrMAd3+b/gWi3pEWDjWXhX/7lX3yXtXPllVfuKhBSSn7oh36ou7/Lgor+l37pl7rnx/k4rxp6vuhRdsjX17/+9T3Hle5xC7GRBRqzGLiV+EpMkMly6Ry1deedd97u8+WXLqjSviJu82UJ5X5M47mInHjiibt5iHkp/eoY8oYCx+9dd93VrfP723IP4jXH/zE9LXu+ESkgUxTEVimlGy3dsY6KeZa41Sgq7b6tJtqPUbxJsi5SYRoB4fL9Ra4JFUqsDFmHxcD3GyNqUFmOlVSLeXqqKF0RK/e4Lv4KjvNtWJtYlrWEYehEJI7niPvPDZOfoojQ3ck5dE+x5PzO7/xO1xVTYo78/O7v/m7nQ6OyQdcW0+L8+Z//+e4+pfP4PVyEUhpaR5nCz0c+KeQvbo+wLorAskEUZZ4n9xYrKMFa/Rr062UEietE3IcpK0qN+Fih8eVX5/RzQVyvZW2/4YYbdruxYjo07lGBoayX7pVfd1wnnyCOx2q4TIVoSKQIR9+pmvT5h03J/8c//vHd+5Uk6yYVppHwNSlTt1t/StJXgYwRr2xq5y75EswhnF/wX3jDVlsHsdGIDQNdSCgSWq+vSSweWHmI2KtRRppVve8cdJthucGyRaMvSwXHcx78b6ZYueJ1O54fFC8UbPw+ZC3BgnXHHXfs2a+Gp9fClGMgHufPx9f7PrX9tJ5r5zmgJKrLhZhNlCeeEWEIsJQOpe3r+GWexvPPP7/rapKS4uUW4Xy//Mu/vPPv//7v+9IVrNPz9TwM5SNuEwSnle8joQ9IW+dwiUrXHFL6eJqSfjxG9VjN6qd74utbJP2Mkm0hFaYJ0Bh+3/d936RKaA6pVVpITZGaQ7jeOPcS62qNhxMrVP3Xclyn/yzTkBIrCD8wrplJLj1Pnj+un64SrBwMa3fH7L48LgrWMzXc5IPZzEvn80ZW189oSLrgSOfYY4/tHK3Zxpe9rD66N/zGdfG5UzaxFHHPdA6XeP5SHoU/G1FLK/5q2f9/8pOf7BQY/Gp0jS5q9EtdNkqT+8K8YPiZca34+DHyqZYPXxfT8uspLZfSi/8RpYlyjpJx8skndz5epbqCZxaP4VeKSWn/sVJSnOYSWcB0nb69JNmdlmw7qTAtAF+3qji8cmgRVZJ9CtCQlCrWRdKLQv5khuc6VQFTQaqh84YkUmpgSo1Pib7tfdtgzPa4zPWMgZFpHMP9Jh1+sXrUYB/unaZ28GdH9ySTMD//+c/v7jVddYzM67ueuI0GiefEcRr1VNovrqs9i9J6X6fl0n5OPFa/8X5r2ffRtlgmhZ+ndI64Tb9R/LxOTBP0vst6pHfNn6Xelb53cWy9sUwFaKxgtfN1knTCTg4qqTAtCFOcUJGNrfyiUCHrKw18+yYI+QPyyvXy5c81a6hxqUHS/xIcI+I+Wu9plNLpW+fb/L/oW1/axjq6ENVwEl6A3xrMPUVXHMfpGfNLNw33kS46dUn4+fy/1pXWi75tQ/e29FsS0bKs/56mP3+VodI5osT9tD3+9uFpeTqkLb8mPaeopLhSVLJ+laRvv2hl0v9Wi826hfuBcI+yWy05DKTCNAM4ujKPEBXd1MouNgibJCgDsStIKL9sY8Re6Us6NkbeOEV8X/5HfP+4LqYb/w8dE39LaJvuAUoP16pGkwbCj1f0bDl1I1iMLr/88n0NSsynX4uu39MXvt6vx3+F0o6/pTzU7r+nJ2rrI76PzlnKj5cf/dey57uUNnONqctSFqFXvepVXagF+QzRdam0p4red8+371cS5a307myS+L3OrrXksJIK04wQDZkKZRFrU6ygfP0yRBaivjxrW2yYtMz6uA6JSmNpZA0NBPvI2VfXquWYfsTXxTzp2Phf3SbEKNJ1RmtgPE5oOVrPGHrPrORxO8j6EBWpP/mTP9lzT4TnU9Cws/+jjz66q5iqISWkgWZHZ24/roeRfPh1sV3KbOwG9PS1Lm7z6433Xv/B71FfunHd0P4qB1qncyofvhyVHv7zTI8//vhdCwddmSpn0Qqk5Wgl0j0uic7nlqWo0MT8LSJurVqXMAoNBUiiyNd9EbCT5LCSCtMSYNoHKuapPgeg5VV/ffZV5ESPJj+EAZB/TGzwYkOp//EXoTF67nOfuyeIXlSwZBXQfzWKKC3855eRbqyTH0VJ2WN0HPvgdButAI7W8XvBBRfsaXiVb0E6BIpkG+dk6g1dr+g7T7wu5YnzkVcpZ6RNNx8R5vWfqVee9rSn7U4PQXcev8RqIjwCXT6ybupeROWLcyvqPM/t3e9+924+a6I8Dy0LP1brIn4ORPeCfOHorucdr0H3QcsuSqvU9aVzSOny7VGGtm+TREUoFZ8kmYdUmJYEldSzn/3sPcrAVFlmRV5TyPq+xDkmNoZxG8SGVetjAxm3xf2F/isfyC233NI19Lfeeuvu+m9961t79tc5IvG/7/eGN7yha4i5HnWNxP1Zh/Kia5AS1Ue8Lqd0bFyn++Tr9d/XaX0fMT3KIg7lKJzxmTHsX4oVxOcVJaZXI27Xce94xzu6jwfunxRBnaOk5Lj4PhynZb0b6mbT+lK51jXGdX2KWE08P1NEiiH5lNXzkUce2Ze/mjAaMJWhJFktqTAtGeZTY2qKRZSeOZSuVqHC7lOWXKj0UWRAx3sD68txPxHX639E59M2T9Px7QzZJ8o4aej6sNoQVyse/8pXvnJ3H8IY8KWu7Tq//5bWxW2lPJbugRO3le6LH6//pTRrxwOBJXV/ESmOSF8+47rHHntstyuLqPgM949pTpGhd6ZWTkvK0qIylJexEp9VTTQXWnaPJclmkArTinj88ce7Btorziky5at4VRLzpgZXy97oegOh7fEY7Rf3j8f7r5ZL3V8a3Rf3/6//+q+ugY3+McSainn2/HjetI+Iy+D7+n8tK8+333777jx8999//5576Q2npxF/fTmuq4nuQbxmfrlvAuVBFiPth9QUmJKyUbPSeJqLSjy3rmURGcpf6zl0v1MpSpLtIRWmNYCPU63BmEum+k8tImpoS1/4nh8aHnUN4Rfk+8d05KtEd44awKgcIMy3Fs+LI/DFF19sd/7b+1922WXdPmrgyZu26Tc2fPG/7xd/Rfwfj5WSwX89f22XDxPXqO4aBEsNfkqI9lHXktKN6emX4J3MkUasqJgnHefHa9mvucW66c921bLsd2mKoAi5I3WSJNtNKkxrhBhONIRDX63bIn4d0XITG2SsJ1omDpGWvSEH/UdJcGdlpa8Gm0Cino4a/TjTPc7TjEpjG8Tza1nndnwfrQM13Axd13QYCPlD6ZOvlPaP1+nnVN7jdv3364v76/+RI0d2fv7nf37fM0FOOeWUfXmIz2SMtChUNSlZnhaRqGhyr+UfFB3iKUdRWeWXbteo4EiSJEkiqTBtANdee23nL1OyzKxKlnluNaqykCA//dM/vWcft1KoMcPZW+u8yweFQPuKr3zlK3uuRcdERQVcGYnpROUj5kXrCIeAUhSP07mkoLzzne/srAoxnXju+Fta79eldCJxXWmbfuNyi4Kj8yNx/5ZjUUb8OfmzXVR0TVMlKkdJkiStpMK0QTz44IPdiCUaJip2bygOm3APZC3gP6jRi/t5l94ZZ5zR7aP9RVxW+lH83PrV/jWJaXrafp6YZkzb99F63xaJ6cTtKCyyvMniIiVG6fdJTcGJyqdvGyMlq9cYiddbkyRJkrlJhWlDISox/itU/v7FvmpZxfm9QQffByVAPkBahzL1sY99bE9DWWs4tS6mGffVOsBSooadbd7IC1+O6cX8xH3iL/gxMT9xH6XPLxMLo9hgqfvhH/7hLvxB33Pq29Yqfg+GRMouzy36XekaSuL3IEqSJMk6SYVpw8G/4pnPfGYxYvZBFZQVKUf8jxYNda3Fhtcb1tp6KDW8cR1KiCxa3gUllHY8h7b7vnFb/K/jvvnNb3bKBNclqxDnP+6443atQ0pTvjctyo+sTL5+GUIYAfLtz2aKJEmSbCqpMG0RzFWGw7I3WJssY60SteO8YVXjWvotCSgdfuN/rfNz+X9Pz9dFRQYFgkl6pXy58lMThT3w9SUp7Re7MPv2myo1i9EUSZIk2SZSYdpSGBrPxK7eoG2rxHABEm3Tsv9KIB6jxjgulxrruF/NGqOYQ76+JCXfnr4h77VzjpEWJSzKouf0+zhGkiRJtplUmA4A11xzzWxBMTdVaHD1C/qP6H9cF/eP6yXqAnNrzFQpncNFykpLlxrSqqhJxipPreL3skWSJEkOGqkwHTDe85737DzrWc/a1+htq8SuLCk3DOlHmZBoX5aJMaQYPFq/qFVlqngwyShjlaE+KVm2XNRVx3nVneb7tIgrRqkcJUlyWEiF6QDz8MMP75x11llLszysQ+ayCB1EiUqRQlNEpcYVnSlKUypISZIcVlJhOkQQKZsGtaZATW1E1y3RklOy5hwUcWURS5GcxKeIp18T7Z8kSXKYSYXpEKOh5wpw6A1qlDm7kFLmE39OY8TTkiRJkiT7SYUp2cUb1Jp4A5vSL37P/H+L1I7xZzNFkiRJkmFSYUqqeMNaEm/AU1Yr/jxqkiRJkixGKkzJKLwhjuKNecq84ve7JEmSJMlySIUpmQVvuDdFiRrKw9D2dYnfx1SIkiRJ1ksqTMnS8UZ/U5WUdUkqREmSJJtPKkzJRnKQlKtUhJIkSbafVJiSA4tbtaZKkiRJkqTClCRJkiRJMkAqTEmSJEmSJAOkwpQkSZIkSTJAKkxJkiRJkiQDpMKUJEmSJEkyQCpMSZIkSZIkA6TClCRJkiRJMkAqTEmSJEmSJAOkwpQkSZIkSTJAKkxJkiRJkiQDpMKUJEmSJEkyQCpMSZIkSZIkA6TClCRJkiRJMkAqTEmSJEmSJAOkwpQkSZIkSTJAKkxJkiRJkiQDpMKUJEmSJEkyQCpMSZIkSZIkA6TClCRJkiRJMkAqTEmSJEmSJAOkwpQkSZIkSTJAKkxJkiRJkiQDpMKUJEmSJEkyQCpMSZIkSZIkA6TClCRJkiRJMkAqTEmSJEmSJAOkwpQkSZIkSTJAKkxJkiRJkiQDpMKUJEmSJEkyQCpMSZIkSZIkA/wvxcZY/1getTcAAAAASUVORK5CYII=>