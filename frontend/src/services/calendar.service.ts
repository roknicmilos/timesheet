import TimesheetDay from './../models/TimesheetDay'
import TimesheetWeek from './../models/TimesheetWeek'

function getCalendarWeeks(month: number, year: number): Array<TimesheetWeek> {
    const calendarWeeks = []
    
    const firstCalendarDay = getFirstCalendarDay(month, year)
    const lastCalendarDay = getLastCalendarDay(month, year)
    
    let timesheetWeek = {order: 1, days: []} as TimesheetWeek
    const currentDate = firstCalendarDay
    while (currentDate <= lastCalendarDay) {
        if (currentDate.getDay() === 1 && timesheetWeek.order) {
            timesheetWeek = {order: timesheetWeek.order + 1, days: []} as TimesheetWeek
        }
        const isDisabled = month === currentDate.getMonth() ? false : true
        const timesheetDay = { date: new Date(currentDate), isDisabled, hours: 7.5 } as TimesheetDay
        timesheetWeek.days.push(timesheetDay)
        currentDate.setDate(currentDate.getDate() + 1)
        if (currentDate.getDay() === 0) {
            calendarWeeks.push(timesheetWeek)
        }
    }

    return calendarWeeks
}

function getFirstCalendarDay(month: number, year: number): Date {
    const firstDayOfTheMonth = new Date(year, month, 1)
    if (firstDayOfTheMonth.getDay() === 1) return firstDayOfTheMonth
    return getMonday(firstDayOfTheMonth)
}

function getLastCalendarDay(month: number, year: number): Date {
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

export {getCalendarWeeks}
