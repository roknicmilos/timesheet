import PageButton from "./PageButton";

interface PagerProps {
    totalPages: number
    currentPage: number
}

export default function Pager({ totalPages, currentPage }: PagerProps) {
    return (
        <div className="pagination">
            <ul className="pagination__navigation">
                <li className="pagination__list">
                    <a className="pagination__button" href="javascript:;">Previous</a>
                </li>
                {Array(totalPages).fill(null).map((_, index) => <PageButton key={index} pageNumber={index + 1} isActive={index + 1 === currentPage} />)}
                <li className="pagination__list">
                    <a className="pagination__button" href="javascript:;">Next</a>
                </li>
            </ul>
        </div>
    )
}

