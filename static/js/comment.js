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
