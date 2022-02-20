import { Navigate } from "react-router-dom";
import { useAuth } from "../core/contexts/Auth.context";

export function requireAnonymous(WrappedComponent: () => JSX.Element) {

    function RequireAnonymous({ children }: { children: JSX.Element }) {
        let { user } = useAuth();

        if (user) return <Navigate to="/" replace />

        return children;
    }

    return () => <RequireAnonymous><WrappedComponent /></RequireAnonymous>
}
