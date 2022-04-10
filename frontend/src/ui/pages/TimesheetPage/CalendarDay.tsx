import TimesheetDay from "../../../core/models/TimesheetDay";
import checkmark from "./../../../assets/images/checkmark.svg";
import { useNavigate } from "react-router-dom";

interface CalendarDayProps {
    timesheetDay: TimesheetDay;
    isDisabled: boolean;
}

export default function CalendarDay({ timesheetDay, isDisabled }: CalendarDayProps) {
    let wrapperElementClasses = ["month-table__regular"];
    if (isDisabled) wrapperElementClasses.push("month-table__regular--disabled");
    const navigate = useNavigate();
    const loadDailyTimesheetPage = function () {
        if (!isDisabled) {
            navigate("/daily-timesheet", {
                state: { timesheetDay },
            });
        }
    };

    return (
        <td className={wrapperElementClasses.join(" ")} onClick={loadDailyTimesheetPage}>
            <div className="month-table__date">
                <span>{timesheetDay.date.getDate()}</span>
                {timesheetDay.hours >= 8 ? (
                    <img className="month-table__checkmark" src={checkmark} alt="search icon" />
                ) : null}
            </div>
            <div className="month-table__hours">
                <a href="/" className="month-table__day">
                    <span>Hours: </span>
                    <span>{timesheetDay.hours}</span>
                </a>
            </div>
        </td>
    );
}
