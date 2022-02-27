import { useCallback, useEffect, useState } from "react";
import { getClients, getClientsAvailableAlphabetLetters } from "../../../core/services/client.service";
import { requireAuthenticated } from "../../../hoc/requireAuthenticated";
import Client from "../../../core/models/Client";
import Accordion from "../../components/Accordion";
import AlphabetFilter from "../../components/AlphabetFilter";
import Pager from "../../components/Pager";

function ClientsPage() {
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [totalPages, setTotalPage] = useState<number>(0);
    const [currentPage, setCurrentPage] = useState<number>(1);
    const [availableAlphabetLetters, setAvailableAlphabetLetters] = useState<string[]>();
    const [clients, setClients] = useState<Client[]>();

    const setupComponentData = useCallback(async () => {
        if (!isLoading) return;

        const letters = await getClientsAvailableAlphabetLetters();
        setAvailableAlphabetLetters(letters);

        const { clients, totalPages } = await getClients(currentPage);
        setClients(clients);
        setTotalPage(totalPages);

        setIsLoading(false);
    }, [isLoading, totalPages, currentPage, availableAlphabetLetters, clients]);

    useEffect(() => {
        // TODO: check why useEffect is called a lot of times
        setupComponentData();
    }, [setupComponentData]);

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
                    <form className="table-navigation__input-container" action="#">
                        <input type="text" className="table-navigation__search" />
                        <button type="submit" className="icon__search"></button>
                    </form>
                </div>
                <AlphabetFilter availableLetters={availableAlphabetLetters} />
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
