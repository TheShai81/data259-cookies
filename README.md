# data259-cookies
Repository of all information, data, and work pertaining to the Spring 2025 final project for DATA 25900 at UChicago


## Members
- Shailesh Bolduc, shaileshbolduc@uchicago.edu
- Kevin Solano, ksolano@uchicago.edu
- Erik Rindner, erikrindner@uchicago.edu

## How to Clone and Use This Repository

*This is a guide for cloning via SSH authentication. You must have a valid SSH key with github to proceed.*

1) Go to the Code tab above the repo contents and select SSH. Copy the link that appears.
2) Go to your computer's terminal/command prompt and navigate to the directory that you want to put the repo.
3) Type `git clone ssh-link` and enter.
4) If you `cd` into the local repo and then type `git remote -v`, you should see 2 lines appear. One ending in "fetch" and the other ending in "push".

For this repository, we will add and merge files via **branches**.
Do NOT push to main unless the team has agreed on it. We want to watch out for merge conflicts.
The following are instructions on how to add a file called "sample.txt" to the repo.

1) Create or "checkout" a new branch. I recommend naming it your name or something meaningful.

    `git checkout -b branch-name`

2) Type `git branch` to ensure that you are working in your branch and NOT main.
3) Add your file. For example: `touch sample.txt` which just creates the file.
4) Add and commit your changes in your branch with an informative commit message.

    `git add sample.txt`
   
    `git commit -m "Commit message"`

6) Push your changes to the repository on GitHub. It is important to specify your working branch.

    `git push origin branch-name`

7) Go to GitHub and open a pull request by navigating to the Pull Request tab and selecting your branch.
8) Ensure that there are no merge conflicts. If you're unsure about merging to main immediately, consult the team.

