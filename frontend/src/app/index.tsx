import TimesheetPage from "../pages/TimesheetPage";
import Footer from "./Footer";
import Header from "./Header";

export default function App() {
    return (
        <>
            <div className="container">
                <Header />
                <div className="wrapper">
                    <TimesheetPage />
                </div>
            </div>
            <Footer />
        </>
    );    
}
