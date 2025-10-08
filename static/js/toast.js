function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'border-red-600', 'text-red-500',
        'border-green-600', 'text-green-500',
        'border-gray-600', 'text-gray-400'
    );

    // Set base styles for dark theme
    toastComponent.className = 'fixed bottom-8 right-8 p-4 px-6 rounded-lg shadow-2xl z-50 transition-all duration-300 bg-[#000000]/70 backdrop-blur-md flex items-center gap-4';
    toastComponent.style.boxShadow = '0 0 10px 4px #3f3f3f';

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('border', 'border-green-600');
        toastTitle.className = 'font-bold text-green-500';
        toastMessage.className = 'text-gray-300 text-sm line-clamp-3';
        toastIcon.textContent = '✅';
    } else if (type === 'error') {
        toastComponent.classList.add('border', 'border-red-600');
        toastTitle.className = 'font-bold text-red-500';
        toastMessage.className = 'text-gray-300 text-sm line-clamp-3';
        toastIcon.textContent = '❌';
    } else {
        toastComponent.classList.add('border', 'border-gray-700/50');
        toastTitle.className = 'font-bold text-white';
        toastMessage.className = 'text-gray-300 text-sm line-clamp-3';
        toastIcon.textContent = 'ℹ️';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Show toast with animation
    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // Hide toast after duration
    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}