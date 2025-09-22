

| Circular Dichroism Spectrometer Traceability Matrix Version 1.0 09-22-20 401 Quality Assurance & Documentation Team |
| :---- |

---

**Table of Contents**

[1\. Introduction](#heading=h.et0tvt7dx1vu)	[**1**](#heading=h.et0tvt7dx1vu)

[1.1 Purpose](#1.-introduction)	[**1**](#1.-introduction)

[1.2 Scope](#1.2-scope)	[**1**](#1.2-scope)

[1.3 Definitions, Acronyms, and Abbreviations](#1.3-definitions,-acronyms,-and-abbreviations)	[**1**](#1.3-definitions,-acronyms,-and-abbreviations)

[1.4 Document References](#1.4-document-references)	[**1**](#1.4-document-references)

[1.5 System Overview](#1.5-system-overview)	[**1**](#1.5-system-overview)

[2\. Traceability](#heading)	[**2**](#heading)

[2.1 Requirements List](#2.1-requirements-list)	[**2**](#2.1-requirements-list)

[2.2 Aspects List](#2.2-aspects-list)	[**3**](#2.2-aspects-list)

[2.3 Traceability Table](#2.3-traceability-table)	[**3**](#2.3-traceability-table)

[3\. Miscellaneous](#3.-miscellaneous)	[**4**](#3.-miscellaneous)

**Revision History**

| Date | Version | Description | Author(s) |
| :---: | :---: | :---: | :---: |
| 9/22/20  | 1.0  | Traceability Matrix First Release |  Annette Orr, Braden Clough, Cameron Carpenter, Edward Park  |
|   |   |   |   |
|   |   |   |   |

---

##### 1\. Introduction {#1.-introduction}

##### 1.1 Purpose

The purpose of this traceability matrix is to provide a full detailed description of the Circular Dichroism Spectrometer (CD Spec) software application’s requirements, aspects, and functionalities. This document shall be of use to all teams involved in the creation of this spectrometer and shall be used to track the completeness of the project. 

##### 1.2 Scope {#1.2-scope}

The scope of the traceability matrix is to check if the current project requirements are fulfilled through the use of tables. It is also used to keep track of project proposals, progress and helps determine what needs to be adjusted in the future. 

##### 1.3 Definitions, Acronyms, and Abbreviations {#1.3-definitions,-acronyms,-and-abbreviations}

* **CD Spec \-** Circular Dichroism Spectrometer  
* **SRS** \- System Requirements Specification

##### 1.4 Document References {#1.4-document-references}

* **Software Requirements Specification**, Version 1.0, 09-17-20

##### 1.5 System Overview {#1.5-system-overview}

The application to be built is a standalone web application that serves as an instrument to analyze circular polarized light. The application will be able to be accessed through most web browsers such as, Google Chrome, Mozilla Firefox, Microsoft edge, etc. Once accessed the user will be asked to input login credentials in order to view information in the site’s database. The web application should be able to be used by at least 200 users. 

---

#####  {#heading}

##### 2\. Traceability

*This section contains a table consisting of a requirements list (columns) and list of "aspects of the system" (rows). The table illustrates any relationships between requirements and aspects through the use of a symbol at the intersection of the two.*

##### 2.1 Requirements List {#2.1-requirements-list}

*The following table contains a list of requirement numbers and the SRS section numbers and section titles they refer to.*

| Requirement Number | SRS Section Number | SRS Section Title |
| :---: | :---: | :---: |
| R1 | 2.1 | Start up page |
| R2 | 2.1.1 | Login page |
| R3 | 2.1.1.1 | Create account button  |
| R4 | 2.1.1.2 | Enter Username |
| R5 | 2.2 | Account Creation Page |
| R6 | 2.2.1 | Login Interface |
| R7 | 2.2.2 | Student/Admin Account Creation (Key) |
| R8 | 2.3 | Application Home Page |
| R9 | 2.3.1 | Data Access |
| R10 | 2.3.2 | Data Search Bar |
| R11 | 2.3.3 | About/Help Tab |
| R12 | 2.3.4 | Data Compare Button |
| R13 | 2.3.4.1 | Data Comparison Parameters |
| R14 | 2.3.4.2 | Data Graphical Representation |
| R15 | 2.3.5 | Admin Upload Page |
| R16 | 2.3.5.1 | Admin Edit/Create Button |
| R17 | 2.3.5.2 | Data Upload (CSV or Text Files) |

##### 2.2 Aspects List {#2.2-aspects-list}

*The following table contains a list of system aspect numbers and a brief description of the aspect. An aspect is a functional subsystem of the whole software program.*

| Aspect Number | Aspect (Subsystem) Description |
| :---: | :---: |
| A1 | Site takes in a username and password |
| A2 | Database accepts file from Admin to upload |
| A3 | Database sorts through and selects files |
| A4 | Site displays information and instructions for database |
| A5 | Site accepts text input from user |
| A6 | Site allows user to download files from database |
| A7 | Site filters private files to hide from public viewers |
| A8 | Site provides graphical representations of data |
| A9 | Site allows data to be searched |
| A10 | Site allows account creation (public, student, or admin) |

##### 2.3 Traceability Table {#2.3-traceability-table}

*The following table cross-references each requirement with each aspect, and vice versa.*

|   | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **R1** | **X** |   |   |  **X** |   |   |   |   |  |  |
| **R2** | **X** |   |   |   | **X**  |   |   |   |  | **X** |
| **R3** |   |  |   |   |   |   |   |   |  | **X** |
| **R4** |   |   |  |   | **X**  |   |   |   |  |  |
| **R5** | **X** |   |  |   | **X**  |   |   |   |  | **X** |
| **R6** |   |   |  |   | **X**  |   |   |   |  |  |
| **R7** |  | **X** |  |  |  |  | **X** |  |  |  |
| **R8** |  |  |  |  | **X** |  |  |  |  |  |
| **R9** |  **X** |  **X** | **X**  |   | **X**  | **X**  |   | **X**  | **X** | **X** |
| **R10** |  |  |  |  | **X** |  |  |  |  |  |
| **R11** |  |  |  | **X** |  |  |  |  |  |  |
| **R12** |  |  |  | **X** |  |  |  | **X** |  |  |
| **R13** |  |  |  |  | **X** |  |  | **X** | **X** |  |
| **R14** |  |  |  |  |  |  |  | **X** |  |  |
| **R15** |  | **X** |  |  |  |  |  |  |  |  |
| **R16** |  | **X** |  |  |  |  | **X** |  |  |  |
| **R17** |  |  |  |  | **X** |  |  |  |  |  |

---

##### 3\. Miscellaneous {#3.-miscellaneous}

*\[Additional material of use to the reader of the Traceability Matrix.\]*

