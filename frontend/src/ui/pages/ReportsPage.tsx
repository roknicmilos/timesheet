import { requireAuthenticated } from "../../hoc/requireAuthenticated";

function ReportsPage() {

    return (
        <div>REPORTS</div>
    )
}

export default requireAuthenticated(ReportsPage)
