document.querySelectorAll('.notice').forEach((notice) => {
    window.setTimeout(() => notice.remove(), 4500);
});