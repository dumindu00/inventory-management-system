import { useEffect, useState } from "react";
import axios from "axios";
import ChartCard from "../components/ChartCard";
import AlertList from "../components/AlertList";

const Dashboard = () => {

  const [dailyRevenue, setDailyRevenue] = useState(0);
  const [monthlyRevenue, setMonthlyRevenue] = useState(0);
  const [salesChart, setSalesChart] = useState([]);
  const [inventoryChart, setInventoryChart] = useState([]);

  useEffect(() => {
    fetchKPIs();
    fetchCharts();
  }, []);

  const fetchKPIs = async () => {
    try {
      const daily = await axios.get("/api/v1/reports/daily");
      const monthly = await axios.get("/api/v1/reports/monthly");

      setDailyRevenue(daily.data.total || 0);
      setMonthlyRevenue(monthly.data.total || 0);

    } catch (error) {
      console.error("KPI error", error);
    }
  };

  const fetchCharts = async () => {
    try {
      const sales = await axios.get("/api/v1/ml/sales/chart/1");
      const inventory = await axios.get("/api/v1/ml/inventory/chart/1");

      setSalesChart(sales.data.data || []);
      setInventoryChart(inventory.data.data || []);

    } catch (error) {
      console.error("Chart error", error);
    }
  };

  return (
    <div className="dashboard-container">
      
      {/* KPI SECTION */}
      <div className="kpi-grid">

        <div className="kpi-card">
          <div className="kpi-title">Daily Revenue</div>
          <div className="kpi-value">${dailyRevenue}</div>
        </div>

        <div className="kpi-card">
          <div className="kpi-title">Monthly Revenue</div>
          <div className="kpi-value">${monthlyRevenue}</div>
        </div>

        <div className="kpi-card">
          <div className="kpi-title">Sales Forecast (Next Day)</div>
          <div className="kpi-value">
            {salesChart.length > 0 && salesChart[salesChart.length - 1].predicted || "-"}
          </div>
        </div>

        <div className="kpi-card">
          <div className="kpi-title">Inventory Risk</div>
          <div className="kpi-value">
            {inventoryChart.some(d => d.anomaly) ? "High" : "Normal"}
          </div>
        </div>

      </div>

      {/* CHART SECTION */}
      <div className="chart-grid">

        <ChartCard
          title="Sales Trend & Prediction"
          data={salesChart}
          dataKey="actual"
        />

        <ChartCard
          title="Inventory Movement & Forecast"
          data={inventoryChart}
          dataKey="actual"
        />

        <AlertList />

      </div>

    </div>
  );
};

export default Dashboard;
