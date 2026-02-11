import api from "./axios";

export const stockIn = (data) =>
  api.post("/inventory/in", data);

export const stockOut = (data) =>
  api.post("/inventory/out", data);
