import { logout } from "../../../core/services/auth.service";
import { useAuth } from "../../../core/contexts/Auth.context";

export default function Navigation() {

    const { user, clearUser } = useAuth()

    const handleLogout = function () {
        logout()
        clearUser()
        window.location.reload()
    }

    return (
        <>
            <nav className="navigation">
                <button id="navigation__link" type="button" className="navigation__link"><span id="navigation__text" className="nav-toggle"></span></button>
                <ul className="navigation__menu">
                    <li className="navigation__list">
                        <a href="/" className="btn navigation__button navigation__button--active">Timesheet</a>
                    </li>
                    <li className="navigation__list">
                        <a href="/" className="btn navigation__button">Clients</a>
                    </li>
                    <li className="navigation__list">
                        <a href="/" className="btn navigation__button">Projects</a>
                    </li>
                    <li className="navigation__list">
                        <a href="/" className="btn navigation__button">Categories</a>
                    </li>
                    <li className="navigation__list">
                        <a href="/" className="btn navigation__button">Employees</a>
                    </li>
                    <li className="navigation__list">
                        <a href="/" className="btn navigation__button">Reports</a>
                    </li>
                </ul>
            </nav>
            <div className="user">
                <div className="user__nav">
                    <h2 className="user__name">{user?.name}</h2>
                    <ul className="user__dropdown">
                        <li className="user__list"><a className="user__link" href="/">Change password</a></li>
                        <li className="user__list"><a className="user__link" href="/">Settings</a></li>
                        <li className="user__list"><a className="user__link" href="/">Export all data</a></li>
                    </ul>
                </div>
                <ul>
                    <li className="logout">
                        <p className="logout__link" onClick={handleLogout}>Logout</p>
                    </li>
                </ul>
            </div>
        </>
    )
}
