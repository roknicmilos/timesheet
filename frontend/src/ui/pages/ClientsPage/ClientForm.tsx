import { useCallback, useState } from "react";
import Client from "../../../core/models/api/Client";
import { updateClient } from "../../../core/services/client.service";

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
                    <ul className="info__wrapper">
                        <li className="info__list">
                            <label className="info__label">Client name:</label>
                            <input
                                className="in-text"
                                name="name"
                                type="text"
                                value={formData.name}
                                onChange={handleChange}
                            />
                        </li>
                        <li className="info__list">
                            <label className="report__label">Address:</label>
                            <input
                                className="in-text"
                                name="street"
                                type="text"
                                value={formData.street}
                                onChange={handleChange}
                            />
                        </li>
                        <li className="info__list">
                            <label className="report__label">City:</label>
                            <input
                                className="in-text"
                                name="city"
                                type="text"
                                value={formData.city}
                                onChange={handleChange}
                            />
                        </li>
                        <li className="info__list">
                            <label className="report__label">Zip/Postal code:</label>
                            <input
                                className="in-text"
                                name="zip_code"
                                type="text"
                                value={formData.zip_code}
                                onChange={handleChange}
                            />
                        </li>
                        <li className="info__list">
                            <label className="report__label">Country:</label>
                            <select className="info__select" name="country" onChange={handleChange}>
                                {/* TODO: add country options (FE should probably provide this) */}
                                <option value={formData.country}>All</option>
                            </select>
                        </li>
                    </ul>
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
