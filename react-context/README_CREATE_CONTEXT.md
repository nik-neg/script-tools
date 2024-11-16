# Generate React Context Component Files

This project includes a Python script that automatically generates the necessary files for a new React context component. The script creates the following files for a specified component name:
- **Context component (`.tsx`)**
- **Reducer (`.ts`)**
- **Types (`.ts`)**

The generated files include the basic setup for a React context provider with a reducer, along with TypeScript types for the state and context.

## Features

- **Generates React Context Provider**: Automatically creates a context provider component using `useReducer` for state management.
- **Generates Reducer File**: Creates a reducer that handles state changes using action types in an enum.
- **Generates TypeScript Types**: Defines types for the context and state to ensure type safety.
- **Handles Initial State**: Initializes the state with a placeholder object which you can modify as needed.

## Usage

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Set the `OUTPUT_DIR` variable to the directory where the generated files should be saved (by default, this is the current directory).

### Running the Script

1. Open the terminal and navigate to the project directory.
2. Run the script:

   ```bash
   python generate_context_component.py
