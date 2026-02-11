import { Link } from "react-router-dom"

export default function Navbar() {
    return (
        <nav className="navbar">
            <Link to="/">Dashboard</Link>
            <Link to="/inventory">Inventory</Link>
            <Link to="/products">Products</Link>
            <Link to="/sales">Sales</Link>
            <Link to="/ml">ML insights</Link>

        </nav>
    )
}