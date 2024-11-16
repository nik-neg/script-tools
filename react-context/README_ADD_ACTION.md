# Add Action to Reducer Script

This project includes a Python script that automates the process of adding new actions to a reducer in a TypeScript-based Redux store. The script takes the name of a context and an action, then updates the corresponding reducer file to include the new action in both the action enum and the reducer's switch statement.

## Features

- **Automatically updates the action enum**: Adds a new action type to the enum if it doesn’t already exist.
- **Adds new case to the reducer**: Inserts the appropriate case within the reducer's switch statement to handle the new action.
- **Ensures proper formatting**: The action name is formatted to uppercase with underscores (e.g., 'removeApple' becomes 'REMOVE_APPLE') for consistency.

## Usage

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed on your system.
3. Set the `OUTPUT_DIR` variable to the directory where your reducer files are located (default is the current directory).

### Running the Script

1. Open the terminal and navigate to the project directory.
2. Run the script:

   ```bash
   python add_action_to_reducer.py
