import csv
import os

# Function to read high scores from a CSV file
def read_high_scores():
    file_path = 'high_scores.csv'

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            high_scores = {}

            for row in reader:
                if len(row) == 2:
                    name, score = row
                    high_scores[name] = int(score)

            return high_scores
    else:
        return {}

# Function to write high scores to a CSV file
def write_high_scores(high_scores):
    with open('high_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for name, score in high_scores.items():
            writer.writerow([name, score])

# Function to add a new high score
def add_high_score(name, score):
    if not name or not name.isalpha():
        print("Invalid name. Please enter a valid name.")
        return
    
    if not score.isdigit():
        print("Invalid score. Please enter a valid numeric score.")
        return
    
    score = int(score)
    
    high_scores = read_high_scores()
    
    if name in high_scores:
        if score > high_scores[name]:
            high_scores[name] = score
    else:
        high_scores[name] = score
    
    write_high_scores(high_scores)

# Function to search for a player's score
def search_score(player_name):
    high_scores = read_high_scores()
    
    if player_name in high_scores:
        return high_scores[player_name]
    else:
        return "Player not found"

# Function to update high scores
def update_high_scores(name, score):
    add_high_score(name, score)

# Function to sort high scores in descending order
def sort_high_scores():
    high_scores = read_high_scores()
    sorted_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_scores)

# Function to handle duplicate names
def handle_duplicate_names(name, score):
    add_high_score(name, score)

# Main function to manage the high score manager
def main():
    print("High Score Manager")
    while True:
        print("\n1. Add High Score\n2. Search Score\n3. Display High Scores\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter player name: ")
            score = input("Enter player score: ")
            add_high_score(name, score)
        elif choice == '2':
            name = input("Enter player name to search: ")
            result = search_score(name)
            print(f"Player Score: {result}")
        elif choice == '3':
            high_scores = sort_high_scores()
            print("\nHigh Scores:")
            for name, score in high_scores.items():
                print(f"{name}: {score}")
        elif choice == '4':
            print("Exiting High Score Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()