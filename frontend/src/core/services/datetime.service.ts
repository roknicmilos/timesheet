export function getMonday(date: Date): Date {
    const day = date.getDay();
    const diff = date.getDate() - day + (day === 0 ? -6 : 1);
    const dateCopy = new Date(date);
    return new Date(dateCopy.setDate(diff));
}

export function getSunday(date: Date): Date {
    const day = date.getDay();
    const diff = date.getDate() - day + (day === 0 ? 0 : 7);
    const dateCopy = new Date(date);
    return new Date(dateCopy.setDate(diff));
}

export function datesRange(start: Date, end: Date): Date[] {
    const dates = [];
    const currentDate = new Date(start.getTime());
    while (currentDate <= end) {
        dates.push(new Date(currentDate));
        currentDate.setDate(currentDate.getDate() + 1);
    }
    return dates;
}

export function getDateIsoFormat(date: Date): string {
    return date.toISOString().split("T")[0];
}
