import whiteLogo from './../assets/images/logo/logo-white.png'

export default function Header() {
    return (
        <header className="header">
            <div className="inner-wrap">
                <a href="/" className="logo">
                    <img src={whiteLogo} alt="logo" />
                </a>
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
                        <h2 className="user__name">Ognjen Adamović</h2>
                        <ul className="user__dropdown">
                            <li className="user__list"><a className="user__link" href="/">Change password</a></li>
                            <li className="user__list"><a className="user__link" href="/">Settings</a></li>
                            <li className="user__list"><a className="user__link" href="/">Export all data</a></li>
                        </ul>
                    </div>
                    <ul>
                        <li className="logout">
                            <a className="logout__link" href="/">Logout</a>
                        </li>
                    </ul>
                </div>
            </div>
        </header>
    )
}
