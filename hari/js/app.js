$(document).ready(function() {
    /**
     * @param person
     * @returns {string}
     * Method which converts passed person into string, I would say html in the form of string
     */
    var renderPerson = function(person) {
        return '<tr><td>'+person.department+'</td><td>'+person.person+'</td><td>'+person.description+'</td></tr>';
    }

    /**
     * @param tableBody
     * In this method we will clear table which is being passed into this method
     */
    var clearTableBody = function(tableBody) {
        tableBody.html('');
    }

    /**
     * @param persons
     * Here we are appending every persons by converting each persons to row in table body
     */
    var renderPersons = function(persons) {
        var personssTableBody = $('#persons');
        clearTableBody(personssTableBody);
        for(var i = 0; i < persons.length; i++) {
            personssTableBody.append(renderPerson(persons[i]));
        }
    }

    /**
     * @param searchQuery
     * Method which sends request to backend with search query
     */
    var getPersons = function(searchQuery) {
        $.get('/?search='+searchQuery, function(data) {
            renderPersons(data.persons)
        });
    }

    //event is fired for every key types, tried to make it instant search instead of explicit button
    $('#search').keyup(function() {
        getPersons($(this).val());
    });

    $('#add').click(function() {
        var person = {department: $('#department').val(), person: $('#person-name').val(), description: $('#description').val()};
        $.ajax({
            type: "POST",
            url: '/',
            headers: {'Content-Type': 'application/json'},
            data: JSON.stringify(person),
            success: function(response) {
                getPersons('');
            }
        });
    });

    //Calling to get all personss on document.ready
    getPersons('');
});