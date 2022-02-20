import { requireAuthenticated } from "../../hoc/requireAuthenticated";

function EmployeesPage() {

    return (
        <div>EMPLOYEES</div>
    )
}

export default requireAuthenticated(EmployeesPage)
