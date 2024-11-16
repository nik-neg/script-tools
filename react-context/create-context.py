import os

OUTPUT_DIR = "."  # Files will be saved in the current directory

def generate_context_component(name):
    Name = name.capitalize()
    state_name = name.lower()  # e.g., "apple" for "Apple"

    # Create the component code with context provider
    component_code = f"""
import {{ createContext, useContext, useReducer }} from 'react';
import {{ {Name}Reducer }} from './{name}Reducer';
import {{ I{Name}Data, I{Name}DataContext, ProviderProps }} from './types';

const {Name}Context = createContext<I{Name}DataContext>();
export const {Name}DispatchContext = createContext(null);

const initial{Name}s: I{Name}Data = {{}};  // You can adjust the initial state as needed

export const {Name}Provider = ({{
    children,
}}: ProviderProps) => {{
    const [state, dispatch] = useReducer({Name}Reducer, initial{Name}s);

    return (
        <{Name}Context.Provider value={{ state }}>
            <{Name}DispatchContext.Provider value={{ dispatch }}>
                {{children}}
            </{Name}DispatchContext.Provider>
        </{Name}Context.Provider>
    );
}};

export const use{Name}Context = () => useContext({Name}Context);
export const use{Name}DispatchContext = () => useContext({Name}DispatchContext);
"""
    return component_code

def generate_reducer(name):
    # Generate reducer and action enum code
    Name = name.capitalize()
    enum_name = f'{Name}Actions'

    reducer_code = f"""
import {{ I{Name}Data, ProviderProps }} from './types';

export enum {enum_name} {{
    ADD_{Name.upper()} = 'ADD_{Name.upper()}'
}}

export const {name}Reducer = (state: I{Name}Data, action: any): I{Name}Data => {{
    switch (action.type) {{
        case {enum_name}.ADD_{Name.upper()}:
            // Handler for adding {name}
            return state;  // You can modify state as needed here
        default:
            return state;
    }}
}};
"""
    return reducer_code

def generate_types(name):
    Name = name.capitalize()

    # Generate types code
    types_code = f"""
import {{ ReactNode }} from 'react';

export interface I{Name}Data {{
    // Define your state properties here
}}

export interface I{Name}DataContext {{
    state: I{Name}Data;
}}

export interface ProviderProps {{
    children: ReactNode;
}}
"""
    return types_code

def main():
    name = input("Enter the name for the React context component: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return

    # Generate component code
    component_code = generate_context_component(name)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate and write the Context component file
    component_file_path = os.path.join(OUTPUT_DIR, f"{name.capitalize()}Context.tsx")
    with open(component_file_path, "w") as file:
        file.write(component_code)

    # Generate and write the Reducer file
    reducer_code = generate_reducer(name)
    reducer_file_path = os.path.join(OUTPUT_DIR, f"{name}Reducer.ts")
    with open(reducer_file_path, "w") as file:
        file.write(reducer_code)

    # Generate and write the Types file
    types_code = generate_types(name)
    types_file_path = os.path.join(OUTPUT_DIR, "types.ts")
    with open(types_file_path, "w") as file:
        file.write(types_code)

    print(f"{name.capitalize()}Context.tsx has been created at {component_file_path}")
    print(f"{name}Reducer.ts has been created at {reducer_file_path}")
    print(f"types.ts has been created at {types_file_path}")

if __name__ == "__main__":
    main()
