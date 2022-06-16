import TableOrders from "./components/TableOrders";
import axios from "axios";
import React from "react";
import './css/style.css'
import Loader from "./components/Loader";

const API_URL = 'http://127.0.0.1/api' //Я не смог победить докер и загрузить environments

class App extends React.Component {
    state = {
        orders: [],
        updateDataUrl: `${API_URL}/update-data/`,
        getOrdersUrl: `${API_URL}/orders/`,
        loading: false

    }

    updateOrders() {
        this.setState({loading:true})
        axios.post(this.state.updateDataUrl).then()
        this.getOrders()
        this.setState({loading:false})
    }

    getOrders() {
        this.setState({orders: []})
        axios.get(this.state.getOrdersUrl)
            .then(response => {
                const orders = response.data;
                this.setState({orders})
            });
    }

    componentDidMount() {
        this.getOrders()
    }

    render() {
        return (
            <div className="App">
                <button type="button" onClick={this.updateOrders.bind(this)} className="btn-custom btn-generator">
                    Update table
                </button>
                {!this.state.loading ?
                    <>
                        <TableOrders orders={this.state.orders}/>
                        <h5 style={{color: 'white'}}>Total {this.state.orders.length}</h5>
                    </>
                    : <Loader/>}

            </div>
        );
    }
}

export default App;
