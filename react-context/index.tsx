import { createContext, useContext, useState, ReactNode } from 'react';

export interface I{name}Data {

}
export interface I{name}DataContext {

}
const {name}Context = createContext<I{name}DataContext>({

});

export interface ProviderProps {
    children: ReactNode;
}

export const {name}Provider = ({ children }: ProviderProps) => {
    const [{name}s, dispatch] = useReducer(
        {name}Reducer,
        initial{name}s
    );


    return (
        <{name}Context.Provider
            value={{
    {name}s
    }}
>
    {children}
    </{name}Context.Provider>
);
};

export const useWeatherContext = () => useContext(WeatherContext);