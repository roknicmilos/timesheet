export default interface User {
    id: number;
    name: string;
    email: string;
    weekly_hours: number;
    is_admin: boolean;
    token: string;
}
