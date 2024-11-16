# Create React Component Boilerplate Script

This project includes a bash script that automates the creation of a basic React component structure with TypeScript. The script generates all necessary files to quickly scaffold a new component, including a TypeScript file for the component itself, a styles file, and a types file.

## Features

- **Generates the following files**:
    - `index.ts` for component exports
    - `${folder_name}.tsx` for the React component
    - `types.ts` for the TypeScript interface defining component props
    - `${folder_name}.styles.ts` for styling the component using MUI's `styled` API

- **Automatically adds exports** to `index.ts` for the component, styles, and types.
- **Creates a basic React functional component** with a styled container and an empty prop interface.

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the script with the desired component folder name:

   ```bash
   ./create_component.sh <folder_name>
