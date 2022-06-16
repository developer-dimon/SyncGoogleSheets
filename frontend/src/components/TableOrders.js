import React from 'react';


class TableOrders extends React.Component {
    render() {
        return (
            <div className="table-container">
                <div className="table-scroll">
                    <table className="centered">
                        <thead>
                        <tr>
                            <th>Id</th>
                            <th>Number</th>
                            <th>Price dollars $</th>
                            <th>Price rubles ₽</th>
                            <th>Delivery date</th>
                        </tr>
                        </thead>
                    </table>
                    <div className="table-scroll-body">
                        <table className="highlight centered">
                            <tbody>
                            {this.props.orders.map(order =>
                                <tr key={order.id}>
                                    <td>{order.id}</td>
                                    <td>{order.order_number}</td>
                                    <td>{order.price_dollars}</td>
                                    <td>{order.price_rubles}</td>
                                    <td>{order.delivery_date}</td>
                                </tr>
                            )}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        )
    }
}

export default TableOrders;