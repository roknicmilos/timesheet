import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AuthContextProvider } from "../core/contexts/Auth.context";
import IndexPage from "./pages/IndexPage";
import Footer from "./layout/Footer";
import Header from "./layout/Header";

export default function App() {
    return (
        <AuthContextProvider>
            <BrowserRouter>
                <div className="container">
                    <Header />
                    <Routes>
                        <Route path='/' element={<IndexPage />} />
                    </Routes>
                </div>
                <Footer />
            </BrowserRouter>
        </AuthContextProvider>
    );
}
