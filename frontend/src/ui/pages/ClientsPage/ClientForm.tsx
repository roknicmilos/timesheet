import { useCallback, useState } from "react";
import Client from "../../../core/models/api/Client";
import { updateClient } from "../../../core/services/client.service";
import InputField from "../../components/InputField";

interface ClientFormProps {
    client: Client;
    onSubmit(updatedClient: Client): void;
}

export default function ClientForm({ client, onSubmit }: ClientFormProps) {
    const [formData, setFormData] = useState<Client>({ ...client });

    const handleSubmit = useCallback(
        (event: any) => {
            event.preventDefault();
            updateClient(formData).then((updatedClient) => onSubmit(updatedClient));
        },
        [formData]
    );

    const handleChange = useCallback((event) => {
        setFormData((previousFormData) => ({ ...previousFormData, [event.target.name]: event.target.value }));
    }, []);

    return (
        <form className="accordion__content" onSubmit={handleSubmit}>
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

                        <div className="info__list">
                            <label className="report__label">Country:</label>
                            <select className="info__select" name="country" onChange={handleChange}>
                                {/* TODO: add country options (FE should probably provide this) */}
                                <option value={formData.country}>All</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div className="btn-wrap">
                <button type="submit" className="btn btn--green">
                    <span>Save changes</span>
                </button>
                <button type="button" className="btn btn--red">
                    <span>Delete</span>
                </button>
            </div>
        </form>
    );
}
