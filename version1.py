import pandas as pd

# Load the dataset
df = pd.read_csv("skill_recommendation_dataset.csv")

# Convert to lowercase for case-insensitive matching
df['Career Goal'] = df['Career Goal'].str.lower()

# Ask user for input
user_goal = input("Enter your career goal (e.g., web developer, data scientist): ").strip().lower()

# Filter matching rows
match = df[df['Career Goal'].str.contains(user_goal)]

# Show results
if not match.empty:
    print("\n📘 Skill Recommendations:")
    for _, row in match.iterrows():
        print(f"\n🎯 Career Goal: {row['Career Goal'].title()}")
        print(f"✅ Recommended Skills: {row['Recommended Skills']}")
        print(f"🛠️  Recommended Projects: {row['Recommended Projects']}")
else:
    print("❌ Sorry, no recommendations found. Try a different career goal.")
