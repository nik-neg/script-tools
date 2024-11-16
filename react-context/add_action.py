import os

OUTPUT_DIR = "."  # Files will be saved in the current directory

def add_action_to_reducer(name, action_name):
    # Capitalize the name for proper casing
    Name = name.capitalize()
    action_enum_name = f'{Name}Actions'

    # Convert the action name to uppercase with underscores (e.g., 'removeApple' -> 'REMOVE_APPLE')
    formatted_action_name = action_name.replace(" ", "_").upper()

    # Read the existing reducer file
    reducer_file_path = os.path.join(OUTPUT_DIR, f"{name}Reducer.ts")
    if not os.path.exists(reducer_file_path):
        print(f"Error: The reducer file {reducer_file_path} does not exist!")
        return

    with open(reducer_file_path, "r") as file:
        reducer_code = file.read()

    # Create the action enum case and reducer case
    new_enum_case = f"    {formatted_action_name} = '{formatted_action_name}',"
    new_reducer_case = f"        case {action_enum_name}.{formatted_action_name}:\n            // Handle {formatted_action_name} action\n            return state;"

    # Check and add the action to the enum if it doesn't exist already
    if f"{formatted_action_name} = '{formatted_action_name}'" not in reducer_code:
        # Add the action to the enum section
        reducer_code = reducer_code.replace(f'export enum {action_enum_name} {{', f'export enum {action_enum_name} {{\n{new_enum_case}')

    # Check and add the action to the reducer switch statement if it doesn't exist already
    if f"case {action_enum_name}.{formatted_action_name}:" not in reducer_code:
        # Add the case to the reducer switch statement
        reducer_code = reducer_code.replace(f'    switch (action.type) {{', f'    switch (action.type) {{\n{new_reducer_case}')

    # Write the updated code back to the reducer file
    with open(reducer_file_path, "w") as file:
        file.write(reducer_code)

    print(f"Action {formatted_action_name} has been added to {reducer_file_path}")

def main():
    name = input("Enter the name of the context component (e.g., 'apple'): ").strip()
    action_name = input("Enter the name of the action to add (e.g., 'remove apple'): ").strip()

    if not name or not action_name:
        print("Error: Name and action cannot be empty!")
        return

    add_action_to_reducer(name, action_name)

if __name__ == "__main__":
    main()
