import TimesheetWeek from './../models/TimesheetWeek'
import TimesheetMonth from './../models/TimesheetMonth'

function createTimesheetMonth(month: number, year: number): TimesheetMonth {
    const firstDayOfTheMonth = new Date(year, month, 1)
    let timesheetMonth: TimesheetMonth
    timesheetMonth = {
        month: month, 
        year:year, 
        label: firstDayOfTheMonth.toLocaleString('default', {month: 'long'}),
        weeks: createTimesheetWeeks(month, year),
        calculateTotalHours: function (){
            let totalHours = 0
            this.weeks.forEach(week => {
                week.days.forEach(day => {
                    if (!day.isDisabled) {
                        totalHours += day.hours
                    }
                })
            });
            return totalHours
        }
    }
    return timesheetMonth
}

function createTimesheetWeeks(month: number, year: number): Array<TimesheetWeek> {
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
        timesheetWeek.days.push({date: new Date(currentDate), isDisabled, hours: 1 })
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

export { createTimesheetMonth }
