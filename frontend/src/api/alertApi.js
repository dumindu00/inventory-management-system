import api from "./axios";

export const getAlerts = () =>
  api.get("/alerts/");
