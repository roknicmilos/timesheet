import axios from "axios";

export async function getCountyNames(): Promise<string[]> {
    try {
        const countries = await axios.get("https://restcountries.com/v3.1/all");
        return countries.data.map((country: any) => country.name.common);
    } catch (error) {
        console.error("Error while fetching countries\n", error);
        return [];
    }
}
