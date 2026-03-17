import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")

#Barchart
plt.figure()
plt.bar(df['Event_Name'], df['Estimated_Deaths'])
plt.title("Estimated Deaths by Event")
plt.xlabel("Event Name")
plt.ylabel("Estimated Deaths")
plt.xticks(rotation=90)
plt.show()

#Pie Chart
top5 = df.sort_values(by='Estimated_Deaths', ascending=False).head(5)

plt.figure()
plt.pie(top5['Estimated_Deaths'],
        labels=top5['Event_Name'],
        autopct='%1.1f%%')
plt.title("Top 5 Deadliest Events")
plt.show()

#Stair Chart
plt.figure()
plt.step(df['Event_Name'], df['Spread_Score'])
plt.title("Spread Score of Events")
plt.xlabel("Event Name")
plt.ylabel("Spread Score")
plt.xticks(rotation=90)
plt.show()