$(document).ready(function() {
    // Get the search input element
    var searchInput = document.getElementById('search-input');
    var delayTimer; // Variable to hold the timer

    // Add event listener for input changes
    searchInput.addEventListener('input', function() {
        clearTimeout(delayTimer); // Clear the previous timer

        // Set a new timer to delay the search
        delayTimer = setTimeout(function() {
            // Get the search query from the input field
            var query = searchInput.value.trim();

            // Perform AJAX request to the server
            $.ajax({
                url: searchUrl, // Use the searchUrl variable here
                method: 'GET',
                data: { query: query },
                success: function(response) {
                    // Update the table body with the retrieved data
                    $('#employee-table-body').html($(response).find('#employee-table-body').html());
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }, 500); // Delay for 500 milliseconds (adjust as needed)
    });
});
