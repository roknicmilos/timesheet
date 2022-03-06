import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AuthContextProvider } from "../core/contexts/Auth.context";
import Footer from "./layout/Footer";
import Header from "./layout/Header";
import LoginPage from "./pages/LoginPage";
import TimesheetPage from "./pages/TimesheetPage";
import ClientsPage from "./pages/ClientsPage";
import ProjectsPage from "./pages/ProjectsPage";
import CategoriesPage from "./pages/CategoriesPage";
import EmployeesPage from "./pages/EmployeesPage";
import ReportsPage from "./pages/ReportsPage";

export default function App() {
    return (
        <AuthContextProvider>
            <BrowserRouter>
                <div className="container">
                    <Header />
                    <div className="wrapper">
                        <Routes>
                            <Route path="/login" element={<LoginPage />} />

                            <Route path="/" element={<TimesheetPage />} />
                            <Route path="/clients" element={<ClientsPage />} />
                            <Route path="/projects" element={<ProjectsPage />} />
                            <Route path="/categories" element={<CategoriesPage />} />
                            <Route path="/employees" element={<EmployeesPage />} />
                            <Route path="/reports" element={<ReportsPage />} />
                        </Routes>
                    </div>
                    <Footer />
                </div>
            </BrowserRouter>
        </AuthContextProvider>
    );
}
