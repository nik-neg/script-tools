
import { createContext, useContext, useReducer, ReactNode } from 'react';

export interface IAppleData {}

export interface IAppleDataContext {}

const AppleContext = createContext<IAppleDataContext>();

const initialApples: IAppleData = {};
const AppleReducer = (state: IAppleData, action: any): IAppleData => {
    switch (action.type) {
        default:
            return state;
    }
};

export interface ProviderProps {
    children: ReactNode;
}

export const AppleProvider = ({
    children,
}: ProviderProps) => {
    const [Apples, dispatch] = useReducer(AppleReducer, initialApples);

    return (
        <AppleContext.Provider
            value={ {
                Apples,
                dispatch,
            } }
        >
            {children}
        </AppleContext.Provider>
    );
};

export const useAppleContext = () => useContext(AppleContext);
