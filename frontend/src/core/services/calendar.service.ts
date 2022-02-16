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
                week.days.forEach(day => {
                    if (!day.isDisabled) {
                        totalHours += day.hours
                    }
                })
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

    const dailyTimesheetChunks = splitArray(dailyTimesheets, 7)
    return dailyTimesheetChunks.map((dailyTimesheets, index) => {
        return {
            order: index + 1,
            days: createTimesheetDays(dailyTimesheets, month)
        }
    })
}

function createTimesheetDays(dailyTimesheets: DailyTimesheet[], targetMonth: number): TimesheetDay[] {
    return dailyTimesheets.map(dailyTimesheet => {
        const dailyTimesheetDate = new Date(dailyTimesheet.date)
        const timesheetDay: TimesheetDay = {
            date: dailyTimesheetDate,
            isDisabled: targetMonth !== dailyTimesheetDate.getMonth(),
            hours: calculateTotalHours(dailyTimesheet.time_sheet_reports)
        }
        return timesheetDay
    })
}

function calculateTotalHours(timesheetReports: TimesheetReport[]): number {
    let totalHours = 0
    timesheetReports.forEach(timesheetReport => {
        totalHours += (timesheetReport.hours + timesheetReport.overtime_hours)
    })
    return totalHours
}

function splitArray(array: DailyTimesheet[], size: number): [][] {
    const arrayCopy = array.splice(0)
    const arrayChunks = [] as any

    while (arrayCopy.length) {
        arrayChunks.push(arrayCopy.splice(0, size))
    }

    return arrayChunks
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
