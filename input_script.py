# test_search_name.py

import subprocess

# Function to run the search_name_script.py and simulate user input
def run_script_with_input(name_to_search):
    # Run the script and pass the input through stdin
    result = subprocess.run(
        ['python3', 'search_name_script.py'],  # This is the path to your script
        input=name_to_search + '\n',  # Simulating user input
        text=True,  # Treat the input and output as text (not bytes)
        capture_output=True  # Capture stdout and stderr
    )
    
    # Output from the script
    return result.stdout

# Test: Searching for a name that is present
def test_name_found():
    output = run_script_with_input("Bob")
    print("Test 1 - Name Found:")
    print(output)  # This will print the result of searching for 'Bob'

# Test: Searching for a name that is not present
def test_name_not_found():
    output = run_script_with_input("George")
    print("Test 2 - Name Not Found:")
    print(output)  # This will print the result of searching for 'George'

if __name__ == "__main__":
    test_name_found()  # Run the test for a name found
    test_name_not_found()  # Run the test for a name not found