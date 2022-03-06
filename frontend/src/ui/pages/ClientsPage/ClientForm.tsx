import { useCallback, useState } from "react";
import { useCountries } from "../../../core/contexts/Countries.context";
import Client from "../../../core/models/api/Client";
import { ClientData, createClient, deleteClient, updateClient } from "../../../core/services/client.service";
import InputField from "../../components/InputField";
import SelectField from "../../components/SelectField";

interface ClientFormProps {
    onSubmit(): void;
    client?: Client;
    onDelete?(): void;
    isInModal?: boolean;
}

export default function ClientForm({ onSubmit, client, onDelete, isInModal = false }: ClientFormProps) {
    const { countryNames } = useCountries();

    const [formData, setFormData] = useState<ClientData>(() => {
        if (client) return { ...client, zipCode: client.zip_code };
        return {
            name: "",
            street: "",
            city: "",
            zip_code: 0,
            country: "Serbia",
        };
    });

    const handleSubmit = useCallback(
        (event: any) => {
            event.preventDefault();
            if (client) {
                updateClient(client?.id, { ...formData }).then(() => onSubmit());
            } else {
                createClient(formData).then(() => onSubmit());
            }
        },
        [formData, onSubmit, client]
    );

    const handleChange = useCallback((event) => {
        setFormData((previousFormData) => ({ ...previousFormData, [event.target.name]: event.target.value }));
    }, []);

    const handleDelete = function () {
        deleteClient(client!.id).then(() => {
            if (onDelete) {
                onDelete();
            }
        });
    };

    return (
        <form
            className="accordion__content"
            onSubmit={handleSubmit}
            style={isInModal ? { border: "none", padding: 0 } : {}}
        >
            <div className="info">
                <div className="info__form">
                    <div className="info__wrapper">
                        <InputField label="Client name" name="name" value={formData.name} onChange={handleChange} />
                        <InputField label="Address" name="street" value={formData.street} onChange={handleChange} />
                        <InputField label="City" name="city" value={formData.city} onChange={handleChange} />
                        <InputField
                            label="Zip/Postal code"
                            name="zip_code"
                            value={formData.zip_code}
                            onChange={handleChange}
                        />
                        <SelectField
                            label="Country"
                            name="country"
                            value={formData.country}
                            onChange={handleChange}
                            options={countryNames}
                        />
                    </div>
                </div>
            </div>
            <div className="btn-wrap">
                <button type="submit" className="btn btn--green">
                    <span>{client ? "Save changes" : "Create"}</span>
                </button>
                {client ? (
                    <button type="button" className="btn btn--red" onClick={handleDelete}>
                        <span>Delete</span>
                    </button>
                ) : null}
            </div>
        </form>
    );
}
