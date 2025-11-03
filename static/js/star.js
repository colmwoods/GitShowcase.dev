function getCookie(name) {
    const match = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return match ? match.pop() : '';
}

document.addEventListener("DOMContentLoaded", () => {
    // Add click listener to all "Star" buttons
    document.querySelectorAll(".btn-action.star").forEach(button => {
        button.addEventListener("click", async () => {
            const repoFullName = button.dataset.repo;
            if (!repoFullName) return;

            button.disabled = true;
            button.textContent = "⭐ Starring...";

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
                    button.textContent = "⭐ Starred!";
                    button.classList.add("starred");
                } else {
                    console.error("❌ Failed to star repo:", data);
                    button.textContent = "⭐ Star";
                    alert("Could not star repository. Try again or check permissions.");
                    button.disabled = false;
                }
            } catch (err) {
                console.error("💥 Network error:", err);
                alert("Network error — could not star repository.");
                button.disabled = false;
            }
        });
    });
});