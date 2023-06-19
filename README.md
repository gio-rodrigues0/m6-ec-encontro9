# Explicação do exercício

Dividido em três scripts:

- publisher.py: abre o vídeo vídeo selecionado e publica cada frame em um tópico.
- subscriber.py: subscriber que acessa todos os frames que são publicados pelo publisher e os guarda numa pasta "recebidos".
- main.py: onde o servidor e as rotas são criadas.

## Publisher

1. Importação das bibliotecas necessárias: classe do nó, tipo da mensagem, OpenCV e a biblioteca que possibilita que imagens lidas pelo OpenCV sejam enviadas via comunicação ROS.
2. Criação do nó junto de um publisher.
3. Abertura do vídeo por meio do OpenCV.
4. Iniciação do CvBridge, que faz a conversão entre imagens do OpenCV e ROS.
5. Função de callback contendo um booleano que resulta em verdadeiro quando há frames disponíveis e publica cada frame no tópico, já se resultar em falso, o vídeo é aberto de novo.

## Subscriber

1. Importação das bibliotecas necessárias: classe do nó, tipo da mensagem, OpenCV, biblioteca que possibilita que imagens lidas pelo OpenCV sejam enviadas via comunicação ROS e das que possibilitam fazer requisições.
2. Criação do nó junto com o subscriber e a inicialização do CvBridge.
3. Por meio de uma requisição de método POST, envia os  frames para uma pasta chamada recebidos.

## Main

1. Servidor criado por meio do FastAPI.
2. Acesso as credenciais do bucket criado no Supabase.
3. Criação de um get que lista todos os itens que estiverem dentro do bucket.
4. Criação de um post que adiciona todos os frames lidos pelo subscriber numa pasta local chamada recebidos.
5. Acesso as imagens que estão dentro da pasta recebidos e que, por meio de um post, são enviadas para o bucket no Supabase.

Vídeo: https://drive.google.com/file/d/1FBBqRr2qrjkvQfwVny1fymx8Q6rhRevr/view

