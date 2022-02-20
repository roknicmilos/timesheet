import { BrowserRouter, Route, Routes, } from "react-router-dom";
import { AuthContextProvider } from "../core/contexts/Auth.context";
import LoginPage from "./pages/LoginPage";
import TimesheetPage from "./pages/TimesheetPage"
import Footer from "./layout/Footer";
import Header from "./layout/Header";

export default function App() {
    return (
        <AuthContextProvider>
            <BrowserRouter>
                <div className="container">
                    <Header />
                    <div className="wrapper">
                        <Routes>
                            <Route path="/" element={<TimesheetPage />} />
                            <Route path="/login" element={<LoginPage />} />
                        </Routes>
                    </div>
                </div>
                <Footer />
            </BrowserRouter>
        </AuthContextProvider>
    );
}
