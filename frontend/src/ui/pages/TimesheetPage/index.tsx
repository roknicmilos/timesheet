import { useCallback, useEffect, useState } from "react"
import CalendarWeek from "./CalendarWeek"
import TimesheetMonth from "../../../core/models/TimesheetMonth"
import { getTimesheetMonth } from "./../../../core/services/calendar.service"
import { useAuth } from "../../../core/contexts/Auth.context"


export default function TimesheetPage() {
    const [currentMonth, setCurrentMonth] = useState<number>(() => {
        const now = new Date()
        return now.getMonth()
    })
    const [currentYear, setCurrentYear] = useState<number>(() => {
        const now = new Date()
        return now.getFullYear()
    })
    const [timesheetMonth, setTimesheetMonth] = useState<TimesheetMonth>()
    const { user } = useAuth()

    useEffect(() => {
        if (timesheetMonth || !user) return

        getTimesheetMonth(user.id, currentMonth, currentYear)
            .then(timesheetMonth => setTimesheetMonth(timesheetMonth))

    }, [user, timesheetMonth, setTimesheetMonth, currentMonth, currentYear])

    const handleNextMonth = useCallback(() => {
        const nextMonth = currentMonth < 11 ? currentMonth + 1 : 0
        const nextYear = nextMonth === 0 ? currentYear + 1 : currentYear

        console.log(nextMonth, nextYear)

        setCurrentMonth(nextMonth)
        setCurrentYear(nextYear)

        getTimesheetMonth(user!.id, nextMonth, nextYear)
            .then(timesheetMonth => setTimesheetMonth(timesheetMonth))

    }, [currentMonth, currentYear, timesheetMonth])

    const handlePreviousMonth = useCallback(() => {
        const previousMonth = currentMonth > 0 ? currentMonth - 1 : 11
        const previousYear = previousMonth === 11 ? currentYear - 1 : currentYear

        console.log(previousMonth, previousYear)

        setCurrentMonth(previousMonth)
        setCurrentYear(previousYear)

        getTimesheetMonth(user!.id, previousMonth, previousYear)
            .then(timesheetMonth => setTimesheetMonth(timesheetMonth))

    }, [currentMonth, currentYear, timesheetMonth])

    const PageContent = function () {
        return (
            <section className="main-content">
                <h2 className="main-content__title">Timesheet</h2>
                <div className="table-navigation">
                    <p className="table-navigation__prev" onClick={handlePreviousMonth}><span>previous month</span></p>
                    <span className="table-navigation__center">{timesheetMonth?.label}, {timesheetMonth?.year}</span>
                    <p className="table-navigation__next" onClick={handleNextMonth}><span>next month</span></p>
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
