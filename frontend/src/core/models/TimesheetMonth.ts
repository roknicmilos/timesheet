import TimesheetWeek from "./TimesheetWeek";

export default interface TimesheetMonth {
    month: number;
    year: number;
    label: string;
    weeks: TimesheetWeek[];
    calculateTotalHours(): number;
}
