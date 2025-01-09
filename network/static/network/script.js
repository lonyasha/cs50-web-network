function toggleLike(postId) {
  fetch(`/like/${postId}`, {
    method: "PUT",
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const likesCount = document.getElementById(`likes-${postId}`);
      likesCount.innerText = `${data.likes}`;

      const heartIcon = document.getElementById(`heart-icon-${postId}`);
      if (data.liked) {
        heartIcon.classList.remove("far");
        heartIcon.classList.add("fas", "liked");
      } else {
        heartIcon.classList.remove("fas", "liked");
        heartIcon.classList.add("far");
      }
    })
    .catch((error) => console.error("Error:", error));
}

function getCSRFToken() {
  let cookieValue = null;
  const cookies = document.cookie.split(";");
  cookies.forEach((cookie) => {
    const [name, value] = cookie.trim().split("=");
    if (name === "csrftoken") cookieValue = value;
  });
  return cookieValue;
}

function editPost(postId) {
  document.getElementById(`post-content-${postId}`).style.display = "none";
  document.getElementById(`edit-post-${postId}`).style.display = "block";
}

function savePost(postId) {
  const newContent = document.getElementById(`edit-content-${postId}`).value;
  fetch(`/edit/${postId}`, {
    method: "PUT",
    headers: {
      "X-CSRFToken": getCSRFToken(),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content: newContent }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        document.getElementById(
          `post-content-${postId}`
        ).innerHTML = `<p>${newContent}</p>`;
        cancelEdit(postId);
      }
    });
}

function cancelEdit(postId) {
  document.getElementById(`post-content-${postId}`).style.display = "block";
  document.getElementById(`edit-post-${postId}`).style.display = "none";
}
