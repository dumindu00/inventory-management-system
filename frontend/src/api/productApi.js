import api from "./axios";

export const getProducts = () =>
  api.get("/products/");

export const createProduct = (data) =>
  api.post("/products/", data);
