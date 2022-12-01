# useMemo()

### for Referential Equality for passing as props non-primitive JavaScript datatypes functions, objects and array.

```jsx
function factorial(n){
    let i = 0;
    while(i<200000) i++;
    //무거운 동작을 할때 느려지는 현상 생김
    //...
}
```

 ```jsx
 function App (){
     const [counter, setCounter] = useState(1);
     const result = useMemo(() => {
         return factorial(counter);
     }, [counter])
     return(
     <>
     	<DisplayName name={name}></DisplayName>    
     </>
     )
 }
 const DisplayName = React.memo(({name}) => {
     return <p>{`MY name is ${name}`}</p>
 })
 ```

https://www.youtube.com/watch?v=fzd2bvlyr70