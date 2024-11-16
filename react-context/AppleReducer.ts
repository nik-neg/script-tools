
import { IAppleData, ProviderProps } from './types';

export enum AppleActions {
    ADD_APPLE = 'ADD_APPLE'
}

export const AppleReducer = (state: IAppleData, action: any): IAppleData => {
    switch (action.type) {
        case AppleActions.ADD_APPLE:
            // Handler for adding Apple
            return state;  // You can modify state as needed here
        default:
            return state;
    }
};
