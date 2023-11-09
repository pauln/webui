#!/usr/bin/haserl
<%
get_system_info

button() {
  id=$(echo "${2// /-}" | tr '[:upper:]' '[:lower:]' | tr -cd '[:alnum:]-' )
  echo "<div class=\"col\"><img id=\"${id}\" src=\"/a/${1}\" alt=\"${2}\" title=\"${2}\" style=\"width:100%\"></div>"
}
%>

<div class="row row-cols-3 g-3 m-5" id="ptnav">
  <% button "arrow-ul.svg" "Pan up left" %>
  <% button "arrow-uc.svg" "Pan up" %>
  <% button "arrow-ur.svg" "Pan up right" %>
  <% button "arrow-cl.svg" "Pan left" %>
  <% button "preset-home.svg" "Preset: Home" %>
  <% button "arrow-cr.svg" "Pan right" %>
  <% button "arrow-dl.svg" "Pan down left" %>
  <% button "arrow-dc.svg" "Pan down" %>
  <% button "arrow-dr.svg" "Pan down right" %>
</div>

<!--
<% button "speed-slow.svg" "Speed" %>
<% button "zoom-close.svg" "Zoom in" %>
<% button "zoom-far.svg" "Zoom out" %>
<% button "focus-plus.svg" "Focus: plus" %>
<% button "focus-auto.svg" "Focus: auto" %>
<% button "focus-minus.svg" "Focus: minus" %>
<% button "image-rotate-cw.svg" "Image rotate 90° CW" %>
<% button "image-rotate-ccw.svg" "Image rotate 90° CCW" %>
<% button "image-flip.svg" "Image: flip" %>
<% button "image-mirror.svg" "Image: mirror" %>
<% button "preset-home.svg" "Preset: Home" %>
<% button "preset-save.svg" "Preset: Save" %>
<% button "preset-1.svg" "Preset 1" %>
<% button "preset-2.svg" "Preset 2" %>
<% button "preset-3.svg" "Preset 3" %>
<% button "preset-4.svg" "Preset 4" %>
<% button "preset-5.svg" "Preset 5" %>
<% button "preset-6.svg" "Preset 6" %>
<% button "preset-7.svg" "Preset 7" %>
<% button "preset-8.svg" "Preset 8" %>
<% button "preset-9.svg" "Preset 9" %>
<input type="range" orient="vertical" id="isp-again" title="aGain">
<input type="range" orient="vertical" id="isp-dgain" title="dGain">
<input type="range" orient="vertical" id="isp-gain" title="Gain">
-->
</div>

<style>
#ptnav img:hover {cursor: pointer; background-color: yellow;}
</style>

<script>
function move(command) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "http://" + network_address + ":8078/execute");
  xhr.send("command=" + command);
}

$$('#ptnav img').forEach(el => el.addEventListener('click', ev => {
  console.log(el.id);
  switch(el.id) {
    case 'pan-up-left':
      move(el.id);
      break;
    case 'pan-up':
      move(el.id);
      break;
    case 'pan-up-right':
      move(el.id);
      break;
    case 'pan-left':
      move(el.id);
      break;
    case 'pan-right':
      move(el.id);
      break;
    case 'pan-down-left':
      move(el.id);
      break;
    case 'pan-down':
      move(el.id);
      break;
    case 'pan-down-right':
      move(el.id);
      break;
    default:
      //
  }
}));
</script>
