import { NavLink } from 'react-router-dom'
import { useAuth } from '../../../core/contexts/Auth.context'
import whiteLogo from './../../../assets/images/logo/logo-white.png'
import Navigation from './Navigation'


export default function Header() {
    const { user } = useAuth()

    return (
        <header className="header">
            <div className="inner-wrap">
                <NavLink to="/" className="logo">
                    <img src={whiteLogo} alt="logo" />
                </NavLink>
                {user ? <Navigation /> : null}
            </div>
        </header>
    )
}
