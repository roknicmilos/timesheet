import DailyTimesheet from "../models/api/DailyTimesheet";
import timesheetApiClient from "../timesheet.api";
import { getDateIsoFormat } from "./datetime.service";

export async function getDailyTimesheets(
    userId: number,
    from: Date,
    until: Date
): Promise<DailyTimesheet[] | undefined> {
    let url = `/users/${userId}/daily-time-sheets/?from_date=${getDateIsoFormat(from)}&until_date=${getDateIsoFormat(until)}`;
    try {
        const response = await timesheetApiClient.get(url);
        return response.data;
    } catch (error) {
        console.error("Error while fetching user's Daily Time Sheets\n", error);
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
