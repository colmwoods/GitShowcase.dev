const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = document.getElementById("deleteModal")
    ? new bootstrap.Modal(document.getElementById("deleteModal"))
    : null;

const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("data-comment_id");
        const commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `/comment/edit/${commentId}/`);
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `/comment/delete/${commentId}/`;
        if (deleteModal) deleteModal.show();
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const commentModal = document.getElementById("commentModal");

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
});
