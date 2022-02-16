import { useAuth } from '../../../core/contexts/Auth.context'
import whiteLogo from './../../../assets/images/logo/logo-white.png'
import Navigation from './Navigation'


export default function Header() {
    const { user } = useAuth()

    return (
        <header className="header">
            <div className="inner-wrap">
                <a href="/" className="logo">
                    <img src={whiteLogo} alt="logo" />
                </a>
                {user ? <Navigation /> : null}
            </div>
        </header>
    )
}
