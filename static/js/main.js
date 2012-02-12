$(document).ready( function()
    {
        if (window.location.search) {
            query_api(window.location.search)
        }

    }
);

function startSearch(event) {
    $("#searchform").submit();
}
function query_api(lyric) {
    var url = '/api/lyricGet' + encodeURI(lyric);
    console.log(url);
        $.ajax({
            url: url,
            data: {},
            success: function(data) {
                build_divs(data);
            }
        });
}
function build_divs(data) {
    console.log(data);
    var formatted_lyric = data.lyric.replace(/\n/g, '<br />');

    $('#lyric').html(formatted_lyric);
    $('#song_title').html(data.song.title);
    $('#artist').html(data.song.artist.name);
    $('#lyric').fadeIn(2500);
    $('#artist').fadeIn(900);
    $('#song_title').fadeIn(500);
    $('#by').fadeIn(700);
    $('#reflected_artist').html(data.song.artist.name);

    setTimeout(function(){$('#reflected_artist').fadeIn(500);}, 1500);
}