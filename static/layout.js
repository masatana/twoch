$(function() {
  $('.dat').click(function() {
    $.getJSON('/_get_dat', {
      thread_id: this.id
    }, function(data) {
      // Do not use remove()
      // Remove previous dat
      $('#reader').empty();
      var splits = data.result.split('\n');
      for (var i = 0; i < splits.length; i++) {
        var strings = splits[i].split("<>");
        if (i == 0) {
          var ichi_id = strings[2].split(" ")[2];
        }
        $('#reader').append(function() {
          var respond_meta = '<span class="respond_meta"><span class="respond_number">' + String(i + 1) + '</span>';
          respond_meta += '<span class="name">' + escapeHtml(strings[0]) + '</span>';
          respond_meta += '<span class="email">' + escapeHtml(strings[1]) + '</span>';
          respond_meta += '<span class="date_id_be">' + escapeHtml(strings[2]) + '</span></span>';
          if (strings[2].split(" ")[2] == ichi_id) {
            var respond_text = '<div class="respond_text ichi">' + escapeRespondText(strings[3]) + '</div:>';
          } else {
            var respond_text = '<div class="respond_text">' + escapeRespondText(strings[3]) + '</div:>';
          }
          return '<div class="respond">' + respond_meta + respond_text + '</div>';
        });
      }
    });
  });
});
function escapeRespondText(unsafe) {
  var safe = escapeHtml(unsafe);
  return safe
    .replace(/&lt;br&gt;/g, '<br>')
    .replace(/&lt;a.*&gt;&amp;gt;&amp;gt;(\d).*\/a&gt;/g, '>>$1')
    .replace(/&amp;gt;/g, '>')
    .replace(/&amp;lt;/g, '<')
    .replace(/&amp;quot;/g, '<');
}
function escapeHtml(unsafe) {
  return unsafe
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
function fold(x) {
  var y = x.nextSibling;
  while (y.nodeType != 1) y = y.nextSibling;
  if (y.style.display == 'none') {
    y.style.display = '';
  } else {
    y.style.display = 'none';
  }
}
$(function() {
  var topButton = $('#page-top');
  topButton.hide();
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      topButton.fadeIn();
    } else {
      topButton.fadeOut();
    }
  });
  topButton.click(function() {
    $('body,html').animate({
      scrollTop: 0
    }, 500);
    return false;
  });
});

