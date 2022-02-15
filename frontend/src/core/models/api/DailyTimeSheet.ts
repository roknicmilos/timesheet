import TimeSheetReport from "./TimeSheetReport";

export default interface DailyTimeSheet {
    id: number;
    time_sheet_reports: TimeSheetReport[];
    created: Date;
    modified: Date;
    date: Date;
    employee: number;
}
