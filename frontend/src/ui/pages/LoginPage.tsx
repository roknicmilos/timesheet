import { useState } from "react"
import { login } from "../../core/api/auth.api";

export default function LoginPage() {

    const [email, setEmail] = useState<string>('')
    const [password, setPassword] = useState<string>('')
    const [hasErrors, setHasErrors] = useState<boolean>(false)


    const handleSubmit = async (event: any) => {
        event.preventDefault();
        const user = await login(email, password)

        if (!user) return setHasErrors(true)

        localStorage.setItem('user', JSON.stringify(user))
        window.location.reload()
    }

    return (
        <div className="initial-form">
            <div className="wrapper">
                <div className="main-content">
                    <h1 className="main-content__title">Login</h1>
                    <form className="info" onSubmit={handleSubmit}>
                        <ul className="info__form">
                            <li className={`info__list ${hasErrors ? 'error' : ''}`}>
                                <label className="info__label">Email:</label>
                                <input type="text" className="in-text" value={email} onChange={(e) => setEmail(e.target.value)} />
                            </li>
                            <li className={`info__list ${hasErrors ? 'error' : ''}`}>
                                <label className="info__label">Password:</label>
                                <input type="password" className="in-text" value={password} onChange={(e) => setPassword(e.target.value)} />
                            </li>
                        </ul>
                        <div className="btn-wrap">
                            <label className="initial-form__checkbox">
                                <input type="checkbox" name="remember-me" />
                                Remember me
                            </label>
                            <a href="/" className="btn btn--transparent">
                                <span>Forgot password</span>
                            </a>
                            <button type="submit" className="btn btn--green">
                                <span>Login</span>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}
