# Scripts Folder

---

All scripts and/or notebooks should be added into this folder. In general, scripts 
are better for workflows while notebooks are better for exploration. Try to 
develop notebooks into scripts once a workflow for analysis has been established. 
For all scripts and notebooks, title them meaningfully and include a docstring 
or markdown cell at the top explaining what the file is for and how it can be used,
 if necessary.

### Basic Formatting Etiquette

- Run "ruff format" in your working directory before staging scripts for commit 
to maintain a clean format following general Python formatting principles. "ruff check" 
is also a good one to see where your formatting is off.
- Ensure your scripts/notebooks are cleaned and well-documented. Included regular 
comments, markdown cells, and docstrings in your code so that teammates can easily 
understand it.
- Notebooks should not be longer than 20 cells. Typically, organizations enforce 
a 10-cell limit, but we won't be so anal.
- Do not hardcode paths or important constants. All should be relative/stored.
- Function and file names are descriptive and non-arbitrary (i.e. not "foo" and "bar")

