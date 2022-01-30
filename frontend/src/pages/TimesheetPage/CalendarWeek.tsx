import CalendarDay from "./CalendarDay"
import TimesheetWeek from "../../models/TimesheetWeek"

interface CalendarWeekProps {
    timesheetWeek: TimesheetWeek
}

export default function CalendarWeek({ timesheetWeek }: CalendarWeekProps) {
    return <tr>{timesheetWeek.days.map(timesheetDay => <CalendarDay key={timesheetDay.date.toString()} timesheetDay={timesheetDay} />)}</tr>
}
