import { createContext, useContext, ReactNode, useState, useEffect } from "react";
import { getCountyNames } from "../services/country.service";

interface CountriesContextValues {
    countryNames: string[];
}

const CountriesContext = createContext<CountriesContextValues>({ countryNames: [] });

export function useCountries() {
    return useContext(CountriesContext);
}

export function CountriesContextProvider({ children }: { children: ReactNode }) {
    const [countryNames, setCountryNames] = useState<string[]>([]);

    useEffect(() => {
        getCountyNames().then((names) => setCountryNames(names.sort()));
    }, []);

    return <CountriesContext.Provider value={{ countryNames }}>{children}</CountriesContext.Provider>;
}
