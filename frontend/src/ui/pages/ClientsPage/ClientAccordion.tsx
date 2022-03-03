import { Collapse } from "react-collapse";
import Client from "../../../core/models/api/Client";
import ClientForm from "./ClientForm";

interface ClientAccordionProps {
    client: Client;
    isSelected: boolean;
    onClick(): void;
    onUpdateClient(updatedClient: Client): void;
}

export default function ClientAccordion({ client, isSelected, onClick, onUpdateClient }: ClientAccordionProps) {
    return (
        <div className="accordion">
            <div className="accordion__intro" onClick={onClick}>
                <h4 className="accordion__title">{client.name}</h4>
            </div>
            <Collapse isOpened={isSelected}>
                <ClientForm client={client} onSubmit={onUpdateClient} />
            </Collapse>
        </div>
    );
}
