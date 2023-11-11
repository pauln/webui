#!/usr/bin/haserl
<%in p/common.cgi %>
<%
page_title="Camera preview"

size=$(yaml-cli -g .mjpeg.size); [ -z "$size" ] && size="640x480"
size_w=${size%x*}
size_h=${size#*x}
%>
<%in p/header.cgi %>

<div class="row preview">
  <div class="col-md-8 col-xl-9 col-xxl-9 position-relative mb-3">
    <% preview 1 %>
    <p class="small text-body-secondary">The image above refreshes once per second and may appear choppy.
    To see a smooth video feed from the camera use one of the <a href="majestic-endpoints.cgi" target="_blank">video endpoints</a>.
  </div>
  <div class="col-md-4 col-xl-3 col-xxl-3">
    <div class="d-grid gap-2 mb-3">
      <div class="input-group">
        <div class="input-group-text">
          <img src="/a/light-off.svg" alt="Image: Night mode indicator" id="night-mode-status">
        </div>
        <button class="form-control btn btn-primary text-start" type="button" id="toggle-night-mode">Toggle night mode</button>
        <div class="input-group-text">
          <a href="majestic-settings.cgi?tab=nightMode" title="Night mode settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <button class="form-control btn btn-primary text-start" type="button" data-sendto="email">Send to email</button>
        <div class="input-group-text">
          <a href="plugin-send2email.cgi" title="Email settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <button class="form-control btn btn-primary text-start" type="button" data-sendto="ftp">Send to FTP</button>
        <div class="input-group-text">
          <a href="plugin-send2ftp.cgi" title="FTP Storage settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <button class="form-control btn btn-primary text-start" type="button" data-sendto="telegram">Send to Telegram</button>
        <div class="input-group-text">
          <a href="plugin-send2telegram.cgi" title="Telegram bot settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <button class="form-control btn btn-primary text-start" type="button" data-sendto="mqtt">Send to MQTT</button>
        <div class="input-group-text">
          <a href="plugin-send2mqtt.cgi" title="MQTT settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <button class="form-control btn btn-primary text-start" type="button" data-sendto="webhook">Send to webhook</button>
        <div class="input-group-text">
          <a href="plugin-send2webhook.cgi" title="Webhook settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <button class="form-control btn btn-primary text-start" type="button" data-sendto="yadisk">Send to Yandex Disk</button>
        <div class="input-group-text">
          <a href="plugin-send2yadisk.cgi" title="Yandex Disk bot settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <button class="form-control btn btn-primary text-start" type="button" data-sendto="openwall">Send to Open Wall</button>
        <div class="input-group-text">
          <a href="plugin-send2openwall.cgi" title="Open Wall settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
      <div class="input-group">
        <div class="input-group-text">
          <img src="/a/light-off.svg" alt="Image: IR filter indicator" id="ircut-status">
        </div>
        <button class="form-control btn btn-secondary text-start" type="button" id="toggle-ircut">IR-cut filter</button>
        <div class="input-group-text">
          <a href="majestic-settings.cgi?tab=nightMode" title="Night mode settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>

<% if fw_printenv -n ir850_led_pin >/dev/null; then %>
      <div class="input-group">
        <div class="input-group-text">
          <img src="/a/light-off.svg" alt="Image: IR LED indicator" id="ir850-led-status">
        </div>
        <button class="form-control btn btn-secondary text-start" type="button" id="toggle-ir850-led">IR LED 850 nm</button>
        <div class="input-group-text">
          <a href="majestic-settings.cgi?tab=nightMode" title="Night mode settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
<% fi %>
<% if fw_printenv -n ir940_led_pin >/dev/null; then %>
      <div class="input-group">
        <div class="input-group-text">
          <img src="/a/light-off.svg" alt="Image: IR LED indicator" id="ir940-led-status">
        </div>
        <button class="form-control btn btn-secondary text-start" type="button" id="toggle-ir940-led">IR LED 940 nm</button>
        <div class="input-group-text">
          <a href="majestic-settings.cgi?tab=nightMode" title="Night mode settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
<% fi %>
<% if fw_printenv -n white_led_pin >/dev/null; then %>
      <div class="input-group">
        <div class="input-group-text">
          <img src="/a/light-off.svg" alt="Image: White LED indicator" id="white-led-status">
        </div>
        <button class="form-control btn btn-secondary text-start" type="button" id="toggle-white-led">White Light</button>
        <div class="input-group-text">
          <a href="majestic-settings.cgi?tab=nightMode" title="Night mode settings"><img src="/a/gear.svg" alt="Gear"></a>
        </div>
      </div>
<% fi %>
    </div>
    <%in p/joystick.cgi %>
  </div>
</div>

<script>
const network_address = "<%= $network_address %>";

<% [ "true" != "$email_enabled"    ] && echo "\$('button[data-sendto=email]').disabled = true;" %>
<% [ "true" != "$ftp_enabled"      ] && echo "\$('button[data-sendto=ftp]').disabled = true;" %>
<% [ "true" != "$mqtt_enabled"     ] && echo "\$('button[data-sendto=mqtt]').disabled = true;" %>
<% [ "true" != "$webhook_enabled"  ] && echo "\$('button[data-sendto=webhook]').disabled = true;" %>
<% [ "true" != "$telegram_enabled" ] && echo "\$('button[data-sendto=telegram]').disabled = true;" %>
<% [ "true" != "$yadisk_enabled"   ] && echo "\$('button[data-sendto=yadisk]').disabled = true;" %>

function sendToApi(endpoint) {
  const xhr = new XMLHttpRequest();
  xhr.addEventListener("load", reqListener);
  xhr.open("GET", 'http://' + ipaddr + endpoint);
  xhr.setRequestHeader("Authorization", "Basic " + btoa("admin:"));
  xhr.send();
}

function reqListener(data) {
  console.log(data.responseText);
}

$$("a[id^=pan-],a[id^=zoom-]").forEach(el => {
  el.addEventListener("click", event => {
    event.preventDefault();
    alert("Sorry, this feature does not work, yet!");
  });
});

$$("button[data-sendto]").forEach(el => {
  el.addEventListener("click", event => {
    event.preventDefault();
    if (!confirm("Are you sure?")) return false;
    const tgt = event.target.dataset["sendto"];
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/cgi-bin/send.cgi?to=" + tgt);
    xhr.send();
  });
});

$("#speed")?.addEventListener("click", event => {
  event.preventDefault();
  event.target.src = (event.target.src.split("/").pop() == "speed-slow.svg") ? "/a/speed-fast.svg" : "/a/speed-slow.svg";
});

$("#toggle-night-mode")?.addEventListener("click", event => {
  event.preventDefault();
  $('#night-mode-status').src = ($('#night-mode-status').src.split("/").pop() == "light-on.svg") ? "/a/light-off.svg" : "/a/light-on.svg";
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/cgi-bin/night.cgi");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send("mode=toggle");
});

$("#toggle-ircut").addEventListener("click", event => {
  event.preventDefault();
  if ($('#ircut-status').src.split("/").pop() == "light-on.svg") {
    $('#ircut-status').src = "/a/light-off.svg";
    mode = 'off';
  } else {
    $('#ircut-status').src = "/a/light-on.svg";
    mode = 'on';
  }
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "/cgi-bin/j/ircut.cgi?mode=" + mode);
  xhr.send();
});

["ir850", "ir940", "white"].forEach(n => {
  if ($('#toggle-' + n + '-led'))
    $('#toggle-' + n + '-led').addEventListener('click', event => {
      event.preventDefault();
      if ($('#' + n + '-led-status').src.split('/').pop() == 'light-on.svg') {
        $('#' + n + '-led-status').src = '/a/light-off.svg';
        mode = 'off';
      } else {
        $('#' + n + '-led-status').src = '/a/light-on.svg';
        mode = 'on';
      }
      const xhr = new XMLHttpRequest();
      xhr.open('GET', '/cgi-bin/j/light.cgi?type=' + n + '&mode=' + mode);
      xhr.send();
    });
})


$$('a[id^=pan-],a[id^=zoom-]').forEach(el => {
  el.addEventListener('click', event => {
    event.preventDefault();
    alert('Sorry, this feature does not work, yet!');
  });
});

if ($('#speed')) $('#speed').addEventListener('click', event => {
  event.preventDefault();
  event.target.src = (event.target.src.split('/').pop() == 'speed-slow.svg') ? '/img/speed-fast.svg' : '/img/speed-slow.svg';
  // sendToApi('/speed/toggle');
});
</script>

<%in p/footer.cgi %>
