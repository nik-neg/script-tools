import os

OUTPUT_DIR = "."  # Files will be saved in the current directory

def generate_context_component(name):
    Name = name.capitalize()
    component_code = """
import {{ createContext, useContext, useReducer, ReactNode }} from 'react';

export interface I{0}Data {{}}

export interface I{0}DataContext {{}}

const {0}Context = createContext<I{0}DataContext>();

const initial{0}s: I{0}Data = {{}};
const {1}Reducer = (state: I{0}Data, action: any): I{0}Data => {{
    switch (action.type) {{
        default:
            return state;
    }}
}};

export interface ProviderProps {{
    children: ReactNode;
}}

export const {0}Provider = ({{
    children,
}}: ProviderProps) => {{
    const [{1}s, dispatch] = useReducer({1}Reducer, initial{0}s);

    return (
        <{0}Context.Provider
            value={{ {{
                {1}s,
                dispatch,
            }} }}
        >
            {{children}}
        </{0}Context.Provider>
    );
}};

export const use{0}Context = () => useContext({0}Context);
""".format(Name, name)
    return component_code

def main():
    name = input("Enter the name for the React context component: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return
    component_code = generate_context_component(name)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, "{}Context.tsx".format(name.capitalize()))
    with open(file_path, "w") as file:
        file.write(component_code)
    print("{}Context.tsx has been created at {}".format(name.capitalize(), file_path))

if __name__ == "__main__":
    main()
