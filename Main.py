import argparse

# Define the list of names in the GET group
GET_Names = ["Parth", "Sidd"]

# Function to search for a name in the predefined group
def search_name(search_name):
    # Check if the name is present in the predefined list of names
    if search_name in GET_Names:
        print(f"'{search_name}' Yes, is present in the GET group!")
        return 1
    else:
        print(f"'{search_name}'? Not found. Well, now they’ve been promoted to Associate Engineer - Firmware. Congrats!")
        return 0

# Main function to execute the program
def main():
    parser = argparse.ArgumentParser(description="Search for a name in the GET group.")
    parser.add_argument('name', type=str, help="The name to search for")
    args = parser.parse_args()

    search_name(args.name)

if __name__ == "__main__":
    main()
