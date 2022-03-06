import { Collapse } from "react-collapse";
import Client from "../../../core/models/api/Client";
import ClientForm from "./ClientForm";

interface ClientAccordionProps {
    client: Client;
    isSelected: boolean;
    onToggleAccordion(): void;
    onUpdateClient(): void;
    onDeleteClient?(): void;
}

export default function ClientAccordion({
    client,
    isSelected,
    onToggleAccordion,
    onUpdateClient,
    onDeleteClient,
}: ClientAccordionProps) {
    return (
        <div className="accordion">
            <div className="accordion__intro" onClick={onToggleAccordion}>
                <h4 className="accordion__title">{client.name}</h4>
            </div>
            <Collapse isOpened={isSelected}>
                <ClientForm client={client} onSubmit={onUpdateClient} onDelete={onDeleteClient} />
            </Collapse>
        </div>
    );
}
