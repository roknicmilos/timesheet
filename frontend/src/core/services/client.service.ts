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

export interface ClientData {
    name: string;
    street: string;
    city: string;
    zip_code: number;
    country: string;
}

export async function updateClient(clientId: number, clientData: ClientData): Promise<Client> {
    try {
        const response = await timesheetApiClient.put(`/clients/${clientId}/`, clientData);
        return response.data;
    } catch (error) {
        console.error("Error while updating a client\n", error);
        return {} as Client;
    }
}

export async function createClient(clientData: ClientData): Promise<Client> {
    try {
        const response = await timesheetApiClient.post("/clients/", clientData);
        return response.data;
    } catch (error) {
        console.error("Error while creating a new client\n", error);
        return {} as Client;
    }
}

export async function deleteClient(clientId: number): Promise<void> {
    try {
        await timesheetApiClient.delete(`/clients/${clientId}`);
    } catch (error) {
        console.error("Error while deleting a client\n", error);
    }
}
