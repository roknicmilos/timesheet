import React from 'react';
import ReactDOM from 'react-dom';
import Footer from './Footer';
import Header from './Header';
import './index.css';

class App extends React.Component {
    render() {
        return (
            <>
                <div className="container">
                    <Header />
                    <div className="wrapper">
                        <section className="main-content">
                            <h2 className="main-content__title">Timesheet</h2>
                            <div className="table-navigation">
                                <a href="javascript:;" className="table-navigation__prev"><span>previous month</span></a>
                                <span className="table-navigation__center">September, 2021</span>
                                <a href="javascript:;" className="table-navigation__next"><span>next month</span></a>
                            </div>
                            <div className="table-wrapper">
                                <table className="month-table">
                                    <thead>
                                        <tr>
                                            <th className="month-table__days">Monday</th>
                                            <th className="month-table__days">Tuesday</th>
                                            <th className="month-table__days">Wednesday</th>
                                            <th className="month-table__days">Thursday</th>
                                            <th className="month-table__days">Friday</th>
                                            <th className="month-table__days">Saturday</th>
                                            <th className="month-table__days">Sunday</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr >
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>30</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day"><span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>31</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>1</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>2</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>3</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>4</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>5</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>6</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>7</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>8</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>9</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>10</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>11</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>12</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>13</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>14</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>15</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>16</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>17</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>18</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>19</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>20</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>21</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>22</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>23</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>24</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>25</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>26</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>27</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular">
                                                <div className="month-table__date">
                                                    <span>28</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>7.5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="negative">
                                                <div className="month-table__date">
                                                    <span>29</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>5</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="current- month-table__day">
                                                <div className="month-table__date">
                                                    <span>30</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>1</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>2</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>3</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>4</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>5</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>6</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>7</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>8</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>9</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                            <td className="month-table__regular month-table__regular--disabled">
                                                <div className="month-table__date">
                                                    <span>10</span>
                                                    <i></i>
                                                </div>
                                                <div className="month-table__hours">
                                                    <a href="./days.html" className="month-table__day">
                                                        <span>Hours: </span><span>0</span>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div className="table-navigation">
                                <div className="table-navigation__next">
                                    <span className="table-navigation__text">Total:</span>
                                    <span>155</span>
                                </div>
                            </div>
                        </section>
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
