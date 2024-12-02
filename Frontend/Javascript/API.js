let deviceMacs = [];
let deviceIps = [];
let deviceNames = [];
let deviceManufacturer = [];
let deviceStatus = [];

const button = document.querySelector('.button');

// Função para buscar dispositivos e adicionar ao HTML
async function fetchDevices() {
    try {
        // Inicia o estado de carregamento
        button.textContent = 'Loading...';
        button.disabled = true; // Desabilita o botão para evitar múltiplos cliques
        button.style.cursor = 'not-allowed';

        // Faz a requisição dos dispositivos
        const response = await fetch("http://127.0.0.1:5000/api/devices");
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const devices = await response.json();

        // Aguarda 2 segundos antes de exibir os resultados
        setTimeout(() => {
            // Seleciona o container da lista e a cover
            const scanContainer = document.querySelector('.scanContainer');
            const cover = document.querySelector('.cover');
            cover.classList.add('invisible'); // Esconde a cover após carregar os dispositivos

            // Limpa os arrays e o container para evitar duplicações
            deviceMacs = [];
            deviceIps = [];
            deviceNames = [];
            deviceManufacturer = [];
            deviceStatus = [];
            scanContainer.innerHTML = '';

            // Adiciona cada dispositivo recebido ao HTML
            devices.forEach(device => {
                const deviceElement = document.createElement('li');
                deviceElement.classList.add('device');

                deviceElement.innerHTML = `
                    <h3>${device.host || "Unknown Device"}</h3>
                    <p><strong>MAC:</strong> ${device.mac || "N/A"}</p>
                    <p><strong>IP:</strong> ${device.ip || "N/A"}</p>
                    <p><strong>Manufacturer:</strong> ${device.manufacturer || "N/A"}</p>
                    <p><strong>Status:</strong> ${device.status || "Unknown"}</p>
                `;

                scanContainer.appendChild(deviceElement);

                // Armazenar os dados nos arrays
                deviceMacs.push(device.mac);
                deviceIps.push(device.ip);
                deviceNames.push(device.host);
                deviceManufacturer.push(device.manufacturer);
                deviceStatus.push(device.status);
            });

            console.log("MACs:", deviceMacs);
            console.log("IPs:", deviceIps);
            console.log("Names:", deviceNames);
            console.log("Manufacturers:", deviceManufacturer);
            console.log("Statuses:", deviceStatus);

            // Reseta o estado do botão
            button.textContent = 'SCAN';
            button.disabled = false;
            button.style.cursor = 'pointer';
        }, 2000); 

    } catch (error) {
        console.error("Failed to fetch devices:", error);
        button.textContent = 'Error!';
    }
}

// Adiciona o evento de clique ao botão "Scan"
button.addEventListener('click', fetchDevices);
