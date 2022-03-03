import Client from "../models/api/Client";
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

export interface ClientsFilters {
    name_starts_with?: string;
    name_contains: string;
}

export async function getClients(page: number, filters?: ClientsFilters): Promise<ClientsListResponse> {
    const urlParams = prepareClientsURLParameters(page, filters);
    try {
        const response = await timesheetApiClient.get(`/clients?${urlParams}`);
        return {
            clients: response.data.items,
            totalPages: response.data.pagination.total_pages,
        };
    } catch (error) {
        console.error("Error while fetching clients\n", error);
        return {} as ClientsListResponse;
    }
}

function prepareClientsURLParameters(page: number, filters?: ClientsFilters): string {
    let urlParams = `page=${page}&ipp=5`;
    if (filters) {
        urlParams += "&";
        urlParams += Object.entries(filters)
            .filter(([_, value]) => value !== "")
            .map(([key, value]) => `${key}=${value}`)
            .join("&");
    }
    return urlParams;
}

export async function updateClient(client: Client): Promise<Client> {
    try {
        const response = await timesheetApiClient.put(`/clients/${client.id}/`, client);
        return response.data;
    } catch (error) {
        console.error("Error while updating client\n", error);
        return {} as Client;
    }
}
