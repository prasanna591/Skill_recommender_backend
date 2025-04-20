import pandas as pd
from difflib import get_close_matches

df =pd.read_csv("skill_recommendation_dataset.csv")

career_goals = df['Career Goal'].str.lower().tolist()


user_goal = input("Enter your carrer goal : ").strip().lower()

match = get_close_matches(user_goal,career_goals, n=1, cutoff=0.3)


if match:
    matched_goal = match[0]
    result = df[df['Career Goal'].str.lower() == matched_goal].iloc[0]
    print(f"\n Career Goal: {result['Career Goal'].title()}")
    print(f"Recommended Skill : {result['Recommended Skills']}")
    print(f"Recommended Projects:{result['Recommended Projects']}")


else:
    print("sorry, no recommendation found ,try a different career goal")