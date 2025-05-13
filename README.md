# data259-cookies
Repository of all information, data, and work pertaining to the Spring 2025 final project for DATA 25900 at UChicago


## Members
- Shailesh Bolduc, shaileshbolduc@uchicago.edu
- Kevin Solano, ksolano@uchicago.edu
- Erik Rindner, erikrindner@uchicago.edu

## Code Dependencies

All code written in this repository was written in Python. You must have Python Version 3.9.13 or greater.
Python dependencies required to reproduce the code in our analyses can be found in `requirements.txt`. Simply run the following in your working directory.

```zsh
pip install -r requirements.txt
```

## Reproducing Results or Using Code

### Dataset
The dataset that was used for this analysis is at `data/cookie_survey_responses.csv`. 
However, if you want to run a new dataset then you can just put it in the data folder. The path to the data is hardcoded into our analyses, so just make sure to change the path to your file in any scripts. An important thing to note, though, is that in order to run our cleaning or analysis scripts without any changes (besides file name), the structure of the dataset must be the same. The data were downloaded as a CSV from Google Forms—where the survey was published.

### Running Scripts
All code is in the `scripts` folder. To obtain visualizations of the results for specific questions and patterns we chose to visualize, simply run `scripts/visualization_paired.py`. You may also see the `scripts/visualization_script.py` file which can visualize some other general visualizations, but may need to be tweaked to better suit your dataset. The visuals in our final deliverable were produced from `scripts/visualization_paired.py`, though.

To replicate our statistical tests, you can go to `scripts/stat_tests.ipynb` and simply run all cells. If you'd like to run your own statistical tests, see `scripts/statistical_tests.py` for some pre-written functions for 2-proportion z-tests, 2-sample t-tests, and calculating p-values from z- and t-values. No statistical tests beyond these are written in this file.

## How to Clone and Use This Repository

*This is a guide for cloning via SSH authentication. You must have a valid SSH key with Github to proceed.*

1) Go to the Code tab above the repo contents and select SSH. Copy the link that appears.
2) Go to your computer's terminal/command prompt and navigate to the directory that you want to put the repo.
3) Type `git clone ssh-link` and enter.
4) If you `cd` into the local repo and then type `git remote -v`, you should see 2 lines appear. One ending in "fetch" and the other ending in "push".

For this repository, we will add and merge files via **branches**.
Do NOT push to main unless the team has agreed on it. We want to watch out for merge conflicts.
The following are instructions on how to add a file called "sample.txt" to the repo.

1) Create or "checkout" a new branch. I recommend naming it your name or something meaningful.

    ```zsh
    git checkout -b branch-name
    ```

2) Type `git branch` to ensure that you are working in your branch and NOT main.
3) Add your file. For example: `touch sample.txt` which just creates the file.
4) Add and commit your changes in your branch with an informative commit message.

    ```zsh
    git add sample.txt
    git commit -m "Commit message"
    ```

6) Push your changes to the repository on GitHub. It is important to specify your working branch.

    ```zsh
    git push origin branch-name
    ```

7) Go to GitHub and open a pull request by navigating to the Pull Request tab and selecting your branch.
8) Ensure that there are no merge conflicts. If you're unsure about merging to main immediately, consult the team.

