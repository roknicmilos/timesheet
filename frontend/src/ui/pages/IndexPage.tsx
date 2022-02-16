import { useAuth } from "../../core/contexts/Auth.context"
import LoginPage from "./LoginPage"
import TimesheetPage from "./TimesheetPage"

export default function IndexPage() {

    const { user } = useAuth()

    return user ? <TimesheetPage /> : <LoginPage />
}
