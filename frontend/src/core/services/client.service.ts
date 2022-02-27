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

interface ClientsListResponse {
    clients: Client[];
    totalPages: number;
}

export async function getClients(page: number, itemsPerPage: number = 5): Promise<ClientsListResponse> {
    try {
        const response = await timesheetApiClient.get(`/clients?page=${page}&ipp=${itemsPerPage}`);
        return {
            clients: response.data.items,
            totalPages: response.data.pagination.total_pages,
        };
    } catch (error) {
        console.error("Error while fetching clients\n", error);
        return {} as ClientsListResponse;
    }
}
