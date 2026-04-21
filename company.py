import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Company_dataset.csv")

#----------------headquarters name of the company----------------------
print("Columns:", df.columns)

if 'hq' in df.columns:
    hq_values = df['hq'].head(10)
    
    print("\nHeadquarters of 10 companies:")
    for i, hq in enumerate(hq_values, start=1):
        print(f"{i}. {hq}")
else:
    print("Column 'hq' not found in dataset.")


#barchart
bar_top10 = df.sort_values(by='ratings', ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.bar(bar_top10['name'], bar_top10['ratings'])
plt.xlabel("Company")
plt.ylabel("Ratings")
plt.title("Top 10 Companies by Ratings")
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()


#-------------funnel chart----------------

# --- Clean review_count column ---
df['review_count'] = df['review_count'].astype(str)

# Extract numeric values (handles '1,000+', '500 reviews', etc.)
df['review_count'] = df['review_count'].str.extract('(\d+)')

# Convert to numeric
df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce')

# Drop invalid values
df = df.dropna(subset=['review_count'])

# --- Get top 10 companies by reviews ---
top10 = df.sort_values(by='review_count', ascending=False).head(10)

# Reverse for funnel (largest on top visually)
top10 = top10[::-1]

# --- Create centered funnel effect ---
values = top10['review_count']
labels = top10['name']

max_val = values.max()
left = (max_val - values) / 2

plt.figure(figsize=(12, 6))
bars = plt.barh(labels, values, left=left)

# Add value labels
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_y() + bar.get_height()/2,
             f'{int(val)}',
             ha='center', va='center')

# Labels and title
plt.xlabel("Review Count")
plt.ylabel("Company")
plt.title("Funnel Chart - Top 10 Companies by Review Count")

plt.tight_layout()
plt.show()



# ------------line chart----------------
# --- Clean employees column properly ---
df['employees'] = df['employees'].astype(str)

# Remove commas, plus signs, spaces
df['employees'] = df['employees'].str.replace(',', '', regex=False)
df['employees'] = df['employees'].str.replace('+', '', regex=False)

# Extract only numbers
df['employees'] = df['employees'].str.extract('(\d+)')

# Convert to numeric
df['employees'] = pd.to_numeric(df['employees'], errors='coerce')

# Drop invalid rows
df = df.dropna(subset=['employees'])

# --- Get top 10 companies ---
top10 = df.sort_values(by='employees', ascending=False).head(10)

# IMPORTANT: sort again for line flow (left → right decreasing)
top10 = top10.sort_values(by='employees', ascending=False)

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.plot(top10['name'], top10['employees'], marker='o')

# Add value labels
for i in range(len(top10)):
    plt.text(top10['name'].iloc[i],
             top10['employees'].iloc[i],
             int(top10['employees'].iloc[i]),
             ha='center', va='bottom')

# Labels
plt.xlabel("Company")
plt.ylabel("Employees")
plt.title("Top 10 Companies by Employee Count")

# Prevent overlap
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()


# -------------Pie chart---------------
# --- Clean 'years' column ---
df['years'] = df['years'].astype(str)

# Extract numeric values
df['years'] = df['years'].str.extract('(\d+)')

# Convert to numeric
df['years'] = pd.to_numeric(df['years'], errors='coerce')

# Drop invalid values
df = df.dropna(subset=['years'])

# --- Get top 5 companies by years ---
top5 = df.sort_values(by='years', ascending=False).head(5)

# --- Plot pie chart ---
plt.figure(figsize=(8, 8))
plt.pie(top5['years'],
        labels=top5['name'],
        autopct='%1.1f%%',
        startangle=140)

plt.title("Top 5 Companies by Years")

plt.tight_layout()
plt.show()