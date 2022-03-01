import { useCallback, useEffect, useState } from "react";
import { ClientsFilters, getClients, getClientsAvailableAlphabetLetters } from "../../../core/services/client.service";
import searchIcon from "./../../../assets/images/search.png";
import { requireAuthenticated } from "../../../hoc/requireAuthenticated";
import Client from "../../../core/models/Client";
import Accordion from "../../components/Accordion";
import AlphabetFilter from "../../components/AlphabetFilter";
import Pager from "../../components/Pager";

function ClientsPage() {
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [totalPages, setTotalPage] = useState<number>(0);
    const [filters, setFilters] = useState<ClientsFilters>({ name_contains: "" });
    const [currentPage, setCurrentPage] = useState<number>(1);
    const [availableAlphabetLetters, setAvailableAlphabetLetters] = useState<string[]>();
    const [clients, setClients] = useState<Client[]>();

    useEffect(() => {
        // TODO: check why this method is called multiple times

        if (!isLoading) return;

        getClientsAvailableAlphabetLetters()
            .then((letters) => {
                setAvailableAlphabetLetters(letters);
                return getClients(currentPage, filters);
            })
            .then(({ clients, totalPages }) => {
                setClients(clients);
                setTotalPage(totalPages);
                setIsLoading(false);
            });
    }, [isLoading, totalPages, currentPage, availableAlphabetLetters, clients]);

    const handleCurrentPage = useCallback(
        (page) => {
            setIsLoading(true);
            setCurrentPage(page);
        },
        [currentPage]
    );

    const handlePreviousPage = useCallback(() => {
        setIsLoading(true);
        setCurrentPage((previousPage) => (previousPage > 1 ? previousPage - 1 : previousPage));
    }, []);

    const handleNextPage = useCallback(() => {
        setIsLoading(true);
        setCurrentPage((previousPage) => (previousPage < totalPages! ? previousPage + 1 : previousPage));
    }, [totalPages]);

    const applyLetterFilter = useCallback((letter: string) => {
        setIsLoading(true);
        setFilters((previousFilters) => ({ ...previousFilters, name_starts_with: letter }));
    }, []);

    const updateSearchWord = useCallback((event) => {
        setFilters((previousFilters) => ({
            ...previousFilters,
            name_contains: event.target.value,
        }));
    }, []);

    const applySearchWord = useCallback((event) => {
        setCurrentPage(1);
        setIsLoading(true);
    }, []);

    const selectClient = useCallback(
        (clientId: number) => {
            setClients((previousClients) => {
                return previousClients!.map((client) => ({
                    ...client,
                    isSelected: client.id === clientId && !client.isSelected,
                }));
            });
        },
        [clients]
    );

    const Accordions = useCallback(() => {
        return (
            <>
                {clients!.map((client) => {
                    return (
                        <Accordion
                            key={client.id}
                            title={client.name}
                            isActive={client.isSelected}
                            onClick={() => selectClient(client.id)}
                        />
                    );
                })}
            </>
        );
    }, [clients]);

    if (isLoading) {
        return <div>LOADING</div>;
    }

    return (
        <section className="content">
            <div className="main-content">
                <h2 className="main-content__title">Clients</h2>
                <div className="table-navigation">
                    <a href="#" className="table-navigation__create btn-modal">
                        <span>Create new client</span>
                    </a>
                    <form className="table-navigation__input-container" onSubmit={applySearchWord}>
                        <input
                            type="text"
                            className="table-navigation__search"
                            value={filters?.name_contains}
                            onChange={updateSearchWord}
                        />
                        <button type="submit" className="icon__search">
                            <img src={searchIcon} alt="search icon" />
                        </button>
                    </form>
                </div>
                <AlphabetFilter
                    availableLetters={availableAlphabetLetters}
                    selectedLetter={filters.name_starts_with}
                    onSelectLetter={applyLetterFilter}
                />
                <Accordions />
            </div>
            <Pager
                totalPages={totalPages}
                currentPage={currentPage}
                onPreviousPage={handlePreviousPage}
                onPageChange={handleCurrentPage}
                onNextPage={handleNextPage}
            />
        </section>
    );
}

export default requireAuthenticated(ClientsPage);
