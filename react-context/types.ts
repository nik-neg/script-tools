
import { ReactNode } from 'react';

export interface IAppleData {
    // Define your state properties here
}

export interface IAppleDataContext {
    state: IAppleData;
}

export interface ProviderProps {
    children: ReactNode;
}
