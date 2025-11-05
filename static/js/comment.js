document.addEventListener("DOMContentLoaded", () => {
    const commentModal = document.getElementById("commentModal");
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteModal = deleteModalElement ? new bootstrap.Modal(deleteModalElement) : null;
    const deleteConfirm = document.getElementById("deleteConfirm");

    // --- COMMENT MODAL (open prefilled) ---
    if (commentModal) {
        commentModal.addEventListener("show.bs.modal", (event) => {
            const button = event.relatedTarget;
            if (!button) return;

            const repoName = button.getAttribute("data-repo");
            const repoUrl = button.getAttribute("data-url");

            const repoNameInput = document.getElementById("modalRepoName");
            const repoUrlInput = document.getElementById("modalRepoUrl");

            if (repoNameInput) repoNameInput.value = repoName || "";
            if (repoUrlInput) repoUrlInput.value = repoUrl || "";

            const modalTitle = document.getElementById("commentModalLabel");
            if (modalTitle) modalTitle.textContent = `💬 Comment on ${repoName}`;
        });
    }

    // --- EDIT COMMENT (reuse modal) ---
    document.querySelectorAll(".btn-edit").forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault();

            const commentId = button.getAttribute("data-comment_id");
            const commentTextElement = button.closest("li").querySelector("div");
            const commentBody = commentTextElement ? commentTextElement.innerText.trim() : "";

            const modalElement = document.getElementById("commentModal");
            if (!modalElement) return;

            const modal = new bootstrap.Modal(modalElement);
            const form = modalElement.querySelector("form");
            const textarea = form.querySelector("textarea");
            const modalTitle = document.getElementById("commentModalLabel");
            const submitButton = form.querySelector("button[type='submit']");

            textarea.value = commentBody;
            form.action = `/comment/edit/${commentId}/`;
            modalTitle.textContent = "✏️ Edit Comment";
            submitButton.textContent = "Update Comment";

            modal.show();
        });
    });

    // --- DELETE COMMENT ONLY ---
    document.querySelectorAll("button.btn-delete[data-comment_id]").forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            const commentId = button.getAttribute("data-comment_id");
            if (!commentId || !deleteConfirm) return;
            deleteConfirm.href = `/comment/delete/${commentId}/`;
            if (deleteModal) deleteModal.show();
        });
    });

    // --- TOGGLE COMMENTS VISIBILITY ---
    document.querySelectorAll(".toggle-comments-btn").forEach((button) => {
        button.addEventListener("click", () => {
            const targetId = button.getAttribute("data-target");
            const target = document.getElementById(targetId);
            if (!target) return;

            const isHidden = target.style.display === "none" || !target.style.display;
            target.style.display = isHidden ? "block" : "none";
            button.textContent = isHidden
                ? button.textContent.replace("💬", "📖")
                : button.textContent.replace("📖", "💬");
        });
    });

    // --- RESET COMMENT MODAL ON CLOSE ---
    if (commentModal) {
        commentModal.addEventListener("hidden.bs.modal", () => {
            const form = commentModal.querySelector("form");
            if (!form) return;

            const textarea = form.querySelector("textarea");
            const submitButton = form.querySelector("button[type='submit']");
            const modalTitle = document.getElementById("commentModalLabel");

            textarea.value = "";
            form.action = "/comment/add/";
            modalTitle.textContent = "💬 Leave a Comment";
            submitButton.textContent = "Post Comment";
        });
    }

    // --- AVOID BOOKMARK FORM CONFLICT ---
    document.querySelectorAll("form[action*='delete_bookmark']").forEach((form) => {
        form.addEventListener("submit", (e) => {
            e.stopPropagation(); // prevent JS conflicts
        });
    });

    // --- STAR BUTTON HANDLER ---
    document.querySelectorAll(".btn-action.star").forEach((button) => {
        button.addEventListener("click", async () => {
            const repoFullName = button.getAttribute("data-repo");
            if (!repoFullName) {
                alert("⚠️ Missing repository name.");
                return;
            }

            try {
                // Use GitHub API to fetch live star count
                const response = await fetch(`https://api.github.com/repos/${repoFullName}`);
                if (response.ok) {
                    const repo = await response.json();
                    alert(`⭐ ${repo.full_name} currently has ${repo.stargazers_count} stars!`);
                } else {
                    alert("❌ Couldn't fetch repo info. Check repository name.");
                }
            } catch (err) {
                console.error("Star fetch error:", err);
                alert("Network error while fetching star data.");
            }
        });
    });
});
