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