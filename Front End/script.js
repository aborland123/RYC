document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('main-search-input'); // Corrected ID
    const searchResults = document.getElementById('search-results');

    // Event listener for search form submission
    searchForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        const searchTerm = searchInput.value.trim();

        // Simulated data - replace with actual API call
        const searchResultsData = [
            { company: 'Bank of America', rating: '4/5' },
            { company: 'Ford', rating: '2.8/5' },
            { company: 'WereAdulting', rating: '2.8/5' }
            // Add more simulated data as needed
        ];

        // Clear previous search results
        searchResults.innerHTML = '';

        // Display search results
        if (searchTerm !== '') {
            const filteredResults = searchResultsData.filter(function(result) {
                return result.company.toLowerCase().includes(searchTerm.toLowerCase());
            });

            if (filteredResults.length > 0) {
                filteredResults.forEach(function(result) {
                    const companyCard = document.createElement('div');
                    companyCard.classList.add('company-card');
                    companyCard.innerHTML = `
                        <h3>${result.company}</h3>
                        <p>${result.rating}</p>
                    `;
                    searchResults.appendChild(companyCard);
                });
            } else {
                searchResults.innerHTML = '<p>No results found.</p>';
            }
        }
    });
});