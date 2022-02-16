import TimesheetWeek from '../models/TimesheetWeek'
import TimesheetMonth from '../models/TimesheetMonth'
import { getDailyTimeSheets } from '../api/dailyTimeSheet.api'
import DailyTimeSheet from '../models/api/DailyTimeSheet'
import TimesheetDay from '../models/TimesheetDay'
import TimeSheetReport from '../models/api/TimeSheetReport'

export async function getTimesheetMonth(userId: number, month: number, year: number): Promise<TimesheetMonth> {
    const firstDayOfTheMonth = new Date(year, month, 1)

    const timeSheetWeeks = await createTimesheetWeeks(userId, month, year)

    const timesheetMonth: TimesheetMonth = {
        month: month,
        year: year,
        label: firstDayOfTheMonth.toLocaleString('default', { month: 'long' }),
        weeks: timeSheetWeeks,
        calculateTotalHours: function () {
            let totalHours = 0
            this.weeks?.forEach(week => {
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

async function createTimesheetWeeks(userId: number, month: number, year: number): Promise<Array<TimesheetWeek>> {
    const firstCalendarDay = getFirstCalendarDay(month, year)
    const lastCalendarDay = getLastCalendarDay(month, year)

    const dailyTimeSheets = await getDailyTimeSheets(userId, firstCalendarDay, lastCalendarDay)
    if (!dailyTimeSheets) return []

    const dailyTimeSheetChunks = splitArray(dailyTimeSheets, 7)
    return dailyTimeSheetChunks.map((dailyTimeSheets, index) => {
        return {
            order: index + 1,
            days: createTimesheetDays(dailyTimeSheets, month)
        }
    })
}

function createTimesheetDays(dailyTimeSheets: DailyTimeSheet[], targetMonth: number): TimesheetDay[] {
    return dailyTimeSheets.map(dailyTimeSheet => {
        const dailyTimeSheetDate = new Date(dailyTimeSheet.date)
        const timesheetDay: TimesheetDay = {
            date: dailyTimeSheetDate,
            isDisabled: targetMonth === dailyTimeSheetDate.getMonth() ? false : true,
            hours: calculateTotalHours(dailyTimeSheet.time_sheet_reports)
        }
        return timesheetDay
    })
}

function calculateTotalHours(timesheetReports: TimeSheetReport[]): number {
    let totalHours = 0
    timesheetReports.forEach(timesheetReport => {
        totalHours += (timesheetReport.hours + timesheetReport.overtime_hours)
    })
    return totalHours
}

function splitArray(array: DailyTimeSheet[], size: number): [][] {
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
