import PageButton from "./PageButton";

interface PagerProps {
    totalPages: number;
    currentPage: number;
    onPreviousPage(): void;
    onPageChange(page: number): void;
    onNextPage(): void;
}

export default function Pager({ totalPages, currentPage, onPreviousPage, onPageChange, onNextPage }: PagerProps) {
    const previousPageClassName = `pagination__button ${currentPage === 1 ? "pagination__button--disabled" : ""}`;
    const nextPageClassName = `pagination__button ${currentPage === totalPages ? "pagination__button--disabled" : ""}`;
    return (
        <div className="pagination">
            <ul className="pagination__navigation">
                <li className="pagination__list">
                    <div className={previousPageClassName} onClick={onPreviousPage}>
                        Previous
                    </div>
                </li>
                {Array(totalPages)
                    .fill(null)
                    .map((_, index) => (
                        <PageButton
                            key={index}
                            pageNumber={index + 1}
                            isActive={index + 1 === currentPage}
                            onClick={() => onPageChange(index + 1)}
                        />
                    ))}
                <li className="pagination__list">
                    <div className={nextPageClassName} onClick={onNextPage}>
                        Next
                    </div>
                </li>
            </ul>
        </div>
    );
}
