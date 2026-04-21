$(document).ready(function() {
    let authorsChartInstance = null;
    let tagsChartInstance = null;
    let sentimentChartInstance = null;

    // Load initial stats on page load
    loadStats();

    $('#run-scraper-btn').click(function() {
        const btn = $(this);
        const statusBox = $('#status-message');
        
        // UI Loading State
        btn.prop('disabled', true);
        btn.html('<i class="fa-solid fa-spinner fa-spin"></i> Scraping (Esto puede tardar unos segundos)...');
        statusBox.addClass('hidden').removeClass('success error');

        // Ajax POST to FastApi
        $.ajax({
            url: '/api/scrape',
            type: 'POST',
            success: function(response) {
                if(response.status === 'success') {
                    statusBox.text(response.message).addClass('success').removeClass('hidden');
                    // Refresh graphs
                    loadStats();
                } else {
                    statusBox.text(response.message).addClass('error').removeClass('hidden');
                }
            },
            error: function(err) {
                statusBox.text('Error de conexión con el servidor.').addClass('error').removeClass('hidden');
            },
            complete: function() {
                // Restore button state
                btn.prop('disabled', false);
                btn.html('<i class="fa-solid fa-play"></i> Iniciar Scraping');
            }
        });
    });

    function loadStats() {
        $.ajax({
            url: '/api/stats',
            type: 'GET',
            success: function(data) {
                renderAuthorsChart(data.top_authors);
                renderTagsChart(data.top_tags);
                renderSentimentChart(data.sentiment);
            }
        });
    }

    // Charting Configuration
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.font.family = 'Inter';

    function renderAuthorsChart(authorsData) {
        const ctx = document.getElementById('authorsChart').getContext('2d');
        if (authorsChartInstance) authorsChartInstance.destroy();

        if (!authorsData || authorsData.length === 0) return;

        authorsChartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: authorsData.map(d => d.name),
                datasets: [{
                    label: 'Citas',
                    data: authorsData.map(d => d.count),
                    backgroundColor: 'rgba(59, 130, 246, 0.7)',
                    borderColor: 'rgba(59, 130, 246, 1)',
                    borderWidth: 1,
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: { y: { beginAtZero: true } }
            }
        });
    }

    function renderTagsChart(tagsData) {
        const ctx = document.getElementById('tagsChart').getContext('2d');
        if (tagsChartInstance) tagsChartInstance.destroy();

        if (!tagsData || tagsData.length === 0) return;

        tagsChartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: tagsData.map(d => d.name),
                datasets: [{
                    label: 'Usos',
                    data: tagsData.map(d => d.count),
                    backgroundColor: 'rgba(139, 92, 246, 0.7)',
                    borderColor: 'rgba(139, 92, 246, 1)',
                    borderWidth: 1,
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: { y: { beginAtZero: true } }
            }
        });
    }

    function renderSentimentChart(sentimentData) {
        const ctx = document.getElementById('sentimentChart').getContext('2d');
        if (sentimentChartInstance) sentimentChartInstance.destroy();

        if (!sentimentData || sentimentData.length === 0) return;

        const colors = {
            'Positivo': 'rgba(16, 185, 129, 0.7)',
            'Neutral': 'rgba(245, 158, 11, 0.7)',
            'Negativo': 'rgba(239, 68, 68, 0.7)'
        };

        sentimentChartInstance = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: sentimentData.map(d => d.label),
                datasets: [{
                    data: sentimentData.map(d => d.count),
                    backgroundColor: sentimentData.map(d => colors[d.label]),
                    borderWidth: 0,
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
            }
        });
    }
});
