# Development using Google Cloud Platform and Visual Studio Code

  

## Setting Up In the Google Cloud

  

-  **Creating Your Project**

	-  Claim your education credits from the email you received
	-  Go to https://console.cloud.google.com
	-  Accept the terms of service
	-  Click agree and Continue
	-  Click Select a Project
	-  Click New Project
	-  For project name enter your firstname-lastname-00 (i.e. simon-read-00)
	-  Your Organization and Location should be smcm.edu
	-  Click create
	-  In the notifications panel to the top right under project name, click Select Project
	-  Select Cloud Overview
	-  Select Dashboard

-  **Creating Your Server**

	-  From the dashboard, under Resources click Compute Engine
	-  Click on Enable if prompted
	-  In the new panel at the top, click on Create Instance
	-  Click on Enable if prompted
	-  Go back to Compute Engine
	-  For your instance name, put your name as firstname-lastname-instance-00 (i.e. simon-read-instance-00) and increment as appropriate
	-  Select Redtion as us-central-1 (Iowa)
	-  Select Any for Zone
	-  Ensure general purpose is selected
	-  Ensure E2 is selected
	-  On the left panel, select OS and Storage
	-  Click change
	-  Under Operating System, select "Ubuntu"
	-  Set version to "Ubuntu 22.04 LTS x86/64"
	-  Click Select
	-  Click on Networking on the left panel
	-  Under the Firewall heading check the boxes "Allow HTTP Traffic" and "Allow HTTPS Traffic"
	-  Scroll down and click on default in Network Interfaces
	-  Click the dropdown to expand default
	-  Ensure under External IPv4 Address that Ephemeral is selected
	-  Under Network Service Tier select Standard
	-  Click Create Instance

-  **Stopping Your Instance**

	-  Remember to Stop your instance every time you have finished working with it, or it will continue to charge against your Educational Credits and you will run out!
	-  In the VM window of Compute Engine select the 3 dots for your instance, and select stop
	-  The Status icon will change from a green tick back to a white square when shutdown is finished, this may take a few moments

-  **Starting Your Instance**

	-  In the VM window of Compute Engine select the 3 dots for your instance, and select start
	-  The Status icon will change from a white square to a green tick when startup is finished, this may take a few moments

-  **Visual Studio Code Setup**

	-  Download Visual Studio Code from https://code.visualstudio.com/download and follow the installation instructions
	-  Open Visual Studio Code
	-  Click in View:Extensions
	-  In the search bar, search for and install the following Extensions:
		-  Remote Development by Microsoft
		-  Remote -- SSH by Microsoft
		-  Python by Microsoft
		-  DJango by Bapiste Darthenay
		-  Markdown All In One by Yu Zhang
		-  Github Markdown Preview by Matt Bierner

-  **Using SSH**

	-  Ensure your computer has **ssh** installed
	-  To do this, you can run the command `ssh` in your computers native command terminal
	-  Command Prompt or Powershell for Windows
	-  Terminal for Linux
	-  Terminal for MacBook
	-  If the command doesn't return an error then you have **ssh** installed and can move on
	-  If it returns an error, install **ssh** on your machine, it varies by machine and version so ensure you install for the proper machine and version that you have

  

## Connecting to your Google Cloud VM through Visual Studio Code

-  **Setting Up a SSH Keypair**

	-  You will need to do this for every unique computer you want to connect to the cloud. These keypairs will also work for multiple different instances, you do not have to create a new keypair for every VM instance you create.
	-  Open Windows Powershell or Linux Terminal or Macbook Terminal
	-  Run the command: ssh-keygen -t ed25519
	-  Click enter 3 times
	-  Run the command: cat .ssh/id_ed25519.pub
	-  Copy the entire output of the command above
	-  Open your Google Cloud VM Dashboard
	-  On the left side of the page, click the 3 line drop down and open the Compute Engine Tab
	-  Scroll down until you see the metadata tab and open it
	-  Click on the SSH keys tab
	-  Click "Add SSH Key"
	-  Paste the output of the command that you ran earlier and compied, and save

-  **Connecting in Visual Studio Code**

	-  Open the command palette
	-  This can be done by click the bar at the top of Visual Studio Code and clicking Run Command
	-  Run Command will display a keybind you can use in the future to open it quicker
	-  Enter "Remote-SSH: Connect To Host" and click enter
	-  Enter your username, which can be found next to the key you pasted into the Google Cloud VM ssh key, for example `sread`
	-  This username is frequently the username of the computer account you are on
	-  Next to your username, add an @ and then the external IP address of your Google Cloud VM
	-  For example `sread@123.456.78.901`
	-  Click enter
	-  It is important to note that if you’re working across multiple computers, you must use the name of each machine, so if machine 1 is john, and machine 2 is johndoe you must use the respective names, and that you have setup a SSH keypair for each computer individually
	-  From here, a new Visual Studio Code window should appear. Select Linux in the drop down menu for the cloud software type
	-  You may need to enter “yes” or “continue” into the console to accept the new SSH footprint, if prompted
	
-	**Using the Visual Studio Code Editor**
	-  In the top left of Visual Studio Code, Press File
	-  Click "Open Folder"
	-  Navigate to the folder you want to open and click "Open Folder"
	-  In the explorer in the left you should now be able to access the files you want to work with

  

## Setting Up Your Google Cloud VM

-  **Creating a Shared Workgroup**

	-  Open your terminal in Visual Studio Code while connected to your virtual machine and run the following commands
	-  sudo mkdir /home/shared_workspace
	- sudo groupadd sharedgroup
	- sudo usermod -aG sharedgroup `name`
		- Name is replaced with the name of the users you want to be able to log into this. Repeat the command for every user (if you dont have multiple computers or want to share, then just do your current user)
	-	sudo chown -R root:sharedgroup /home/shared_workspace
	-	sudo chmod -R 2770 /home/shared_workspace
	-	sudo chmod g+s /home/shared_workspace
	-	Restart your Google Cloud VM Session to update user permissions
