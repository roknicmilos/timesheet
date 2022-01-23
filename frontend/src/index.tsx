import React from 'react';
import ReactDOM from 'react-dom';
import Footer from './Footer';
import Header from './Header';
import './index.css';
import TimesheetPage from './pages/TimesheetPage';

class App extends React.Component {
    render() {
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
}

// ========================================

ReactDOM.render(
    <App />,
    document.getElementById('root')
);
