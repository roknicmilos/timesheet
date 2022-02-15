import { AuthContextProvider } from "../core/contexts/Auth.context";
import IndexPage from "../pages/IndexPage";
import Footer from "./Footer";
import Header from "./Header";

export default function App() {
    return (
        <AuthContextProvider>
            <div className="container">
                <Header />
                <IndexPage />
            </div>
            <Footer />
        </AuthContextProvider>
    );
}
