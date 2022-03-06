import Client from "../../../core/models/api/Client";
import ClientAccordion from "./ClientAccordion";

interface CleintAccordionList {
    clients: Client[];
    selectedClientId: number;
    onSelectClient(clientId: number): void;
    onUpdateClient(updatedClient: Client): void;
}

export default function CleintAccordionList({
    clients,
    selectedClientId,
    onSelectClient,
    onUpdateClient,
}: CleintAccordionList) {
    return (
        <>
            {clients.map((client) => {
                return (
                    <ClientAccordion
                        key={client.id}
                        client={client}
                        isSelected={client.id === selectedClientId}
                        onClick={() => onSelectClient(client.id)}
                        onUpdateClient={onUpdateClient}
                    />
                );
            })}
        </>
    );
}
