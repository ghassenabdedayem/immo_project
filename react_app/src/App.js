import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div>
      Hello Pote !

      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
        </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
        </a>
        </header>
      </div>
    </div>
  );
}

function App_2() {
  var dictionnaire = {};
  dictionnaire = [
    {
      Name: 'Ghassen',
      Surname: 'Pote',
      Age: 30
    }
  ];
  var data = []
  data.push({ "id": "7", "name": "pote", "surname": "pote" });
  data.push({ "id": "7", "name": "to", "surname": "zerzer" });
  data.push({ "id": "7", "name": "dfgdfg", "surname": "gdgdfgfd" });
  // var table = document.createElement('table');
  // table.setAttribute('width', '100%');
  // for (var i = 0; i < data.length; i++) {
  //   var tr = document.createElement('tr');
  //   var td1 = document.createElement('td');
  //   var td2 = document.createElement('td');
  //   var td3 = document.createElement('td');
  //   var text1 = document.createTextNode(data[i]["id"]);
  //   var text2 = document.createTextNode(data[i].name);
  //   var text3 = document.createTextNode(data[i]["surname"]);
  //   td1.appendChild(text1);
  //   td2.appendChild(text2);
  //   td3.appendChild(text3);
  //   tr.appendChild(td1);
  //   tr.appendChild(td2);
  //   tr.appendChild(td3);
  //   table.appendChild(tr);
  // }
  // document.body.appendChild(table);
  return (
    <div>
      {data[1]["name"]}
      <table>
        <tbody>
          {
            data.map((myobj, i) => (
              <tr key={i}>
                {
                  Object.keys(myobj).map((key,j) =>
                    <td key={j}>{myobj[key]}</td>
                  )
                }
              </tr>
            ))
          }
        </tbody>
      </table>

      <div>
        <h1>elements in dictionnaire</h1>
      </div>
    </div>
  )
}

export default App_2;
