// La variable API_URL viene inyectada desde el HTML (ver base.html)

document.addEventListener('DOMContentLoaded', () => {
    // Detectar en qué página estamos para cargar la lógica adecuada
    if (document.getElementById('profile-form')) {
        setupProfilePage();
    }
    if (document.getElementById('chat-form')) {
        setupChatPage();
    }
});

// --- Lógica de Perfiles ---

function setupProfilePage() {
    loadProfiles();

    const form = document.getElementById('profile-form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const bio = document.getElementById('bio').value;
        const interests = document.getElementById('interests').value;

        const submitBtn = form.querySelector('button');
        submitBtn.disabled = true;
        submitBtn.textContent = "Saving...";

        try {
            const response = await fetch(`${API_URL}/profile`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, bio, interests })
            });

            if (response.ok) {
                alert("Profile created successfully!");
                form.reset();
                loadProfiles();
            } else {
                const err = await response.json();
                alert("Error: " + err.error);
            }
        } catch (error) {
            console.error("Connection Error:", error);
            alert("Could not connect to Backend.");
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = "Create Profile";
        }
    });
}

async function loadProfiles() {
    const listContainer = document.getElementById('profiles-container');
    listContainer.innerHTML = '<p>Loading profiles...</p>';

    try {
        const response = await fetch(`${API_URL}/profile`);
        const profiles = await response.json();

        listContainer.innerHTML = '';
        if (profiles.length === 0) {
            listContainer.innerHTML = '<p>No profiles found.</p>';
            return;
        }

        profiles.forEach(p => {
            const card = document.createElement('div');
            card.className = 'profile-card';
            
            let tagsHtml = '';
            if (p.analysis && p.analysis.keywords) {
                p.analysis.keywords.forEach(k => {
                    tagsHtml += `<span class="tag">${k}</span>`;
                });
            }

            card.innerHTML = `
                <h3>${p.name}</h3>
                <p><strong>Bio:</strong> ${p.bio}</p>
                <p><small>Language: ${(p.analysis?.language || 'unknown').toUpperCase()}</small></p>
                <div style="margin-top:5px;">${tagsHtml}</div>
            `;
            listContainer.appendChild(card);
        });

    } catch (error) {
        listContainer.innerHTML = '<p style="color:red">Error loading profiles. Is Backend running?</p>';
    }
}

// --- Lógica del Chat REAL (Conectado a DB) ---

function setupChatPage() {
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');
    const input = document.getElementById('chat-input');

    // 1. Cargar historial real al iniciar
    loadChatHistory();

    // 2. Revisar nuevos mensajes cada 3 segundos (Sincronización automática)
    setInterval(loadChatHistory, 3000);

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = input.value.trim();
        if (!text) return;

        input.value = ''; // Limpiar input

        try {
            // Enviar mensaje al backend real
            await fetch(`${API_URL}/chat`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            // Recargar historial inmediatamente
            loadChatHistory();
        } catch (error) {
            console.error("Error sending message:", error);
        }
    });

    async function loadChatHistory() {
        try {
            const res = await fetch(`${API_URL}/chat`);
            const messages = await res.json();
            
            // Limpiar chat actual
            chatBox.innerHTML = '';
            
            // Dibujar mensajes reales de la DB
            messages.forEach(msg => {
                const div = document.createElement('div');
                div.className = `msg ${msg.sender}`;
                div.innerHTML = `
                    <small style="display:block; font-size:0.7em; margin-bottom:2px; opacity:0.7">${msg.sender.toUpperCase()}</small>
                    ${msg.text}
                `;
                chatBox.appendChild(div);
            });
            
            // Bajar scroll al final
            chatBox.scrollTop = chatBox.scrollHeight;
        } catch (e) {
            // Si falla, no hacemos nada (silencioso)
        }
    }
}