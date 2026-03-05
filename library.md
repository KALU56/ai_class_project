# Smart Library Book Recommendation Agent

## Model-Based Intelligent Agent

---

## 1. Introduction

Artificial Intelligence (AI) agents are systems that **perceive their environment, make decisions, and take actions** to achieve specific goals.

A **Model-Based Agent** is a type of AI agent that maintains an **internal model** of the environment. Unlike reactive agents that respond only to the current input, model-based agents **store information**, reason about the environment, and make more intelligent decisions.

In this project, we implement a **Smart Library Book Recommendation Agent**, which helps students **choose books based on their interests**.
This agent demonstrates **how a model-based agent works** in a simple and interactive way.

---

## 2. What is a Model-Based Agent?

A **Model-Based Agent** uses an **internal representation of the environment** to:

1. Track what it knows about the world
2. Handle partially observable environments
3. Make decisions based on both the current input and past information

**Key Components:**

| Component       | Description                                    |
| --------------- | ---------------------------------------------- |
| Perception      | Observing the environment and receiving input  |
| Internal Model  | Storing knowledge about the environment        |
| Decision Making | Reasoning based on the model to choose actions |
| Action          | Performing an action to achieve a goal         |

Our **Book Recommendation Agent** implements all four components.

---

## 3. How the Agent Works

The agent follows a structured process to recommend books:

### Step 1: Perception

* The agent **asks the student for their interest**, for example:

```
Student enters interest: programming
```

* This is the **current observation** that the agent uses to make decisions.

---

### Step 2: Internal Model

* The agent has a **internal database of books** (its model of the environment).
* Each book contains:

  * `title` – the name of the book
  * `category` – the subject or interest area

Example internal model:

```python
books = [
    {"title": "Python Basics", "category": "programming"},
    {"title": "World History", "category": "history"},
    {"title": "Physics Fundamentals", "category": "science"}
]
```

* This model allows the agent to **remember all available books** and **use this knowledge in decision making**.

---

### Step 3: Decision Making

* The agent compares the student's interest with the book categories in its model.
* Books that match the student’s interest are **selected as recommendations**.
* The agent can also return **top 3 books** if multiple matches exist.

Decision logic example:

```python
for book in books:
    if book["category"].lower() == student_interest.lower():
        recommend(book)
```

* This step demonstrates **reasoning using the internal model**.

---

### Step 4: Action

* The agent outputs the recommended books to the student.
* Example output:

```
Recommended Books:
- Python Basics
- Data Structures
```

* This action completes the agent cycle.

---

## 4. Full Example Execution

1. Student runs the agent.
2. Agent asks: *“Enter your interest:”*
3. Student types: `programming`
4. Agent perceives the input and accesses its internal model.
5. Agent selects matching books.
6. Agent outputs recommendations:

```
Recommended Books:
- Python Basics
- Data Structures
```

7. Student can search again for another interest.

---

## 5. Agent Architecture Diagram

```
Student Input
      ↓
Agent Perception → reads student interest
      ↓
Internal Model → books database
      ↓
Decision Making → match interest with categories
      ↓
Action → recommend books
```

* **Perception:** reads the input
* **Model:** stores the book database
* **Decision:** selects books matching interest
* **Action:** outputs recommendations

---

## 6. Python Implementation (Improved Version)

```python
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
            if count == 3:   # show top 3 books
                break
    else:
        print("\nNo books found for that interest.")

    again = input("\nDo you want another recommendation? (yes/no): ")
    if again.lower() != "yes":
        print("\nThank you for using Smart Library Agent 📚")
        break
```

---

## 7. Advantages of a Model-Based Agent

* **Remembers knowledge:** The book database allows multiple queries.
* **Flexible:** New books can be added easily.
* **Intelligent decision-making:** Matches input with stored knowledge.
* **Interactive:** Can handle multiple student inputs.

---

## 8. Applications

* Library book recommendation systems
* Online learning platforms
* Personalized tutoring systems
* E-commerce recommendation systems

---

## 9. Conclusion

The **Smart Library Book Recommendation Agent** demonstrates the concept of a **Model-Based AI Agent**:

1. **Perception:** Reads student input
2. **Model:** Uses internal book database
3. **Decision:** Selects matching books
4. **Action:** Recommends books

This project is simple, interactive, and clearly illustrates **how a model-based agent works in real life**.

It can be **expanded** for:

* personalized history tracking
* ratings-based recommendations
* top-N suggestions

```
```
