import { TailSpin } from "react-loader-spinner";

export default function Spinner() {
    return (
        <div className="page-spinner">
            <TailSpin color="#f1592a" height={80} width={80} />
        </div>
    );
}
