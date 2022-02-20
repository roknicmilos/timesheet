import { requireAuthenticated } from "../../hoc/requireAuthenticated";

function ProjectsPage() {

    return (
        <div>PROJECTS</div>
    )
}

export default requireAuthenticated(ProjectsPage)
