interface PageButtonProps {
    pageNumber: number
    isActive: boolean
}

export default function PageButton({ pageNumber, isActive }: PageButtonProps) {
    const className = `pagination__button ${isActive ? "pagination__button--active" : ""}`
    return (
        <li className="pagination__list">
            <a className={className} href="javascript:;">{pageNumber}</a>
        </li>
    )
}
