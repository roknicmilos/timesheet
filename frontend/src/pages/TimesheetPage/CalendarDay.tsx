import TimesheetDay from "../../core/models/TimesheetDay"

interface CalendarDayProps {
    timesheetDay: TimesheetDay;
}

export default function CalendarDay({ timesheetDay }: CalendarDayProps) {
    let wrapperElementClasses = ['month-table__regular']
    if (timesheetDay.isDisabled) wrapperElementClasses.push('month-table__regular--disabled')

    return (
        <td className={wrapperElementClasses.join(' ')}>
            <div className="month-table__date">
                <span>{timesheetDay.date.getDate()}</span>
                <i></i>
            </div>
            <div className="month-table__hours">
                <a href="/" className="month-table__day">
                    <span>Hours: </span><span>{timesheetDay.hours}</span>
                </a>
            </div>
        </td>
    )
}
