import subprocess
import os

# Function to run the filename.py and simulate user input
def run_script_with_input(name_to_search):
    current_directory = os.getcwd()
    script_path = os.path.join(current_directory, 'Main.py')  # Build path dynamically
    
    try:
        process = subprocess.Popen(
            ['python3', script_path],  # Use the absolute path to Main.py
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Send the input (name to search) to the script and capture output and errors
        output, error = process.communicate(input=name_to_search + '\n')

        # Check if there's an error in stderr and print it
        if error:
            print(f"Error occurred: {error}")
        
        # Return the captured output
        return output
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

# Test: Searching for a name that is present
def test_name_found():
    print("Test 1 - Name Found: This name was found in the GET group.")

# Test: Searching for a name that is not present
def test_name_not_found():
    print("Test 2 - Not found. Well, now they’ve been promoted to Associate Engineer - Firmware. Congrats Sanket")

def check_name_status(output, name_to_search):
    """ Function to check if the name was found or not, based on output """
    # Check for presence of the name in the GET group (i.e. the found case)
    if f"'{name_to_search}' Yes, is present in the GET group!" in output:
        print(f"{name_to_search} found!")
        return 1  # Name found, return 1
    else:
        print(f"{name_to_search} not found!")
        return 0  # Name not found, return 0

if __name__ == "__main__":
    # List of names to test
    names_to_test = ["Parth" ,]

    # Loop through each name and run the script
    for name in names_to_test:
        # Get the output for the current name
        output = run_script_with_input(name)

        if output:  # Only process if we got output from the script
            # Check if the name is found or not based on the output
            status = check_name_status(output, name)

            # Depending on the result, run the corresponding test function
            if status == 1:
                test_name_found()  # Run the test for a name found
            elif status == 0:
                test_name_not_found()  # Run the test for a name not found
