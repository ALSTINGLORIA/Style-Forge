document.getElementById("submit-btn").addEventListener("click", 
    function sendPrompt() {

    let prompt = document.getElementById("prompt").value;

    fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("display").innerText =
            data.message;
    });
}
)