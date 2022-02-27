import { Collapse } from "react-collapse";

interface AccordionProps {
    title: string;
    isActive: boolean;
    onClick(): void;
    // TODO: add form fields
}

export default function Accordion({ title, isActive, onClick }: AccordionProps) {
    return (
        <div className="accordion" onClick={onClick}>
            <div className="accordion__intro">
                <h4 className="accordion__title">{title}</h4>
            </div>
            <Collapse isOpened={isActive}>
                <form className="accordion__content" action="#">
                    <div className="info">
                        <div className="info__form">
                            <ul className="info__wrapper">
                                <li className="info__list">
                                    <label className="info__label">Client name:</label>
                                    <input type="text" className="in-text" />
                                </li>
                                <li className="info__list">
                                    <label className="report__label">Address:</label>
                                    <input type="text" className="in-text" />
                                </li>
                                <li className="info__list">
                                    <label className="report__label">City:</label>
                                    <input type="text" className="in-text" />
                                </li>
                                <li className="info__list">
                                    <label className="report__label">Zip/Postal code:</label>
                                    <input type="text" className="in-text" />
                                </li>
                                <li className="info__list">
                                    <label className="report__label">Country:</label>
                                    <select className="info__select">
                                        <option value="">All</option>
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
            </Collapse>
        </div>
    );
}
