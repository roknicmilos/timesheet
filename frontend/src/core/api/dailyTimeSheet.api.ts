import timesheetApiClient from ".";
import DailyTimeSheet from "../models/api/DailyTimeSheet"

export async function getDailyTimeSheets(userId: number, from: Date, until: Date): Promise<DailyTimeSheet[] | undefined> {
    let url = `/users/${userId}/daily-time-sheets/?from=${getDateIsoFormat(from)}&until=${getDateIsoFormat(until)}`
    try {
        const response = await timesheetApiClient.get(url);
        return response.data
    } catch (error) {
        console.error('Error while fetching user\'s Daily Time Sheets\n', error);
    }
}

function getDateIsoFormat(date: Date): string {
    return date.toISOString().split('T')[0]
}
