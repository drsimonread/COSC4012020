

| Circular Dichroism Spectrometer Traceability Matrix Version 2.0 02-24-21 402 Quality Assurance & Documentation Team |
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

[**2.2 Aspects List**](#2.2-aspects-list)	**[4](#2.2-aspects-list)**

[**2.3 Traceability Table**](#2.3-traceability-table)	**[5](#2.3-traceability-table)**

[**3\. Miscellaneous**](#3.-miscellaneous)	**[6](#3.-miscellaneous)**

**Revision History**

| Date | Version | Description | Author(s) |
| :---: | :---: | :---: | :---: |
| 9/22/20  | 1.0  | Traceability Matrix First Release |  Annette Orr, Braden Clough, Cameron Carpenter, Edward Park  |
| 2/24/21  |  2.0 | Traceability Matrix Second Release  | Annette Orr, Christopher Beatrez, Faith Meyer, Edward Park    |
|   |   |   |   |

---

##### **1\. Introduction** {#1.-introduction}

##### **1.1 Purpose** {#1.1-purpose}

The purpose of this Traceability Matrix is to document the Circular Dichroism Spectrometer’s (CD Spec) requirements, aspects, and functionalities. This document will be used by both the Research and Development (R\&D) team as well as the Quality Assurance and Documentation team (Q\&A) to keep track of the CD Spec project’s completeness.

##### **1.2 Scope** {#1.2-scope}

This document pertains to the CD Spec project and all of its associated documentation and files. The Traceability Matrix shall be used by project team members to check if the project’s requirements and functions have been implemented through the use of tables.

##### **1.3 Definitions, Acronyms, and Abbreviations** {#1.3-definitions,-acronyms,-and-abbreviations}

* **CD Spec \-** Circular Dichroism Spectrometer  
* **SRS \-** Software Requirements Specification  
* **R\&D** \- Research & Development  
* **Q\&A \-** Quality & Assurance

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

##### **2.2 Aspects List** {#2.2-aspects-list}

| Aspect Number | Aspect (Subsystem) Description |
| :---: | :---: |
| **A1** | Site takes in a username and password |
| **A2** | Database accepts file from Admin to upload |
| **A3** | Database sorts through and selects files |
| **A4** | Site displays information and instructions for database |
| **A5** | Site accepts text input from user |
| **A6** | Site allows user to download files from database |
| **A7** | Site filters private files to hide from public viewers |
| **A8** | Site provides graphical representations of data |
| **A9** | Site allows data to be searched |
| **A10** | Site allows account creation (public, student, or admin) |
| **A11** | Graph displays different colors for data differentiation |
| **A12** | Student account can upload files to the database |
| **A13** | Admin account can upload files to the database |

##### 

##### **2.3 Traceability Table** {#2.3-traceability-table}

|   | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 | A11 | A12 | A13 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **R1** | **X** |   |   |  **X** |   |   |   |   |  |  |  |  |  |
| **R2** | **X** |   |   |   | **X**  |   |   |   |  | **X** |  |  |  |
| **R3** |   |  |   |   |   |   |   |   |  | **X** |  |  |  |
| **R4** |   |   |  |   | **X**  |   |   |   |  |  |  |  |  |
| **R5** | **X** |   |  |   | **X**  |   |   |   |  | **X** |  |  |  |
| **R6** |   |   |  |   | **X**  |   |   |   |  |  |  |  |  |
| **R7** |  | **X** |  |  |  |  | **X** |  |  |  |  |  |  |
| **R8** |  |  |  |  | **X** |  |  |  |  |  |  |  |  |
| **R9** |  **X** |  **X** | **X**  |   | **X**  | **X**  |   | **X**  | **X** | **X** |  |  |  |
| **R10** |  |  |  |  | **X** |  |  |  |  |  |  |  |  |
| **R11** |  |  |  | **X** |  |  |  |  |  |  |  |  |  |
| **R12** |  |  |  | **X** |  |  |  | **X** |  |  |  |  |  |
| **R13** |  |  |  |  | **X** |  |  | **X** | **X** |  |  |  |  |
| **R14** |  |  |  |  |  |  |  | **X** |  |  |  |  |  |
| **R15** |  | **X** |  |  |  |  |  |  |  |  |  |  |  |
| **R16** |  | **X** |  |  |  |  | **X** |  |  |  |  |  |  |
| **R17** |  |  |  |  | **X** |  |  |  |  |  |  |  |  |
| **R18** |  |  |  | **X** |  |  |  |  |  |  |  |  |  |
| **R19** |  | **X** |  |  |  |  | **X** |  | **X** | **X** |  |  |  |
| **R20** |  |  |  |  |  |  |  | **X** |  |  | **X** |  |  |
| **R21** |  | **X** | **X** | **X** |  |  |  |  | **X** |  |  | **X** | **X** |
| **R22** |  |  |  |  |  |  |  | **X** |  |  | **X** |  |  |
| **R23** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R24** |  |  |  |  |  |  |  | **X** |  |  | **X** |  |  |

##### ---

**3\. Miscellaneous** {#3.-miscellaneous}

None.  
