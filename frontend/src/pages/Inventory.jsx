import { useState } from "react";
import { stockIn, stockOut } from "../api/inventoryApi";

export default function Inventory() {
  const [data, setData] = useState({ product_id: "", quantity: "" });
  const [loading, setLoading] = useState(false);

  const handleStock = async (type) => {
    if (!data.product_id || !data.quantity) return alert("Please fill all fields");
    setLoading(true);
    try {
      if (type === "in") await stockIn({ product_id: +data.product_id, quantity: +data.quantity });
      else await stockOut({ product_id: +data.product_id, quantity: +data.quantity });
      alert(`Stock ${type === "in" ? "added" : "removed"} successfully`);
      setData({ product_id: "", quantity: "" });
    } catch (err) {
      console.error(err);
      alert("Error updating stock");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Inventory Management</h1>

      <div className="kpi-grid">
        <div className="kpi-card">
          <div className="kpi-title">Product ID</div>
          <input
            placeholder="Product ID"
            value={data.product_id}
            onChange={(e) => setData({ ...data, product_id: e.target.value })}
          />
        </div>
        <div className="kpi-card">
          <div className="kpi-title">Quantity</div>
          <input
            placeholder="Quantity"
            value={data.quantity}
            onChange={(e) => setData({ ...data, quantity: e.target.value })}
          />
        </div>
      </div>

      <button onClick={() => handleStock("in")} disabled={loading}>
        {loading ? "Processing..." : "Stock In"}
      </button>
      <button onClick={() => handleStock("out")} disabled={loading}>
        {loading ? "Processing..." : "Stock Out"}
      </button>
    </div>
  );
}
