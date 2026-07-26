console.log("CareerPilot AI Loaded");

async function generateInterview() {

    const button = document.getElementById("generateBtn");

    const container = document.getElementById("questions");

    button.disabled = true;
    button.innerText = "Generating...";

    container.innerHTML = "";

    try {

        const response = await fetch("/api/interview", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({})
        });

        const data = await response.json();

        button.disabled = false;
        button.innerText = "Generate Interview Questions";

        if (data.error) {

            container.innerHTML =
                `<div class="alert alert-danger">${data.error}</div>`;

            return;
        }

        data.questions.forEach((q, index) => {

            const category = q.category || "Interview";

            const question = q.question || q;

            const hint = q.hint || "";

            container.innerHTML += `
            <div class="card mb-3">
                <div class="card-body">

                    <h5>Question ${index + 1}</h5>

                    <span class="badge bg-primary mb-2">
                        ${category}
                    </span>

                    <p class="fw-bold">
                        ${question}
                    </p>

                    <small class="text-muted">
                        ${hint}
                    </small>

                </div>
            </div>
            `;
        });

    } catch (err) {

        button.disabled = false;
        button.innerText = "Generate Interview Questions";

        container.innerHTML =
            `<div class="alert alert-danger">${err}</div>`;
    }

}