import { useState } from "react";
import { createSale } from "../api/salesApi";

export default function Sales() {
  const [sale, setSale] = useState({ product_id: "", quantity: "" });
  const [loading, setLoading] = useState(false);

  const handleSale = async () => {
    if (!sale.product_id || !sale.quantity) return alert("Fill all fields");
    setLoading(true);
    try {
      await createSale({ product_id: +sale.product_id, quantity: +sale.quantity });
      setSale({ product_id: "", quantity: "" });
      alert("Sale recorded successfully");
    } catch (err) {
      console.error(err);
      alert("Error recording sale");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Sales</h1>

      <div className="kpi-grid">
        <div className="kpi-card">
          <div className="kpi-title">Product ID</div>
          <input
            placeholder="Product ID"
            value={sale.product_id}
            onChange={(e) => setSale({ ...sale, product_id: e.target.value })}
          />
        </div>
        <div className="kpi-card">
          <div className="kpi-title">Quantity</div>
          <input
            placeholder="Quantity"
            value={sale.quantity}
            onChange={(e) => setSale({ ...sale, quantity: e.target.value })}
          />
        </div>
      </div>

      <button onClick={handleSale} disabled={loading}>
        {loading ? "Recording..." : "Record Sale"}
      </button>
    </div>
  );
}
