# Development using  \
Google Cloud Platform \
And \
Visual Studio Code


# Table of Contents


# Setting up in the Google Cloud


## Creating Your Project



1. Claim your Education Credits as in the email you received.

    You will need to use your smcm.edu account for all your interactions with the Google Cloud Platform.

2. Goto [https://console.cloud.google.com](https://console.cloud.google.com) .
3. Tick the box to accept the Terms of Service.
4. Click Agree and Continue.
5. Click Select a Project.
6. Click New Project (in the top right corner.
7. In Project Name type your name and -00 (as in simon-read-00).
8. Your Organization and Location should be smcm.edu.
9. Click on the button that says Create
10. In the Notifications panel (to the right) under your project name, click Select Project.
11. Select the three bars in the top left of the window.
12. Select Cloud Overview
13. Select Dashboard


## Creating Your Server



1. From the Dashboard, under Resources click Compute Engine.
2. Possibly click on enable
3. In the new panel at the top, click on Create Instance.
4. Click on Enable
5. In name, put your name then -instance-00 (as in simon-read-instance-00)
6. Select Region as us-central-1 (Iowa) (probably the default).
7. Select Any for Zone (probably the default).
8. Ensure General purpose is selected.
9. Ensure E2 is selected.
10. In the left panel, select OS and Storage
11. Select Change.
12. Under Operating System select “Ubuntu”
13. Ensure the Version is Ubuntu 20.04 LTS.
14. Click Select
15. Click on Networking in the left panel
16. Under the Firewall heading check the boxes “Allow HTTP Traffic” and “Allow HTTPS Traffic”
17. Scroll down click on default in Network Interfaces.
18. Click the dropdown to expand “Default” under “Network Interfaces”
19. Ensure under External IPv4 Address “Ephemeral” is selected. (probably default)
20. Under Network Service Tier select Standard
21. Click Create at the bottom of the window


## Stopping Your Instance

Remember to Stop your instance every time you have finished working with it, or it will continue to charge against your Educational Credits and you will run out!



1. In the Compute Engine – VM Instances window
2. Select the three dots for your instance (you may need to scroll the main screen to see all the options under this menu).
3. Select Stop
4. The Status icon will change from a tick mark in a green circle to a white square in a grey circle.


## Restarting Your Instance



1. In the Compute Engine – VM Instances window
2. Select the three dots for your instance
3. Select Start
4. In the modal window that comes up click Start
5. The Status icon will change from a white square in a grey circle to a tick mark in a green circle.


# Setting Up Visual Studio Code


## Installing Visual Studio Code



1. Download Visual Studio Code from [https://code.visualstudio.com/download](https://code.visualstudio.com/download) and follow the installation instructions.


### Installing Visual Studio Code Extensions



1. Open Visual Studio Code
2. Click on View:Extensions
3. In the Search Bar, search for the following extensions and click install for each one:
1. Remote Development (by Microsoft)
2. Remote – SSH (by Microsoft)
3. Python (The Microsoft Developed Extension)
4. Django (by Baptiste Darthenay)
5. MarkDown All In One (by Yu Zhang)
6. GitHub Markdown Preview (by Matt Bierner)


## Getting SSH for Windows


### Installing PowerShell on Windows

PowerShell should already be installed on your computer, if it is not then follow the instructions at [https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5)


### Installing the OpenSSH client on Windows

The OpenSSH client should have been installed when you installed the Remote Development plug-in for Visual Studio Code.  If that is not the case then follow the instructions at [https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-server-2025](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-server-2025)


### Testing your OpenSSH installation



1. Search for and open the PowerShell application
2. Type ssh &lt;username>@login.cs.smcm.edu to log in to the CS server as you did in Computer Architecture and/or Programming Languages
3. You should be asked if a key is okay, accept it.
4. Check that you are at the server by typing hostname.  You should get the response prometheus.


### Cygwin Warning

You may have Cygwin (a Unix emulation suite) installed and this might be what’s used by Remote – SSH later.  If you think this is the case, consult an expert but you might try the following:



1. Locate the cygwin directory (usually C:\cygwin).
2. Copy your ed25519 key from C:\Users<username>/.ssh
3. Paste it into Cygwin’s .ssh directory
4. Start bash.exe in Cygwin’s bin directory
5. Type the command chmod 400 .ssh/ed25519


## Getting SSH for macOS

SSH is installed by default in macOS.  All you need to do is open the Terminal application to get a Unix Command line.


## Getting SSH for Linux

Most Linux distributions install the SSH client by default (but not the server, which you will not need).  If you find that your distribution has not installed the client, then use Google to find instructions specific to your distribution.

All you need to do is to open a Terminal and type your commands there.


## To Find the External IP Address of your VM Instance



1. Make sure your instance is running.
2. Scroll the VM instances window to the left (or is it right) until you see the External IP box.
3. The dotted quad in that box is your external IP.

 \
**Connecting to your Google Cloud VM through Visual Studio Code**



1. <span style="text-decoration:underline;">Setting up a SSH Keypair. You will need to do this for every unique computer you want to connect to the cloud. These keypairs will also work for multiple different instances, you do not have to create a new keypair for every VM instance you create.</span>
    1. Open Windows Powershell or Linux Terminal
        1. Run the command ssh-keygen -t ed25519
            1. Click enter 3 times
        2. Run the command cat .ssh/id_ed25519.pub
        3. Copy the output of the above command
    2. Navigate to your Google Cloud VM Dashboard
    3. On the left side of the page, click the 3 line dropdown menu and navigate to the Compute Engine tab. 
    4. On the left side, scroll down until you see the metadata tab, click this to open it.
    5. Click on the SSH keys tab.
    6. Click on “Add SSH Key”
    7. Paste in the output of the command we ran earlier that you copied, and save.
2. <span style="text-decoration:underline;">Connecting in Visual Studio Code</span>
    8. Open the command palette by pressing F1 (Windows) or pressing CTRL+SHIFT+P (ChromeBook) or CMD+SHIFT+P (MacBook)
    9. In the popup, enter “Remote-SSH: Connect to Host” and press enter
    10. In the prompt to enter the host, and the username next to the key you put into the google cloud VM ssh key, for example johndoe
    11. Then, next to your username and @, add the external IP address to your google cloud vm
        4. It will look like this johndoe@123.456.78.901
            2. Hit enter
        5. It is important to note that if you’re working across multiple computers, you must use the name of each machine, so if machine 1 is john, and machine 2 is johndoe you must use the respective names
    12. From here, a new Visual Studio Code window should appear. Select Linux in the drop down menu for the cloud software type
    13. You may need to enter “yes” or “continue” into the console to accept the new SSH footprint, if prompted
3. <span style="text-decoration:underline;">Using the Visual Studio Code Editor</span>
    14. Top left of VS, press File
    15. Click “Open Folder”
    16. Navigate to the folder you want to open, then click “Open Folder”
    17. In your explorer, you should now be able to access the files you want to work with!

**Setting up your Google Cloud VM**



1. <span style="text-decoration:underline;">Installing all the dependencies and apps your Virtual Machine will need</span>
    1. Enter the console for your Virtual Machine, this can be done in various ways
        1. Open a Windows Powershell and type the command “ssh johndoe@123.456.78.901” where in you replace johndoe@123.456.78.901 with your credentials and the ip address you want to connect to
        2. Connect to the virtual machine on Visual Studio and open terminal, which will automatically enter the VM
        3. On the google cloud console where you activate the VM, click on the ssh button. This will open a new window that is linked to the VM
2. <span style="text-decoration:underline;">Creating a shared workgroup (not necessary if only working from one computer, necessary if working from many)</span>
    2. Open terminal (CTRL+J on Windows and Chromebook, CMD+J on Macbook)
    3. sudo mkdir /home/shared_workspace
    4. sudo groupadd sharedgroup
    5. sudo usermod -aG sharedgroup name (repeat for however many users need access, where name is the name of the users youve connected from)
    6. sudo chown -R root:sharedgroup /home/shared_workspace
    7. sudo chmod -R 2770 /home/shared_workspace
    8. sudo chmod g+s /home/shared_workspace
    9. This creates a folder in the home directory called shared_workspace where all users added in step C are able to access and modify files
    10. Restart your Google Cloud VM Session to update user permissions
3. <span style="text-decoration:underline;">Installing everything necessary</span>
    11. Start installing, run all of the following commands:
        4. If you’ve made a shared workspace
            1. cd /home/shared_workspace
        5. sudo apt update 
        6. sudo apt install python3
        7. sudo apt install git
        8. git config --global user.name "****" (between “” needs to be the github username”
        9. git config --global user.email "****" (between the “” needs to be the github email address”
        10. git init
        11. git clone [https://github.com/swbn1/ChesapeakeCommunityConnect-FA24](https://github.com/swbn1/ChesapeakeCommunityConnect-FA24)
        12. git clone [https://github.com/swbn1/CDSpecCollab_COSC4012020-FA24](https://github.com/swbn1/CDSpecCollab_COSC4012020-FA24)
        13. sudo apt-get install python3-pip
            2. Press y and then enter when prompted
        14. sudo apt install python3-django
            3. Press y and then enter when prompted
        15. sudo apt install libapache2-mod-wsgi-py3
            4. Press y and then enter when prompted
        16. sudo apt install mariadb-server
            5. Press y and then enter when prompted
        17. sudo mysql_secure_installation
            6. Return for no current password
            7. Select Y to set the new root password to software_startup_simulator
            8. Select Y to remove anonymous users
            9. Select Y to disallow remote root login
            10. Select Y to remove test database
            11. Select Y to reload data table privileges
        18. sudo apt install postgresql
            12. Press y and then enter when prompted
        19. sudo apt install python3.8-venv

**Setting up CDSpec**



1. <span style="text-decoration:underline;">Installing CDSpec Requirements</span>
    1. cd shared_workspace/CDSpecCollab_COSC4012020-FA24/Deployed\ Version/cd_spec_viewer_web/
    2. pip install -r requirements.txt
    3. curl -sS https://bootstrap.pypa.io/get-pip.py | python3
    4. pip install whitenoise
2. <span style="text-decoration:underline;">Configuring Postgres</span>
    5. sudo systemctl status postgresql
    6. Press CTRL+C to go back to cmd line prompt
    7. sudo -i -u postgres
        1. psql
            1. ALTER USER postgres PASSWORD 'PASS';
            2. \q
        2. exit
    8. sudo nano /etc/postgresql/*/main/pg_hba.conf
        3. Navigate to:
            3. # Database administrative login by Unix domain socket
            4. local   all             postgres                                peer
        4. Change “peer” to “md5” (without quotations)
            5. Ctrl + X
            6. Y
            7. Enter
            8. sudo systemctl restart postgresql
3. <span style="text-decoration:underline;">Starting CDSpec Web</span>
    9. cd shared_workspace/CDSpecCollab_COSC4012020-FA24/Deployed\ Version/cd_spec_viewer_web/
    10. python3 manage.py makemigrations
    11. python3 manage.py migrate
    12. python3 manage.py runserver
        5. If you’re using Visual Studio Code, this should give you a prompt that says “Your application running on port 8000 is available”. Click on “Open in Browser”
        6. Alternatively, enter “[http://127.0.0.1:8000/](http://127.0.0.1:8000/)” in your browser
