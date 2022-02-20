import { requireAuthenticated } from "../../hoc/requireAuthenticated";

function CategoriesPage() {

    return (
        <div>CATEGORIES</div>
    )
}

export default requireAuthenticated(CategoriesPage)
