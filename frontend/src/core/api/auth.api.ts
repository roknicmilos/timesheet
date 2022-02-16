import timesheetApiClient from ".";
import User from "../models/api/User";

async function login(email: string, password: string): Promise<User | undefined> {
    try {
        const response = await timesheetApiClient.post('/login/', { email, password });
        return response.data;
    } catch (error) {
        console.error('Login error\n', error);
    }
}

async function logout() {
    try {
        await timesheetApiClient.get('/logout/');
    } catch (error) {
        console.error('Logout error\n', error);
    }
}

export { login, logout }
