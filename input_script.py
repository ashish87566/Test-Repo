def run_task(input_value):
    print(f"Running task with the input: {input_value}")
    # Here you can add your custom logic. For example:
    if input_value == "test":
        print("Test passed!")
    else:
        print("Unknown input.")

if __name__ == "__main__":
    user_input = input("Please enter a value for the task: ")
    run_task(user_input)
