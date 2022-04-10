import { DateTime } from "luxon";
import { datesRange, getMonday, getSunday } from "../../../core/services/datetime.service";

interface WeekDaySelectorProps {
    selectedDate: Date;
    onDayChange(date: Date): void;
}

export default function WeekDaySelector({ selectedDate, onDayChange }: WeekDaySelectorProps) {
    const selectedDateTime = DateTime.fromJSDate(selectedDate);
    const sunday = getSunday(selectedDate);
    const monday = getMonday(selectedDate);
    const weekDays = datesRange(monday, sunday);
    const weekStart = DateTime.fromJSDate(monday).toFormat("DDD").split(",")[0];
    const weekEnd = DateTime.fromJSDate(sunday).toFormat("DDD").split(",")[0];

    const DayButton = function ({ date }: { date: Date }) {
        const dateTime = DateTime.fromJSDate(date);
        const isSeleted = date.getTime() === selectedDate.getTime();
        return (
            <li className={`day-table__list ${isSeleted ? "day-table__list--active" : ""}`}>
                <div className="day-table__link" onClick={() => onDayChange(date)}>
                    <b className="day-table__month">{dateTime.toFormat("DD").split(",")[0]}</b>{" "}
                    <i className="day-table__day">{/* TODO: display hours */}</i>
                    <span className="day-table__span hide-on-mob">{dateTime.toFormat("cccc")}</span>
                    <span className="day-table__span show-on-mob">{dateTime.toFormat("ccc")}</span>
                </div>
            </li>
        );
    };

    return (
        <>
            <div className="table-navigation">
                <div className="table-navigation__prev" onClick={() => alert("TO BE IMPLEMENTED")}>
                    <span>previous week</span>
                </div>
                <span className="table-navigation__center">
                    {weekStart} - {weekEnd}, {selectedDateTime.year} (week {selectedDateTime.weekNumber})
                </span>
                <div className="table-navigation__next" onClick={() => alert("TO BE IMPLEMENTED")}>
                    <span>next week</span>
                </div>
            </div>
            <div className="day-table">
                <ul className="day-table__wrap">
                    {weekDays.map((date) => (
                        <DayButton key={date.toString()} date={date} /> // TODO
                    ))}
                </ul>
            </div>
        </>
    );
}
