const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
$.get(url, function(data){
	for (let i = 0; i < 7; i++){
		$('#list_movies').append('<li>'+ data.results[i].title +'</li>')
	}
});