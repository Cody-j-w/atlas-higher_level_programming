$('document').ready(() => {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    context: document.body
  }).done((data) => {
    $('div#character').text(data.name);
  })
});
