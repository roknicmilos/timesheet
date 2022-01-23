import CalendarDay from "./CalendarDay"
import TimesheetDay from "../../models/TimesheetDay"

interface CalendarWeekProps {
    timesheetDays: TimesheetDay[]
}

export default function CalendarWeek({ timesheetDays }: CalendarWeekProps) {
    return <tr>{timesheetDays.map(timesheetDay => <CalendarDay timesheetDay={timesheetDay} />)}</tr>
}
