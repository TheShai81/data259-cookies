import numpy as np
import matplotlib.pyplot as plt
import random
from preprocess_data import preprocess_survey_data as clean

print("Loading data and cleaning it.")
DATASET_PATH = "../data/cookie_survey_responses.csv"  # change if needed
df, colmap, encmap = clean(DATASET_PATH)

# ================= Respondent Demographics ====================

print("Starting Respondent Demographics.")

# 1x3 grid of plots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Set universal font size
plt.rcParams.update({'font.size': 14})

# ages histogram
axes[0].hist(df["Question 1"], color="lightskyblue", edgecolor='black')
axes[0].set_title("Distribution of Respondents' Ages", fontsize=14)
axes[0].set_xlabel("Age", fontsize=12)
axes[0].set_ylabel("Count", fontsize=12)

# browsers pie chart
counts = df['Question 3'].value_counts()
labels = counts.index
sizes = counts.values
colors = [plt.cm.Paired(i / len(sizes)) for i in range(len(sizes))]
axes[1].pie(sizes, labels=labels, colors=colors, textprops={'fontsize': 10},
            autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
axes[1].set_title("Main Browsers that Respondents Use", fontsize=14)

# technological domain pie chart
colors = [plt.cm.Paired(i / 2) for i in range(2)]
axes[2].pie([8/22, 14/22], labels=["Technological Domain", "Non-technological Domain"],
            colors=colors, textprops={'fontsize': 10}, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
axes[2].set_title("Proportion in Technological Domains", fontsize=14)

plt.tight_layout()
plt.savefig("charts/demographics.png", dpi=300)

# ================= Insights by Respondent Browser ====================

print("Starting Insights by Respondent Browser.")

# How easy is it to reject cookies in each browser?
browser_ease = df.groupby("Question 3")["Question 13"].mean().sort_values()

# Plot
fig, ax = plt.subplots(figsize=(10, 2))
ax.scatter(browser_ease.values, [1]*len(browser_ease), color="mediumseagreen", s=100)

# Add labels next to each dot
for i, (browser, val) in enumerate(browser_ease.items()):
    ax.text(val, 1.05, browser, ha='center', va='bottom', fontsize=12)

# Styling
ax.set_yticks([])
ax.set_xlabel("Average Ease of Cookie Rejection (1–5)")
ax.set_title("Average Ease of Cookie Rejection by Browser", fontsize=14)
ax.set_xlim(1, 5)
ax.set_ylim(0.95, 1.1)
ax.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("charts/browser_ease_of_reject.png", dpi=300)

# Do people know how to stop sharing cookies with a website in their browser?

counts = df.groupby(['Question 3', 'Question 14']).size().unstack(fill_value=0)

# Sort browser order (optional)
counts = counts.sort_index()

# Setup
labels = counts.index.tolist()  # Browsers
response_types = ["No", "Yes", "Not sure"]
x = np.arange(len(labels))  # browser positions
width = 0.25  # width of each bar
colors = plt.cm.Paired(np.linspace(0, 1, len(response_types)))

# Plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, response in enumerate(response_types):
    ax.bar(x + i * width - width, counts[response], width, label=response, color=colors[i], edgecolor="black")

# Formatting
ax.set_xlabel("Main Browser", fontsize=12)
ax.set_ylabel("Number of Respondents", fontsize=12)
ax.set_title('Relationship Between Main Browser and\n"Do You Know How to Stop Sharing Cookies with a Website?"', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.legend(title="Response to Q14")
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("charts/browser_change_cookie_settings.png", dpi=300)

# Relationship between main browser and "Are you able to block all third-party cookies by default on your browser?"

q10_map = {
    0: "I don't know",
    1: "Yes, blocks",
    2: "Yes, doesn't block"
}
df['Q10_decoded'] = df['Question 10'].map(q10_map)

# Create grouped counts
counts = df.groupby(['Question 3', 'Q10_decoded']).size().unstack(fill_value=0)
counts = counts.sort_index()

# Setup
labels = counts.index.tolist()  # Browsers
response_types = ["I don't know", "Yes, blocks", "Yes, doesn't block"]
x = np.arange(len(labels))  # browser positions
width = 0.25
colors = plt.cm.Paired(np.linspace(0, 1, len(response_types)))

# Plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, response in enumerate(response_types):
    ax.bar(
        x + i * width - width,
        counts[response],
        width,
        label=response,
        color=colors[i],
        edgecolor="black"
    )

# Formatting
ax.set_xlabel("Main Browser", fontsize=12)
ax.set_ylabel("Number of Respondents", fontsize=12)
ax.set_title('Relationship Between Main Browser and\n"Ability to Block All Third-Party Cookies by Default"', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.legend(title="Response to Q10")
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("charts/broswer_block_third_party.png", dpi=300)

# ======================== General College Student Behavior ========================

print("Starting General College Student Behavior.")

# Do college students care about the data that cookies may collect?

df['Q8_decoded'] = df['Question 8'].map(encmap["Question 8"])

# Count the responses
counts = df['Q8_decoded'].value_counts()
labels = counts.index
sizes = counts.values
colors = [plt.cm.Paired(i / len(labels)) for i in range(len(labels))]

# Plot pie chart
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'black'}
)
ax.set_title("Concern About Third-Party Cookie Tracking", fontsize=14)

plt.tight_layout()
plt.savefig("charts/third_party_concern.png", dpi=300)

# What do college students generally do when presented with a cookie banner? (Accept, reject, etc)

df['Q11_decoded'] = df['Question 11'].map(encmap["Question 11"])

# Count the responses
counts = df['Q11_decoded'].value_counts()
labels = counts.index
sizes = counts.values

# Shuffle Paired colormap
base_colors = [plt.cm.Accent(i) for i in range(9)]
random.shuffle(base_colors)
colors = base_colors[:len(labels)]

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 11},
    wedgeprops={'edgecolor': 'black'}
)
ax.set_title("Students' Actions When Presented with Cookie Banner", fontsize=13)

plt.tight_layout()
plt.savefig("charts/action_at_cookie_prompt.png", dpi=300)

print("All figures saved as PNGs in \"charts\" folder.")