```react
	const [scroll, setScroll] = useState('#ffffff00')
	
	useEffect(() => {
		window.addEventListener('scroll', handleScroll);
		return () => {
			window.removeEventListener('scroll', handleScroll); //clean up
		};
	}, []);

	const handleScroll = () => {
	// 스크롤이 Top에서 500px 이상 내려오면 흰색 useState에 넣어줌
		if(window.scrollY >= 500 ){
			setScroll('#ffffff');
			// console.log(scroll)
		}else{
		// 스크롤이 500px 미만일경우 투명 넣어줌
			setScroll('#ffffff00');
		}
	}


  const transparentTheme = createTheme({
    palette: {
      primary: {
        main: `${scroll}`,//'#ffffff',
        boxShadow: 'none'
      }
    }
  })


```

