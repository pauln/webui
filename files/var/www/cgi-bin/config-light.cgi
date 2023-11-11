#!/usr/bin/haserl
<%in p/common.cgi %>
<%
page_title="Illumination"
if [ "POST" = "$REQUEST_METHOD" ]; then
  error=""

  update_uboot_env ir850_led_pin $POST_ir850_led_pin
  update_uboot_env ir940_led_pin $POST_ir940_led_pin
  update_uboot_env white_led_pin $POST_white_led_pin

  # save 850 mn pin into Majestic config
  cli -s .nightMode.backlightPin $POST_ir850_led_pin
fi

ir850_led_pin=$(fw_printenv -n ir850_led_pin)
ir940_led_pin=$(fw_printenv -n ir940_led_pin)
white_led_pin=$(fw_printenv -n white_led_pin)
%>
<%in p/header.cgi %>

<form action="<%= $SCRIPT_NAME %>" method="post">
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mb-4">
    <div class="col">
      <% field_number "ir850_led_pin" "850 nm IR LED GPIO pin" %>
      <% field_number "ir940_led_pin" "940 nm IR LED GPIO pin" %>
      <% field_number "white_led_pin" "White Light LED GPIO pin" %>
    </div>
    <div class="col">
      <h3>Environment settings</h3>
      <pre>
ir850_led_pin: <%= $ir850_led_pin %>
ir940_led_pin: <%= $ir940_led_pin %>
white_led_pin: <%= $white_led_pin %>
</pre>
    </div>
    <div class="col">
      <% button_webui_log %>
    </div>
  </div>
  <% button_submit %>
</form>

<%in p/footer.cgi %>
