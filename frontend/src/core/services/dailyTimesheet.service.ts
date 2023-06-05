import DailyTimesheet from "../models/api/DailyTimesheet";
import timesheetApiClient from "../timesheet.api";
import { getDateIsoFormat } from "./datetime.service";

interface DailyTimesheetListResponse {
    dailyTimesheets: DailyTimesheet[];
    totalPages: number;
}

export async function getDailyTimesheets(
    userId: number,
    from: Date,
    until: Date
): Promise<DailyTimesheetListResponse> {
    let url = `/users/${userId}/daily-time-sheets/?from_date=${getDateIsoFormat(from)}&until_date=${getDateIsoFormat(until)}`;
    try {
        const response = await timesheetApiClient.get(url);
        return {
            dailyTimesheets: response.data.items,
            totalPages: response.data.pagination.total_pages,
        };
    } catch (error) {
        console.error("Error while fetching user's Daily Time Sheets\n", error);
        return {} as DailyTimesheetListResponse;
    }
}

export async function getDailyTimesheetByDate(userId: number, date: Date): Promise<DailyTimesheet | undefined> {
    let url = `/users/${userId}/daily-time-sheets/?date=${getDateIsoFormat(date)}`;
    try {
        const response = await timesheetApiClient.get(url);
        return response.data ? response.data[0] : undefined;
    } catch (error) {
        console.error("Error while fetching user's Daily Time Sheet by date\n", error);
    }
}
