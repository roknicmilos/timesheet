import { useCallback, useState } from "react";
import { requireAuthenticated } from "../../../hoc/requireAuthenticated";
import Accordion from "../../components/Accordion";
import AlphabetFilter from "../../components/AlphabetFilter";
import Pager from "../../components/Pager";

function ClientsPage() {

    const [availableLetters, setAvailableLetters] = useState(() => {
        // TODO: fetch from API
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    })

    const [clients, setClients] = useState<{ id: number, title: string, isSelected: boolean }[]>(() => {
        // TODO: fetch from API
        return [
            {
                id: 1,
                title: 'Client 1',
                isSelected: false
            },
            {
                id: 2,
                title: 'Client 2',
                isSelected: false
            }
        ]
    })


    const selectClient = useCallback((clientId: number) => {
        setClients(previousClients => {
            return previousClients.map(client => ({ ...client, isSelected: client.id === clientId }))
        })
    }, [clients])

    const Accordions = useCallback(() => {
        return (
            <>
                {clients.map(client => {
                    return (
                        <Accordion
                            key={client.id}
                            title={client.title}
                            isActive={client.isSelected}
                            onClick={() => selectClient(client.id)} />
                    )
                })}
            </>
        )
    }, [clients])

    return (
        <section className="content">
            <div className="main-content">
                <h2 className="main-content__title">Clients</h2>
                <div className="table-navigation">
                    <a href="javascript:;" className="table-navigation__create btn-modal">
                        <span>Create new client</span>
                    </a>
                    <form className="table-navigation__input-container" action="javascript:;">
                        <input type="text" className="table-navigation__search" />
                        <button type="submit" className="icon__search"></button>
                    </form>
                </div>
                <AlphabetFilter availableLetters={availableLetters} selectedLetter="l" />
                <Accordions />
            </div>
            <Pager totalPages={5} currentPage={2} />
        </section>
    )
}

export default requireAuthenticated(ClientsPage)
