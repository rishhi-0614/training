import random

subjects = [
    "Success", "Failure", "Happiness", "Discipline",
    "Learning", "Time", "Dreams", "Confidence"
]

verbs = [
    "comes from", "is built by", "grows through",
    "is shaped by", "requires", "is found in"
]

objects = [
    "consistent effort",
    "patience and persistence",
    "small daily actions",
    "believing in yourself",
    "learning from mistakes",
    "never giving up"
]

endings = [
    "— even when it’s hard.",
    "when no one is watching.",
    "one step at a time.",
    "before you feel ready.",
    "more than talent ever will."
]

def generate_quote():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(endings)}"

# Generate multiple quotes
if __name__ == "__main__":
    print("\n✨ AI Quote Generator ✨\n")
    for i in range(5):
        print(f"{i+1}. {generate_quote()}")