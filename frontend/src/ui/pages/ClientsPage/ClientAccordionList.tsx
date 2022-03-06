import Client from "../../../core/models/api/Client";
import ClientAccordion from "./ClientAccordion";

interface ClientAccordionListProps {
    clients: Client[];
    selectedClientId: number;
    onToggleAccordion(clientId: number): void;
    onUpdateClient(): void;
    onDeleteClient?(): void;
}

export default function ClientAccordionList({
    clients,
    selectedClientId,
    onToggleAccordion,
    onUpdateClient,
    onDeleteClient,
}: ClientAccordionListProps) {
    return (
        <>
            {clients.map((client) => {
                return (
                    <ClientAccordion
                        key={client.id}
                        client={client}
                        isSelected={client.id === selectedClientId}
                        onToggleAccordion={() => onToggleAccordion(client.id)}
                        onUpdateClient={onUpdateClient}
                        onDeleteClient={onDeleteClient}
                    />
                );
            })}
        </>
    );
}
