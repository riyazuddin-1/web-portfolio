function changeTemplate(template_name, render_at) {
    fetch('/'+template_name)
        .then(response => response.text())
        .then(data => {
            $(render_at).html(data);
        })
        .catch(error => console.error(error));
}

$(document).ready(() => changeTemplate('projects', '.projects'));

$('.render-tpl').click(function() {
    if($(this).attr('id') != 'get-in-touch') {
        $('.render-tpl.btn').removeClass('active');
        $(this).addClass('active');
        changeTemplate($(this).data('template'), '#content');
    }
})