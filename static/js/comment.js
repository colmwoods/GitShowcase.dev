document.addEventListener("DOMContentLoaded", () => {
    const commentModal = document.getElementById("commentModal");
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteModal = deleteModalElement ? new bootstrap.Modal(deleteModalElement) : null;
    const deleteConfirm = document.getElementById("deleteConfirm");

    if (commentModal) {
        commentModal.addEventListener("show.bs.modal", (event) => {
            const button = event.relatedTarget;
            if (!button) return;

            const repoName = button.getAttribute("data-repo");
            const repoUrl = button.getAttribute("data-url");

            document.getElementById("modalRepoName").value = repoName || "";
            document.getElementById("modalRepoUrl").value = repoUrl || "";

            const modalTitle = document.getElementById("commentModalLabel");
            if (modalTitle) modalTitle.textContent = `Leave a Comment on ${repoName}`;
        });
    }

    document.querySelectorAll(".btn-edit").forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault();

            const commentId = button.getAttribute("data-comment_id");
            const commentTextElement = button.closest("li").querySelector("div");
            const commentBody = commentTextElement ? commentTextElement.innerText.trim() : "";

            const modalElement = document.getElementById("commentModal");
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

    document.querySelectorAll(".btn-delete").forEach((button) => {
        button.addEventListener("click", (e) => {
            const commentId = button.getAttribute("data-comment_id");
            if (!commentId || !deleteConfirm) return;
            deleteConfirm.href = `/comment/delete/${commentId}/`;
            if (deleteModal) deleteModal.show();
        });
    });

    document.querySelectorAll(".toggle-comments-btn").forEach((button) => {
        button.addEventListener("click", () => {
            const targetId = button.getAttribute("data-target");
            const target = document.getElementById(targetId);
            if (!target) return;

            const isHidden = target.style.display === "none" || !target.style.display;
            target.style.display = isHidden ? "block" : "none";
            button.textContent = button.textContent.replace(isHidden ? "💬" : "📖", isHidden ? "📖" : "💬");
        });
    });

    const commentModalEl = document.getElementById("commentModal");
    commentModalEl.addEventListener("hidden.bs.modal", () => {
        const form = commentModalEl.querySelector("form");
        const textarea = form.querySelector("textarea");
        const submitButton = form.querySelector("button[type='submit']");
        const modalTitle = document.getElementById("commentModalLabel");

        textarea.value = "";
        form.action = "/comment/add/";
        modalTitle.textContent = "Leave a Comment";
        submitButton.textContent = "Post Comment";
    });
});
