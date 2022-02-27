interface PageButtonProps {
    pageNumber: number;
    isActive: boolean;
    onClick(): void;
}

export default function PageButton({ pageNumber, isActive, onClick }: PageButtonProps) {
    const className = `pagination__button ${isActive ? "pagination__button--active" : ""}`;
    return (
        <li className="pagination__list" onClick={onClick}>
            <a className={className} href="#">
                {pageNumber}
            </a>
        </li>
    );
}
