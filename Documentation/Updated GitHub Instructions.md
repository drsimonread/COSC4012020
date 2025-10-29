# GitHub Workflow & Branching Guide

This document outlines the standard workflow for contributing to the CDSPEC project. Please follow these steps to ensure a smooth and organized development process.

## Branching Strategy

A branch is a unique copy of the project. Changes made on a branch are isolated from other branches until they are intentionally merged. Our project follows a structured branching model:

##### `Prod` / `Main` / `Production`
*   This is the version of the project currently in use by customers. **You will never pull from or push to this branch directly.**

##### `Stable`
*   This is a stable version of the project that is more up-to-date than the current `Prod` branch. **You also will not pull from or push to this branch.**

##### `Integration`
*   This is the primary development branch. Students will **pull from** this branch to get the latest code and **push to** it via a Pull Request once a feature is complete. When starting a new issue, you will always create your new branch from `integration`. This is the 'living' project.

##### `Feature Branch` / User Stories
*   These are the individual branches where developers work on specific issues or features. **DO NOT TOUCH THESE BRANCHES WITHOUT PERMISSION FROM THE BRANCH DEVELOPER.**

---

## Workflow: Creating a Branch for an Issue

Follow these steps for every new issue you work on.


# 1. Setup Your Local Repository
```bash
git clone https://github.com/swbn1/CDSpecCollab_COSC4012020-FA24.git
cd CDSpecCollab_COSC4012020-FA24
```
# 2. Sync with the Integration Branch
```bash
git checkout main
git pull origin integration
```
# 3. Create a New Feature Branch
```bash
git checkout -b the-name-of-your-issue-YourName
```
# 4. Work and Commit Your Changes
```bash
git add .
git commit -m "Fixed this issue: [Short description of what was fixed]"
```
# 5. Push Your Branch to GitHub
```bash
git push -u origin the-name-of-your-issue-YourName
# For subsequent pushes to the same branch:
git push
```
IMPORTANT: Always double-check that you are on your own branch before pushing by running git branch.

# 6. Create a Pull Request (PR)
 After pushing your branch, you need to propose merging it into the integration branch.

1. Go to the main repository page on GitHub: CDSpec Repository

2. You should see a prompt to create a pull request for your recently pushed branch. Click the "Compare & pull request" button.

3. Ensure the base repository is set to integration and the head repository is your feature branch.

4. Fill in the title and details for the pull request. In the description, be sure to reference the issue number you are working on (e.g., Fixes #5). This automatically links the PR to the issue.

5.Click "Create pull request" and submit it for review.

# Useful Commands

Here is a quick reference for common Git commands.

#### git branch
*   Shows all branches on your local machine. The branch with an asterisk (*) next to it is the one you are currently on.

#### git checkout branchname
*   Switches you to the specified branch.

#### git status
*   Shows the current status of your branch, including modified files that are staged or unstaged.

#### git pull origin branchname
*   Downloads updates from the specified remote branch and merges them into your current local branch.
    *   Example: git pull origin integration pulls updates from the integration branch into your current branch.

#### git fetch origin
*   Downloads all information (including new branches) from the remote repository but does not merge it.

#### git branch -r
*   Lists all remote branches available on GitHub.

#### git checkout -b branchname origin/branchname
*   Creates a new local branch that tracks a specific remote branch.

# Etiquette and Best Practices

* Do not use other people's development branches unless you have been given explicit permission (e.g., for quality checks).

* Before creating a pull request, pull the latest changes from the integration branch into your feature branch to resolve any potential merge conflicts locally.

* After you've merged your feature into integration, you can safely delete your local and remote feature branch.

* Always use descriptive commit messages that explain what was changed and why.

* Keep your branches focused on a single issue or feature.
