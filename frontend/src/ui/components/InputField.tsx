interface InputFieldProps {
    label: string;
    name: string;
    value: string | number;
    onChange(event: any): void;
}

export default function InputField({ label, name, value, onChange }: InputFieldProps) {
    return (
        <div className="info__list">
            <label className="info__label">{label}:</label>
            <input className="in-text" name={name} type={getInputType(value)} value={value} onChange={onChange} />
        </div>
    );
}

function getInputType(value: any): string {
    const valueType = typeof value;
    switch (valueType) {
        case "number":
            return "number";
        case "string":
            return "text";
        default:
            console.log("value:", value);
    }
    throw Error("Invalid value type for input field");
}
