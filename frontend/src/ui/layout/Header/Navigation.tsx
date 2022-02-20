import { logout } from "../../../core/services/auth.service";
import { useAuth } from "../../../core/contexts/Auth.context";
import { NavLink } from "react-router-dom";

export default function Navigation() {

    const { user, clearUser } = useAuth()

    const handleLogout = function () {
        logout()
        clearUser()
        window.location.reload()
    }

    const getNavLinkClassName = function ({ isActive }: { isActive: boolean }): string {
        return `btn navigation__button ${isActive ? "navigation__button--active" : ""}`
    }

    return (
        <>
            <nav className="navigation">
                <button id="navigation__link" type="button" className="navigation__link"><span id="navigation__text" className="nav-toggle"></span></button>
                <ul className="navigation__menu">
                    <li className="navigation__list">
                        <NavLink to="/" className={isActive => getNavLinkClassName(isActive)}>Timesheet</NavLink>
                    </li>
                    <li className="navigation__list">
                        <NavLink to="/clients" className={isActive => getNavLinkClassName(isActive)}>Clients</NavLink>
                    </li>
                    <li className="navigation__list">
                        <NavLink to="/projects" className={isActive => getNavLinkClassName(isActive)}>Projects</NavLink>
                    </li>
                    <li className="navigation__list">
                        <NavLink to="/categories" className={isActive => getNavLinkClassName(isActive)}>Categories</NavLink>
                    </li>
                    <li className="navigation__list">
                        <NavLink to="/employees" className={isActive => getNavLinkClassName(isActive)}>Employees</NavLink>
                    </li>
                    <li className="navigation__list">
                        <NavLink to="/reports" className={isActive => getNavLinkClassName(isActive)}>Reports</NavLink>
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
