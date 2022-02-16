import CalendarDay from "./CalendarDay"
import TimesheetWeek from "../../../core/models/TimesheetWeek"
import TimesheetDay from "../../../core/models/TimesheetDay"

interface CalendarWeekProps {
    timesheetWeek: TimesheetWeek
}

export default function CalendarWeek({ timesheetWeek }: CalendarWeekProps) {

    const renderDisabledCalendarDays = function (timesheetDays: TimesheetDay[]) {
        return timesheetDays.map(timesheetDay => <CalendarDay key={timesheetDay.date.toString()} timesheetDay={timesheetDay} isDisabled={true} />)
    }

    const renderEnabledCalendarDays = function (timesheetDays: TimesheetDay[]) {
        return timesheetDays.map(timesheetDay => <CalendarDay key={timesheetDay.date.toString()} timesheetDay={timesheetDay} isDisabled={false} />)
    }

    return (
        <tr>
            {renderDisabledCalendarDays(timesheetWeek.previousMonthDays)}
            {renderEnabledCalendarDays(timesheetWeek.days)}
            {renderDisabledCalendarDays(timesheetWeek.nextMonthDays)}
        </tr>
    )
}
