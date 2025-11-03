document.addEventListener("DOMContentLoaded", () => {
    const token = document.body.dataset.githubToken;

    if (!token) {
        console.warn("⚠️ No GitHub token found — star feature disabled.");
        return;
    }

    document.querySelectorAll(".btn-action.star").forEach(button => {
        button.addEventListener("click", async () => {
            const repoFullName = button.dataset.repo;

            try {
                const response = await fetch(`https://api.github.com/user/starred/${repoFullName}`, {
                    method: "PUT",
                    headers: {
                        "Authorization": `token ${token}`,
                        "Accept": "application/vnd.github+json"
                    }
                });

                if (response.status === 204) {
                    button.textContent = "⭐ Starred!";
                    button.style.background = "linear-gradient(135deg, #28a745, #20c997)";
                } else {
                    console.error("❌ Failed to star repo:", response.status);
                    alert("Could not star the repository. Check permissions.");
                }
            } catch (err) {
                console.error("💥 Error starring repo:", err);
            }
        });
    });
});
