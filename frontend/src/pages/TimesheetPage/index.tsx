import { useEffect, useState } from "react"
import CalendarWeek from "./CalendarWeek"
import TimesheetWeek from "../../models/TimesheetWeek"
import { getCalendarWeeks } from "../../services/calendar.service"


export default function TimesheetPage() {
    const [timesheetWeeks, setTimesheetWeek] = useState<TimesheetWeek[]>([])

    useEffect(() => {
        const now = new Date()
        const weeks = getCalendarWeeks(now.getMonth(), now.getFullYear())
        setTimesheetWeek(weeks)
    }, [])

    return (
        <section className="main-content">
            <h2 className="main-content__title">Timesheet</h2>
            <div className="table-navigation">
                <a href="/" className="table-navigation__prev"><span>previous month</span></a>
                <span className="table-navigation__center">September, 2021</span>
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
                        {timesheetWeeks.map(timesheetWeek => <CalendarWeek key={timesheetWeek.order} timesheetWeek={timesheetWeek} />)}
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
    )
}
