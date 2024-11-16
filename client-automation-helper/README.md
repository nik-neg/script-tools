# Add Data Test IDs to React Components

This project includes a Python script that automatically adds `data-testid` attributes to JSX elements in React component files (`.tsx`). The script traverses the specified directory, finds all `.tsx` files, and inserts the appropriate `data-testid` attributes based on the component's structure.

## Functionality

- **Converts JSX elements**: It adds `data-testid` to each JSX element based on its tag name and its parent tag's name (if applicable).
- **Kebab-case transformation**: Converts camelCase or PascalCase tag and parent names to kebab-case for consistency in test IDs.
- **Recursive file handling**: Traverses all `.tsx` files in the specified directory and applies the changes to each one.

## Usage

1. Clone or download the repository to your local machine.
2. Install Python if it's not already installed.
3. Make sure you have the necessary access to the directory where your React components are located.

### Running the Script

The script will walk through the `src` directory and add `data-testid` attributes to all `.tsx` files.

1. Open the terminal and navigate to the project directory.
2. Modify the `src_path` variable to point to the correct `src` folder in your React project.
3. Run the script:

   ```bash
   python add_data_test_ids.py
