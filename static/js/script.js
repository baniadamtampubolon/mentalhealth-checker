// static/js/script.js
// This file contains the JavaScript code for the mental health predictor web application.
// Progress bar functionality
function updateProgressBar() {
    const scrollTop = window.pageYOffset;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    document.getElementById('progressBar').style.width = scrollPercent + '%';
}

// Question counter functionality
function updateQuestionCounter() {
    const questions = document.querySelectorAll('.question-group');
    const windowHeight = window.innerHeight;
    let currentQuestion = 1;

    questions.forEach((question, index) => {
    const rect = question.getBoundingClientRect();
    if (rect.top < windowHeight / 2 && rect.bottom > windowHeight / 2) {
        currentQuestion = index + 1;
    }
    });

    document.getElementById('questionCounter').textContent = `Question ${currentQuestion} of ${questions.length}`;
}

// Scroll to top functionality
function scrollToTop() {
    window.scrollTo({
    top: 0,
    behavior: 'smooth'
    });
}

// Random generator function
function generateRandom() {
    const form = document.getElementById('quizForm');
    const inputs = form.querySelectorAll('input[type="number"], select');
    
    inputs.forEach(input => {
    if (input.type === 'number') {
        input.value = Math.floor(Math.random() * 80) + 18; // Random age between 18-98
    } else if (input.tagName === 'SELECT') {
        input.value = Math.random() > 0.5 ? '1' : '0';
    }
    });

    // Add visual feedback
    inputs.forEach((input, index) => {
    setTimeout(() => {
        input.style.transform = 'scale(1.05)';
        input.style.borderColor = '#667eea';
        setTimeout(() => {
        input.style.transform = 'scale(1)';
        input.style.borderColor = '#e2e8f0';
        }, 200);
    }, index * 50);
    });
}

// Event listeners
window.addEventListener('scroll', () => {
    updateProgressBar();
    updateQuestionCounter();
});

window.addEventListener('load', () => {
    updateProgressBar();
    updateQuestionCounter();
});

// Add hover effects to form elements
document.querySelectorAll('.form-control, .form-select').forEach(element => {
    element.addEventListener('focus', function() {
    this.closest('.question-group').style.borderLeftColor = '#667eea';
    this.closest('.question-group').style.transform = 'translateY(-2px)';
    });

    element.addEventListener('blur', function() {
    this.closest('.question-group').style.borderLeftColor = 'transparent';
    this.closest('.question-group').style.transform = 'translateY(0)';
    });
});

// Add smooth transitions to buttons
document.querySelectorAll('.btn-predict, .btn-random').forEach(button => {
    button.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-3px) scale(1.02)';
    });

    button.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0) scale(1)';
    });
});
