import api from "./axios";

export const inventoryChart = (productId) =>
  api.get(`/ml/inventory/chart/${productId}`);
