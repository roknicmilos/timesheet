import TimeSheetReport from "./TimeSheetReport";

export default interface DailyTimeSheet {
    id: number;
    time_sheet_reports: TimeSheetReport[];
    created: string;
    modified: string;
    date: string;
    employee: number;
}
