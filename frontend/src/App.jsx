import { useState } from "react";

import Home from "./pages/Home";
import FinanceDashboard from "./pages/FinanceDashboard";


function App() {

    const [page, setPage] = useState("chat");


    return (

        <div className="chimera-app">

            <nav className="top-navigation">

                <div className="nav-brand">
                    CHIMERA
                </div>


                <div className="nav-actions">

                    <button
                        className={
                            page === "chat"
                                ? "nav-button active"
                                : "nav-button"
                        }
                        onClick={() => setPage("chat")}
                    >
                        Chat
                    </button>


                    <button
                        className={
                            page === "finance"
                                ? "nav-button active"
                                : "nav-button"
                        }
                        onClick={() => setPage("finance")}
                    >
                        Finance Controller
                    </button>

                </div>

            </nav>


            <div className="page-container">

                {page === "chat" && <Home />}

                {page === "finance" && <FinanceDashboard />}

            </div>

        </div>

    );

}


export default App;