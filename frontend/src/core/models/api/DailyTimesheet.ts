import TimesheetReport from "./TimesheetReport";

export default interface DailyTimesheet {
    id: number;
    time_sheet_reports: TimesheetReport[];
    created: string;
    modified: string;
    date: string;
    employee: number;
}
