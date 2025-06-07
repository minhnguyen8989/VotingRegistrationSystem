"""
Title:       Critical Thinking Assignment #4
Author:      Minh Nguyen
Created:     2025-06-07
Last Edited: 2025-06-07
Description: This program is an advanced voting system designed to securely register voters, validate their information, and store voting data.
            The system allows users to input voter information including name, age, candidate choice, and a unique voter ID.
            It ensures all inputs are valid before storing them. Users can register multiple voters, search for voters by ID, and display a list of all registered voters.
            The program provides a simple menu-driven interface to access all features.
User Input:
    - Voter Information with candidate choice
    - Search for voter by voter ID
    - Exit the Program
Program Output:
    - Display all voters information
    - Voter information with voter ID search
"""

candidates_list = ["Alice", "Bob", "Charlie"]
voters_list = []

def voter_age_validation():
    while True:
        age_input = input("Enter voter age (18-120): ").strip()
        if not age_input:
            print("Age cannot be empty.")
        elif not age_input.isdigit():
            print("Age must be a number.")
        else:
            age = int(age_input)
            if 18 <= age <= 120:
                return age
            else:
                print("Age must be between 18 and 120.")

def candidate_choice_validation():
    while True:
        choice = input(f"Enter candidate choice ({', '.join(candidates_list)}): ").strip()
        if not choice:
            print("Candidate choice cannot be empty.")
        elif choice not in candidates_list:
            print("Invalid candidate choice. Choose from the list.")
        else:
            return choice

def voter_id_validation(existing_ids):
    while True:
        voter_id = input("Enter voter ID (alphanumeric): ").strip()
        if not voter_id:
            print("Voter ID cannot be empty.")
        elif not voter_id.isalnum():
            print("Voter ID must be alphanumeric.")
        elif voter_id in existing_ids:
            print("Voter ID already registered.")
        else:
            return voter_id

# Register new voter
def register_new_voter():
    voter_name = input("Enter voter name: ").strip()
    if not voter_name:
        print("Name cannot be empty.")
        return

    voter_age = voter_age_validation()
    candidate_choice = candidate_choice_validation()
    voter_id = voter_id_validation([v["voter_id"] for v in voters_list])

    voter_info = {
        "voter_name": voter_name,
        "age": voter_age,
        "candidate": candidate_choice,
        "voter_id": voter_id
    }
    voters_list.append(voter_info)
    print("Voter registered successfully.\n")

def display_all_voters():
    if not voters_list:
        print("No voters registered yet.")
    else:
        print("\nRegistered Voters:")
        for i, voter in enumerate(voters_list, start=1):
            print(f"{i}. ID: {voter['voter_id']}, Name: {voter['voter_name']}, Age: {voter['age']}, Voted for: {voter['candidate']}")
    print()

def search_voter_by_id():
    search_id = input("Enter voter ID to search: ").strip()
    for voter in voters_list:
        if voter["voter_id"] == search_id:
            print(f"Voter Found: ID: {voter['voter_id']}, Name: {voter['voter_name']}, Age: {voter['age']}, Voted for: {voter['candidate']}\n")
            return
    print("Voter not found.\n")

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Register New Voter")
        print("2. Display All Registered Voters")
        print("3. Search for a Voter by Voter ID")
        print("4. Exit the Program")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            register_new_voter()
        elif choice == '2':
            display_all_voters()
        elif choice == '3':
            search_voter_by_id()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 4.\n")

if __name__ == "__main__":
    main_menu()
