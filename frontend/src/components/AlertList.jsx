import { useEffect, useState } from "react";
import axios from "axios";

const AlertList = () => {
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAlerts();
  }, []);

  const fetchAlerts = async () => {
    try {
      const res = await axios.get("/api/v1/alerts");

      console.log("Alerts response:", res.data);

      // Defensive handling
      if (Array.isArray(res.data)) {
        setAlerts(res.data);
      } else if (Array.isArray(res.data.data)) {
        setAlerts(res.data.data);
      } else {
        setAlerts([]);
      }

    } catch (error) {
      console.error("Alert fetch error:", error);
      setAlerts([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chart-card">
      <h3>Active Alerts</h3>

      {loading && <p>Loading...</p>}

      {!loading && alerts.length === 0 && (
        <p>No active alerts</p>
      )}

      {!loading &&
        alerts.map((a) => (
          <p key={a.id}>⚠ {a.message}</p>
        ))}
    </div>
  );
};

export default AlertList;
