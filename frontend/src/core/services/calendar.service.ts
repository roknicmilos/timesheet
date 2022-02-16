import TimesheetWeek from '../models/TimesheetWeek'
import TimesheetMonth from '../models/TimesheetMonth'
import DailyTimesheet from '../models/api/DailyTimesheet'
import TimesheetDay from '../models/TimesheetDay'
import TimesheetReport from '../models/api/TimesheetReport'
import { getDailyTimesheets } from './dailyTimesheet.service'

export async function getTimesheetMonth(userId: number, month: number, year: number): Promise<TimesheetMonth> {
    const firstDayOfTheMonth = new Date(year, month, 1)

    const timesheetWeeks = await createTimesheetWeeks(userId, month, year)

    return {
        month: month,
        year: year,
        label: firstDayOfTheMonth.toLocaleString('default', { month: 'long' }),
        weeks: timesheetWeeks,
        calculateTotalHours: function () {
            let totalHours = 0
            timesheetWeeks?.forEach(week => {
                week.days.forEach(day => totalHours += day.hours)
            });
            return totalHours
        }
    }
}

async function createTimesheetWeeks(userId: number, month: number, year: number): Promise<Array<TimesheetWeek>> {
    const firstCalendarDay = getFirstCalendarDay(month, year)
    const lastCalendarDay = getLastCalendarDay(month, year)

    const dailyTimesheets = await getDailyTimesheets(userId, firstCalendarDay, lastCalendarDay)

    if (!dailyTimesheets) return []

    let currentWeekMonday = firstCalendarDay
    let currentWeekOrder = 1

    const timesheetWeeks = []
    while (currentWeekMonday < lastCalendarDay) {
        const timesheetWeek = createTimesheetWeek(currentWeekMonday, dailyTimesheets, currentWeekOrder, month)
        timesheetWeeks.push(timesheetWeek)
        currentWeekMonday.setDate(currentWeekMonday.getDate() + 7)
        currentWeekOrder++
    }

    return timesheetWeeks
}

function createTimesheetWeek(weekMonday: Date, dailyTimesheets: DailyTimesheet[], order: number, month: number): TimesheetWeek {
    const monday = new Date(weekMonday)
    const sunday = new Date(weekMonday)
    sunday.setDate(monday.getDate() + 6)

    const timesheetDays = createTimesheetDays(monday, sunday, dailyTimesheets)
    const timesheetWeek: TimesheetWeek = {
        order,
        previousMonthDays: [],
        days: [],
        nextMonthDays: [],
    }
    timesheetDays.forEach(timesheetDay => {
        if (timesheetDay.date.getMonth() < month) {
            timesheetWeek.previousMonthDays.push(timesheetDay)
        } else if (timesheetDay.date.getMonth() > month) {
            timesheetWeek.nextMonthDays.push(timesheetDay)
        } else {
            timesheetWeek.days.push(timesheetDay)
        }
    })

    return timesheetWeek
}

function createTimesheetDays(from: Date, until: Date, dailyTimesheets: Array<DailyTimesheet|undefined>): TimesheetDay[] {
    return datesRange(from, until).map(date => {
        const dailyTimesheet = dailyTimesheets.find(dailyTimesheet => {
            if (!dailyTimesheet) return false
            const dailyTimesheetDate = new Date(dailyTimesheet.date)
            return dailyTimesheetDate.toDateString() === date.toDateString()
        })
        return {
            date,
            hours: dailyTimesheet ? calculateTotalHours(dailyTimesheet.time_sheet_reports) : 0
        }
    })
}

function datesRange(start: Date, end: Date): Date[] {
    const dates = []
    const currentDate = start
    while (currentDate <= end) {
        dates.push(new Date(currentDate))
        currentDate.setDate(currentDate.getDate() + 1)
    }
    return dates
}

function calculateTotalHours(timesheetReports: TimesheetReport[]): number {
    let totalHours = 0
    timesheetReports.forEach(timesheetReport => {
        totalHours += (timesheetReport.hours + timesheetReport.overtime_hours)
    })
    return totalHours
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
