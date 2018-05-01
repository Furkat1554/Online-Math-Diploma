document.getElementsByTagName("body")[0].innerHTML  += "";
document.getElementsByClassName("container")[0].innerHTML  += "";

// =================		Slider			=====================

function getCurrentUser(){

}

function urlAsArray(){
  var link = window.location.href.replace(window.location.origin,"").split("/");
  var c = 0;
  while(true){
    if(c >= link.length || link[c] == null)
      break;
    if(link[c] == ""){
      link.splice(c,1);
      continue;
    }
    c++;
  }
  return link;
}

function getUrlPart(u){
  return u == null ? urlAsArray() : urlAsArray()[u];
}

function ajaxGet(reqUrl){
  let s = "";
  $.ajax({
    async: false,
    url: reqUrl,
    type: "GET",
    dataType: "json",
    success: function (data) {
      s = data;
    }
  });
  return s;
}

function ajaxPost(reqUrl,sendData){
  let response;
  $.ajax({
    async: false,
    type: "POST",
    url: reqUrl,
    dataType: "json",
    data: sendData,
    success: function(p){
      // console.log("it's ok: " + JSON.stringify(p.status));
      response = p.status;
    },
    error: function(err){
      console.log("it's not ok");
      response = err;
    },
  });
  return response;
}
