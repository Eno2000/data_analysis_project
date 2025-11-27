import pandas as pd

#Read from CSV and Excel files
df_for_csv_original = pd.read_csv(r"C:\Users\DELL\OneDrive\Documents\student_performance_data.csv")

#copied the original data into another variable
df_csv_copied = df_for_csv_original.copy()  #the reason why it was copied is so that the original data would remain unto
#refer back to the original one

df_csv_copied.head()  #first 5 rows(csv format).


df_csv_copied.loc[df_csv_copied["AttendanceRate"] >= 80, "status"] = "pass"
df_csv_copied.loc[df_csv_copied["AttendanceRate"] < 80, "status"] = "fail"
df_csv_copied.head(10)
df_csv_copied.loc[df_csv_copied["GPA"] >= 3.5, "grade"] = "A"
df_csv_copied.loc[(df_csv_copied["GPA"] >= 3.0) & (df_csv_copied["GPA"] < 3.5), "grade"] = "B"
df_csv_copied.loc[(df_csv_copied["GPA"] >= 2.0) & (df_csv_copied["GPA"] < 3.0), "grade"] = "C"
df_csv_copied.loc[df_csv_copied["GPA"] < 2.0, "grade"] = "D"
df_csv_copied.head(5)
df_csv_copied.loc[df_csv_copied["StudyHoursPerWeek"] >= 39, "study"] = "Real Readers"
df_csv_copied.loc[(df_csv_copied["StudyHoursPerWeek"] >= 30) & (df_csv_copied["StudyHoursPerWeek"] < 39), "study"] = "Average Readers"
df_csv_copied.loc[(df_csv_copied["StudyHoursPerWeek"] >= 20) & (df_csv_copied["StudyHoursPerWeek"] < 29), "study"] = "Fair Readers"
df_csv_copied.loc[df_csv_copied["StudyHoursPerWeek"] < 20, "study"] = "Lazybones"
df_csv_copied.head(10)