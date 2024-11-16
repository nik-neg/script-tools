# Client Automation Helper

This repository contains various automation scripts and tools designed to streamline and accelerate the development process for React applications. These tools include utilities for creating React components, managing context with reducers, and enhancing development workflows.

## Features

- **`client-automation-helper`**: adds test-ids to components

- **`create_react_component_folder`**: Automates the creation of a new React component folder, including essential files like `index.ts`, component `.tsx`, `.styles.ts`, and `types.ts`. This script helps you quickly scaffold a React component with proper structure.**

- **`react-context`**: Generates the necessary files for a new React context, including a context provider, reducer, and TypeScript types. It allows you to easily set up a new context with state management via `useReducer`.

- **`aliases`**: aliases for cli

## Usage

1. Clone or download the repository to your local machine.
2. Each script has its own functionality, and you can run them independently.
3. To get started, follow the instructions in the respective folder README files to set up or run the desired script.

### Example: Create React Component Folder

For automating React component folder creation, you can run the following:

```bash
./create_react_component_folder.sh <folder_name>
