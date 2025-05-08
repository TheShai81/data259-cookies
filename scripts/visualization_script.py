'''This file contains script to generate visualizations after stats testing.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set style
sns.set_theme(style="whitegrid", context="paper", palette="muted")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['legend.fontsize'] = 10

#load dataset
df = pd.read_csv('data.csv')

#basic info
print("DataFrame shape:", df.shape)
print("Column types:\n", df.dtypes)
print("Missing values:\n", df.isnull().sum())

#identify numeric and categorical columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include='object').columns

#1. Histogram of numeric columns
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col].dropna(), bins= 30, kde=True, color='steelblue')
    plt.title(f'Distribution of {col}', fontsize=14)
    plt.xlabel(col, fontsize=12)
    plt.tight_layout()
    plt.savefig(f'hist_{col}.png', dpi = 300, bbox_inches='tight')
    plt.close()

#2. Boxplots: for mean comparison (t-tests)
for cat_col in categorical_cols:
    unique_vals = df[cat_col].nunique()
    if 2 <= unique_vals<= 6: #to avoid too many categories
        for num_col in numeric_cols:
            plt.figure()
            sns.boxplot(x=cat_col, y=num_col, data=df)
            plt.title(f'Boxplot of {num_col} by {cat_col}')
            plt.xticks(rotation=45, ha='right')
            plt.xlabel(cat_col)
            plt.ylabel(num_col)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f"Boxplot_{num_col}_by_{cat_col}.png", dpi=300, bbox_inches='tight')
            plt.close()
       
#3. Count plots: for proportion comparison (z-tests)
for cat_col in categorical_cols:
    plt.figure()
    sns.countplot(x=cat_col, data=df)
    plt.title(f'Count plot of {cat_col}')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel(cat_col)
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Group', loc='upper right')
    plt.tight_layout()
    plt.savefig(f'countplot_{cat_col}.png', dpi=300, bbox_inches='tight')
    plt.close()

#4. Correlation heatmap (numerical only)
if len(numeric_cols) > 1:
    corr = df[numeric_cols].corr()
    plt.figure()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

#5. Pairplot
if 2 <= len(numeric_cols) <= 5:
    sns.pairplot(df[numeric_cols].dropna(), plot_kws={'alpha':0.6, 's':30})
    plt.title('Pairplot of Numerical Columns')
    plt.savefig('pairplot.png', dpi=300, bbox_inches='tight')
    plt.close()

print("All visualizations saved as PNGs.")