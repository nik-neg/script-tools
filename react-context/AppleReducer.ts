
import { IAppleData, } from './types';

export enum AppleActions {
    FETCH_APPLES = 'FETCH_APPLES',
    FIND_APPLE = 'FIND_APPLE',
    REMOVE_APPLE = 'REMOVE_APPLE',
    ADD_APPLE = 'ADD_APPLE'
}

export const AppleReducer = (state: IAppleData, action: any): IAppleData => {
    switch (action.type) {
        case AppleActions.FETCH_APPLES:
            // Handle FETCH_APPLES action
            return state;
        case AppleActions.FIND_APPLE:
            // Handle FIND_APPLE action
            return state;
        case AppleActions.REMOVE_APPLE:
            // Handle REMOVE_APPLE action
            return state;
        case AppleActions.ADD_APPLE:
            // Handler for adding Apple
            return state;  // You can modify state as needed here
        default:
            return state;
    }
};
