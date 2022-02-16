import { createContext, useContext, ReactNode, useState } from "react";
import User from "../models/api/User";

interface AuthContextValues {
    user?: User;
    clearUser(): void;
}

const clearUser = function () {
    localStorage.removeItem('user')
}

const AuthContext = createContext<AuthContextValues>({ clearUser });

export function useAuth() {
    return useContext(AuthContext)
}

export function AuthContextProvider({ children }: { children: ReactNode }) {
    const [user] = useState<User | undefined>(() => {
        const jsonUser = localStorage.getItem('user')
        return jsonUser ? JSON.parse(jsonUser) : undefined
    })

    return (
        <AuthContext.Provider value={{ user, clearUser }}>
            {children}
        </AuthContext.Provider>
    )
}
