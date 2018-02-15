$(document).ready(function(){
    $(document).keypress(
        function(event){
         if (event.which == '13') {
            event.preventDefault();
          }
    });

    var template_post = `<div class="col-md-6 post-item">
        <div class="inner">
                <a alt="{{title}}" href="/catalogo/herramientas/{{slug}}">
                    <img src="https://datos.gob.mx/public/img/uploads/5a3801925f14526e00dcdd64/f6GxgdxBGHm13LbR.png">
                </a>

                <a alt="nula" class="tag" href="/">
                    <span class="tag-icon tag-nula"></span>
                </a>

            </div>

            <div class="post-info">
                <h3>
                    <a alt="{{title}}" href="/catalogo/herramientas/{{slug}}">{{title}}</a>
                    <!-- end ngIf: !post.external_link -->
                </h3>
                <p class="excerpt hidden-xs hidden-sm ">{{description}}</p>
                <p class="category">
                    <a alt="Noticias" href="#">{{category}}</a>
                </p>
                <p class="author">Coordinación de Estrategia Digital Nacional (CEDN)
                    <a alt="{{title}}" class="read-more" href="/catalogo/herramientas/{{slug}}">Leer más</a>
                </p>
            </div>
    </div>`;

    function callAPIPosts(){
        Mustache.parse(template_post);
        $('.pagination-div').hide();
        $('.server-posts').hide();

        var filtros = "";
        var dificultad_herramienta = $('#dificultad-herramienta').val();
        var tipo_herramienta = $('#tipo-herramienta').val();
        var titulo_herramienta = $('#titulo-herramienta').val();

        if(titulo_herramienta.trim()){
            filtros = "title__icontains=" + titulo_herramienta.trim();
        }

        if(tipo_herramienta.trim()){
            if(filtros.trim()){
               filtros = filtros + "&";
            }

            filtros += "category=" + tipo_herramienta.trim();
        }

        if(dificultad_herramienta.trim()){
            if(filtros.trim()){
                filtros = filtros + "&";
             }

             filtros += "level=" + dificultad_herramienta.trim();
        }
        
        $.get('/catalogo/api/posts/?' + filtros).done(function(response){
            $('.api-posts').html('');

            for(var x=0; x < response.results.length; x++){
                var rendered = Mustache.render(template_post, response.results[x]);
                $('.api-posts').append(rendered);
            }

            $('.api-posts').show();
        }).fail(function(response){
            console.log(response);
            $('.pagination-div').show();
            $('.server-posts').show();
        });
    }

    $('#titulo-herramienta').keypress(function(event){
        if(event.which == 13){
            callAPIPosts();
        }
    });

    $('#titulo-herramienta').keyup(function(event){
        if(!$('#titulo-herramienta').val().trim()){
            $('.api-posts').hide();
            $('.pagination-div').show();
            $('.server-posts').show();
        }
    });

    $('.search-button').click(function(event){
        callAPIPosts();
        return false;
    });
});