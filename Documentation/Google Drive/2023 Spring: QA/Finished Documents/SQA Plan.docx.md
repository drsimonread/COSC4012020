**Circular Dichroism Spectrometer**  
**Software Quality Assurance**  
**Version 1.1**  
**02-08-23**

**402 Quality Assurance & Documentation Team**  
---

Suggestions From 401 Team to Incoming Team:

* Try New ideas()  
* Possibility go out and try to meet face to face for user stories  
* Discuss the project’s potential and possibilities for the future

DO’s

1. **SDP-** this document will help you set up the whole plan for the semester. This will include what requirements you plan to complete any and all documents that will be worked on as well. Every part of your plan will form in this document and this will set the tempo for both QA & R\&D.  
2. **SRS** \- The Software Requirement Specifications document is very important as it will detail all the requirements that have  been requested by the client. It is necessary to have at least this document as it will help the team remember what needs to be implemented into the application.  
3. **STP** \- The Software Test Plan document is necessary for documenting test plans and procedures that the team will go through to ensure that the application is running as intended. Test procedures need to be written and followed in order to catch any errors or bugs that the application may have so that the team does not deploy a buggy product to the client.  
4. **Traceability Matrix \-** The purpose of this traceability matrix is to provide a full detailed description of the Circular Dichroism Spectrometer (CD Spec) software application’s requirements, aspects, and functionalities. This document shall be of use to all teams involved in the creation of this spectrometer and shall be used to track the completeness of the project.   
5. **Gantt Chart** \- this is not strictly necessary, but helpful to lay out the overall plans for document completion. Team members can use this chart to keep track of what needs to be done and what has already been done.  
6. **User stories** \- absolutely necessary. The team needs a clear understanding of what users of the application want it to do for them. These requirements, as well as the ones given by the client, will then need to be documented in the SRS document.  
7. **SQA** \- Software Quality Assurance document (this document): detail all documents that will be made by the team. This is the overall plan of what the Q\&A team will be doing throughout the duration of the course. Please update this with new documents and other information that pertains to producing this product until this project is taken out of commission.  
8. **Presentations** \- present the documents that have been completed as well as documents that planned to be completed in the future. The goal is to provide the client with an understanding of what is being accomplished in the Q\&A team throughout the duration of the project. Also include in the presentation the details of the project as understood by the Q\&A team so that there can be communication between the team and the client (if needed) about the specified requirements of the project.  
9. **Update Logs** \- A written Update Document that contains the current functions of the project, new additions, removed or replaced variations, and the legacy programs left over  
     
     
   

DON’Ts

Please do not copy our work from previous semesters. This project requires us to be able to produce our own documentation for the project or it proves nothing in terms of your knowledge and skill.

R\&D Getting Started ([Reference Slides](https://docs.google.com/presentation/d/1sUcOJ-2MaxNYep1vZ-9mD6MNnpN2O9dfuUiqZe4mRM8/edit?usp=sharing))

To get setup with our prototype you need a couple pieces of software. First, some git clients, you can use the git command line, but I really recommend [GitHub Desktop](https://desktop.github.com/), it makes managing different branches and commits really easy. You will also need [Docker Desktop,](https://www.docker.com/products/docker-desktop) which will let you run our docker container. Docker desktop requires you to be on the latest version of windows, and you may run into some areas you need to troubleshoot, such as if your bios need to have virtualization enabled, or if you have multiple hard drives.

It's also important to understand the differences between the different command lines we will be working with. The command line for your computer is what I will call command prompt, for windows that’s Command Prompt, for mac its Terminal. Later we will instead use command lines that are “inside” our docker containers.

To test your Docker installation worked, run: **docker run \-d \-p 80:80 docker/getting-started**

Then open docker desktop, find the container it created, it will be a random name, but will have the image name, “docker/getting-started” next to it. If you hover over it, you will see buttons appear to the right, those give you the ability to run certain functions on the container without having to use the command line. For now just click the one with the arrow coming out of the square that says open in the browser. If everything works, you should get a docker tutorial landing page. If not, clicking on the container will bring up its logs which will help you debug. You can then stop and delete the container using those function buttons.

           	Now that you have verified your docker installation works, you can install our container. To do so, you first clone our github repo, it’s url is: [https://github.com/lhjamieson/COSC4012020](https://github.com/lhjamieson/COSC4012020) and to clone it in GitHub Desktop you click, File \-\> Clone Repository, and either click on the repository if your logged in or paste in the URL. Next open your command prompt and navigate to the folder that your repository is located at, in Windows user’s case it's most likely located in Documents. To do this, I would open the command prompt and type **cd Documents, cd GitHub, cd COSC4012020 or just cd Documents/GitHub/COSC4012020.** Once you're located in our repository, you want to cd into the  **cd\_spec\_viewer\_web** folder. It should be the one with a docker-compose file inside it. Now we need to build our containers. Our app uses multiple containers, so instead of using the docker command in the command prompt, we instead use docker-compose, which lets us compose multiple containers.

           	To build our containers we first run **docker-compose \-f docker-compose.yml build**, this may take a couple minutes as it downloads all the requirements. Next you run **docker-compose \-f docker-compose.yml up**, after this you should be able to just use the buttons in the Docker Desktop gui stop and start the container and you should be able to see our landing screen at [http://localhost:8000](http://localhost:8000/). Just as a note, if you are on windows and after closing docker are still getting Vmmem taking up lots of resources, you can run **wsl \--shutdown** to force shutdown the virtual machine in the background.

           	Some important things to note about docker, if you add requirements to the project, such as django libraries you need to update that in the requirements/base.txt and need to delete the container and rebuild it. You should however, unless requirements change, be able to change files within the container, directly or via GitHub without needing to restart or rebuild. It's also important to note that things inside the database shared with the container or GitHub, it will be empty for everyone when they first build it.

           	Within our docker app, we have two main containers, Django and Postgres. Django is our web framework and Postgres is our database, they are housed in different containers just for ease of setup with Docker. Django+Docker is nice, and we don’t ever have to touch the database directly, it just has to be running. All your work will happen within the Django container.

           	Our base Django app and Docker setup comes from a template called [Django Cookiecutter](https://cookiecutter-django.readthedocs.io/en/latest/index.html), it has a lot of stuff for us already done and is a good place to reference if you have questions about the project structure and what things are included. If you want to run commands within the Django container, like if a guide somewhere tells you to run pip or python manage.py, you can get a shell within the container by clicking on the stack of containers, then the Django container and choosing the CLI button. The most common time you will have to do this is to migrate model changes to the database.

I recommend doing the [Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-the-polls-app) before jumping into our project, it walks you through how Django apps work and will be a great point of comparison when understanding our application. The distinct differences between our project and the tutorial is just where files are and the fact we have both local and production versions of some things. For instance, all our template files are inside the template folder, with respective folders for our different apps within the project. The settings files are located in the config file and are made up of base, local and production. This is also seen elsewhere in the project. Base has things that are always necessary, where local and production only have things that apply to those unique environments. If you compose with docker-compose.yml you are using the local versions of everything, to deploy to production later you would use production.yml we just renamed local.yml to docker-compose for ease of use with Docker Desktop. Requirements within the requirements folder, also work this way, these are pip requirements.

 

