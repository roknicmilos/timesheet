import { createContext, useContext, ReactNode, useState } from "react";
import User from "../models/api/User";

interface AuthContextValues {
    user: User | undefined;
}

const AuthContext = createContext<AuthContextValues>({
    user: undefined,
});

export function useAuth() {
    return useContext(AuthContext)
}

export function AuthContextProvider({ children }: { children: ReactNode }) {
    const [user, setUser] = useState<User | undefined>(() => {
        const jsonUser = localStorage.getItem('user')

        console.log('jsonUser:', jsonUser)

        return jsonUser ? JSON.parse(jsonUser) : undefined
    })

    return (
        <AuthContext.Provider value={{ user }}>
            {children}
        </AuthContext.Provider>
    )
}
