// static/js/result.js
// This file contains the JavaScript code for the result page of the mental health predictor web application
// Add entrance animations
document.addEventListener('DOMContentLoaded', function() {
    // Animate elements on load
    const animatedElements = document.querySelectorAll('.prediction-card, .chart-container, .disclaimer');
    animatedElements.forEach((element, index) => {
    element.style.animationDelay = `${index * 0.3}s`;
    });

    // Add hover effects to stat cards
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px) scale(1.02)';
        this.style.boxShadow = '0 15px 35px rgba(0, 0, 0, 0.15)';
    });

    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
        this.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.1)';
    });
    });
});

// Download results functionality
function downloadResults() {
    const button = event.target.closest('.btn-download');
    const originalText = button.innerHTML;
    
    // Show loading state
    button.innerHTML = '<div class="loading-spinner" style="display: inline-block; width: 20px; height: 20px; border: 2px solid rgba(255,255,255,0.3); border-top: 2px solid white; margin-right: 8px;"></div>Preparing...';
    button.disabled = true;

    // Simulate download process
    setTimeout(() => {
    // Create a simple text report
    const resultText = `
Mental Health Assessment Report
================================
Date: ${new Date().toLocaleDateString()}
Result: {{ label }}
Questions Analyzed: 28
Processing Time: < 1 second

DISCLAIMER:
This assessment is for informational purposes only and is not intended as a substitute for professional mental health diagnosis or treatment.
    `;

    const blob = new Blob([resultText], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'mental-health-assessment-results.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);

    // Reset button
    button.innerHTML = originalText;
    button.disabled = false;
    }, 2000);
}

// Add smooth hover effects to buttons
document.querySelectorAll('.btn-try-again, .btn-download').forEach(button => {
    button.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-3px) scale(1.02)';
    });

    button.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0) scale(1)';
    });
});

// Add click ripple effect
document.querySelectorAll('.btn-try-again, .btn-download').forEach(button => {
    button.addEventListener('click', function(e) {
    const ripple = document.createElement('span');
    const rect = this.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;
    
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.style.position = 'absolute';
    ripple.style.borderRadius = '50%';
    ripple.style.background = 'rgba(255, 255, 255, 0.3)';
    ripple.style.transform = 'scale(0)';
    ripple.style.animation = 'ripple 0.6s linear';
    ripple.style.pointerEvents = 'none';
    
    this.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
    });
});

// Add CSS for ripple animation
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
    to {
        transform: scale(4);
        opacity: 0;
    }
    }
`;
document.head.appendChild(style);
