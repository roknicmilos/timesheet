import TimeheetDay from "./TimesheetDay";

export default interface TimeheetWeek {
    order: number;
    days: TimeheetDay[];
}
