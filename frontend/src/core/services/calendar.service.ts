import TimesheetWeek from "../models/TimesheetWeek";
import TimesheetMonth from "../models/TimesheetMonth";
import DailyTimesheet from "../models/api/DailyTimesheet";
import TimesheetDay from "../models/TimesheetDay";
import TimesheetReport from "../models/api/TimesheetReport";
import { getDailyTimesheets } from "./dailyTimesheet.service";
import { datesRange, getMonday, getSunday } from "./datetime.service";

export async function getTimesheetMonth(userId: number, month: number, year: number): Promise<TimesheetMonth> {
    const timesheetWeeks = await createTimesheetWeeks(userId, month, year);

    const firstDayOfTheMonth = new Date(year, month, 1);

    return {
        month: month,
        year: year,
        label: firstDayOfTheMonth.toLocaleString("default", { month: "long" }),
        weeks: timesheetWeeks,
        calculateTotalHours: function () {
            let totalHours = 0;
            timesheetWeeks?.forEach((week) => {
                week.days.forEach((day) => (totalHours += day.hours));
            });
            return totalHours;
        },
    };
}

async function createTimesheetWeeks(userId: number, month: number, year: number): Promise<Array<TimesheetWeek>> {
    const firstCalendarDay = getFirstCalendarDay(month, year);
    const lastCalendarDay = getLastCalendarDay(month, year);

    const dailyTimesheets = await getDailyTimesheets(userId, firstCalendarDay, lastCalendarDay);

    if (!dailyTimesheets) return [];

    let currentWeekMonday = firstCalendarDay;
    let currentWeekOrder = 1;

    const timesheetWeeks = [];
    while (currentWeekMonday < lastCalendarDay) {
        const timesheetWeek = createTimesheetWeek(currentWeekMonday, dailyTimesheets, currentWeekOrder, month);
        timesheetWeeks.push(timesheetWeek);
        currentWeekMonday.setDate(currentWeekMonday.getDate() + 7);
        currentWeekOrder++;
    }

    return timesheetWeeks;
}

function createTimesheetWeek(
    weekMonday: Date,
    dailyTimesheets: DailyTimesheet[],
    order: number,
    month: number
): TimesheetWeek {
    const timesheetWeek: TimesheetWeek = {
        order,
        previousMonthDays: [],
        days: [],
        nextMonthDays: [],
    };

    const monday = new Date(weekMonday);
    const sunday = new Date(weekMonday);
    sunday.setDate(monday.getDate() + 6);

    const timesheetDays = createTimesheetDays(monday, sunday, dailyTimesheets);
    timesheetDays.forEach((timesheetDay) => {
        if (isPreviousMonthDate(timesheetDay.date, month)) {
            timesheetWeek.previousMonthDays.push(timesheetDay);
        } else if (isNextMonthDate(timesheetDay.date, month)) {
            timesheetWeek.nextMonthDays.push(timesheetDay);
        } else {
            timesheetWeek.days.push(timesheetDay);
        }
    });

    return timesheetWeek;
}

/**
 * Function expects a date that has a month equal to or next to (- or + 1) the target month
 *
 * @param date
 * @param targetMonth
 * @returns
 */
function isPreviousMonthDate(date: Date, targetMonth: number): boolean {
    // target month is January and the date is from December:
    if (targetMonth === 0 && date.getMonth() === 11) return true;

    // target month is December and the date is from January:
    if (targetMonth === 11 && date.getMonth() === 0) return false;

    return date.getMonth() < targetMonth;
}

/**
 * Function expects a date that has a month equal to or next to (- or + 1) the target month
 *
 * @param date
 * @param targetMonth
 * @returns
 */
function isNextMonthDate(date: Date, targetMonth: number): boolean {
    // target month is December and the date is from January:
    if (targetMonth === 11 && date.getMonth() === 0) return true;

    // target month is January and the date is from December:
    if (targetMonth === 0 && date.getMonth() === 11) return false;

    return date.getMonth() > targetMonth;
}

function createTimesheetDays(
    from: Date,
    until: Date,
    dailyTimesheets: Array<DailyTimesheet | undefined>
): TimesheetDay[] {
    return datesRange(from, until).map((date) => {
        const dailyTimesheet = dailyTimesheets.find((dailyTimesheet) => {
            if (!dailyTimesheet) return false;
            const dailyTimesheetDate = new Date(dailyTimesheet.date);
            return dailyTimesheetDate.toDateString() === date.toDateString();
        });
        return {
            dailyTimesheetID: dailyTimesheet?.id,
            date,
            hours: dailyTimesheet ? calculateTimesheetDayTotalHours(dailyTimesheet.time_sheet_reports) : 0,
        };
    });
}

export function calculateTimesheetDayTotalHours(timesheetReports: TimesheetReport[]): number {
    let totalHours = 0;
    timesheetReports.forEach((timesheetReport) => {
        totalHours += timesheetReport.hours + timesheetReport.overtime_hours;
    });
    return totalHours;
}

function getFirstCalendarDay(month: number, year: number): Date {
    const firstDayOfTheMonth = new Date(year, month, 1);
    if (firstDayOfTheMonth.getDay() === 1) return firstDayOfTheMonth;
    return getMonday(firstDayOfTheMonth);
}

function getLastCalendarDay(month: number, year: number): Date {
    const monthDayCount = new Date(year, month + 1, 0).getDate();
    const lastDayOfTheMonth = new Date(year, month, monthDayCount);
    if (lastDayOfTheMonth.getDay() === 0) return lastDayOfTheMonth;
    return getSunday(lastDayOfTheMonth);
}
