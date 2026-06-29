import matplotlib.pyplot as plt
import pandas as pd

input_file = "raw_student_data.csv"
df = pd.read_csv(input_file)

print("\n--- Original Data Summary ---")
print(df.info())

df.drop_duplicates(inplace=True)

df["Branch"] = df["Branch"].fillna("Not Specified")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance_%"] = df["Attendance_%"].fillna(df["Attendance_%"].mean())

output_excel = "Cleaned_Student_Report.xlsx"
df.to_excel(output_excel, index=False, sheet_name="Cleaned Data")
print(f"\n✅ Cleaned report saved successfully as '{output_excel}'")

plt.figure(figsize=(14, 6))
plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="black")
plt.title("Student Marks Analytics (50 Rows Dataset)")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)

graph_file = "Student_Marks_Summary.png"
plt.savefig(graph_file, bbox_inches="tight")
plt.close()
print(f"📊 Visual chart summary saved as '{graph_file}'")

print("\n🎉 Automation Workflow Completed Successfully!")