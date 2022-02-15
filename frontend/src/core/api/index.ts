import axios from "axios";
import User from "../models/api/User";

const jsonUser = localStorage.getItem('user')
const user: User = jsonUser ? JSON.parse(jsonUser) : null;
const headers = user ? { 'Authorization': `Bearer ${user.token!}` } : undefined

const timesheetApiClient = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    headers: headers
});

export default timesheetApiClient
