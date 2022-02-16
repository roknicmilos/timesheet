import { useEffect, useState } from "react"
import CalendarWeek from "./CalendarWeek"
import TimesheetMonth from "../../../core/models/TimesheetMonth"
import { getTimesheetMonth } from "./../../../core/services/calendar.service"
import { useAuth } from "../../../core/contexts/Auth.context"


export default function TimesheetPage() {
    const [timesheetMonth, setTimesheetWeek] = useState<TimesheetMonth>()
    const { user } = useAuth()

    useEffect(() => {
        if (!timesheetMonth && user) {
            const now = new Date()
            getTimesheetMonth(user.id, now.getMonth(), now.getFullYear()).then(timesheetMonth => setTimesheetWeek(timesheetMonth))
        }
    }, [user, timesheetMonth, setTimesheetWeek])

    const PageContent = function () {
        return (
            <section className="main-content">
                <h2 className="main-content__title">Timesheet</h2>
                <div className="table-navigation">
                    <a href="/" className="table-navigation__prev"><span>previous month</span></a>
                    <span className="table-navigation__center">{timesheetMonth?.label}, {timesheetMonth?.year}</span>
                    <a href="/" className="table-navigation__next"><span>next month</span></a>
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
                            {timesheetMonth?.weeks?.map(timesheetWeek => <CalendarWeek key={timesheetWeek.order} timesheetWeek={timesheetWeek} />)}
                        </tbody>
                    </table>
                </div>
                <div className="table-navigation">
                    <div className="table-navigation__next">
                        <span className="table-navigation__text">Total:</span>
                        <span>{timesheetMonth?.calculateTotalHours()}</span>
                    </div>
                </div>
            </section>
        )
    }

    return timesheetMonth ? <PageContent /> : <div>LOADING</div>
}
