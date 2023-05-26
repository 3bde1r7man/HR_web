$(document).ready(function() {
    var searchInput = document.getElementById('search-input');
    var delayTimer; 
    searchInput.addEventListener('input', function() {
        clearTimeout(delayTimer); 

        delayTimer = setTimeout(function() {
            var query = searchInput.value.trim();
            $.ajax({
                url: searchUrl, 
                method: 'GET',
                data: { query: query },
                success: function(response) {
                    
                    $('#employee-table-body').html($(response).find('#employee-table-body').html());
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }, 500); 
    });
});

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
        const hasInvalidParam = urlParams.has('invalid');
        if (hasInvalidParam) {
            alert('You have already submitted a request!');
            window.location.href = searchUrl;
        }
}