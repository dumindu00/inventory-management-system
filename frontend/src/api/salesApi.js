import api from "./axios";

export const createSale = (data) =>
  api.post("/sales/", {
    product_id: Number(data.product_id),
    quantity: Number(data.quantity),
  });

export const getDailyRevenue = () =>
  api.get("/reports/daily");

export const getMonthlyRevenue = () =>
  api.get("/reports/monthly");

export const getProductSalesReport = () =>
  api.get("/reports/products");
