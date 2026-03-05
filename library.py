# Smart Library Recommendation Agent (Improved)

books = [
    {"title": "Python Basics", "category": "programming"},
    {"title": "Data Structures", "category": "programming"},
    {"title": "Artificial Intelligence Intro", "category": "technology"},
    {"title": "World History", "category": "history"},
    {"title": "Ancient Civilizations", "category": "history"},
    {"title": "Physics Fundamentals", "category": "science"},
    {"title": "Chemistry Principles", "category": "science"},
    {"title": "Algebra Guide", "category": "mathematics"},
    {"title": "Calculus Basics", "category": "mathematics"}
]

print("📚 Smart Library Recommendation Agent")
print("--------------------------------------")

while True:

    interest = input("\nEnter your interest (programming / technology / history / science / mathematics): ")

    recommendations = []

    for book in books:
        if book["category"].lower() == interest.lower():
            recommendations.append(book["title"])

    if recommendations:

        print("\nRecommended Books:")

        count = 0
        for title in recommendations:
            print("-", title)
            count += 1

            if count == 3:   # show top 3
                break

    else:
        print("\nNo books found for that interest.")

    again = input("\nDo you want another recommendation? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using Smart Library Agent 📚")
        break