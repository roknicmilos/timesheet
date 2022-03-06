interface SelectFieldProps {
    label: string;
    name: string;
    value: string | number;
    options: string[];
    onChange(event: any): void;
}

export default function SelectField({ label, name, value, options, onChange }: SelectFieldProps) {
    return (
        <div className="info__list">
            <label className="report__label">{label}:</label>
            <select className="info__select" name={name} onChange={onChange} value={value}>
                {options.map((option) => {
                    let label = option.slice(0, 30);
                    label += label < option ? "..." : "";
                    return (
                        <option key={option} value={option}>
                            {label}
                        </option>
                    );
                })}
            </select>
        </div>
    );
}
