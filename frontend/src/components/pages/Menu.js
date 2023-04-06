import React, {useState, useEffect} from 'react';
import '../../App.css';

function Menu() {
    
    const [menu,setmenu] = useState([]);

    const handlemessage = (msg) => {
    setmenu(msg)
    }



    fetch('/menu' , {
        method:"GET",
      }).then(response => response.json())
        .then(message => (
            // console.log(message["user"])
            handlemessage(message['menuList'])
            // console.log(message['menuList'])
        ))

    const Redirect1 = (event) => {
        window.location.href='/addFoodItem'
    }

    // const Redirect2 = (event) => {
    //     window.location.href='/createMenu'
    // }

    // const Redirect3 = (event) => {
    //     window.location.href='/presentOrdersforRestaurant'           //not in backend
    // }

    // const Redirect4 = (event) => {
    //     window.location.href='/pastOrdersforRestaurant'                      //not in backend
    // }


    // const table = document.createElement("table");
    // const tableHead = table.createTHead();
    // const tableHeaderRow = tableHead.insertRow();
    // const itemHeader = tableHeaderRow.insertCell(0);
    // itemHeader.innerHTML = "Item";
    // const quantityHeader = tableHeaderRow.insertCell(1);
    // quantityHeader.innerHTML = "Quantity";

    // const tableBody = table.createTBody();
    // for (let i = 0; i < menu.length; i++) {
    //   const row = tableBody.insertRow();
    //   const itemCell = row.insertCell();
    //   const quantityCell = row.insertCell();
    //   itemCell.innerHTML = menu[i]['name'];
    //   quantityCell.innerHTML = menu[i]['price'];
    // }

    // document.body.appendChild(table);


    let content = [];
    for (let i=0;i<menu.length;i++) {
      // console.log(menu[i]['pricePerItem'])
      // console.log(menu[i]['name'])
      // console.log("Hello World")
      content.push(<li>{menu[i]['name']}</li>);
      content.push(<li>{menu[i]['pricePerItem']}</li>);
    }
    

    return(
        <>
            <div className="Welcome">
            <h1>Menu</h1>    
            </div>
            <div>
            <ul>{content}</ul>
            </div>
            <div className="options">
                <button onClick={Redirect1}>Add Food Item</button>
            </div>
        </>
    );

  }

export default Menu;