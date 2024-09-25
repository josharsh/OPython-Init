The following is not necessary for the completion of this course, however could be benficial if you plan to continue working with python after completing this course.

## Downloading and Installing IDE

1. Installing PyCharm on Windows
   *   Step 1: Download PyCharm
       *   Go to the official PyCharm website: JetBrains PyCharm.
       *   Choose Windows as the platform.
       *   You’ll see two versions: Professional (paid) and Community (free, open-source). Select the one you prefer and click Download.
         
   *   Step 2: Run the Installer
       *   Once the download is complete, locate the .exe file in your downloads folder and double-click it to run the installer.
         
   *   Step 3: Begin the Installation Process
       *   A setup wizard will appear. Click Next to start the installation.
       *   Choose the installation path where you want PyCharm to be installed, or leave the default location and click Next.
         
   *   Step 4: Installation Options
       *   You'll see a list of installation options:
           *   Create Desktop Shortcut: Choose if you want a desktop icon for PyCharm.
           *   Update PATH variable: This allows you to launch PyCharm from the command line.
           *   .py file association: Choose this option if you want PyCharm to open .py files by default.
           *   Install JRE x86: Choose this if you do not have Java Runtime Environment (JRE) installed.
             
   *   Step 5: Install PyCharm
       *   Click Install to begin the installation process.
       *   Wait for the installation to complete.
       
   *   Step 6: Finish Installation
       *   Once the installation is complete, you’ll get an option to Run PyCharm. If you want to start using it right away, check this box and click Finish.
       
   *   Step 7: Configure PyCharm
       *   When PyCharm launches for the first time, it will prompt you to import settings from a previous version or start fresh. Choose as per your requirement and click OK.
       *   You can also choose a UI theme (Light/Dark) during the first-time setup.
       
2. Installing PyCharm on macOS
   *   Step 1: Download PyCharm
       *   Go to the official PyCharm website: JetBrains PyCharm.
       *   Choose macOS as the platform and download the version (Professional or Community) you need.
         
   *   Step 2: Install PyCharm
       *   Once the download completes, locate the .dmg file in your Downloads folder and double-click it.
       *   A window will pop up, prompting you to drag the PyCharm icon into the Applications folder.
       *   Drag and drop the PyCharm icon into the Applications folder.
         
   *   Step 3: Launch PyCharm
       *   Open your Applications folder and double-click PyCharm to launch it.
       *   If you see a warning about an unverified developer, click Open (you may need to go to System Preferences > Security & Privacy to allow this).
         
   *   Step 4: Initial Setup
       *   Once PyCharm is launched, it will ask if you want to import settings or start with default settings. Choose your preferred option.
       *   You will also get to choose a Light or Dark theme during the setup.
         
3. Installing PyCharm on Linux
   
   *   Step 1: Download PyCharm
       *   Visit the official PyCharm website: JetBrains PyCharm.
       *   Choose Linux as the platform and download the version (Professional or Community) you need.
       *   You will download a .tar.gz file.
         
   *   Step 2: Extract the File
       *   Open the terminal and navigate to the directory where the downloaded file is located:
           *   cd ~/Downloads
       *   Extract the .tar.gz file using the following command:
           *   tar -xzf pycharm-community-*.tar.gz
             
   *   Step 3: Move PyCharm to the Desired Directory
       *   After extraction, move the PyCharm folder to a suitable directory (like /opt):
           *   sudo mv pycharm-community-* /opt/pycharm
             
   *   Step 4: Run PyCharm
       *   To start PyCharm, use the following commands:
           *   cd /opt/pycharm/bin
           *   ./pycharm.sh
   
   *   Step 5: Create a Desktop Entry (Optional)
       *   To easily launch PyCharm from the desktop or application launcher, you can create a desktop entry.
       *   In PyCharm, go to Tools > Create Desktop Entry. This will automatically create a launcher in your application menu.
         
   *   Step 6: Initial Setup
       *   When PyCharm first starts, it will ask if you want to import settings from a previous version or use default settings.
       *   You'll also be prompted to choose a UI theme.
         
4. Configuring Python Interpreter in PyCharm

   *   Regardless of the platform you're using, once PyCharm is installed, you need to configure the Python interpreter.

   *   Step 1: Open or Create a New Project
       *   Click New Project or Open to create/open a Python project.

   *   Step 2: Configure Python Interpreter
       *   Go to File > Settings (on Windows/Linux) or PyCharm > Preferences (on macOS).
       *   Navigate to Project: [project_name] > Python Interpreter.
       *   Click the gear icon and choose Add.
       *   Select your desired Python interpreter from the list or browse to the location where your Python interpreter is installed (e.g., a virtual environment, Anaconda, or system Python).
       *   Click OK to apply the settings.
 
   *   Step 3: Verify Installation
       *   After selecting the interpreter, you can create a Python file in your project, write a simple script like print("Hello, World!"), and run it to verify that the interpreter is set up correctly.
         
## GitHub Basics

1. Forking a Repository on GitHub
   *   Forking creates a personal copy of someone else's repository on your GitHub account. Here are the steps:
   *   Step 1: Log in to GitHub
       *   Go to GitHub and log in to your account. If you don't have one, create an account first.
   *   Step 2: Find the Repository to Fork
       *   Navigate to the repository you want to fork by searching for it or using a direct link.
   *   Step 3: Fork the Repository
       *   At the top-right corner of the repository page, click the Fork button. This will create a copy of the repository under your GitHub account.
       *   Once you've forked the repository, you’ll have a personal copy of it in your account. Now, let’s move on to cloning it.

2. Cloning the Forked Repository
   *   Cloning a repository means downloading it to your local machine so you can work on it using your IDE (PyCharm in this case).

   *   Step 1: Get the Clone URL
       *   After forking, go to your GitHub profile and find the forked repository.
       *   Click on the Code button, which will show a dropdown with several clone options (HTTPS, SSH, or GitHub CLI). Copy the URL (choose HTTPS for simplicity unless you are using SSH).
   *   Step 2: Open PyCharm
       *   Launch PyCharm.
   *   Step 3: Start a New Project from Version Control
       *   On the PyCharm start screen, select Get from VCS (Version Control System).
       *   If PyCharm is already open, go to File > New > Project from Version Control.
   *   Step 4: Paste the Repository URL
       *   In the window that appears, paste the repository URL you copied from GitHub (e.g., https://github.com/your-username/repo-name.git).
   *   Step 5: Choose a Directory to Clone Into
       *   Select the directory on your local machine where you want the repository to be cloned. PyCharm will create a project folder for it.
       *   Click Clone.
   *   Step 6: Wait for the Repository to Download
       *   PyCharm will clone the repository, download its contents, and set up the project.
3. Configuring and Managing Your Project in PyCharm
   *   Once the repository is cloned into PyCharm, you'll need to configure the environment and manage your workflow.

   *   Step 1: Configure the Python Interpreter
       *   Go to File > Settings > Project: [project_name] > Python Interpreter.
       *   If the project requires a specific Python version or environment, you can set it here.
       *   You can add a virtual environment or use an existing interpreter like Anaconda.
   *   Step 2: Pull Latest Changes (Optional)
       *   If the original repository (the upstream repo) is being updated frequently, you may want to keep your fork updated.
       *   In PyCharm, go to VCS > Git > Pull to pull the latest changes from your fork (or the original repository if you've added it as a remote).
   *   Step 3: Start Coding!
       *   At this point, the repository is ready in your IDE. You can now open files, edit code, and write new features.
4. Making Changes, Committing, and Pushing (Optional)
   *   Once you make changes to the repository, you’ll want to commit and push them to your fork on GitHub.

   *   Step 1: Make Your Code Changes
       *   Open any file, make the necessary changes, and save them.
   *   Step 2: Commit the Changes
       *   Go to VCS > Commit (or use the keyboard shortcut Ctrl+K on Windows/Linux or Cmd+K on macOS).
       *   In the commit dialog box, you can:
           *   Write a commit message describing the changes.
           *   Select the files you want to include in the commit (if you edited multiple files).
           *   Optionally run a code analysis or reformat the code before committing.
       *   Once you’ve filled out the commit message and selected files, click Commit.
   *   Step 3: Push Your Changes to GitHub
       *   To push the committed changes to your fork on GitHub, go to VCS > Git > Push (or use the shortcut Ctrl+Shift+K on Windows/Linux or Cmd+Shift+K on macOS).
       *   PyCharm will push the changes to the remote repository.
       
