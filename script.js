document.addEventListener("DOMContentLoaded", function() {
    const generateBSTBtn = document.getElementById("generateBST");
    const insertBtn = document.getElementById("insertBtn");
    const insertKeyInput = document.getElementById("insertKey");
    const removeBtn = document.getElementById("removeBtn");
    const removeKeyInput = document.getElementById("removeKey");
    const treeTvslSelect = document.getElementById("treeTvslSelect");
    const treeTvslBtn = document.getElementById("treeTvslBtn");
    // const clearBtn = document.getElementById("clearBtn");
    const treeDiv = document.getElementById("treeDisplayArea");
    const elementsDiv = document.getElementById("elementsDisplayArea");

    generateBSTBtn.addEventListener("click", function() {
        fetch("http://localhost:5000/generate", {
            method: "GET",
        })
        .then(response => response.json())
        .then(data => {
            treeDiv.innerHTML = `<pre>${data.result}</pre>`;
        });
    });

    insertBtn.addEventListener("click", function() {
        const key = insertKeyInput.value;
        fetch(`http://localhost:5000/insert/${key}`, {
            method: "POST",
        })
        .then(response => response.json())
        .then(data => {
            treeDiv.innerHTML = `<pre>${data.result}</pre>`;
        });
    });

    removeBtn.addEventListener("click", function() {
        const key = removeKeyInput.value;
        fetch(`http://localhost:5000/remove/${key}`, {
            method: "DELETE",
        })
        .then(response => response.json())
        .then(data => {
            treeDiv.innerHTML = `<pre>${data.result}</pre>`;
        });
    });

    
    // clearBtn.addEventListener("click", function() {
    //     const key = removeKeyInput.value;
    //     fetch(`http://localhost:5000/clear`, {
    //         method: "DELETE",
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         treeDiv.innerHTML = `<pre>${data.result}</pre>`;
    //     });
    // });

    treeTvslBtn.addEventListener("click", function() {
        fetch("http://localhost:5000/" + treeTvslSelect.value)
        .then(response => response.json())
        .then(data => {
            elementsDiv.innerHTML = `<p>${treeTvslSelect.value} Traversal: ${data.result}</p>`;
        });
    });
});
