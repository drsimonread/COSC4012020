

| CD Spectrometer System Overview Version 1.0 12/16/2022Eythan Jenkins |
| :---: |

---

**Table of Contents**

[**1\. Introduction**](#introduction)	**[3](#introduction)**

[1.1 Purpose](#1.1-purpose)	[3](#1.1-purpose)

[1.2 Notable Documents (QA)](#1.2-notable-documents-\(qa\))	[3](#1.2-notable-documents-\(qa\))

[1.3 Notable Documents (R\&D \+ SysOps)](#1.3-notable-documents-\(r&d-+-sysops\))	[3](#1.3-notable-documents-\(r&d-+-sysops\))

[1.4 Project Lead tips](#1.4-project-lead-tips)	[3](#1.4-project-lead-tips)

[1.4.1 Schedule the semester](#1.4.1-schedule-the-semester)	[3](#1.4.1-schedule-the-semester)

[1.4.2 Determine team member capabilities](#1.4.2-determine-team-member-capabilities)	[4](#1.4.2-determine-team-member-capabilities)

[1.4.3 Project kickoffs](#1.4.3-project-kickoffs)	[4](#1.4.3-project-kickoffs)

[1.4.4 Investing in your Teams](#1.4.4-investing-in-your-teams)	[4](#1.4.4-investing-in-your-teams)

[1.4.5 Sprints and SMART goals](#1.4.5-sprints-and-smart-goals)	[5](#1.4.5-sprints-and-smart-goals)

[**2\. Problem Overview**](#problem-overview)	**[5](#problem-overview)**

[2.1 The Problem](#2.1-the-problem)	[5](#2.1-the-problem)

[2.2 Where to Start](#2.2-where-to-start)	[5](#2.2-where-to-start)

[**3\. Technologies**](#technologies)	**[6](#technologies)**

[3.1 Python/Django](#3.1-python/django)	[6](#3.1-python/django)

[3.2 Docker](#3.2-docker)	[7](#3.2-docker)

[3.3 GitHub](#3.3-github)	[7](#3.3-github)

[3.4 Postgres SQL](#3.4-postgres-sql)	[7](#3.4-postgres-sql)

[3.5 HTML](#3.5-html)	[7](#3.5-html)

[**4\. Miscellaneous**](#miscellaneous)	**[7](#miscellaneous)**

[4.1 Contact](#4.1-contact)	[7](#4.1-contact)

## 

1. ## **Introduction** {#introduction}

   ### **1.1 Purpose** {#1.1-purpose}

   	The purpose of this document is to put some of the most pertinent information up-front for you. This way, you don’t have to waste time scavenging through old documentation to find what you need. That said, this isn’t a fully comprehensive system overview; it only features the basic important information. Essentially, this document will just buy you (the team leader) some time to look through the rest of the documentation found in the Google Drive; you can distribute this basic information while you compile everything else you need.  
   	I will also give a brief summary of the problem, and a good place for you to start in Section 2\. Finally, I will give a quick guide of the technologies that were used in the CD Spectrometer in Section 3\.

   ### **1.2 Notable Documents (QA)** {#1.2-notable-documents-(qa)}

* [2020 Technologies and Setup of Docker/Program](https://docs.google.com/document/d/1wzThzRE0e8TytDtg5rliTSWjFywjgGcn/edit)  
* [Fall 2022 Software Development Plan](https://docs.google.com/document/d/1NCrCfgMO1vy-2-5pCEFXUddSaNVeE5q6/edit)  
* [Fall 2022 Software Requirements Specification](https://docs.google.com/document/d/1B5RWXDXoBzKk53BP8v5asbVrYDeHQ5Yu/edit)  
* [Fall 2022 Software Design Document](https://docs.google.com/document/d/1QHaugyZJza6F5Ha1sR35XyYQeH17drAK/edit)  
* [Fall 2022 Software Test Plan/Results](https://docs.google.com/document/d/1mc7_ivK7_dAfEJkCivOyOHRxO1GsEfL_/edit)  
* [Fall 2022 Traceability Matrices](https://docs.google.com/document/d/1va4yA-UqGLyqWU0UNdptg5Mc37l0xCEl/edit)

  ### **1.3 Notable Documents (R\&D \+ SysOps)** {#1.3-notable-documents-(r&d-+-sysops)}

* [2020 Technologies and Setup of Docker/Program](https://docs.google.com/document/d/1wzThzRE0e8TytDtg5rliTSWjFywjgGcn/edit)  
* [2020 R\&D Getting Started](https://docs.google.com/presentation/d/1yGZHITerYEItUUly-sde05A_tJxClaWn/edit#slide=id.p1)  
* [2020 OIT Deployment Certificate Documentation](https://docs.google.com/document/d/1dWw2RABaazVd9OSh_3Z-aBpQjHWACIU7/edit) (at end of document)  
* [Docker Commands](https://docs.google.com/document/d/1EhWOe5ux8Tb_wdZmYBiu0DyDyOIOcGez/edit) (may need to be changed to match your GitHub Repository pathing)  
* [Chart of all .py files](https://drive.google.com/drive/u/1/folders/1WLPizIaEkl8I5MGQ3Wulv1Ar7_w-a8ZH) (inside drive folder)

  ### **1.4 Project Lead tips** {#1.4-project-lead-tips}

  	As project lead, you have a lot of work ahead of you\! I was fresh to being a project lead, and I made a lot of blunders early on. However, I learned from these mistakes, and I want to share what worked well for me and how to avoid some of these mistakes. I want to lay out a few tips for starting off as project lead, to help organize you as you begin on this project:

  #### **1.4.1 Schedule the semester**  {#1.4.1-schedule-the-semester}

* You may find it helpful to outline the entire semester’s schedule; you will want to be knowledgeable of any holidays that you won’t have class in, as well as the final in-class day, and final day within finals week.


* You don’t need to have specific goals set for these times when you begin the project; it is just important for you to gauge how much time you have so you can be aware of your total time resources.


  #### **1.4.2 Determine team member capabilities**  {#1.4.2-determine-team-member-capabilities}

* You will also want to determine the capabilities of your teams. Here’s a quick story: On my 3rd or 4th day as project lead, I had a bunch of plans ready for my teams. Instead, about half of one of my R\&D teams were absent and a bunch of other people too. Why? Because there was a Sports game that they had to play on that day. The lesson I learned: make sure you understand the other obligations your team members have, so that you can better gauge how many labor resources you will have access to on a given day.


* You will want to consider sports obligations, club obligations, birthdays, pretty much anything. You may find a Gantt chart or Excel sheet to be useful for compiling this information. Charting it alongside the 1.4.1 schedule may also be beneficial.


  #### **1.4.3 Project kickoffs**  {#1.4.3-project-kickoffs}

* You will want to give a presentation on the project that everyone is about to start on, basically a ‘Project Kickoff.’ You should include their responsibilities, the goal you want to have them achieve, and a tentative plan on how it will get accomplished. You will want to mention the technologies they will be using. This will offer direction and guidance to everyone.


  #### **1.4.4 Investing in your Teams**  {#1.4.4-investing-in-your-teams}

* It is perfectly fine to set aside multiple days for your teams to understand the technologies that they are going to work with. The more time you allow them to explore and familiarize themselves with the system and technologies they will be working with, the less blind they will be. Think of it as an investment.


* However, you should still set some framework for them to follow; it would be bad to just tell them to “play with \[technology\]” this week. You should try to assign them an actionable activity, with a measurable outcome (think SMART goals). This can be tangible tasks, like completing a tutorial, or watching specific YouTube videos on the topic.


  #### **1.4.5 Sprints and SMART goals** {#1.4.5-sprints-and-smart-goals}

* Hopefully you are familiar with the Agile workflow from COSC 301 Software Engineering. I believe that a great way of maintaining a schedule and distributing to-do lists for your teams are through Agile “Sprints”. Originally, I tried to distribute a daily plan, with objectives I wanted accomplished that day. BAD IDEA. This made everyday very rigid, and was far too micromanager-esque. It burnt me out pretty quickly. Instead, by swapping into bi-weekly Sprints, I created an overhead of activities, which allowed for flexibility and a much clearer picture of the project goals for the teams.


* You should set clear objectives for your teams; even better, have them be SMART goals. I failed hard at the start of the semester with one of my R\&D teams (I had two projects at once). I needed them to comment legacy code, but my only objective for them was, “comment the legacy code.” This didn’t work. What was much more effective, was giving them a measurable quota and breaking down the work into manageable components. My new goals became “Lets have .py files 1-18 commented by next Monday.” This was far better, because there was a measurable goal and a time for them to hit that goal by. Essentially, I went from a vague objective to an actionable one, and I started seeing results. 


2. ## **Problem Overview** {#problem-overview}

   ### **2.1 The Problem** {#2.1-the-problem}

   	The problem is simple, but complex. Simple: the software mostly functions, but has some bugs that need to be squashed. Complex: finding these bugs, and figuring out how to debug them.  
   	Fortunately, I can give you a bit of a head start, and offer a plan to locate these bugs, but you will need to devise your teams to fix them and schedule it out.

   ### **2.2 Where to Start** {#2.2-where-to-start}

   	I’ll start with a few pointers on the project’s structure, since it was pretty labyrinthine when we first started. Assuming you are viewing it through GitHub, there will be a “\_Deployed\_Folder” folder and a “\_cd\_Spec\_viewer\_web\_Folder.” The contents within them should be mostly identical. However, I believe that the \_cd\_Spec\_viewer\_web\_Folder has the Docker compose file (.yaml or .yml). Wherever the Docker compose file is, is the folder the Docker will create the project image from those folder’s contents.  
   	You will want to start by looking at these two documents (also found in section 1.3): [2020 Technologies and Setup of Docker/Program](https://docs.google.com/document/d/1wzThzRE0e8TytDtg5rliTSWjFywjgGcn/edit) and [2020 R\&D Getting Started](https://docs.google.com/presentation/d/1yGZHITerYEItUUly-sde05A_tJxClaWn/edit#slide=id.p1). These will assist you in being able to deploy the software on your own system. This will be imperative for the next steps. Make sure to adjust to changes made between then and now, like project pathing or name changes.  
   I recommend beginning with baselining the software. That is, take the software test plan we created, and have your team test the software as it currently is. This way, you can gather a status quo of the software and start identifying where the software is unsuccessful at. You may find the traceability matrices my QA team designed to be of help here; you should be able to decipher where the bugs are based on the tests which failed and which .py files are responsible for those tests.  
   	Our final test was conducted in December 2022, and you can review the results [here](https://docs.google.com/document/d/1mc7_ivK7_dAfEJkCivOyOHRxO1GsEfL_/edit). I would recommend using this to check for any discrepancies between your test results and ours. There should be no difference, but if there is a difference, then that is cause for concern since no one would have worked on it between our separate testing times. If they are different, this could be indicative of technologies going out-of-date and becoming incompatible with each other.  
   	Now that you have identified the errors with the software, you will need to assign your teams to fix these issues. They will likely be in the Python files, since the PostgresSQL database should be well encapsulated, and the HTML files should only deal with the website visual.  
   	

3. ## **Technologies** {#technologies}

   ### **3.1 Python/Django** {#3.1-python/django}

   	Python with Django is the meat of the technologies used for the CD Spectrometer website. If your R\&D team is new to this technology, you will likely find it advantageous to invest some knowledge into them with [a tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/). The base Django app and Docker setup comes from a template called [Django Cookiecutter](https://cookiecutter-django.readthedocs.io/en/latest/index.html), it has a lot of stuff already done and is a good place to reference if you have questions about the project structure and what things are included.

   ### **3.2 Docker** {#3.2-docker}

   	Docker is tricky; the first class which created this system used Docker to control for dependencies, and allow for easy packaging of the system. This is best explained by example: section 3.4 is “Postgres SQL,” which I am assuming you do not have installed on your system. Despite this, you will be able to run this program on your system, because Docker essentially creates a “container” of Postgres SQL for you.  
   	The endgame here is that as long as you have the Docker, you can run an ‘image’ of the program; you do not need to have Python, Django, or Postgres– you only need Docker.  
   	You may be interested in looking at the documentation left by the 2020 class; they contain both [a text document](https://docs.google.com/document/d/1wzThzRE0e8TytDtg5rliTSWjFywjgGcn/edit) and [a presentation](https://docs.google.com/presentation/d/1yGZHITerYEItUUly-sde05A_tJxClaWn/edit#slide=id.p1) which can help you get started with Docker technology. 

   ### **3.3 GitHub** {#3.3-github}

   	GitHub is used as the project’s source control. You may find it useful to use GitHub Desktop, as this in conjunction with Docker will make it easier to create an image of the program (Docker will clone a GitHub repository). 

   ### **3.4 Postgres SQL** {#3.4-postgres-sql}

   	Postgres SQL is the language used to upkeep the CD Spectrometer database. You shouldn’t have to interface directly with it; instead, the manage.py file should be able to create ‘migrations,’ which serve as a template for the database. 

   ### **3.5 HTML** {#3.5-html}

   	HTML was used to construct the visuals of the website. Similar to the Postgres SQL, this is a technology you shouldn’t have to worry about unless you plan on updating the visuals or displayed text.  
   

4. ## **Miscellaneous** {#miscellaneous}

   ### **4.1 Contact** {#4.1-contact}

   	I may be contactable at my school email [eajenkins1@smcm.edu](mailto:eajenkins1@smcm.edu)  
     
   	However, since I graduated FA 2022, you may have better luck contacting me at my default email, [eajenkins343@gmail.com](mailto:eajenkins343@gmail.com)  
   