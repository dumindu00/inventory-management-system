import { useEffect, useState } from "react";
import { getProducts, createProduct } from "../api/productApi";

export default function Product() {
  const [products, setProducts] = useState([]);
  const [form, setForm] = useState({
    name: "",
    category_id: "",
    subcategory_id: "",
    unit_cost: "",
    selling_price: "",
    lower_threshold: "",
    upper_threshold: "",
  });
  const [loading, setLoading] = useState(false);

  const loadProducts = async () => {
    const res = await getProducts();
    setProducts(res.data);
  };

  useEffect(() => {
    loadProducts();
  }, []);

  const submit = async () => {
    if (!form.name || !form.category_id || !form.unit_cost) return alert("Fill required fields");
    setLoading(true);
    try {
      await createProduct({
        name: form.name,
        category_id: Number(form.category_id),
        subcategory_id: Number(form.subcategory_id),
        unit_cost: Number(form.unit_cost),
        selling_price: Number(form.selling_price),
        lower_threshold: Number(form.lower_threshold),
        upper_threshold: Number(form.upper_threshold),
        initial_stock: 0,
      });
      setForm({
        name: "",
        category_id: "",
        subcategory_id: "",
        unit_cost: "",
        selling_price: "",
        lower_threshold: "",
        upper_threshold: "",
      });
      await loadProducts();
      alert("Product created successfully");
    } catch (err) {
      console.error(err);
      alert("Error creating product");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Product Management</h1>

      <div className="kpi-grid">
        {Object.keys(form).map((key) => (
          <div className="kpi-card" key={key}>
            <div className="kpi-title">{key.replace("_", " ").toUpperCase()}</div>
            <input
              placeholder={key.replace("_", " ")}
              value={form[key]}
              onChange={(e) => setForm({ ...form, [key]: e.target.value })}
            />
          </div>
        ))}
      </div>

      <button onClick={submit} disabled={loading}>
        {loading ? "Creating..." : "Create Product"}
      </button>

      <h3>Product List</h3>
      <div className="kpi-grid">
        {products.map((p) => (
          <div className="kpi-card" key={p.id}>
            <div>{p.name}</div>
            <div>Stock: {p.current_stock}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
