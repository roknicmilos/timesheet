import { useEffect, useState } from "react"
import CalendarWeek from "./CalendarWeek"
import TimesheetDay from "../../models/TimesheetDay"

const getCalendarWeeks = function (month: number, year: number): Array<Array<TimesheetDay>> {
    const firstCalendarDay = getFirstCalendarDay(month, year)
    const lastCalendarDay = getLastCalendarDay(month, year)
    const calendarWeeks = []
    let weekDays = []
    const currentDate = firstCalendarDay
    while (currentDate <= lastCalendarDay) {
        if (currentDate.getDay() === 1 && weekDays.length) {
            weekDays = []
        }
        const isDisabled = month === currentDate.getMonth() ? false : true
        const timesheetDay = { date: new Date(currentDate), isDisabled, hours: 7.5 } as TimesheetDay
        console.log(timesheetDay)
        weekDays.push(timesheetDay)
        currentDate.setDate(currentDate.getDate() + 1)
        if (currentDate.getDay() === 0) {
            calendarWeeks.push(weekDays)
        }
    }
    return calendarWeeks

}

const getFirstCalendarDay = function (month: number, year: number): Date {
    const firstDayOfTheMonth = new Date(year, month, 1)
    if (firstDayOfTheMonth.getDay() === 1) return firstDayOfTheMonth
    return getMonday(firstDayOfTheMonth)
}

const getLastCalendarDay = function (month: number, year: number): Date {
    const monthDayCount = new Date(year, month + 1, 0).getDate()
    const lastDayOfTheMonth = new Date(year, month, monthDayCount)
    if (lastDayOfTheMonth.getDay() === 0) return lastDayOfTheMonth
    return getSunday(lastDayOfTheMonth)
}

function getMonday(date: Date): Date {
    const day = date.getDay();
    const diff = date.getDate() - day + (day === 0 ? -6 : 1);
    return new Date(date.setDate(diff));
}

function getSunday(date: Date): Date {
    const day = date.getDay();
    const diff = date.getDate() - day + (day === 0 ? 0 : 7);
    return new Date(date.setDate(diff));
}

export default function TimesheetPage() {
    const [calendarWeeks, setCalendarWeeks] = useState<Array<Array<TimesheetDay>>>([])

    useEffect(() => {
        const now = new Date()
        const weeks = getCalendarWeeks(now.getMonth(), now.getFullYear())
        setCalendarWeeks(weeks)
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
                        {calendarWeeks.map(weekDays => <CalendarWeek timesheetDays={weekDays} />)}
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
