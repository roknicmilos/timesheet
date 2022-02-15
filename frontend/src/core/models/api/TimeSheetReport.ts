export default interface TimeSheetReport {
    id: number;
    created: Date;
    modified: Date;
    hours: number;
    overtime_hours: number;
    description: string;
    daily_time_sheet: number;
    project: number;
    category: number;
}
