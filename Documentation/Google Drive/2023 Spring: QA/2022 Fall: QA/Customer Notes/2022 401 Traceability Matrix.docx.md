

| Circular Dichroism Spectrometer Traceability Matrix Version 3.1 10/5/2022 401 Quality Assurance & Documentation Team |
| :---: |

---

**Table of Contents**

**[1\. Introduction](#1.-introduction)	[2](#1.-introduction)**

[**1.1 Purpose**](#1.1-purpose)	**[2](#1.1-purpose)**

[**1.2 Scope**](#1.2-scope)	**[2](#1.2-scope)**

[**1.3 Definitions, Acronyms, and Abbreviations**](#1.3-definitions,-acronyms,-and-abbreviations)	**[2](#1.3-definitions,-acronyms,-and-abbreviations)**

[**1.4 Document References**](#1.4-document-references)	**[2](#1.4-document-references)**

[**1.5 System Overview**](#1.5-system-overview)	**[2](#1.5-system-overview)**

[**2\. Traceability**](#2.-traceability)	**[2](#2.-traceability)**

[**2.1 Requirements List**](#2.1-requirements-list)	**[3](#2.1-requirements-list)**

[**2.2 Aspects List**](#2.2-tests-list)	**3**

**2.3 Python Files List	[4](#2.2-tests-list)**

[**2.4 Traceability of Aspects to Requirements Table**](#2.4-traceability-table) 	**[5](#2.4-traceability-table)**

**2.5 Traceability of Python Files to Requirements Table**	

[**3\. Miscellaneous**](#3.-miscellaneous)	**[6](#3.-miscellaneous)**

**Revision History**

| Date | Version | Description | Author(s) |
| :---: | :---: | :---: | :---: |
| 9/22/20  | 1.0  | Traceability Matrix First Release |  Annette Orr, Braden Clough, Cameron Carpenter, Edward Park  |
| 2/24/21  |  2.0 | Traceability Matrix Second Release  | Annette Orr, Christopher Beatrez, Faith Meyer, Edward Park    |
| 9/14/22 | 3.0 | Traceability Matrix Third Release  | Mathias Boddicker,  Victor Riley, Marian Marteja, Liam Pratt, Jordan Reece, Gavin McDonald  |
| 10/5/22 | 3.1 | Traceability Matrix Python Files and Requirements Update | Mathias Boddicker,  Victor Riley, Marian Marteja, Liam Pratt, Jordan Reece, Gavin McDonald |
|  |  |  |  |

---

##### **1\. Introduction** {#1.-introduction}

##### **1.1 Purpose** {#1.1-purpose}

The purpose of this Traceability Matrix is to document the Circular Dichroism Spectrometer’s (CD Spec) requirements, aspects, and functionalities. This document will be used by both the Research and Development (R\&D) team as well as the Quality Assurance and Documentation team (QA) to keep track of the CD Spec project’s completeness.

##### **1.2 Scope** {#1.2-scope}

This document pertains to the CD Spec project and all of its associated documentation and files. The Traceability Matrix shall be used by project team members to check if the project’s requirements and functions have been implemented through the use of tables.

##### **1.3 Definitions, Acronyms, and Abbreviations** {#1.3-definitions,-acronyms,-and-abbreviations}

* **CD Spec \-** Circular Dichroism Spectrometer  
* **SRS \-** Software Requirements Specification  
* **R\&D** \- Research & Development  
* **QA \-** Quality & Assurance

##### **1.4 Document References** {#1.4-document-references}

* **SRS \-** Software Requirements Specification

##### **1.5 System Overview** {#1.5-system-overview}

The application to be built is a standalone web application that serves as an instrument to analyze circular polarized light. The application will be able to be accessed through most web browsers such as Google Chrome, Mozilla Firefox, Microsoft Edge, etc. Once accessed the user will be asked to input login credentials in order to view information in the site’s database. The web application should be able to be used by at least 200 users. 

##### ---

**2\. Traceability** {#2.-traceability}

##### **2.1 Requirements List** {#2.1-requirements-list}

| Requirement Number | SRS Section Number | SRS Section Title |
| :---: | :---: | :---: |
| **R1** | 2.1 | Start up page |
| **R2** | 2.1.1 | Login page |
| **R3** | 2.1.1.1 | Create account button  |
| **R4** | 2.1.1.2 | Enter Username |
| **R5** | 2.2 | Account Creation Page |
| **R6** | 2.2.1 | Login Interface |
| **R7** | 2.2.2 | Student/Admin Account Creation (Key) |
| **R8** | 2.5 | Application Home Page |
| **R9** | 2.5.6 | Data Access |
| **R10** | 2.5.2 | Data Search Bar |
| **R11** | 2.5.3 | About Page |
| **R12** | 2.5.4 | Data Compare Button |
| **R13** | 2.5.4.1 | Data Comparison Parameters |
| **R14** | 2.5.4.2 | Data Graphical Representation |
| **R15** | 2.5.5 | Admin Upload Page |
| **R16** | 2.5.5.1 | Admin Edit/Create Button |
| **R17** | 2.6.1 | Data Upload (CSV or Text Files) |
| **R18** | 2.4 | Help Page |
| **R19** | 2.5.1 | Data Unlocks (account privileges) |
| **R20** | 2.5.4.3 | Temperature Parameter (Graphing/Z-Axis) |
| **R21** | 2.5.5.2 | Description Box (Data Upload) |
| **R22** | 2.7.3 | Multi-Graph |
| **R23** | 2.7.1 | Voltage Parameter \* |
| **R24** | 2.7.2 | Temporal Scale Parameter/Display \* |

* (\*) \= TBD requirements/possibly not implemented in final product

##### **2.2 Tests List** {#2.2-tests-list}

| Test Number | Test (Subsystem) Description |
| :---: | ----- |
| **T1** | This test is intended to test the functionality of the user registration and login menus |
| **T2** | This test is intended to test the functionality of the password reset function |
| **T3** | This test is intended to test the functionality of the application within several web browsers, including but not limited to: Google Chrome, Mozilla Firefox, Safari, and Microsoft Edge. |
| **T4** | This test is intended to test the functionality of the data upload function. |
| **T5** | This test is intended to test the functionality of the search engine. |
| **T6** | This test is intended to test the functionality of an administrator account. |
| **T7** | This test is intended to test the functionality of a student account |
| **T8** | This test is intended to test the functionality of a public account. |
| **T9** | This test is intended to test the functionality of student account creation (by admin or in general). |
| **T10** | The purpose of this test is to test the character limits within the file description. |
| **T11** | This test is intended to test the functionality of the color customizer on multi graphs |
| **T12** | This test is intended to test the functionality of graph image downloading  |
| **T13** | The purpose of this test is to test the capabilities of the administrator level account. |
| **T14** | The purpose of this test is to test the constraints of the multi-graph function. |
| **T15** | This test is to test the functionality of account authentication and permissions |
| **T16** | This test is to test the application’s handling of invalid file uploads. |
| **T17** | This test is to test the application’s About page. |

##### 

**2.3 Python Files List**

| Python Number | Python File Name |
| :---: | :---: |
| **P1** | manage.py |
| **P2** | urls.py |
| **P3** | wsgi.py |
| **P4** | admin.py |
| **P5** | apps.py |
| **P6** | forms.py |
| **P7** | models.py |
| **P8** | tests.py |
| **P9** | urls.py |
| **P10** | util.py |
| **P11** | views.py |
| **P12** | 0001\_initial.py |
| **P13** | 0002\_auto\_20210420\_1801.py |
| **P14** | 0003\_auto\_20210420\_1809.py |
| **P15** | adapters.py |
| **P16** | admin.py |
| **P17** | apps.py |
| **P18** | forms.py |
| **P19** | models.py |
| **P20** | urls.py |
| **P21** | views.py |
| **P22** | 0001\_initial.py |
| **P23** | 0002\_auto\_20210316\_2244.py |
| **P24** | 0003\_auto\_20210412\_1302.py |
| **P25** | factories.py |
| **P26** | test\_forms.py |
| **P27** | test\_models.py |
| **P28** | test\_urls.py |
| **P29** | test\_views.py |

##### **2.4 Traceability Table** {#2.4-traceability-table}

|   | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 | T15 | T16 | T17 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **R1** |  | **X** | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R2** | **X** | **X** | **X** |  |  |  | **X** | **X** | **X** |  |  |  |  |  |  |  |  |
| **R3** |  |  | **X** |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |
| **R4** |  |  | **X** |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |
| **R5** |  |  | **X** |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |
| **R6** |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R7** |  |  | **X** |  |  | **X** | **X** |  | **X** |  |  |  |  |  |  |  |  |
| **R8** |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R9** |  |  | **X** |  |  |  |  | **X** |  |  |  | **X** |  |  |  |  |  |
| **R10** |  |  | **X** |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |
| **R11** |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |
| **R12** |  |  | **X** |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |
| **R13** |  |  | **X** |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |
| **R14** |  |  | **X** |  |  |  |  |  |  |  | **X** |  |  | **X** |  |  |  |
| **R15** |  |  | **X** | **X** |  | **X** |  |  |  |  |  |  | **X** |  |  | **X** |  |
| **R16** |  |  | **X** |  |  | **X** |  |  |  |  |  |  | **X** |  |  |  |  |
| **R17** |  |  | **X** | **X** |  | **X** | **X** |  |  |  |  |  |  |  |  | **X** |  |
| **R18** |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R19** |  |  | **X** |  |  | **X** | **X** | **X** |  |  |  |  |  |  | **X** |  |  |
| **R20** |  |  | **X** |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |
| **R21** |  |  | **X** | **X** |  | **X** | **X** |  |  | **X** |  |  |  |  |  |  |  |
| **R22** |  |  | **X** |  |  |  |  |  |  |  | **X** |  |  | **X** |  |  |  |
| **R23** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R24** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**2.5 Traceability Table of Python File to Requirements**

|  | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P17 | P18 | P19 | P20 | P21 | P22 | P23 | P24 | P25 | P26 | P27 | P28 | P29 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **R1** |  | **x** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |
| **R2** | **x** | **x** |  |  |  |  |  |  |  |  |  | **X** |  |  | **X** |  |  |  |  |  |  | **X** |  |  |  |  |  |  | **X** |
| **R3** |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  | **z** |
| **R4** |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  | **X** | **X** |
| **R5** |  | **x** |  | **x** |  |  |  |  | **X** |  |  |  |  |  | **X** |  |  |  |  |  |  | **X** |  |  |  | **X** |  | **X** |  |
| **R6** |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  | **X** |  |  |  | **X** |  | **X** | **X** |
| **R7** |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |
| **R8** |  | **x** |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |
| **R9** |  |  |  |  |  | **X** |  |  |  |  | **X** | **X** |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  | **X** |  |
| **R10** |  | **x** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R11** |  | **x** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R12** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |
| **R13** |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |   |
| **R14** |  |  |  |  |  |  | **X** |  |  | **X** | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |
| **R15** |  | **x** |  | **x** |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  | **X** |  |
| **R16** |  |  |  | **x** |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** | **X** |  |
| **R17** |  |  |  | **x** |  |  |  |  |  | **X** | **X** | **X** |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |
| **R18** |  | **x** |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R19** |  |  |  |  |  |  |  |  |  |  | **X** | **X** |  |  | **X** |  |  |  |  |  |  | **X** |  |  |  |  |  | **X** |  |
| **R20** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  | **X** |  |  |
| **R21** |  |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R22** |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |  |  |  | **X** |  |  |  |  |  |  |  |
| **R23** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **?** |  |  |  |  | **X** |  |  |
| **R24** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **?** |  |  |  |  | **X** |  |  |

##### ---

**3\. Miscellaneous** {#3.-miscellaneous}

None.  
