# HOC (Higher-Order Components)

### 컴포넌트 로직을 재사용하기 위함

[참고 유튜브](# https://www.youtube.com/watch?v=tsCoBd7xSK8)

[깃허브](# https://github.com/dmalvia/React_Higher_Order_Component_Example/tree/master/src)

```jsx
import React from "react";

const HOC = (WrappedComponenet, entity) => {
  return class extends React.Component {
    state = {
      data: [],
      term: "",
    };
    componentDidMount() {
      const fetchData = async () => {
        const res = await fetch(
          `https://jsonplaceholder.typicode.com/${entity}`
        );
        const json = await res.json();
        this.setState({ ...this.state, data: json });
      };
      fetchData();
    }
    render() {
      let { term, data } = this.state;
      let filteredData = data.slice(0, 10).filter((d) => {
        if (entity === "users") {
          const { name } = d;
          return name.indexOf(term) >= 0;
        }
        if (entity === "todos") {
          const { title } = d;
          return title.indexOf(term) >= 0;
        }
      });
      return (
        <div>
          <h2>{entity}</h2>
          <input
            type="text"
            value={term}
            onChange={(e) =>
              this.setState({ ...this.state, term: e.target.value })
            }
          />
          <WrappedComponenet data={filteredData}></WrappedComponenet>
        </div>
      );
    }
  };
};

export default HOC;
```

```jsx
import React, { useEffect, useState } from "react";
import HOC from "./HOC";

const UsersList = ({ data }) => {
  let renderUsers = data.map((user) => {
    return (
      <div key={user.id}>
        <p>
          <strong>{user.name}</strong>
        </p>
      </div>
    );
  });
  return (
    <div>
      <div>{renderUsers}</div>
    </div>
  );
};

const SearchUsers = HOC(UsersList, "users");

export default SearchUsers;
```

```jsx
//app.jsx
function App(){
    return(
    <div>
    	<SearchUsers />
    </div>
    )
}
```

