const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
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
        deleteModal.show();
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const commentModal = document.getElementById('commentModal');
    if (commentModal) {
        commentModal.addEventListener('show.bs.modal', event => {
            const button = event.relatedTarget;
            document.getElementById('modalRepoName').value = button.dataset.repo;
            document.getElementById('modalRepoUrl').value = button.dataset.url;
        });
    }

    document.querySelectorAll(".toggle-comments-btn").forEach(button => {
        button.addEventListener("click", () => {
            const targetId = button.getAttribute("data-target");
            const target = document.getElementById(targetId);
            if (target.style.display === "none") {
                target.style.display = "block";
                button.textContent = button.textContent.replace("💬", "📖"); // changes icon when open
            } else {
                target.style.display = "none";
                button.textContent = button.textContent.replace("📖", "💬");
            }
        });
    });
});
