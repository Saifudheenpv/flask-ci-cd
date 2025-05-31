// Update timestamp every second
function updateTimestamp() {
    const timestampElements = document.querySelectorAll('.timestamp');
    timestampElements.forEach(element => {
        const now = new Date();
        element.textContent = now.toLocaleString();
    });
}

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    // Update timestamp every second
    setInterval(updateTimestamp, 1000);
    
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}); 