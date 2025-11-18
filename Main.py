# Define the list of names in the GET group
GET_Names = ["Parth", "Sidd"]

# Function to search for a name in the predefined group
def search_name():
    search_name = input("Enter the name you want to search for: ").strip()  # Strip to remove any extra spaces or quotes
    
    # Check if the name is present in the predefined list of names
    if search_name in GET_Names:
        print(f"'{search_name}' Yes, is present in the GET group!")
        return 1
    else:
        print(f"'{search_name}' is now become Associate Engineer - Firmware.")
        return 0
    

# Main function to execute the program
def main():
    # Search for a name in the predefined group
    return search_name()

if __name__ == "__main__":
    main()
