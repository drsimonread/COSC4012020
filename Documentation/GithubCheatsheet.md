
## Branch Structure

  

  

- **Overview**

	- Branches are separate lines of development within the same repository.
	- They allow multiple developers to work on features or fixes simultaneously without interfering with each other.

- **Main Branch**

	- Often named `main`, `production`, or `deployed`.
	- Represents the stable, deployed version of the project.
	- Do not push or pull directly without permission.
	- Serves as the final, working version of the code used in production.

- **Integration Branch**
	- Serves as the shared development branch for all contributors.
	- Pull from this branch when beginning your own development.
	- Acts as a middle ground between personal branches and `main`.
	- Everyone’s completed and reviewed work is typically merged here before `main`.

- **Personal Development Branch (`your-branch-name`)**
	- Created from `integration` (or another relevant base).
	- Used for developing or fixing a specific issue assigned to you.
	- Do not modify other people’s branches without permission.
	- Only push to your own branch.
	- When work is complete, it can be reviewed and merged into `integration`.

## Issues (Task Management)

  

  

- **Purpose**

	- Issues track bugs, feature requests, or tasks in the project.
	- Each issue represents a specific task to be solved.

- **Claiming Issues**
	
	- Assign the issue to yourself (or request assignment).
	- Prevents multiple people from working on the same issue.

- **Creating a Branch for an Issue**

	- In the GitHub issue “Development” section, create a branch.
	- Set the source branch (usually `integration`).
	- Locally checkout your branch with:
	git checkout -b your-branch-name origin/your-branch-name
	- This creates a local branch that tracks the remote branch.

- **Committing and Pushing Changes**

	- git add .
		- Stages modified files for commit
	- git commit -m "Your descriptive commit message"
		- Records your changes locally with message about commit
	- git push -u `origin your-branch-name`
		- Uploads your changes to GitHub

  

  

- **Useful GitHub Commands**

	- git clone `repository-link`
		- Clones a GitHub repository to your machine
	- git branch -r
		- Lists all remote branches on GitHub
	- git branch
		- Lists all branches on your machine, the branch you are on is marked with an asterisk *
	- git checkout -b `your-branch-name`
		- Creates a new local branch and switches to it
	- git fetch origin
		- Fetches remote cupdates without changing local files
	- git pull origin `branchname`
		- Fetches and merges updates from a remote branch to your current branch
	- git checkout -b `branchname origin/branchname`
		- Creates a local branch that tracks an existing remote branch
		- Useful for viewing or referencing another developers work safely
