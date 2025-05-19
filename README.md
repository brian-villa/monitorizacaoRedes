# NETHOUND Network Monitoring

Nethound is a network monitoring tool that scans devices on your network and alerts you about unauthorized connections and network activity.

# Backend Setup

Requirements

Python 3.8 or higher
pip package manager

Step 1: Install dependencies  
Navigate to the backend directory in your terminal and run:  
pip install -r requirements.txt

Step 2: Configure environment variables  
Create or edit the .env file located in the backend folder and add the following variables:  
MAC_VENDORS=your_macvendors_api_key_here
api_key=your_api_key_here
mongodb=your_mongodb_connection_string
vm_user=your_vm_username
vm_ip_public=your_vm_public_ip

Note:

- To get the MAC_VENDORS API key, register at MacVendors (https://macvendors.com/) and generate your key.
- Replace your_mongodb_connection_string with your actual MongoDB connection URI.
- Replace other variables with your relevant data.

Step 3: Connect MongoDB Compass (optional)  
If you want to visualize your database via MongoDB Compass, use your MongoDB connection string manually in the Compass connection window.

Step 4: Run the backend  
Start the backend by running:  
python main.py

# Frontend Setup

Requirements  
Node.js (version 16 or higher recommended)  
npm or yarn package manager

Step 1: Install dependencies  
Navigate to the frontend directory and run:  
npm install  
or  
yarn install

Step 2: Configure environment variables  
Create or edit the .env.local file in the frontend directory with your API keys:

VITE_API_KEY=your_api_key_here

Step 3: Run the development server  
Start the frontend with:  
npm run dev  
or  
yarn dev

By default, the app will be available at http://localhost:5000.

# Usage

- Click the Start button to scan your network.
- View detected devices, their statuses, and alerts.
- Make sure the api_key matches between the frontend and backend .env files for proper communication.

# Additional Notes

- All frontend dependencies (such as Tailwind CSS, FontAwesome, React, etc.) are defined in package.json and will be installed automatically when you run npm install or yarn install.
- Ensure the backend (main.py) is running before using the frontend interface.

/////////////////////////////////////////VERSAO EM PORTUGUES ////////////////////////////////////

# NETHOUND Monitoramento de Rede

Nethound é uma ferramenta de monitoramento de rede que escaneia dispositivos na sua rede e alerta sobre conexões não autorizadas e atividade de rede.

# Configuração do Backend

Requisitos

Python 3.8 ou superior  
Gerenciador de pacotes pip

Passo 1: Instalar dependências  
Navegue até a pasta do backend no terminal e execute:  
pip install -r requirements.txt

Passo 2: Configurar variáveis de ambiente  
Crie ou edite o arquivo .env localizado na pasta do backend com as seguintes variáveis:  
MAC_VENDORS=sua_chave_api_macvendors_aqui  
api_key=sua_chave_api_aqui  
mongodb=sua_string_de_conexao_mongodb  
vm_user=seu_usuario_vm  
vm_ip_public=ip_publico_da_vm

Observações:

- Para obter a chave API do MAC_VENDORS, registre-se no site MacVendors (https://macvendors.com/) e gere sua chave.
- Substitua a string de conexão do MongoDB pela sua URI real.
- Substitua as demais variáveis pelos seus dados.

Passo 3: Conectar no MongoDB Compass (opcional)  
Se desejar visualizar seu banco de dados via MongoDB Compass, insira manualmente a string de conexão do MongoDB na conexão do Compass.

Passo 4: Executar o backend  
Inicie o backend executando:  
python main.py

# Configuração do Frontend

Requisitos  
Node.js (recomenda-se versão 16 ou superior)  
Gerenciador de pacotes npm ou yarn

Passo 1: Instalar dependências  
Navegue até a pasta do frontend e execute:  
npm install  
ou  
yarn install

Passo 2: Configurar variáveis de ambiente  
Crie ou edite o arquivo .env.local na pasta do frontend com as suas chaves API:  
VITE_API_KEY=sua_chave_api_aqui  
VITE_MAC_VENDORS=sua_chave_api_macvendors_aqui

Passo 3: Executar o servidor de desenvolvimento  
Inicie o frontend com:  
npm run dev  
ou  
yarn dev

Por padrão, a aplicação estará disponível em http://localhost:5000.

# Uso

- Clique no botão Start para iniciar a varredura da rede.
- Visualize os dispositivos detectados, seus status e alertas.
- Certifique-se de que a chave api_key seja igual nos arquivos .env do frontend e backend para comunicação correta.

# Notas Adicionais

- Todas as dependências do frontend (como Tailwind CSS, FontAwesome, React, etc.) estão definidas no package.json e serão instaladas automaticamente ao executar npm install ou yarn install.
- Certifique-se de que o backend (main.py) esteja rodando antes de usar a interface frontend.
