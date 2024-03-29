import { useCallback, useEffect, useState } from "react";
import { ClientsFilters, getClients, getClientsAvailableAlphabetLetters } from "../../../core/services/client.service";
import searchIcon from "./../../../assets/images/search.png";
import { requireAuthenticated } from "../../../hoc/requireAuthenticated";
import Client from "../../../core/models/api/Client";
import AlphabetFilter from "../../components/AlphabetFilter";
import Pager from "../../components/Pager";
import Spinner from "../../components/Spinner";
import ClientAccordionList from "./ClientAccordionList";
import CreateClientModal from "./CreateClientModel";

function ClientsPage() {
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [isCreatingClient, setIsCreatingClient] = useState<boolean>(false);
    const [totalPages, setTotalPage] = useState<number>(0);
    const [filters, setFilters] = useState<ClientsFilters>({ name_contains: "" });
    const [currentPage, setCurrentPage] = useState<number>(1);
    const [availableAlphabetLetters, setAvailableAlphabetLetters] = useState<string[]>();
    const [clients, setClients] = useState<Client[]>();
    const [selectedClientId, setSelectedClientId] = useState<number | undefined>(undefined);

    useEffect(() => {
        setup();

        // TODO: useEffect complains about missing dependency (setup)
        // eslint-disable-next-line
    }, []);

    const setup = () => {
        setIsLoading(true);
        getClientsAvailableAlphabetLetters().then((letters) => {
            setAvailableAlphabetLetters(letters);
        });
        fetchClients(currentPage, filters);
    };

    const fetchClients = (page: number, filters: ClientsFilters) => {
        setIsLoading(true);
        getClients(page, filters).then(({ clients, totalPages }) => {
            setClients(clients);
            setTotalPage(totalPages);
            setIsLoading(false);
        });
    };

    const changePage = useCallback(
        (page) => {
            setCurrentPage(page);
            fetchClients(page, filters);
        },
        [filters]
    );

    const getPreviousPage = useCallback(() => {
        const previousPage = currentPage - 1;
        setCurrentPage(previousPage);
        fetchClients(previousPage, filters);
    }, [currentPage, filters]);

    const getNextPage = useCallback(() => {
        const nextPage = currentPage + 1;
        setCurrentPage(nextPage);
        fetchClients(nextPage, filters);
    }, [currentPage, filters]);

    const applyLetterFilter = useCallback((letter: string) => {
        setCurrentPage(1);
        setFilters((previousFilters) => {
            const newFilters = { ...previousFilters, name_starts_with: letter };
            fetchClients(1, newFilters);
            return newFilters;
        });
    }, []);

    const updateSearchWord = useCallback((event) => {
        setFilters((previousFilters) => ({
            ...previousFilters,
            name_contains: event.target.value,
        }));
    }, []);

    const applySearchWord = useCallback(
        (event) => {
            setCurrentPage(1);
            fetchClients(1, filters);
        },
        [filters]
    );

    const selectClient = useCallback(
        (clientId: number) => {
            setSelectedClientId(selectedClientId !== clientId ? clientId : undefined);
        },
        [selectedClientId]
    );

    const updateClient = useCallback(() => {
        fetchClients(currentPage, filters);
    }, [currentPage, filters]);

    const addClient = useCallback(() => {
        setCurrentPage(1);
        fetchClients(1, filters);
        setIsCreatingClient(false);
    }, [filters]);

    const removeClient = useCallback(() => {
        fetchClients(currentPage, filters);
    }, [currentPage, filters]);

    return isLoading ? (
        <Spinner />
    ) : (
        <section className="content">
            <CreateClientModal
                isOpen={isCreatingClient}
                onSubmit={addClient}
                onClose={() => setIsCreatingClient(false)}
            />
            <div className="main-content">
                <h2 className="main-content__title">Clients</h2>
                <div className="table-navigation">
                    <div className="table-navigation__create btn-modal" onClick={() => setIsCreatingClient(true)}>
                        <span>Create new client</span>
                    </div>
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
                <ClientAccordionList
                    clients={clients!}
                    selectedClientId={selectedClientId!}
                    onToggleAccordion={selectClient}
                    onUpdateClient={updateClient}
                    onDeleteClient={removeClient}
                />
            </div>
            <Pager
                totalPages={totalPages}
                currentPage={currentPage}
                onPreviousPage={getPreviousPage}
                onPageChange={changePage}
                onNextPage={getNextPage}
            />
        </section>
    );
}

export default requireAuthenticated(ClientsPage);
