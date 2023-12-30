document.addEventListener("DOMContentLoaded", function() {
    let perguntas = JSON.parse(document.getElementById('perguntas-json').textContent);

    function exibirPergunta(indice) {
        let perguntaAtual = perguntas[indice];
        document.getElementById('pergunta-container').innerHTML = `

            <div class="container">

            <div id="image">
                <img src="${perguntaAtual.fields.image}" class="d-block w-50" alt="...">
            </div>
            
            <div class="mb-3">
                <div class="input-group">
                      <span class="input-group-text" id="basic-addon3">In english ?</span>
                      <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4">
                      <button type="submit" class="btn btn-success" onclick="pegarTexto(${perguntaAtual.fields.name})" >Enviar</button>
                </div>
            </div>
            
        </div>
        `;

        
    }

    function proximaPergunta(proximaIndice) {
        if (proximaIndice < perguntas.length) {
            exibirPergunta(proximaIndice);
        } else {
            alert("Você respondeu todas as perguntas!");
        }
    }

    // Iniciando com a primeira pergunta
    exibirPergunta(0);
});



function pegarTexto(text_task) {

    var inputElement = document.getElementById('basic-url');

    var text_user = inputElement.value;

    if (text_task === text_user) {

        var conteudoAtual = document.getElementById('sucess').innerHTML;

        var novoConteudo = conteudoAtual + '<div class="alert alert-success" role="alert">A palavra ' + text_user + ' esta correta!</div>';

        document.getElementById('sucess').innerHTML = novoConteudo;      

    }else{

        var conteudoAtual = document.getElementById('danger').innerHTML;

        var novoConteudo = conteudoAtual + '<div class="alert alert-danger" role="alert">A palavra ' + text_user + ' esta errada!</div>';

        document.getElementById('danger').innerHTML = novoConteudo;    

    }
    
}
