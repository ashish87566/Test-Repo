import subprocess

def run_main(name_to_search):
    try:
        # Run the Main.py script with the given name
        result = subprocess.run(
            ['python3', 'Main.py', name_to_search],  # Run Main.py with the name as an argument
            check=True,  # Will raise CalledProcessError if the command fails
            text=True,  # Ensure the output is in text format (not bytes)
            capture_output=True  # Capture output of the command
        )
        print(result.stdout)  # Print the output of Main.py
    except subprocess.CalledProcessError as e:
        print(f"Error running Main.py: {e}")
        print(f"Error message: {e.stderr}")

def test_name(name_to_search):
    print(f"Running test for: {name_to_search}")
    run_main(name_to_search)

# Run the test for specific names
test_name('Sidd')  # Test with 'Sidd'
# test_name('Sanket')  # Test with 'John'
