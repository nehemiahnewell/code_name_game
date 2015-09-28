var $span = $("span");

// status either started or waiting
if ( $span.attr('id') === "started" ) {
  $("#enter").show()
  $("#restart").hide()
} else {
  $("#enter").hide()
  $("#restart").show()
}

