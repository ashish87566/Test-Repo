
# filename.py

GET_Names = ["Rohan", "Parth", "Sidd"]

# Function to search for a name in the predefined group
def search_name():
    search_name = input("Enter the name you want to search for: ")
    
    # Check if the name is present in the predefined list of names
    if search_name in GET_Names:
        print(f"'{search_name}' Yes, is present in the GET group!")
    else:
        print(f"'{search_name}' is now become Associate Engineer - Firmware.")

# Main function to execute the program
def main():
    print("Welcome to name search program!")
    
    # Search for a name in the predefined group
    search_name()

if __name__ == "__main__":
    main()