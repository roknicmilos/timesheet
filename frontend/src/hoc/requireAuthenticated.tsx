import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../core/contexts/Auth.context";

export function requireAuthenticated(WrappedComponent: () => JSX.Element) {

    function RequireAuthenticated({ children }: { children: JSX.Element }) {
        let { user } = useAuth();
        let location = useLocation();

        if (!user) return <Navigate to="/login" state={{ from: location }
        } replace />

        return children;
    }

    return () => <RequireAuthenticated><WrappedComponent /></RequireAuthenticated >
}
