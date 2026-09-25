const scanButton = document.getElementById("scanButton");
const screenshotInput = document.getElementById("screenshot");

const messageInput = document.getElementById("message");
const languageSelect = document.getElementById("language");

const resultsSection = document.getElementById("results");

const riskLabel = document.getElementById("riskLabel");
const riskScore = document.getElementById("riskScore");
const riskCategory = document.getElementById("riskCategory");

const signalsList = document.getElementById("signalsList");
const evidenceList = document.getElementById("evidenceList");
const tacticsList = document.getElementById("tacticsList");
const actionsList = document.getElementById("actionsList");


scanButton.addEventListener("click", async () => {

    const message = messageInput.value.trim();
    const language = languageSelect.value;
    const screenshot = screenshotInput.files[0];

    if (!message && !screenshot) {
        alert("Please enter a message or upload a screenshot first.");
        return;
    }

    scanButton.disabled = true;
    scanButton.textContent = "🔄 Analyzing...";


    try {

        let response;

if (screenshot) {

    const formData = new FormData();

    formData.append("file", screenshot);
    formData.append("language", language);

    response = await fetch(
        "http://127.0.0.1:8000/analyze-screenshot",
        {
            method: "POST",
            body: formData
        }
    );

} else {

    response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message,
                language: language
            })
        }
    );
}


        if (!response.ok) {
            throw new Error("Backend request failed.");
        }


        const result = await response.json();


        // Show results
        displayResults(result);


    } catch (error) {

        console.error(error);

        alert(
            "Could not connect to ScamShield AI backend.\n\n" +
            "Make sure FastAPI is running on port 8000."
        );

    } finally {

        scanButton.disabled = false;

        scanButton.textContent = "🔍 Scan for Scam Risk →";

    }

});


function displayResults(result) {

    // Show results section
    resultsSection.classList.remove("hidden");


    // Risk information
    const score = result.risk_score ?? 0;
    const level = result.risk_level ?? "UNKNOWN";
    const category = result.scam_category ?? "Unknown";

    const riskMeter = document.getElementById("riskMeter");

if (riskMeter) {
    riskMeter.style.width = `${score}%`;
}


    riskLabel.textContent = `🚨 ${level} RISK`;

    riskScore.innerHTML = `${score}<span>/100</span>`;

    riskCategory.textContent = category;


    // Suspicious signals
    renderList(
        signalsList,
        result.signals,
        "⚠️"
    );


    // Evidence
    renderList(
        evidenceList,
        result.evidence,
        "🔎"
    );


    // Manipulation tactics
    renderList(
        tacticsList,
        result.manipulation_tactics,
        "🎭"
    );


    // Safe actions
    renderList(
        actionsList,
        result.safe_actions,
        "✓"
    );


    // Scroll to results
    resultsSection.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });

}


function renderList(container, items, icon) {

    container.innerHTML = "";


    if (!items || items.length === 0) {

        container.innerHTML = `
            <div class="result-item">
                No information available.
            </div>
        `;

        return;
    }


    items.forEach(item => {

        const element = document.createElement("div");

        element.className = "result-item";

        element.textContent = `${icon} ${item}`;

        container.appendChild(element);

    });

}


// =========================
// EMERGENCY MODE
// =========================

const emergencyButton = document.getElementById("emergencyButton");
const emergencyPanel = document.getElementById("emergencyPanel");
const closeEmergency = document.getElementById("closeEmergency");
const emergencyResponse = document.getElementById("emergencyResponse");


// Open Emergency Mode
emergencyButton.addEventListener("click", () => {

    emergencyPanel.classList.remove("hidden");

    emergencyPanel.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });

});


// Close Emergency Mode
closeEmergency.addEventListener("click", () => {

    emergencyPanel.classList.add("hidden");

    emergencyResponse.classList.add("hidden");

});


// Emergency options
document.querySelectorAll(".emergency-option").forEach(option => {

    option.addEventListener("click", () => {

        const action = option.dataset.action;

        let title = "";
        let steps = [];


        if (action === "link") {

            title = "🔗 You clicked a suspicious link";

            steps = [
                "Close the suspicious website or page.",
                "Do not enter any more passwords, OTPs or banking information.",
                "If you entered a password, change it using the official website or app.",
                "Check your account for unusual activity."
            ];

        }


        if (action === "information") {

            title = "🔐 You shared sensitive information";

            steps = [
                "Do not share any additional OTPs, PINs or passwords.",
                "Contact your bank or service provider using its official contact method.",
                "If banking information was exposed, ask the bank about securing your account.",
                "Watch for unusual transactions or further scam messages."
            ];

        }


        if (action === "money") {

            title = "💸 You transferred money";

            steps = [
                "Contact your bank or payment provider immediately through an official channel.",
                "Report the transaction as suspected fraud.",
                "Save the transaction ID, screenshots, phone number and scam message.",
                "Do not send additional money, even if the scammer promises a refund."
            ];

        }


        emergencyResponse.innerHTML = `
            <h3>${title}</h3>

            <ul>
                ${steps.map(step => `<li>${step}</li>`).join("")}
            </ul>
        `;


        emergencyResponse.classList.remove("hidden");

        emergencyResponse.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });

    });

});

// =========================
// SIDEBAR NAVIGATION
// =========================

document.querySelectorAll(".sidebar-item").forEach(item => {

    item.addEventListener("click", () => {

        const target = item.dataset.target;

        if (target) {
            document.getElementById(target)?.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }

    });

});