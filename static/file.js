$(document).ready(function(){
     function getCookie(name)
        {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does tcharthis cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        function Showfile(id){
         console.log(id)
            var csrftoken = getCookie('csrftoken');
            $.ajaxSetup({   headers: {  "X-CSRFToken": csrftoken  }  });
            $.ajax({
                url : URLshowfile,
                type : "POST",
                data : {'file_id':id } ,
                success : function (data) {
                    console.log(data)
                    $('#showfileframe').attr('src','http://127.0.0.1:8000/media/'+data[0].url)
                },
                error : function () {

                }
            });
        }
        $('.showfile').click(function (e) {
            var shwf=e.currentTarget.id
            var file_id=shwf.split('_')[1]
            Showfile(file_id)
        })
});