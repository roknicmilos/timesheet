export default function LoginPage() {

    // TODO: on submit, send login request to API, set user to local storage and navigate to index page

    return (
        <div className="initial-form">
            <div className="wrapper">
                <div className="main-content">
                    <h1 className="main-content__title">Login</h1>
                    <form className="info" action="index.html">
                        <ul className="info__form">
                            <li className="info__list">
                                <label className="info__label">Email:</label>
                                <input type="text" className="in-text" />
                            </li>
                            <li className="info__list">
                                <label className="report__label">Password:</label>
                                <input type="text" className="in-text" />
                            </li>
                        </ul>
                        <div className="btn-wrap">
                            <label className="initial-form__checkbox">
                                <input type="checkbox" name="remember-me" />
                                Remember me
                            </label>
                            <a href="./forgot-password.html" className="btn btn--transparent">
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
