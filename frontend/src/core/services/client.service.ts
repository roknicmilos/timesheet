import Client from "../models/Client";
import timesheetApiClient from "../timesheet.api";

export async function getClientsAvailableAlphabetLetters(): Promise<string[]> {
    try {
        const response = await timesheetApiClient.get("/clients/available-alphabet-letters/?fields=name");
        return response.data.name;
    } catch (error) {
        console.error("Error while fetching clients available alphabet letters\n", error);
        return [];
    }
}

export async function getClients(): Promise<Client[]> {
    try {
        const response = await timesheetApiClient.get("/clients");
        return response.data;
    } catch (error) {
        console.error("Error while fetching clients\n", error);
        return [];
    }
}
