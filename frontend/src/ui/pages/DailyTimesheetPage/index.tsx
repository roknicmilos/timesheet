import { useLocation, useNavigate } from "react-router-dom";
import { requireAuthenticated } from "../../../hoc/requireAuthenticated";
import { useEffect, useState } from "react";
import { getDailyTimesheets } from "../../../core/services/dailyTimesheet.service";
import { useAuth } from "../../../core/contexts/Auth.context";
import DailyTimesheet from "../../../core/models/api/DailyTimesheet";
import WeekDaySelector from "./WeekSelector";
import TimesheetDay from "../../../core/models/TimesheetDay";
import { getMonday, getSunday } from "../../../core/services/datetime.service";
import { calculateTimesheetDayTotalHours } from "../../../core/services/calendar.service";

function DailyTimesheetPage() {
    const navigate = useNavigate();
    const location: any = useLocation();
    const { user } = useAuth();
    const [isLoading, setIsLoading] = useState<boolean>(true);

    const [currentTimesheetDay, setCurrentTimesheetDay] = useState<TimesheetDay>(location.state.timesheetDay);
    const sunday = getSunday(currentTimesheetDay.date);
    const monday = getMonday(currentTimesheetDay.date);

    const [dailyTimesheets, setDailyTimesheets] = useState<DailyTimesheet[]>();
    const [selectedDailyTimesheet, setSelectedDailyTimesheet] = useState<DailyTimesheet | undefined>();

    useEffect(() => {
        if (!isLoading) return;

        // TODO: check why it runs more than it should

        getDailyTimesheets(user!.id, monday, sunday).then((response) => {
            setDailyTimesheets(response.dailyTimesheets);
            setSelectedDailyTimesheet(
                response.dailyTimesheets!.find((dailyTimesheet) => {
                    const dailyTimesheetDate = new Date(dailyTimesheet.date);
                    return dailyTimesheetDate.getDate() === currentTimesheetDay.date.getDate();
                })
            );
            setIsLoading(false);
        });
    }, [isLoading, user, monday, sunday, currentTimesheetDay]);

    function onTimesheetDayChange(date: Date) {
        const selectedDailyTimesheet = dailyTimesheets!.find((dailyTimesheet) => {
            const dailyTimesheetDate = new Date(dailyTimesheet.date);
            return dailyTimesheetDate.getDate() === date.getDate();
        });
        setCurrentTimesheetDay({
            dailyTimesheetID: selectedDailyTimesheet?.id,
            date,
            hours: selectedDailyTimesheet
                ? calculateTimesheetDayTotalHours(selectedDailyTimesheet.time_sheet_reports)
                : 0,
        });
    }

    return (
        <section className="content">
            <form id="mainContent" className="main-content" action="javascript">
                <h2 className="main-content__title">Timesheet</h2>
                <WeekDaySelector selectedDate={currentTimesheetDay.date} onDayChange={onTimesheetDayChange} />
                <table className="project-table">
                    <thead>
                        <tr className="project-table__top">
                            <th className="project-table__title">Client *</th>
                            <th className="project-table__title">Project *</th>
                            <th className="project-table__title">Category *</th>
                            <th className="project-table__title project-table__title--large">Description</th>
                            <th className="project-table__title project-table__title--small">Hours *</th>
                            <th className="project-table__title project-table__title--small">Overtime</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td className="project-table__name">
                                <select className="project-table__select">
                                    <option>Choose client</option>
                                    <option>Client name 1</option>
                                    <option>Client name 2</option>
                                    <option>Client name 3</option>
                                    <option>Client name 4</option>
                                </select>
                            </td>
                            <td className="project-table__name">
                                <select className="project-table__select">
                                    <option value="">Choose project</option>
                                    <option value="">Choose category</option>
                                </select>
                            </td>
                            <td className="project-table__name">
                                <select className="project-table__select">
                                    <option value="">Choose category</option>
                                    <option value="">Choose category</option>
                                </select>
                                <span className="validationMessage" style={{ display: "none" }}></span>
                            </td>
                            <td className="project-table__name">
                                <input type="text" className="in-text medium" />
                            </td>
                            <td className="project-table__name">
                                <input type="text" className="in-text" />
                            </td>
                            <td className="project-table__name">
                                <input type="text" className="in-text" />
                            </td>
                        </tr>
                        <tr>
                            <td className="project-table__name">
                                <select className="project-table__select">
                                    <option>Choose client</option>
                                    <option>Client name 1</option>
                                    <option>Client name 2</option>
                                    <option>Client name 3</option>
                                    <option>Client name 4</option>
                                </select>
                            </td>
                            <td className="project-table__name">
                                <select className="project-table__select">
                                    <option value="">Choose project</option>
                                    <option value="">Choose category</option>
                                </select>
                            </td>
                            <td className="project-table__name">
                                <select className="project-table__select">
                                    <option value="">Choose category</option>
                                    <option value="">Choose category2</option>
                                </select>
                                <span className="validationMessage" style={{ display: "none" }}></span>
                            </td>
                            <td className="project-table__name">
                                {/* TODO: <input type="text" className="in-text medium" /> */}
                                <p>{selectedDailyTimesheet?.time_sheet_reports[0]?.description || "unknown"}</p>
                            </td>
                            <td className="project-table__name">
                                {/* TODO: <input type="text" className="in-text" /> */}
                                <p>{selectedDailyTimesheet?.time_sheet_reports[0]?.hours || "unknown"}</p>
                            </td>
                            <td className="project-table__name">
                                {/* TODO: <input type="text" className="in-text" /> */}
                                <p>{selectedDailyTimesheet?.time_sheet_reports[0]?.overtime_hours || "unknown"}</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div className="table-navigation">
                    <div className="table-navigation__prev" onClick={() => navigate("/")}>
                        <span>back to monthly view</span>
                    </div>
                    <div className="table-navigation__next">
                        <span className="table-navigation__text">Total:</span>
                        <span>7.5</span>
                    </div>
                </div>
                <div className="btn-wrap">
                    <button type="submit" className="btn btn--green">
                        <span>Save changes</span>
                    </button>
                </div>
            </form>
        </section>
    );
}

export default requireAuthenticated(DailyTimesheetPage);
