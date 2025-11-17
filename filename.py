
# Predefined list of names
group_names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Function to search for a name in the predefined group
def search_name():
    search_name = input("Enter the name you want to search for: ")
    
    # Check if the name is present in the predefined list of names
    if search_name in group_names:
        print(f"'{search_name}' is present in the group!")
    else:
        print(f"'{search_name}' is not present in the group.")

# Main function to execute the program
def main():
    print("Welcome to the group name search program!")
    
    # Search for a name in the predefined group
    search_name()

if __name__ == "__main__":
    main()