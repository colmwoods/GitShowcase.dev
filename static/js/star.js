function getCookie(name) {
    const match = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return match ? match.pop() : '';
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".btn-action.star").forEach(button => {
        button.addEventListener("click", async () => {
            const repoFullName = button.dataset.repo;
            if (!repoFullName) return;

            button.disabled = true;
            const originalText = button.textContent;
            button.textContent = "⭐ Working...";

            try {
                const response = await fetch("/api/star/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken"),
                    },
                    body: JSON.stringify({ repo: repoFullName }),
                });

                const data = await response.json();

                if (response.ok && data.ok) {
                    // Toggle button text and style
                    if (data.starred) {
                        button.textContent = "⭐ Starred!";
                        button.classList.add("starred");
                    } else {
                        button.textContent = "⭐ Star";
                        button.classList.remove("starred");
                    }
                } else {
                    console.error("❌ Failed to toggle star:", data);
                    button.textContent = originalText;
                    alert("Could not star/unstar repository.");
                }
            } catch (err) {
                console.error("💥 Network error:", err);
                alert("Network error — could not star/unstar repository.");
                button.textContent = originalText;
            } finally {
                button.disabled = false;
            }
        });
    });
});