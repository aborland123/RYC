document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    // Event listener for search form submission
    searchForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        const searchTerm = searchInput.value.trim();

        // Simulated data - replace with actual API call
        const searchResultsData = [
            { name: 'John Smith', university: 'University of Example' },
            { name: 'Jane Doe', university: 'Another University' },
            // Add more simulated data as needed
        ];

        // Clear previous search results
        searchResults.innerHTML = '';

        // Display search results
        if (searchTerm !== '') {
            const filteredResults = searchResultsData.filter(function(result) {
                return result.name.toLowerCase().includes(searchTerm.toLowerCase());
            });

            if (filteredResults.length > 0) {
                filteredResults.forEach(function(result) {
                    const companyCard = document.createElement('div');
                    companyCard.classList.add('company-card');
                    companyCard.innerHTML = `
                        <h3>${result.name}</h3>
                        <p>${result.university}</p>
                    `;
                    searchResults.appendChild(companyCard);
                });
            } else {
                searchResults.innerHTML = '<p>No results found.</p>';
            }
        }
    });
});