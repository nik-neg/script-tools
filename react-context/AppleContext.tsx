
import { createContext, useContext, useReducer } from 'react';
import { AppleReducer } from './AppleReducer';
import { IAppleData, IAppleDataContext, ProviderProps } from './types';

const AppleContext = createContext<IAppleDataContext>();
export const AppleDispatchContext = createContext(null);

const initialApples: IAppleData = {};  // You can adjust the initial state as needed

export const AppleProvider = ({
    children,
}: ProviderProps) => {
    const [state, dispatch] = useReducer(AppleReducer, initialApples);

    return (
        <AppleContext.Provider value={ state }>
            <AppleDispatchContext.Provider value={ dispatch }>
                {children}
            </AppleDispatchContext.Provider>
        </AppleContext.Provider>
    );
};

export const useAppleContext = () => useContext(AppleContext);
export const useAppleDispatchContext = () => useContext(AppleDispatchContext);
