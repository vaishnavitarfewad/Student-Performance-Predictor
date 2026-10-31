import pandas as pd
import random

random.seed(42)
rows = []

for _ in range(300):
    study_hours = round(random.uniform(0, 10), 1)
    attendance = random.randint(30, 100)
    previous_marks = random.randint(20, 100)
    assignment_score = random.randint(20, 100)

    # Simple rule-based labels for a demonstration dataset
    score = (
        study_hours * 4
        + attendance * 0.20
        + previous_marks * 0.25
        + assignment_score * 0.15
    )

    if score >= 48:
        performance = "Good"
    elif score >= 34:
        performance = "Average"
    else:
        performance = "At Risk"

    rows.append({
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_marks": previous_marks,
        "assignment_score": assignment_score,
        "performance": performance
    })

df = pd.DataFrame(rows)
df.to_csv("student_data.csv", index=False)
print("Dataset created successfully! student_data.csv")
print(df.head())
