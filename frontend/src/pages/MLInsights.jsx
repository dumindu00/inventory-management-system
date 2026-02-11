import { useState } from "react";
import { inventoryChart } from "../api/mlApi";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

export default function MLInsights() {
  const [productId, setProductId] = useState("");
  const [chart, setChart] = useState(null);
  const [loading, setLoading] = useState(false);

  const loadChart = async () => {
    if (!productId) return alert("Enter a product ID");
    setLoading(true);
    try {
      const res = await inventoryChart(productId);
      const dataset = res.data.data || [];
      if (!dataset.length) return alert("No data returned");

      setChart({
        labels: dataset.map((d) => d.date),
        datasets: [
          { label: "Actual", data: dataset.map((d) => d.actual), borderWidth: 2 },
          { label: "Predicted", data: dataset.map((d) => d.predicted), borderDash: [5, 5] },
        ],
      });
    } catch (err) {
      console.error(err);
      alert("Error loading chart");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container">
      <h1>ML Inventory Insights</h1>
      <div className="kpi-grid">
        <div className="kpi-card">
          <div className="kpi-title">Product ID</div>
          <input
            placeholder="Product ID"
            value={productId}
            onChange={(e) => setProductId(e.target.value)}
          />
        </div>
      </div>

      <button onClick={loadChart} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {chart && (
        <div className="chart-grid">
          <div className="chart-card">
            <Line data={chart} />
          </div>
        </div>
      )}
    </div>
  );
}
