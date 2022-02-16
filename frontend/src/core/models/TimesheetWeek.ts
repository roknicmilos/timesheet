import TimesheetDay from "./TimesheetDay";

export default interface TimesheetWeek {
    order: number;
    days: TimesheetDay[];
    previousMonthDays: TimesheetDay[];
    nextMonthDays: TimesheetDay[];
}
